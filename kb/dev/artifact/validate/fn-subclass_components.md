---
id: https://agentic-knowledge-base.dev/id/chunk/03af6d80-e46c-44f7-acd5-12d186d9bb75
type: artifact
level: executable
title_ko: 함수 subclass_components (tools/validate.py)
title: function subclass_components in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `subclass_components(asserted)` 다. 단언된 rdfs:subClassOf 간선(이름 IRI 사이)의 강한 연결 요소 중 클래스가 둘 이상인 것 — 각 요소는 정렬된 클래스 목록이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def subclass_components(asserted: Graph) -> list[list]:
    """단언된 rdfs:subClassOf 간선(이름 IRI 사이)의 강한 연결 요소 중 클래스가 둘 이상인 것 — 각 요소는 정렬된 클래스 목록이다.

    폐포가 아니라 단언 그래프를 본다 — 폐포의 반사적 공리와 동치가 낳은 상호 하위를 순환으로 세지 않는다. 자기 자신으로의 간선은
    폐포가 반사적으로 더하는 공리와 같아 계층을 무너뜨리지 않으므로 순환이 아니다. 반복형 Kosaraju 다.
    """
    succ: dict = {}
    pred: dict = {}
    for s, o in asserted.subject_objects(RDFS.subClassOf):
        if isinstance(s, URIRef) and isinstance(o, URIRef) and s != o:
            succ.setdefault(s, set()).add(o)
            pred.setdefault(o, set()).add(s)
    order, seen = [], set()
    for root in sorted(set(succ) | set(pred), key=str):
        if root in seen:
            continue
        seen.add(root)
        stack = [(root, iter(sorted(succ.get(root, ()), key=str)))]
        while stack:
            node, it = stack[-1]
            nxt = next((n for n in it if n not in seen), None)
            if nxt is None:
                order.append(node)
                stack.pop()
            else:
                seen.add(nxt)
                stack.append((nxt, iter(sorted(succ.get(nxt, ()), key=str))))
    comps, done = [], set()
    for root in reversed(order):
        if root in done:
            continue
        comp, todo = [], [root]
        done.add(root)
        while todo:
            node = todo.pop()
            comp.append(node)
            for n in pred.get(node, ()):
                if n not in done:
                    done.add(n)
                    todo.append(n)
        if len(comp) > 1:
            comps.append(sorted(comp, key=str))
    return sorted(comps, key=lambda c: str(c[0]))
```
<!-- 인용 끝 -->
