---
id: https://agentic-knowledge-base.dev/id/chunk/0ce6acc5-e836-4236-a940-b32c38e5c86b
type: artifact
level: executable
title_ko: 함수 gendoc_tree_notice (tools/kb_lib.py)
title: function gendoc_tree_notice in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_tree_notice(source, target)` 다. G7 — 생성 트리 파일(SKILL·BUILD)의 성격 경고.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_tree_notice(source: str, target: str) -> str:
    """G7 — 생성 트리 파일(SKILL·BUILD)의 성격 경고. target 은 드리프트를 잡는 검사 타깃이다."""
    return f"{GENDOC_TREE_MARK} 원본은 {source}이다. 검사: `{target}`. {GENDOC_DETERMINISTIC_NOTE}"
```
<!-- 인용 끝 -->
