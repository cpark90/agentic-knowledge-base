---
id: https://agentic-knowledge-base.dev/id/chunk/2dd3cb51-cd3b-45a5-979a-41cc7e02aeae
type: artifact
level: executable
title_ko: 함수 age_cell (tools/open_questions.py)
title: function age_cell in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `age_cell(days)` 다. 나이 셀 — 일수다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def age_cell(days) -> str:
    """나이 셀 — 일수다. 시각이 없으면 생성 문서의 빈 값 표기(`kb_lib.NONE_MARK`)를 쓴다."""
    return kb_lib.NONE_MARK if days is None else str(days)
```
<!-- 인용 끝 -->
