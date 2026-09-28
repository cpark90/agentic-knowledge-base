---
id: https://agentic-knowledge-base.dev/id/chunk/8c9efac1-c449-42bf-9a95-94c571603b41
type: decision
level: abstract
title_ko: 시나리오 요인 — 정지 규칙 없는 반복 라운드가 노출하는 현상
title: Scenario factors — the phenomena exposed by repeated rounds without a stop rule
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/unknownStopCondition, https://agentic-knowledge-base.dev/agt/worksetBudgetOverrun]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ba04ada0-2f37-4bc2-ad15-c2ac77fbe18e
specializationOf: https://agentic-knowledge-base.dev/id/chunk/c1ad3b4a-d86c-4c63-ab91-7294a56a76e2
---
**요인** — 노출하려는 현상은 `agt:unknownStopCondition`(P15)이 주이고 `agt:worksetBudgetOverrun`(P6)이 부다. 라운드가 멈추지 않으면 예산이 먼저 소진되므로 둘이 같은 자극에서 함께 드러난다.

주입하는 한정자는 `agt:missingQualifier` 하나다. 정지 규칙이 틀린 것이 아니라 없는 것이 이 부류의 결함 형태다. 부류가 주입하는 것은 정지 규칙의 부재이고, 라운드가 끝나는 조건이 선언되어 있는가를 묻는다.

기여하는 검증 목표는 `kb/vv/goal/verification-round-stop-rule.md`(`https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78`)다. 정지 규칙 없는 강화가 진행 대신 안전 정지로 가는가를 이 부류가 자극한다.

미확정: 라운드 수 대비 신규 결함 수의 관측 수단이 없어 logical 높이의 판정식을 아직 쓸 수 없다.
