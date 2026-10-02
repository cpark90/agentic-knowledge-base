---
id: https://agentic-knowledge-base.dev/id/chunk/7985ad2f-b7d8-45b2-8d1f-a688617bb614
type: artifact
level: executable
title_ko: 함수 gate_catalogue_section (tools/doccheck.py)
title: function gate_catalogue_section in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197
---
**함수** — `gate_catalogue_section(lines)` 다. 게이트 총람 절의 줄들과 그 시작 줄 번호 — 절은 다음 `## ` 머리에서 끝난다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gate_catalogue_section(lines: list[str]) -> tuple[list[str], int]:
    """게이트 총람 절의 줄들과 그 시작 줄 번호 — 절은 다음 `## ` 머리에서 끝난다."""
    start = next((i for i, l in enumerate(lines) if l.startswith(GATE_CATALOGUE_HEADING)), -1)
    if start < 0:
        return [], 0
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return lines[start:end], start + 1
```
<!-- 인용 끝 -->
