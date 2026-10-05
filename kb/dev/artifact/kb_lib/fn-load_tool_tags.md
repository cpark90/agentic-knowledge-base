---
id: https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f
type: artifact
level: executable
title_ko: 함수 load_tool_tags (tools/kb_lib.py)
title: function load_tool_tags in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e]
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
---
**함수** — `load_tool_tags(path)` 다. `defs/kb.bzl` 의 `TOOL_TAGS` 리터럴 — 게이트가 아닌 도구 태그(입력 문제·보고)의 둘째 경계다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_tool_tags(path: str | Path | None = None) -> tuple[str, ...]:
    """`defs/kb.bzl` 의 `TOOL_TAGS` 리터럴 — 게이트가 아닌 도구 태그(입력 문제·보고)의 둘째 경계다."""
    return load_bzl_list(Path(path) if path else gates_bzl_path(), TOOL_TAGS_NAME)
```
<!-- 인용 끝 -->
