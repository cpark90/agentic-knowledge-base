---
id: https://agentic-knowledge-base.dev/id/chunk/a45854d1-6d8a-4a1a-890e-a55aa166d992
type: artifact
level: executable
title_ko: 함수 check_labels (tools/validate.py)
title: function check_labels in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8d31b7a9-85c6-48b3-875b-1223f473d503]
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `check_labels(per_file)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_labels(per_file: dict[str, Graph]) -> list[str]:
    errors = []
    for path, g in per_file.items():
        for term in kb_lib.defined_terms(g):
            langs = {
                lbl.language
                for lbl in g.objects(term, RDFS.label)
                if getattr(lbl, "language", None)
            }
            missing = {"ko", "en"} - langs
            if missing:
                errors.append(
                    f"[{LABELS}] {path}: {g.qname(term)} 에 rdfs:label 누락 (언어: {sorted(missing)})"
                )
            if (term, SKOS.definition, None) not in g:
                errors.append(f"[{LABELS}] {path}: {g.qname(term)} 에 skos:definition 없음")
    return errors
```
<!-- 인용 끝 -->
