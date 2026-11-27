---
id: https://agentic-knowledge-base.dev/id/chunk/95d45893-5c33-4f3f-96b6-972c17dafbc2
type: decision
level: logical
title_ko: 판정자 보정 후보의 근거는 확신도 어휘와 과신의 측정이 이미 있다는 것이다
former_title_ko: ["판정자 보정 후보의 근거는 확신도 어휘와 과신의 실측이 이미 있다는 것이다"]
title: The calibrated-judge candidate rests on existing confidence vocabulary and measured overconfidence
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d
---
**근거** — 확신도 임계·보정 어휘(judge-threshold·judge-calibration 온톨로지, 구간 표본 하한 20)가 이미 있다. 판정자가 유저보다 높게 판정한 과신(확신도 0.93~0.97, 정확도 a 4/10 · b 3/10)도 측정됐다. 학습 판정자의 정확도·판별력·캘리브레이션을 재라는 결정(`p8-learned-environment-and-judge`)과도 맞는다. 대가는 사람 라벨 표본(Q91-b)이 차기 전에는 쓸 수 없다는 것이다.

**보정 조건과 방법의 개정** (Q186-b, 2026-11-27) — 첫 측정(S3)에서 보정 전 확신도의 Brier는 0.166으로 기저율 0.160보다 높았고, 평균 예측은 0.603, 참 비율은 0.800이었다. 실패의 꼴은 평균 수준의 어긋남이고, 보정이 고치는 결함이다. 옛 조건 "확신도 구간마다 표본 하한 20"은 확신도 분포(구간별 1·12·7)로는 표본 60 이상에서도 채워지지 않았다. 판정자 어휘의 구간 속성은 이미 폐기되었다(Q119-a). 그래서 조건을 합격 기준의 표본 하한(|S| ≥ 20)과 같은 수로 맞춘다. 표본 20건에 라벨 0이 4건이므로 매개변수가 둘인 Platt을 고른다. 같은 표본으로 맞추고 평가하면 값이 좋게 나오므로 하나씩 빼는 교차 검증으로 평가한다.
