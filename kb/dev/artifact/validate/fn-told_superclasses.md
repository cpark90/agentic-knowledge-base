---
id: https://agentic-knowledge-base.dev/id/chunk/da2d5667-a0ed-4a3d-bfa8-6a83213f1d3f
type: artifact
level: executable
title_ko: 함수 told_superclasses (tools/validate.py)
title: function told_superclasses in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `told_superclasses(g, cls)` 다. 단언된 계층에서 cls 의 상위 노드(cls 자신 포함) — 단언 rdfs:subClassOf 와 양방향 owl:equivalentClass 를 따라간다(빈 노드 포함).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def told_superclasses(g: Graph, cls) -> set:
    """단언된 계층에서 cls 의 상위 노드(cls 자신 포함) — 단언 rdfs:subClassOf 와 양방향 owl:equivalentClass 를 따라간다(빈 노드 포함).

    프로브 폐포의 상하 관계는 불만족 판정에 쓰지 못한다 — owl:Nothing 이 모든 클래스의 하위(scm-cls)라 불만족 클래스는 폐포에서
    모든 클래스의 하위가 된다. 그래서 불만족의 근거 공리와 근원·하위의 구분은 단언된 계층을 읽는다.
    """
    seen, todo = {cls}, [cls]
    while todo:
        node = todo.pop()
        for n in (*g.objects(node, RDFS.subClassOf), *g.objects(node, OWL.equivalentClass), *g.subjects(OWL.equivalentClass, node)):
            if n not in seen:
                seen.add(n)
                todo.append(n)
    return seen
```
<!-- 인용 끝 -->
