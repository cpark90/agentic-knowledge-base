---
id: https://agentic-knowledge-base.dev/id/chunk/4b222206-08d6-4720-9b58-644cd8cdd017
type: artifact
level: executable
title_ko: 함수 gate_catalogue_block (tools/kb_lib.py)
title: function gate_catalogue_block in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/81809a6f-d845-4673-8a0f-b53283ae332c
---
**함수** — `gate_catalogue_block(text)` 다. 문서 줄들에서 생성 구간의 (여는 표지 줄 색인, 닫는 표지 줄 색인) — 표지가 하나씩 정확히 없으면 None 이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gate_catalogue_block(text: str) -> tuple[int, int] | None:
    """문서 줄들에서 생성 구간의 (여는 표지 줄 색인, 닫는 표지 줄 색인) — 표지가 하나씩 정확히 없으면 None 이다."""
    lines = text.split("\n")
    opens = [i for i, l in enumerate(lines) if l == GATE_CATALOGUE_OPEN]
    closes = [i for i, l in enumerate(lines) if l == GATE_CATALOGUE_CLOSE]
    if len(opens) != 1 or len(closes) != 1 or closes[0] < opens[0]:
        return None
    return opens[0], closes[0]
```
<!-- 인용 끝 -->
