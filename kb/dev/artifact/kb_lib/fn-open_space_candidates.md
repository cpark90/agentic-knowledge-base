---
id: https://agentic-knowledge-base.dev/id/chunk/3f9e7300-40c1-4755-9e4d-f22da6f54774
type: artifact
level: executable
title_ko: 함수 open_space_candidates (tools/kb_lib.py)
title: function open_space_candidates in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `open_space_candidates(g)` 다. 열린 공간(`agt:spaceStatus "open"`)의 열린 후보(state open → linkState candidate)가 가리키는 대상 IRI 집합이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def open_space_candidates(g: Graph) -> set:
    """열린 공간(`agt:spaceStatus "open"`)의 열린 후보(state open → linkState candidate)가 가리키는 대상 IRI 집합이다.

    결정 완결률이 이 집합에 결론이 든 결정을 따로 센다 (유저 결정 Q60-a). resolved 공간의 confirmed 후보는 확정 결정이므로
    들지 않는다.
    """
    _, has_cand, link_to = SPACE_LINKAGE_PREDICATES
    open_state = SPACE_STATE_LINK["open"][1]
    out = set()
    for space, st in g.subject_objects(AGT.spaceStatus):
        if str(st) != SPACE_STATUS[0]:
            continue
        for link in g.objects(space, has_cand):
            if str(next(g.objects(link, AGT.linkState), "")) == open_state:
                out.update(g.objects(link, link_to))
    return out
```
<!-- 인용 끝 -->
