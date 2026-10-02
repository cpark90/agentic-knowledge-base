---
id: https://agentic-knowledge-base.dev/id/chunk/a2ba3352-fcbb-4d76-9b20-a5d8b6eb5402
type: artifact
level: executable
title_ko: 함수 _term (tools/canonicalize.py)
title: function _term in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/0dbea10c-f751-4ac3-b58a-ee9b7bb1ba4b]
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
---
**함수** — `_term(t, prefixes)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _term(t, prefixes: dict[str, str]) -> str:
    if isinstance(t, URIRef):
        return _shorten(str(t), prefixes)
    if isinstance(t, BNode):
        return f"_:{t}"
    if isinstance(t, Literal):
        s = t.n3()  # 전체 IRI datatype 포함
        if t.datatype:
            s = s[: s.rindex("^^")] + "^^" + _shorten(str(t.datatype), prefixes)
        return s
    return t.n3()
```
<!-- 인용 끝 -->
