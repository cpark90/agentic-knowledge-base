---
id: https://agentic-knowledge-base.dev/id/chunk/de11ca60-357f-597b-a28a-b4d22359c830
type: decision
level: logical
title_ko: 논리 시나리오 요인 — 신규 결함이 줄지 않은 두 라운드 뒤 셋째 라운드 기록의 정지 규칙 판정이 노출하는 현상
title: Logical scenario factors — the phenomena exposed by judging the stop rule on a third round record after two rounds whose new defects did not fall
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/unknownStopCondition]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:16:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/90e4464e-15dc-5cdc-9105-ba97d62261a8
---
**요인** — 노출하려는 현상은 `agt:unknownStopCondition`(P15) 하나다. 정지 규칙이 성립했는데 다음 라운드를 다른 사유로 닫는 기록이 그 현상의 관측 형태다. 표본 근거는 둘이다. 등가분할이 keep 값 `roundEndedByStopRule` 로 준수 케이스 하나를 내고, 요인 주입이 keep 밖 값 `roundEndedByCompletion` 으로 위반 케이스 하나를 낸다. 기여하는 검증 목표는 `kb/vv/goal/verification-round-stop-rule.md`(`https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78`)다.
