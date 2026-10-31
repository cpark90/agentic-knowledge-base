---
id: https://agentic-knowledge-base.dev/id/chunk/0eba15f1-9ab6-4d48-bb9a-8809fc98a603
type: artifact
level: executable
title_ko: 함수 check_space (tools/validate.py)
title: function check_space in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/464fe842-81a3-438f-901c-e9cef6f1dc88, https://agentic-knowledge-base.dev/id/chunk/6b263b93-09d3-4458-ba0b-03ba81f30852, https://agentic-knowledge-base.dev/id/chunk/7253cc54-4d5c-47ee-b402-6574573c23ef, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4, https://agentic-knowledge-base.dev/id/chunk/908a996f-e2c4-43ce-a43f-63ff651548af, https://agentic-knowledge-base.dev/id/chunk/95affdef-9253-4022-a9ec-ea650d4b30ed]
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_space(merged, files)` 다. 설계 공간(agt:Space)의 규칙 (결정 p9-candidate-storage, 요구 r-011-no-groundless-assignment, 게이트 id `space`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_space(merged: Graph, files: dict[str, Graph]) -> list[str]:
    """설계 공간(agt:Space)의 규칙 (결정 p9-candidate-storage, 요구 r-011-no-groundless-assignment, 게이트 id `space`).

    후보는 확정 링크와 다른 자리에 살고 결코 deps 가 되지 않으므로, Bazel 이 로드 시점에 잡아 주는 것(끝점의 실재·방향)을
    여기서 그래프로 대신 판정한다. 검사는 다섯이다.
      (a) 변수의 출발 항목(agt:variableFrom)과 각 후보(후보 쪽 끝 — kb_lib.space_candidate_of)가 실재한다 — 끊긴 후보는 실제 선택지를 오도한다.
      (b) 후보 링크의 변수 쪽 끝·링크 타입이 그 공간의 변수와 같다 — 다른 변수의 후보가 섞이면 "무엇이 열려 있는가"의 답이 틀린다.
          두 끝 가운데 하나가 변수의 출발 항목이고 방향은 변수 종류(링크 타입, 출발 항목의 지식 종류)의 방향 표
          kb_lib.SPACE_CANDIDATE_DIRECTION 과 같다 (Q-0055 Q112-b).
      (c) agt:spaceStatus 가 resolved 면 확정 후보가 정확히 하나다 — 둘이면 할당이 아니고 0 이면 해소가 아니다.
      (d) 배제된 후보(linkState invalid)에 (−) 증거가 있다 — 근거 없는 배제 금지가 r-011 의 요지다.
      (e) 확정 후보(linkState confirmed)에 구축(+)·실행(+)·유저 결정(+) 증거가 있다 — 근거 없는 할당 금지 (9.11절).
    """
    AGT_ = kb_lib.AGT
    gate = kb_lib.SPACE_GATE
    subjects = set(merged.subjects())
    plane_of = kb_lib.item_plane_resolver(merged)
    errors = []
    for space in sorted(merged.subjects(RDF.type, AGT_.Space), key=str):
        where = _chunk_location(merged, space)
        froms = list(merged.objects(space, AGT_.variableFrom))
        kinds = list(merged.objects(space, AGT_.variableKind))
        for o in froms:  # (a) 출발 항목의 실재 — 수는 shape(agt:SpaceShape)가 본다
            if isinstance(o, URIRef) and str(o).startswith(str(kb_lib.ID)) and o not in subjects:
                errors.append(f"[{gate}] {where}: 변수의 출발 항목이 없다: {_qname(merged, o)} — 없는 항목에 변수를 걸 수 없다 (참조 무결성 8.2절)")
        confirmed = 0
        kind_name = str(kinds[0]).rsplit("/", 1)[-1] if kinds else ""
        from_plane = plane_of(froms[0]) if froms else None
        for link in sorted(merged.objects(space, AGT_.hasCandidate), key=str):
            to = kb_lib.space_candidate_of(merged, space, link)
            state = str(next(merged.objects(link, AGT_.linkState), ""))
            label = _qname(merged, to) if to is not None else kb_lib.NONE_MARK
            if isinstance(to, URIRef) and str(to).startswith(str(kb_lib.ID)) and to not in subjects:  # (a)
                errors.append(f"[{gate}] {where}: 후보의 대상이 없다: {label} — 없는 항목은 후보가 될 수 없다 (참조 무결성 8.2절)")
            ends = (next(merged.objects(link, AGT_.linkFrom), None), next(merged.objects(link, AGT_.linkTo), None))
            if froms and froms[0] not in ends:  # (b) 변수 쪽 끝
                errors.append(f"[{gate}] {where}: 후보 {label} 의 링크가 변수의 출발 항목 {_qname(merged, froms[0])} 에 닿지 않는다 — "
                              f"한 공간은 변수 하나다 (p9-candidate-storage)")
            elif froms and to is not None and (kind_name, from_plane) in kb_lib.SPACE_CANDIDATE_DIRECTION:  # (b) 방향
                want = kb_lib.space_link_ends(froms[0], kind_name, from_plane, to)
                if ends != want:
                    errors.append(f"[{gate}] {where}: 후보 {label} 의 링크 방향이 변수 종류 ({kind_name}, {from_plane}) 의 방향 표와 반대다 — "
                                  f"방향 규칙은 kb_lib.SPACE_CANDIDATE_DIRECTION 하나다 (Q-0055 Q112-b)")
            for o in merged.objects(link, AGT_.linkKind):  # (b)
                if kinds and o not in kinds:
                    errors.append(f"[{gate}] {where}: 후보 {label} 의 링크 타입 {_agt_qname(merged, o)} 이 변수의 타입 "
                                  f"{_agt_qname(merged, kinds[0])} 과 다르다 — 타입이 다르면 다른 변수다 (p9-uncertainty-as-link-uncertainty)")
            polarities = {str(pol) for e in merged.objects(link, AGT_.hasEvidence) for pol in merged.objects(e, AGT_.polarity)}
            if state == kb_lib.LINK_STATE_INVALID and "-" not in polarities:  # (d)
                errors.append(f"[{gate}] {where}: 배제된 후보 {label} 에 배제 근거가 없다 — 후보를 지우려면 (−) 증거 한 줄이 있어야 한다 "
                              f"(`eliminated_by`, 요구 r-011-no-groundless-assignment)")
            if state == kb_lib.LINK_STATE_CONFIRMED:  # (e)
                confirmed += 1
                kinds_ok = {str(k).split("/")[-1] for e in merged.objects(link, AGT_.hasEvidence)
                            for k in merged.objects(e, AGT_.evidenceKind)}
                if not kinds_ok & set(kb_lib.SPACE_CONFIRMING_EVIDENCE):
                    errors.append(f"[{gate}] {where}: 확정된 후보 {label} 에 지지 증거가 없다 — 구축 기록·실행 결과·유저 결정"
                                  f"({' | '.join(kb_lib.SPACE_CONFIRMING_EVIDENCE)}) 없이 확정할 수 없다 "
                                  f"(9.11절, 요구 r-011-no-groundless-assignment)")
        status = str(next(merged.objects(space, AGT_.spaceStatus), ""))
        if status == "resolved" and confirmed != 1:  # (c)
            errors.append(f"[{gate}] {where}: agt:spaceStatus 가 resolved 인데 확정 후보가 {confirmed}개다 — 정확히 하나여야 한다 "
                          f"(둘이면 할당이 아니고 0 이면 해소가 아니다, p9-candidate-storage)")
    return errors
```
<!-- 인용 끝 -->
