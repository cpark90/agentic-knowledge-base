---
id: https://agentic-knowledge-base.dev/id/chunk/f9f4e245-6a05-4f51-b5b5-532470213ed5
type: artifact
level: executable
title_ko: 함수 _namespace (tools/validate.py)
title: function _namespace in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `_namespace(iri)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _namespace(iri: URIRef) -> str:
    s = str(iri)
    return s[: max(s.rfind("#"), s.rfind("/")) + 1]
```
<!-- 인용 끝 -->
