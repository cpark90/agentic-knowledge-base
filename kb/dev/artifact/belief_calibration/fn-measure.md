---
id: https://agentic-knowledge-base.dev/id/chunk/7669e3bf-cc66-40bb-b8db-155171086ea6
type: artifact
level: executable
title_ko: 함수 measure (tools/belief_calibration.py)
title: function measure in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5e436aa5-2cdd-42eb-ad10-ad7050c25ebf, https://agentic-knowledge-base.dev/id/chunk/69a84092-df60-4eb4-aed8-32d7724ec3f2]
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `measure(pairs)` 다. [(p_i, y_i)] → 측정 하나.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def measure(pairs: list[tuple[Fraction, int]]) -> dict:
    """[(p_i, y_i)] → 측정 하나. n 이 0 이면 {'n': 0} 이다."""
    n = len(pairs)
    if not n:
        return {"n": 0}
    ybar = Fraction(sum(y for _, y in pairs), n)
    brier = sum((p - y) ** 2 for p, y in pairs) / n
    base = sum((ybar - y) ** 2 for _, y in pairs) / n
    bins = []
    for k, (_, _, name) in enumerate(BINS):
        items = [(p, y) for p, y in pairs if bin_of(p) == k]
        if not items:
            bins.append({"name": name, "n": 0})
            continue
        nk, hits = len(items), sum(y for _, y in items)
        pbar = sum(p for p, _ in items) / nk
        lo, hi = binom_quantile(nk, pbar, Q_LO), binom_quantile(nk, pbar, Q_HI)
        bins.append({"name": name, "n": nk, "pbar": pbar, "hits": hits, "lo": lo, "hi": hi, "inside": lo <= hits <= hi})
    p2 = all(b["inside"] for b in bins if b["n"]) if n < BINS_UNDER else None
    return {"n": n, "pos": sum(y for _, y in pairs), "ybar": ybar, "brier": brier, "base": base, "p1": brier < base, "p2": p2, "bins": bins}
```
<!-- 인용 끝 -->
