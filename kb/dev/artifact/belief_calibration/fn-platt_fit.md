---
id: https://agentic-knowledge-base.dev/id/chunk/bf33cf95-5df1-495f-8130-22031411177b
type: artifact
level: executable
title_ko: 함수 platt_fit (tools/belief_calibration.py)
title: function platt_fit in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `platt_fit(pairs, max_iter)` 다. [(p_i, y_i)] → Platt 보정 식의 (a, b, 반복 수) 또는 보정 불가 사유(문자열).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def platt_fit(pairs: list[tuple[Fraction, int]], max_iter: int = PLATT_MAX_ITER) -> tuple[float, float, int] | str:
    """[(p_i, y_i)] → Platt 보정 식의 (a, b, 반복 수) 또는 보정 불가 사유(문자열). x_i 는 [ε, 1 − ε]로 자른 p_i 의 로짓이고, a·b 는
    q = σ(a·x + b)의 로그 우도를 최대화하는 뉴턴법으로 맞춘다. 라벨이 한 값뿐이거나 분리된 표본, 특이한 헤세 행렬, 반복 상한 안의 미수렴은
    사유를 돌려준다 — 값을 조용히 내지 않는다."""
    xs = [log(p / (1 - p)) for p in (min(max(float(p), PLATT_EPS), 1 - PLATT_EPS) for p, _ in pairs)]
    ys = [y for _, y in pairs]
    pos, neg = [x for x, y in zip(xs, ys) if y], [x for x, y in zip(xs, ys) if not y]
    if not pos or not neg:
        return "라벨이 한 값뿐이므로 최대 우도 해가 무한이다"
    if max(neg) <= min(pos) or max(pos) <= min(neg):
        return "분리 표본이다. 한 라벨의 로짓이 모두 다른 라벨의 로짓 이하이므로 최대 우도 해가 무한이다"

    def sigmoid(z: float) -> float:
        return 1 / (1 + exp(-z)) if z >= 0 else exp(z) / (1 + exp(z))

    def loglik(a: float, b: float) -> float:   # log σ(z) = −log(1 + e^(−z)), log(1 − σ(z)) = log σ(−z)
        return -sum(log1p(exp(-abs(z))) + max(-z if y else z, 0) for z, y in ((a * x + b, y) for x, y in zip(xs, ys)))

    a = b = 0.0
    for it in range(1, max_iter + 1):
        qs = [sigmoid(a * x + b) for x in xs]
        ga, gb = sum((y - q) * x for x, y, q in zip(xs, ys, qs)), sum(y - q for y, q in zip(ys, qs))
        ws = [q * (1 - q) for q in qs]
        haa, hab, hbb = sum(w * x * x for w, x in zip(ws, xs)), sum(w * x for w, x in zip(ws, xs)), sum(ws)
        det = haa * hbb - hab * hab
        if not (isfinite(det) and det > 0):
            return f"헤세 행렬이 반복 {it}에서 특이해 맞춤을 계속할 수 없다"
        da, db = (hbb * ga - hab * gb) / det, (haa * gb - hab * ga) / det
        step, base = 1.0, loglik(a, b)
        for _ in range(PLATT_HALVINGS):
            if loglik(a + step * da, b + step * db) >= base:
                break
            step /= 2
        a, b = a + step * da, b + step * db
        if max(abs(step * da), abs(step * db)) < PLATT_TOL:
            return a, b, it
    return f"뉴턴법이 반복 상한 {max_iter}번 안에 수렴하지 않았다"
```
<!-- 인용 끝 -->
