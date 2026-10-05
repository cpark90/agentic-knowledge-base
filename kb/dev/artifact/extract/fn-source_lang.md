---
id: https://agentic-knowledge-base.dev/id/chunk/8b283654-cf54-4445-a8f4-95c8bef0f888
type: artifact
level: executable
title_ko: 함수 source_lang (tools/extract.py)
title: function source_lang in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**함수** — `source_lang(src_rel)` 다. 인용 펜스의 언어 — `.bzl` 이면 starlark, 그 밖의 소스 파일은 python 이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_lang(src_rel: str) -> str:
    """인용 펜스의 언어 — `.bzl` 이면 starlark, 그 밖의 소스 파일은 python 이다."""
    return "starlark" if src_rel.endswith(STARLARK_SUFFIX) else "python"
```
<!-- 인용 끝 -->
