---
id: https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8
type: artifact
level: executable
title_ko: 함수 chunk_planes (tools/kb_lib.py)
title: function chunk_planes in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2aa8020a-1553-48b5-8a54-b93aab820bbe]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `chunk_planes(g)` 다. 청크 → plane 이름 — rdf:type 중 plane 청크 클래스인 첫 것 (plane_of_class, 정의처 chunk2kg.CLASS_PLANE).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def chunk_planes(g: Graph) -> dict:
    """청크 → plane 이름 — rdf:type 중 plane 청크 클래스인 첫 것 (plane_of_class, 정의처 chunk2kg.CLASS_PLANE)."""
    out = {}
    for c in g.subjects(AGT.tokenCount, None):
        plane = plane_of_node(g, c)
        if plane:
            out[c] = plane
    return out
```
<!-- 인용 끝 -->
