---
id: https://agentic-knowledge-base.dev/id/chunk/c32e7981-57d1-4c87-bd5a-a41189661360
type: artifact
level: executable
title_ko: 함수 gate_catalogue_ids (tools/doccheck.py)
title: function gate_catalogue_ids in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197
---
**함수** — `gate_catalogue_ids(section)` 다. 총람 표의 `id` 열에 적힌 게이트 id 전수 — 열 자리는 헤더 행이 정한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gate_catalogue_ids(section: list[str]) -> set[str]:
    """총람 표의 `id` 열에 적힌 게이트 id 전수 — 열 자리는 헤더 행이 정한다."""
    col = None
    out: set[str] = set()
    for line in section:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            col = cells.index(GATE_CATALOGUE_ID_COLUMN) if GATE_CATALOGUE_ID_COLUMN in cells else None
            continue
        if set(line.strip()) <= set("|-: ") or col is None or len(cells) <= col:
            continue
        out |= {m.group(1) for m in BACKTICK_TOKEN.finditer(cells[col])}
    return out
```
<!-- 인용 끝 -->
