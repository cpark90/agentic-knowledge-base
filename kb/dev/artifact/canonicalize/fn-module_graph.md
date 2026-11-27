---
id: https://agentic-knowledge-base.dev/id/chunk/d8eae456-6327-477b-8cb2-b53024a57d90
type: artifact
level: executable
title_ko: 함수 module_graph (tools/canonicalize.py)
title: function module_graph in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/48c79ecc-7011-4d44-bc3e-be0cc65036b7
---
**함수** — `module_graph(iri, files, imports)` 다. 모듈 하나의 합본 그래프 — 원본 파일의 합집합에 owl:Ontology 머리와 그 모듈의 owl:imports 를 더한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def module_graph(iri: str, files: list[str], imports: list[str]) -> Graph:
    """모듈 하나의 합본 그래프 — 원본 파일의 합집합에 owl:Ontology 머리와 그 모듈의 owl:imports 를 더한다."""
    g = Graph()
    for f in files:
        g.parse(f, format="turtle")
    node = URIRef(iri)
    g.add((node, RDF.type, OWL.Ontology))
    for imp in imports:
        g.add((node, OWL.imports, URIRef(imp)))
    return g
```
<!-- 인용 끝 -->
