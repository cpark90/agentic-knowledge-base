---
id: https://agentic-knowledge-base.dev/id/chunk/f77d538c-0691-4335-8f96-eec9429afa95
type: artifact
level: executable
title_ko: 함수 platt_loo (tools/belief_calibration.py)
title: function platt_loo in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bf33cf95-5df1-495f-8130-22031411177b]
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `platt_loo(pairs)` 다. [(p_i, y_i)] → (항목마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def platt_loo(pairs: list[tuple[Fraction, int]]) -> tuple[list[tuple[float, float, int, float]], str | None]:
    """[(p_i, y_i)] → (항목마다 (a, b, 반복 수, q_i), 보정 불가 사유 또는 None). q_i 는 i 를 뺀 나머지로 맞춘 식의 i 의 보정값이다.
    한 번의 맞춤이라도 보정 불가이면 값 목록은 비고 첫 사유를 낸다."""
    out = []
    for i, (p, _) in enumerate(pairs):
        fit = platt_fit(pairs[:i] + pairs[i + 1:])
        if isinstance(fit, str):
            return [], f"항목 {i + 1}을 뺀 맞춤이 보정 불가다. {fit}"
        a, b, it = fit
        c = min(max(float(p), PLATT_EPS), 1 - PLATT_EPS)   # platt_fit 과 같은 자름
        x = log(c / (1 - c))
        out.append((a, b, it, 1 / (1 + exp(-(a * x + b)))))
    return out, None
```
<!-- 인용 끝 -->
