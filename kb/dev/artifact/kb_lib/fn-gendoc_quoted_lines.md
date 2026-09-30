---
id: https://agentic-knowledge-base.dev/id/chunk/68b9e471-9de9-45d6-8c8c-4d7b5b1609b2
type: artifact
level: executable
title_ko: 함수 gendoc_quoted_lines (tools/kb_lib.py)
title: function gendoc_quoted_lines in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_quoted_lines(lines)` 다. 인용 구역에 속하는 1-기준 줄 번호.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_quoted_lines(lines: list[str]) -> set[int]:
    """인용 구역에 속하는 1-기준 줄 번호."""
    out: set[int] = set()
    inside = False
    for i, line in enumerate(lines, start=1):
        s = line.strip()
        if s == GENDOC_QUOTE_OPEN:
            inside = True
        if inside or s.endswith(GENDOC_QUOTE_LINE):
            out.add(i)
        if s == GENDOC_QUOTE_CLOSE:
            inside = False
    return out
```
<!-- 인용 끝 -->
