---
id: https://agentic-knowledge-base.dev/id/chunk/b3507553-ac86-49c8-b418-34672c646729
type: decision
level: abstract
title_ko: 시나리오 배제 자극 — 정지 규칙 없는 반복 라운드에서 다루지 않는 것
title: Scenario excluded stimuli — what repeated rounds without a stop rule does not cover
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ba04ada0-2f37-4bc2-ad15-c2ac77fbe18e
specializationOf: https://agentic-knowledge-base.dev/id/chunk/c1ad3b4a-d86c-4c63-ab91-7294a56a76e2
---
**배제 자극** — 다루지 않는 자극은 셋이다.

- 라운드 수 자체는 ODD 속성이 아니다. ODD 밖 자극이므로 `odd:outside`로만 존재하고 커버리지의 분모에 들지 않는다.
- 사람이 라운드를 손으로 멈추는 경우는 이 부류가 다루지 않는다. 정지 규칙의 존재를 묻는 자극이므로 사람의 개입은 규칙의 부재를 가린다.
- 라운드가 새 결함을 하나도 내지 않는 경우는 다른 부류가 덮는다. 이 부류는 신규 결함이 계속 나오는 쪽만 자극한다.
