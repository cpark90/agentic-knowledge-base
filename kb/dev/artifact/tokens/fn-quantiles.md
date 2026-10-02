---
id: https://agentic-knowledge-base.dev/id/chunk/2dcb7b2a-d62d-446a-abd6-5f776c990c7e
type: artifact
level: executable
title_ko: 함수 quantiles (tools/tokens.py)
title: function quantiles in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee6ebd51-06bf-439a-875f-bf4afa341c35
---
**함수** — `quantiles(values)` 다. (최소, 1사분위, 중앙, 3사분위, 최대) — 표본이 하나여도 다섯 값을 낸다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def quantiles(values: list[int]) -> tuple[int, int, int, int, int]:
    """(최소, 1사분위, 중앙, 3사분위, 최대) — 표본이 하나여도 다섯 값을 낸다."""
    s = sorted(values)
    if len(s) == 1:
        return (s[0],) * 5
    q1, _, q3 = statistics.quantiles(s, n=4, method="inclusive")
    return s[0], round(q1), round(statistics.median(s)), round(q3), s[-1]
```
<!-- 인용 끝 -->
