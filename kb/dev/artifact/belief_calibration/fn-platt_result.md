---
id: https://agentic-knowledge-base.dev/id/chunk/a02757cf-661e-45f1-b13e-7a3916c3a854
type: artifact
level: executable
title_ko: 함수 platt_result (tools/belief_calibration.py)
title: function platt_result in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7669e3bf-cc66-40bb-b8db-155171086ea6, https://agentic-knowledge-base.dev/id/chunk/bf33cf95-5df1-495f-8130-22031411177b, https://agentic-knowledge-base.dev/id/chunk/f77d538c-0691-4335-8f96-eec9429afa95]
part_of: https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390
---
**함수** — `platt_result(pairs)` 다. 보정 전 C 의 [(p_i, y_i)] → 보정한 C 의 결과.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def platt_result(pairs: list[tuple[Fraction, int]]) -> dict:
    """보정 전 C 의 [(p_i, y_i)] → 보정한 C 의 결과. status 는 'ok'(LOO 값의 측정 measure 를 싣는다) · 'short'(n < CALIBRATION_MIN) ·
    'fail'(보정 불가, reason) 셋이다. 'ok' 와 'fail' 은 전체 표본 맞춤 full 을 싣는다 — 보정 식의 기록이고 판정 값이 아니다."""
    n = len(pairs)
    if n < CALIBRATION_MIN:
        return {"status": "short", "n": n}
    full = platt_fit(pairs)
    folds, reason = platt_loo(pairs)
    if reason is not None:
        return {"status": "fail", "n": n, "full": full, "reason": reason}
    return {"status": "ok", "n": n, "full": full, "folds": folds,
            "measure": measure([(Fraction(q), y) for (_, _, _, q), (_, y) in zip(folds, pairs)])}
```
<!-- 인용 끝 -->
