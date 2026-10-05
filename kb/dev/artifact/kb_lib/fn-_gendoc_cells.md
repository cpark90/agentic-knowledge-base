---
id: https://agentic-knowledge-base.dev/id/chunk/df94eed1-fa2e-4203-9b68-c415799b6b9a
type: artifact
level: executable
title_ko: 함수 _gendoc_cells (tools/kb_lib.py)
title: function _gendoc_cells in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `_gendoc_cells(line)` 다. 표 한 행의 셀 — 이스케이프된 `\|` 는 셀 구분이 아니다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_cells(line: str) -> list[str]:
    """표 한 행의 셀 — 이스케이프된 `\\|` 는 셀 구분이 아니다 (GFM 표의 규칙, 생성기가 셀 안의 `|` 를 그렇게 낸다)."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]
```
<!-- 인용 끝 -->
