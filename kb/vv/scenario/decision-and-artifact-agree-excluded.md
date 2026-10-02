---
id: https://agentic-knowledge-base.dev/id/chunk/5e0b0569-58c0-4450-83b6-62841414f57e
type: decision
level: abstract
title_ko: 시나리오 배제 자극 — 결정 본문과 산출물이 어긋난 편집에서 다루지 않는 것
title: Scenario excluded stimuli — what an edit that makes the decision body and the artefact disagree does not cover
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-links-only-interaction, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/65c71b3f-efa7-47bb-b4fa-f7b491e99078
specializationOf: https://agentic-knowledge-base.dev/id/chunk/fb826dc5-88fa-4bbb-bf98-7536fc095df7
---
**배제 자극** — 다루지 않는 자극은 셋이다.

- 결정과 산출물을 같은 커밋에서 함께 고치는 경우는 이 부류가 다루지 않는다. 어긋남이 생기지 않으므로 자극이 아니다.
- 결정을 `supersedes` 로 대체하는 경우는 다른 부류가 덮는다. 그쪽은 시간축 대체이고 `deprecated` 전파가 이미 규칙이다.
- 산출물이 아예 없는 경우는 `agt:requirementWithoutVerification`(P10)의 자리이고 게이트가 이미 센다.
