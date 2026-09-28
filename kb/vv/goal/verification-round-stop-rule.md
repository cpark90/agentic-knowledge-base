---
id: https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78
type: requirement
level: functional
pattern: unwanted-behaviour
title_ko: 강화 라운드에 정지 규칙이 없으면 체계가 진행 대신 안전 정지해야 한다
title: When a hardening round has no stop rule, the system must come to a safe stop instead of proceeding
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/unknownStopCondition, https://agentic-knowledge-base.dev/agt/worksetBudgetOverrun]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:20:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
---
**검증 목표** — 강화·검증 라운드에 정지 규칙이 없어 라운드마다 새 결함이 나오는 상황에서 체계가 다음 라운드를 열지 않고 채널로 되돌린다는 것이 보여져야 한다. 이 목표가 다루는 위험은 현상 `agt:unknownStopCondition`(P15)이다.

- **이해관계자**: 검증자 · **관심사**: 검증 수단의 신뢰

**무엇을 관측하면 성립하는가**

- 실행 기록(`kb/vv/run/`)이 라운드마다 신규 결함 수를 남기고, 연속한 두 라운드에서 그 수가 줄지 않으면 다음 라운드가 열리지 않는다.
- 멈춘 자리가 임의가 아니라 규칙이라는 것이 판정 주석 하나로 남고, 그 주석의 `해소:`가 진행 여부를 가른다.
- 예산을 소진해 멈춘 경우와 정지 규칙으로 멈춘 경우가 실행 기록에서 구분된다.
- 이 목표는 기존 검증 목표 35건과 파생의 출처가 다르다. 35건은 게이트·음성 시험을 사슬로 묶은 것이고 이 목표는 위험 분석 G1의 현상에서 나왔다. 파생의 표지는 본문의 현상 IRI 인용이며 `agt:usesConcept` 로 질의된다.

미확정: 라운드 수 대비 신규 결함 수를 재는 관측 수단이 없다 — 현상 개체의 `agt:observationMeans`가 `미확정`이다.
