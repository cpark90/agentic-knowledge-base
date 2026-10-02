---
id: https://agentic-knowledge-base.dev/id/chunk/a82c512c-7648-4b7c-b506-56a5a18e9cd5
type: artifact
level: executable
title_ko: 함수 log_chunk (tools/judge.py)
title: function log_chunk in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2b69cd72-19b5-4d4d-adc7-b20e75c687ce, https://agentic-knowledge-base.dev/id/chunk/8d622313-8c2c-4f87-9279-fce0b31cb0ff]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `log_chunk(rows, q, name, th, source, stamp)` 다. 판정 로그 청크 하나 — frontmatter + 본문.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def log_chunk(rows: list[dict], q: dict, name: str, th: dict, source: str, stamp: str) -> str:
    """판정 로그 청크 하나 — frontmatter + 본문."""
    return "\n".join(log_frontmatter(rows, q, name, th, stamp) + log_body(rows, q, name, th, source, stamp)) + "\n"
```
<!-- 인용 끝 -->
