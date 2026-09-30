---
id: https://agentic-knowledge-base.dev/id/chunk/e9b943fe-3fee-4433-8018-038f1deb41c6
type: artifact
level: executable
title_ko: 함수 check_boundary (tools/validate.py)
title: function check_boundary in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `check_boundary(per_file)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_boundary(per_file: dict[str, Graph]) -> list[str]:
    owner: dict[URIRef, str] = {}
    errors = []
    for path, g in per_file.items():
        for term in kb_lib.defined_terms(g):
            if term in owner and owner[term] != path:
                errors.append(
                    f"[boundary] {path}: {g.qname(term)} 가 {owner[term]} 에서 이미 정의됨 — 한 용어는 한 모듈 파일에서만 정의된다 (2.3절)"
                )
            owner.setdefault(term, path)
    return errors
```
<!-- 인용 끝 -->
