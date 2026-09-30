---
id: https://agentic-knowledge-base.dev/id/chunk/76e74bc8-5ade-4a57-8804-6270a72fd693
type: artifact
level: executable
title_ko: 함수 _gendoc_tables (tools/kb_lib.py)
title: function _gendoc_tables in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `_gendoc_tables(rows)` 다. 연속한 표 줄들의 묶음 — (줄 번호, 줄).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_tables(rows: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    """연속한 표 줄들의 묶음 — (줄 번호, 줄). 펜스 밖의 '|' 로 시작하는 줄이 표다."""
    blocks: list[list[tuple[int, str]]] = []
    cur: list[tuple[int, str]] = []
    prev = None
    for ln, line in rows:
        if line.lstrip().startswith("|"):
            if cur and prev is not None and ln != prev + 1:
                blocks.append(cur)
                cur = []
            cur.append((ln, line))
        elif cur:
            blocks.append(cur)
            cur = []
        prev = ln
    if cur:
        blocks.append(cur)
    return blocks
```
<!-- 인용 끝 -->
