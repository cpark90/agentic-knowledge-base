---
id: https://agentic-knowledge-base.dev/id/chunk/a0d074b3-52e3-4233-a75d-696cd28faef4
type: decision
level: abstract
title_ko: 시나리오 요인 — 두 로딩 설정의 지표 실행이 노출하는 현상
title: Scenario factors — the phenomenon exposed by measuring under two loading configurations
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/metricVariesByLoadingOption]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/14e499e9-6a33-4c4b-8832-e4e3edbdd924
---
**요인** — 노출하려는 현상은 `agt:metricVariesByLoadingOption`(P21) 하나다. 등급은 S3·E2·D3이고 인과는 `agt:coverageImpact`다. 분모가 갈리면 커버리지 비율이 도구마다 달라지므로 피해가 커버리지에 떨어진다.

주입하는 한정자는 `agt:incorrectQualifier` 하나다. 도구가 union을 읽지 않는 것이 아니라 서로 다른 union을 읽는 것이 이 부류의 결함 형태다. 자극이 겨누는 자리는 `//kg:metrics`가 ODD 그래프를 읽고 `//kg:link_candidates`는 읽지 않는 차 71 트리플이며, `//kg:audit`은 온톨로지 모듈까지 읽어 1544 트리플을 더 본다.

기여하는 검증 목표는 `kb/vv/goal/metric-varies-by-loading-option.md`(`https://agentic-knowledge-base.dev/id/chunk/91d72e63-e72e-4803-aaf3-281a81994a31`)다. 표본 근거는 참조 저장소 `../harness-functional`의 실패 R5이며 그 저장소는 내용의 원천이고 빌드 의존이 아니다.
