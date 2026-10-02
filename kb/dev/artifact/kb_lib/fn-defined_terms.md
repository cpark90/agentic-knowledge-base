---
id: https://agentic-knowledge-base.dev/id/chunk/8d31b7a9-85c6-48b3-875b-1223f473d503
type: artifact
level: executable
title_ko: 함수 defined_terms (tools/kb_lib.py)
title: function defined_terms in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
---
**함수** — `defined_terms(g)` 다. 그래프가 정의하는 agt: 용어(클래스·속성·개체)의 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def defined_terms(g: Graph):
    """그래프가 정의하는 agt: 용어(클래스·속성·개체)의 집합."""
    terms = set()
    for t in DEFINING_TYPES:
        for s in g.subjects(RDF.type, t):
            if isinstance(s, URIRef) and str(s).startswith(str(AGT)):
                terms.add(s)
    return terms
```
<!-- 인용 끝 -->
