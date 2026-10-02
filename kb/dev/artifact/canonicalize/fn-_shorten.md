---
id: https://agentic-knowledge-base.dev/id/chunk/0dbea10c-f751-4ac3-b58a-ee9b7bb1ba4b
type: artifact
level: executable
title_ko: 함수 _shorten (tools/canonicalize.py)
title: function _shorten in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
---
**함수** — `_shorten(iri, prefixes)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _shorten(iri: str, prefixes: dict[str, str]) -> str:
    for p, ns in prefixes.items():
        if iri.startswith(ns):
            local = iri[len(ns):]
            if _PN_LOCAL.match(local) and not local.endswith("."):
                return f"{p}:{local}"
    return f"<{iri}>"
```
<!-- 인용 끝 -->
