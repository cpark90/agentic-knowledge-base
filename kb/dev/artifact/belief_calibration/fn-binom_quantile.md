---
id: https://agentic-knowledge-base.dev/id/chunk/5e436aa5-2cdd-42eb-ad10-ad7050c25ebf
type: artifact
level: executable
title_ko: 함수 binom_quantile (tools/belief_calibration.py)
title: function binom_quantile in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `binom_quantile(n, p, q)` 다. Binomial(n, p) 의 q 분위수 — 누적분포 F(x) ≥ q 인 가장 작은 정수 x.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def binom_quantile(n: int, p: Fraction, q: Fraction) -> int:
    """Binomial(n, p) 의 q 분위수 — 누적분포 F(x) ≥ q 인 가장 작은 정수 x. 분수로 정확히 계산한다(외부 의존 없음)."""
    acc = Fraction(0)
    for x in range(n + 1):
        acc += comb(n, x) * p ** x * (1 - p) ** (n - x)
        if acc >= q:
            return x
    return n
```
<!-- 인용 끝 -->
