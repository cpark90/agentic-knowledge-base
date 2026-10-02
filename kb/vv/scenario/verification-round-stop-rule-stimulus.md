---
id: https://agentic-knowledge-base.dev/id/chunk/c1ad3b4a-d86c-4c63-ab91-7294a56a76e2
type: decision
level: abstract
title_ko: 시나리오 자극 — 정지 규칙 없는 반복 라운드
title: Scenario stimulus — repeated rounds without a stop rule
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78]
part_of: https://agentic-knowledge-base.dev/id/composite/ba04ada0-2f37-4bc2-ad15-c2ac77fbe18e
composite: {id: https://agentic-knowledge-base.dev/id/composite/ba04ada0-2f37-4bc2-ad15-c2ac77fbe18e, title_ko: 정지 규칙 없는 반복 라운드, title: Repeated rounds without a stop rule, ordered: [https://agentic-knowledge-base.dev/id/chunk/c1ad3b4a-d86c-4c63-ab91-7294a56a76e2, https://agentic-knowledge-base.dev/id/chunk/8c9efac1-c449-42bf-9a95-94c571603b41, https://agentic-knowledge-base.dev/id/chunk/b3507553-ac86-49c8-b418-34672c646729]}
---
**자극** — 부류의 자극은 같은 작업 집합에 강화 라운드를 반복해 열고 라운드마다 신규 결함 수를 세는 것이다. actor는 라운드를 반복해 여는 세션이고 action은 라운드마다 신규 결함 수를 세는 것이다. 순서는 라운드 열기 → 강화 → 계수의 반복이고, `keep()`은 라운드 사이에 유지되는 작업 집합과 계수 방식이다.

변수는 ODD 속성 둘이다. `id:cond-concurrent-agents`(동시 에이전트 수, 0~5)가 라운드를 여는 주체 수를 가르고, `id:cond-build-system`(빌드 체계)이 라운드마다 무엇을 다시 도는지를 가른다. 범위는 logical 높이에서 채운다.
