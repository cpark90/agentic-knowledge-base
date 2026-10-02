---
id: https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c
type: artifact
level: executable
title_ko: 함수 gendoc_view_notice (tools/kb_lib.py)
title: function gendoc_view_notice in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_view_notice(source)` 다. G7 — Bazel 뷰의 성격 경고.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_view_notice(source: str) -> str:
    """G7 — Bazel 뷰의 성격 경고. source 는 고칠 원본(청크·frontmatter·그래프)이다."""
    return f"{GENDOC_VIEW_MARK} 저장하지 않고 인용한다. 고칠 것은 {source}이다 (`p12-documents-are-generated`)"
```
<!-- 인용 끝 -->
