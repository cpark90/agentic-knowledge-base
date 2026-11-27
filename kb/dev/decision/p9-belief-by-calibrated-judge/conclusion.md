---
id: https://agentic-knowledge-base.dev/id/chunk/88b97e4d-57de-4ec9-8824-5decb2f9184f
type: decision
level: logical
title_ko: 믿음 정도는 판정자의 확신도를 사람 정답 라벨로 보정한 값이다
title: Degree of belief is the judge's confidence calibrated on human ground-truth labels
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}]
layer: methodology
composite: {id: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d, title_ko: 사람 라벨로 보정한 판정자 확신도, title: Judge confidence calibrated on human labels}
part_of: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d
---
**결론** — 세션 판정자가 링크·후보마다 성립 여부와 확신도를 내고, 사람 정답 라벨 표본으로 확신도를 보정한 값을 믿음 정도로 둔다. 보정은 사람 라벨 표본이 20건 이상이면 적용한다(Q186-b).

**보정 방법** — Platt 보정이다. 판정 확신도 p의 로짓 ln(p/(1−p))을 입력으로 하는 로지스틱 회귀 σ(a·x + b)를 사람 라벨에 최대 우도로 맞춘다. 매개변수는 기울기 a와 절편 b의 둘이다.

**평가 방식** — 하나씩 빼는 교차 검증이다. 항목 i의 보정값은 i를 뺀 나머지 표본으로 맞춘 식으로 계산하고, 합격 기준의 술어 1(Brier)과 술어 2(신뢰도 구간)는 그 값으로 판정한다. 맞춘 표본으로 평가하지 않는다. 계산은 `tools/belief_calibration.py`가 하고 결과는 `//kg:belief_calibration`이 낸다.
