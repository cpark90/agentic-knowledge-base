---
id: https://agentic-knowledge-base.dev/id/chunk/2aa8020a-1553-48b5-8a54-b93aab820bbe
type: artifact
level: executable
title_ko: 함수 plane_of_node (tools/kb_lib.py)
title: function plane_of_node in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `plane_of_node(g, c)` 다. 청크 노드의 plane — rdf:type 가운데 plane 청크 클래스인 것(plane_of_class).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def plane_of_node(g: Graph, c) -> str:
    """청크 노드의 plane — rdf:type 가운데 plane 청크 클래스인 것(plane_of_class). 실체 클래스는 건너뛴다. 없으면 빈 문자열이다."""
    for t in g.objects(c, RDF.type):
        plane = plane_of_class(t)
        if plane:
            return plane
    return ""
```
<!-- 인용 끝 -->
