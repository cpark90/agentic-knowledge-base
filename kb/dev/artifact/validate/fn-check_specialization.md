---
id: https://agentic-knowledge-base.dev/id/chunk/d26c3802-192f-4414-81da-25abd63211fc
type: artifact
level: executable
title_ko: 함수 check_specialization (tools/validate.py)
title: function check_specialization in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_specialization(merged, files)` 다. prov:specializationOf 규율 (p10-split-keeps-work-identity, 게이트 id `specialization`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_specialization(merged: Graph, files: dict[str, Graph]) -> list[str]:
    """prov:specializationOf 규율 (p10-split-keeps-work-identity, 게이트 id `specialization`).

    분할 조각은 원 청크를 특수화한다 — 같은 것의 다른 입도다. 그래서 대상은 (a) 같은 plane 의 청크이고 (b) 살아 있어야 하며
    (deprecated 원본의 조각은 원본을 승계했어야 한다), (c) 사슬은 순환하지 않는다 (뿌리 uuid 를 계산할 수 없다). 대상 부재는
    check_dangling 이 본다. 순환은 성분마다 한 번 보고한다.
    """
    gate = kb_lib.SPECIALIZATION_GATE
    plane = kb_lib.chunk_planes(merged)
    errors = []
    spec: dict = {}
    for s, o in sorted(merged.subject_objects(kb_lib.PROV.specializationOf), key=lambda so: (str(so[0]), str(so[1]))):
        where = _chunk_location(merged, s)
        if not isinstance(o, URIRef) or o not in plane:
            continue  # 청크가 아닌 대상은 dangling 이 보고한다
        spec[s] = o
        if s == o:
            errors.append(f"[{gate}] {where}: prov:specializationOf 가 자기 자신이다 — 조각은 원본을 특수화한다")
            continue
        if plane.get(s) != plane[o]:
            errors.append(f"[{gate}] {where}: prov:specializationOf 대상 {_qname(merged, o)} 의 plane 이 다르다 ({plane.get(s)} ≠ {plane[o]}) — "
                          f"분할 조각은 같은 plane 의 원본을 특수화한다 (p10-split-keeps-work-identity)")
        if str(next(merged.objects(o, kb_lib.AGT.status), "")) == "deprecated":
            errors.append(f"[{gate}] {where}: prov:specializationOf 대상 {_qname(merged, o)} 이 deprecated 다 — 원본은 살아 있는 청크여야 한다 "
                          f"(폐기된 원본의 조각은 uuid 를 승계했어야 한다)")
    reported: set = set()
    for start in sorted(spec, key=str):
        seen, cur = [], start
        while cur in spec and cur not in seen:
            seen.append(cur)
            cur = spec[cur]
        if cur in seen:  # 순환 — cur 부터 되돌아온다
            cycle = tuple(seen[seen.index(cur):])
            key = min(map(str, cycle))
            if key not in reported:
                reported.add(key)
                errors.append(f"[{gate}] {_chunk_location(merged, cycle[0])}: prov:specializationOf 사슬이 순환한다: "
                              + " → ".join(_qname(merged, c) for c in cycle + (cycle[0],)) + " — 뿌리 uuid 를 계산할 수 없다")
    return errors
```
<!-- 인용 끝 -->
