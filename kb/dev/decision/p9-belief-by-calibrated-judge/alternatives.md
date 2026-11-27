---
id: https://agentic-knowledge-base.dev/id/chunk/0643cbf2-e3aa-4933-8b74-bb24c85d0703
type: decision
level: logical
title_ko: 판정자 보정 후보 곁의 두 후보
title: The two candidates beside the calibrated-judge candidate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:20:05+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d
---
**대안** — 같은 공간의 다른 후보는 둘이다. 후보 `p9-belief-by-evidence-kind-rank`의 증거 종류 서열 가중 점수와 후보 `p9-belief-by-beta-binomial`의 베타-이항 사후는 증거 기록에서 값을 낸다. 이 후보만 증거 기록 밖의 판정자 출력을 원천으로 쓴다.

**보정 방법의 다른 후보** (Q186-b에서 고르지 않음) — 구간 빈도(확신도 구간마다 관측 빈도로 바꾼다)는 구간마다 표본이 필요해 지금 분포(1·12·7)로는 쓸 수 없다. 등위 회귀는 단조 계단 함수라 매개변수가 표본 수만큼 늘어 20건에서 과적합한다. 절편만 맞추는 보정(매개변수 하나)은 평균의 어긋남만 고치고 확신도의 퍼짐을 고치지 못한다.

**충돌** — 이 후보는 확정된 결정 하나와 어긋난다. `p8-judge-session-agreement`의 규칙 ②는 확신도가 자기 보고라 캘리브레이션을 재지 않는다고 정했으나, 이 후보는 그 확신도를 사람 정답 라벨로 보정한다. 그래서 이 후보가 확정되면 ②는 "확신도는 사람 정답 라벨 표본이 20건 이상일 때 보정해 믿음 정도로 쓰고, 그 전에는 판정 불가로 적는다"로 바뀌어야 한다.
