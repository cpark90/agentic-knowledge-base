---
id: https://agentic-knowledge-base.dev/id/chunk/aa162d57-f8c9-4997-886c-33e23f8cab0a
type: artifact
level: executable
title_ko: 함수 kind_definitions (tools/label_sample.py)
title: function kind_definitions in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `kind_definitions(root)` 다. 링크 종류(agt: 지역명) → 한글 skos:definition — 온톨로지 모듈이 원본이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def kind_definitions(root: Path) -> dict[str, str]:
    """링크 종류(agt: 지역명) → 한글 skos:definition — 온톨로지 모듈이 원본이다."""
    from rdflib import Graph, Literal
    from rdflib.namespace import SKOS
    g = Graph()
    for f in sorted((root / "kb/ontology").rglob("*-ontology.ttl")):
        g.parse(f, format="turtle")
    out = {}
    for s, o in g.subject_objects(SKOS.definition):
        if str(s).startswith(str(kb_lib.AGT)) and isinstance(o, Literal) and o.language == "ko":
            out[str(s)[len(str(kb_lib.AGT)):]] = str(o)
    return out
```
<!-- 인용 끝 -->
