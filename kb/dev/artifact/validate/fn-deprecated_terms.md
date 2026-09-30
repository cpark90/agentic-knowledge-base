---
id: https://agentic-knowledge-base.dev/id/chunk/cd8732ca-a14b-4a4b-a190-8317553867ad
type: artifact
level: executable
title_ko: 함수 deprecated_terms (tools/validate.py)
title: function deprecated_terms in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/040c4845-cfe9-495a-91c7-f98702044ca6
---
**함수** — `deprecated_terms(ontology)` 다. 폐기된 용어 — owl:deprecated true 가 기준이고, 라벨의 "(deprecated)"/"(폐기)" 표기도 인정한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def deprecated_terms(ontology: Graph) -> set[URIRef]:
    """폐기된 용어 — owl:deprecated true 가 기준이고, 라벨의 "(deprecated)"/"(폐기)" 표기도 인정한다."""
    terms = {s for s, v in ontology.subject_objects(OWL.deprecated) if str(v).lower() == "true"}
    for s, lbl in ontology.subject_objects(RDFS.label):
        if "(deprecated)" in str(lbl) or "(폐기)" in str(lbl):
            terms.add(s)
    return {t for t in terms if isinstance(t, URIRef)}
```
<!-- 인용 끝 -->
