---
id: https://agentic-knowledge-base.dev/id/chunk/cd2d5603-718a-4f3a-886a-3ce4d6b89880
type: artifact
level: executable
title_ko: 함수 parse_space (tools/space2kg.py)
title: function parse_space in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9875f781-35a4-413a-beae-89f20bb6ea33, https://agentic-knowledge-base.dev/id/chunk/a17c39f7-acf4-442e-a8e3-c996b7156e77, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/d3b6910f-bf07-4997-9d87-d61f68beb577]
part_of: https://agentic-knowledge-base.dev/id/composite/fc3f9858-3941-435d-b741-071b871ce613
---
**함수** — `parse_space(path)` 다. `-space` 청크 하나 → 방출에 필요한 값들.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_space(path: str) -> dict:
    """`-space` 청크 하나 → 방출에 필요한 값들. 형식 위반은 SpaceError 다."""
    meta, body = chunk2kg.parse_chunk(path)
    if meta["type"] != kb_lib.SPACE_TYPE:
        raise SpaceError(f"{path}: type 이 {kb_lib.SPACE_TYPE} 가 아니다 — 실제 {meta['type']!r} (설계 공간이 아닌 청크는 "
                         f"tools/chunk2kg.py 가 head 로 올린다)")
    data = body_block(path, kb_lib.chunk_body(Path(path).read_text(encoding="utf-8")))

    var = data.get("variable")
    if not isinstance(var, dict) or sorted(var) != ["from", "kind"] or not var["from"] or not var["kind"]:
        raise SpaceError(f"{path}: variable 은 {{from: <출발 항목 IRI>, kind: <링크 타입>}} 이어야 한다 — 실제 {var!r} "
                         f"(변수는 값이 아니라 출발 항목과 링크 타입의 쌍이다, p9-uncertainty-as-link-uncertainty)")
    kind = str(var["kind"])
    if kind not in chunk2kg.LINK_KEYS:
        raise SpaceError(f"{path}: variable.kind {kind!r} 가 링크 타입이 아니다 — {' | '.join(chunk2kg.LINK_KEYS)} 중 하나다 (8.2절)")
    status = str(data.get("status", ""))
    if status not in kb_lib.SPACE_STATUS:
        raise SpaceError(f"{path}: status 는 {' | '.join(kb_lib.SPACE_STATUS)} 중 하나다 — 실제 {status!r} (p9-candidate-storage)")

    candidates, seen = [], {}
    for item in data.get("candidates") or []:
        if not isinstance(item, dict) or not set(item) <= set(CANDIDATE_KEYS):
            raise SpaceError(f"{path}: 후보의 키는 {' · '.join(CANDIDATE_KEYS)} 다 — 실제 {item!r}")
        to, state = str(item.get("to", "")), str(item.get("state", ""))
        if not to:
            raise SpaceError(f"{path}: 후보에 to(대상 IRI)가 없다 — {item!r}")
        if state not in kb_lib.SPACE_STATES:
            raise SpaceError(f"{path}: 후보 {to} 의 state {state!r} 가 어휘 밖이다 — {' | '.join(kb_lib.SPACE_STATES)} 중 하나다")
        if to in seen:
            raise SpaceError(f"{path}: 후보 {to} 가 두 번 적혔다 — 한 후보는 한 줄이다")
        seen[to] = state
        support = evidence_of(path, f"후보 {to}", item["evidence"], "+") if item.get("evidence") else []
        elim = None
        if state == "eliminated":
            if not item.get("eliminated_by"):
                raise SpaceError(f"{path}: 후보 {to} 가 eliminated 인데 eliminated_by 가 없다 — 근거 없는 배제를 금지한다 "
                                 f"(요구 r-011-no-groundless-assignment)")
            elim = evidence_of(path, f"후보 {to} 의 배제", item["eliminated_by"], "-")[0]
        elif item.get("eliminated_by"):
            raise SpaceError(f"{path}: 후보 {to} 는 state 가 {state} 인데 eliminated_by 가 있다 — 배제 근거는 eliminated 에만 적는다")
        if state == "confirmed" and not any(k in kb_lib.SPACE_CONFIRMING_EVIDENCE for k, _ in support):
            raise SpaceError(f"{path}: 후보 {to} 가 confirmed 인데 지지 증거가 없다 — 구축 기록 또는 실행 결과"
                             f"({' | '.join(kb_lib.SPACE_CONFIRMING_EVIDENCE)}) 없이 확정할 수 없다 (9.11절, 요구 r-011-no-groundless-assignment)")
        candidates.append({"to": to, "state": state, "when": str(item.get("when", "")), "support": support, "elim": elim})

    prefs = []
    for item in data.get("preferences") or []:
        if not isinstance(item, dict) or sorted(item) != ["over", "prefer"]:
            raise SpaceError(f"{path}: preferences 항목은 {{prefer: <IRI>, over: <IRI>}} 여야 한다 — 실제 {item!r} (8.9절 부분순서)")
        a, b = str(item["prefer"]), str(item["over"])
        for iri in (a, b):
            if iri not in seen:
                raise SpaceError(f"{path}: preferences 가 후보가 아닌 {iri} 를 가리킨다 — 선호는 같은 공간의 두 후보 사이의 부분순서다")
        if a == b:
            raise SpaceError(f"{path}: preferences 의 prefer 와 over 가 같다 ({a}) — 선호는 비대칭 관계다")
        prefs.append((a, b))

    constraints = [str(c) for c in (data.get("constraints") or [])]
    if any(not c for c in constraints):
        raise SpaceError(f"{path}: 빈 양립 제약이 있다 — 제약이 없으면 constraints 를 적지 않는다 (STYLEGUIDE §0 빈 값)")
    return {"meta": meta, "body": body, "path": path, "var": (str(var["from"]), kind), "status": status,
            "candidates": candidates, "constraints": constraints, "preferences": prefs}
```
<!-- 인용 끝 -->
