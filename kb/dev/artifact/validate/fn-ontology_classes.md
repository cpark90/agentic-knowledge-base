---
id: https://agentic-knowledge-base.dev/id/chunk/785609a5-d625-4486-b3dc-b0429b1de31c
type: artifact
level: executable
title_ko: 함수 ontology_classes (tools/validate.py)
title: function ontology_classes in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `ontology_classes(onto_files)` 다. 판정 대상 클래스 — 온톨로지 파일이 `a owl:Class` 로 선언한 이름 IRI.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def ontology_classes(onto_files: dict[str, Graph]) -> set:
    """판정 대상 클래스 — 온톨로지 파일이 `a owl:Class` 로 선언한 이름 IRI. 빈 노드와 owl:Thing·owl:Nothing 은 뺀다."""
    return {s for g in onto_files.values() for s in g.subjects(RDF.type, OWL.Class)
            if isinstance(s, URIRef) and s not in (OWL.Thing, OWL.Nothing)}
```
<!-- 인용 끝 -->
