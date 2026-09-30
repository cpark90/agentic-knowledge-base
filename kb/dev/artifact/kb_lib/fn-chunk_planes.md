---
id: https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8
type: artifact
level: executable
title_ko: 함수 chunk_planes (tools/kb_lib.py)
title: function chunk_planes in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `chunk_planes(g)` 다. 청크 → plane 이름 — rdf:type 중 `…Chunk` 로 끝나는 첫 클래스 (metrics·weave 가 같은 규칙으로 plane 을 읽는다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def chunk_planes(g: Graph) -> dict:
    """청크 → plane 이름 — rdf:type 중 `…Chunk` 로 끝나는 첫 클래스 (metrics·weave 가 같은 규칙으로 plane 을 읽는다)."""
    out = {}
    for c in g.subjects(AGT.lineCount, None):
        for t in g.objects(c, RDF.type):
            name = str(t).split("/")[-1]
            if name.endswith("Chunk"):
                out[c] = name[: -len("Chunk")].lower()
                break
    return out
```
<!-- 인용 끝 -->
