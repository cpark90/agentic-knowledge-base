---
id: https://agentic-knowledge-base.dev/id/chunk/ba1f7e1e-92c3-4692-9023-f2fb9dddbbc4
type: artifact
level: executable
title_ko: 함수 check_vocab (tools/validate.py)
title: function check_vocab in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `check_vocab(data_files, ontology)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_vocab(data_files: dict[str, Graph], ontology: Graph) -> list[str]:
    defined = kb_lib.defined_terms(ontology)
    errors = []
    for path, g in data_files.items():
        preds = {p for p in g.predicates() if isinstance(p, URIRef)}
        for p in sorted(preds):
            iri = str(p)
            if kb_lib.is_well_known(iri):
                continue
            if p in defined:
                continue
            if iri.startswith(str(AGT)):
                errors.append(f"[vocab] {path}: 온톨로지에 정의되지 않은 agt: 술어 {iri}")
            else:
                errors.append(f"[vocab] {path}: 미등록 어휘의 술어 {iri} (0.3절 네임스페이스 참조)")
    return errors
```
<!-- 인용 끝 -->
