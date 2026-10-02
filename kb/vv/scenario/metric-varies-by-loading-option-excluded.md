---
id: https://agentic-knowledge-base.dev/id/chunk/045a2d31-d37b-411e-8d97-92d9611a0eab
type: decision
level: abstract
title_ko: 시나리오 배제 자극 — 두 로딩 설정의 지표 실행에서 다루지 않는 것
title: Scenario excluded stimuli — what measuring under two loading configurations does not cover
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/14e499e9-6a33-4c4b-8832-e4e3edbdd924
---
**배제 자극** — 다루지 않는 자극은 셋이다.

- 추론 켜짐과 꺼짐의 차는 이 부류가 다루지 않는다. 이 저장소의 도구는 OWL 추론기를 켜지 않으므로 그 설정은 ODD 속성이 아니고 `odd:outside`로만 존재해 커버리지의 분모에 들지 않는다.
- 리비전이 다른 두 실행의 값 차는 다루지 않는다. 같은 리비전이 이 부류의 전제이고 리비전 사이의 변동은 부류 `reproducible-runs`가 덮는다.
- 이름은 같으나 뜻이 다른 수치, 곧 분모를 달리 정의한 비율은 다루지 않는다. 그 자리는 문서와 생성물의 대조를 묻는 부류 `document-table-matches-generated`가 덮는다.
