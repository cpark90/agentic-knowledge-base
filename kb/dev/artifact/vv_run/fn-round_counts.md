---
id: https://agentic-knowledge-base.dev/id/chunk/f0e6f002-4d5d-46c0-abba-ab242b4572e4
type: artifact
level: executable
title_ko: 함수 round_counts (tools/vv_run.py)
title: function round_counts in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `round_counts(bounds, defects)` 다. 경계마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def round_counts(bounds: list[datetime], defects: list[datetime]) -> list[int]:
    """경계마다 new(n) — 직전 경계 뒤부터 그 경계까지(첫 라운드는 처음부터). verify 질의와 같은 정의다."""
    out, prev = [], None
    for b in bounds:
        out.append(sum(1 for t in defects if t <= b and (prev is None or t > prev)))
        prev = b
    return out
```
<!-- 인용 끝 -->
