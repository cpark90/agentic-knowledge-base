---
id: https://agentic-knowledge-base.dev/id/chunk/6caa6876-675f-4e0a-a42e-115c6f7e71d5
type: artifact
level: executable
title_ko: 함수 check_cyclic_hierarchy (tools/validate.py)
title: function check_cyclic_hierarchy in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/03af6d80-e46c-44f7-acd5-12d186d9bb75, https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe]
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `check_cyclic_hierarchy(asserted, files)` 다. 단언된 rdfs:subClassOf 의 순환 (게이트 `cyclic-hierarchy`, 유저 결정 Q179-a) — 강한 연결 요소마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_cyclic_hierarchy(asserted: Graph, files: dict[str, Graph]) -> list[str]:
    """단언된 rdfs:subClassOf 의 순환 (게이트 `cyclic-hierarchy`, 유저 결정 Q179-a) — 강한 연결 요소마다 한 줄이다.

    FAIL 줄은 요소의 가장 앞 클래스에서 출발해 돌아오는 가장 짧은 순환을 간선 공리와 그 파일로 적는다. 요소가 그 순환보다 크면
    요소의 클래스 수를 함께 적는다. <경로> 자리는 첫 간선 공리의 파일이다.
    """
    gate = CYCLIC_HIERARCHY
    errors = []
    for comp in subclass_components(asserted):
        members, start = set(comp), comp[0]
        back = {start: None}  # 너비 우선 — 요소 안에서 start 로 돌아오는 가장 짧은 길
        frontier, end = [start], None
        while frontier and end is None:
            nxt = []
            for node in frontier:
                for o in sorted(asserted.objects(node, RDFS.subClassOf), key=str):
                    if o == start and node != start:
                        end = node
                        break
                    if o in members and o not in back:
                        back[o] = node
                        nxt.append(o)
                if end is not None:
                    break
            frontier = nxt
        path = [end]
        while back[path[-1]] is not None:
            path.append(back[path[-1]])
        cycle = list(reversed(path)) + [start]
        edges = [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)]
        where = [_axiom_file(files, (s, RDFS.subClassOf, o)) for s, o in edges]
        text = ", ".join(f"{_term(asserted, s)} rdfs:subClassOf {_term(asserted, o)}({w})" for (s, o), w in zip(edges, where))
        size = f" (강한 연결 요소 클래스 {len(comp)}개)" if len(comp) > len(edges) else ""
        errors.append(f"[{gate}] {where[0]}: 단언된 rdfs:subClassOf 가 순환한다 — {text}{size}")
    return errors
```
<!-- 인용 끝 -->
