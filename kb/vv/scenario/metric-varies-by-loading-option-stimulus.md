---
id: https://agentic-knowledge-base.dev/id/chunk/40fe7c24-903a-49b6-9cfa-c97404641dc2
type: decision
level: abstract
title_ko: 시나리오 자극 — 같은 입력을 두 로딩 설정으로 재는 지표 실행
title: Scenario stimulus — measuring one input under two loading configurations
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/91d72e63-e72e-4803-aaf3-281a81994a31]
part_of: https://agentic-knowledge-base.dev/id/composite/14e499e9-6a33-4c4b-8832-e4e3edbdd924
composite: {id: https://agentic-knowledge-base.dev/id/composite/14e499e9-6a33-4c4b-8832-e4e3edbdd924, title_ko: 같은 입력을 두 로딩 설정으로 재는 지표 실행, title: Measuring one input under two loading configurations, ordered: [https://agentic-knowledge-base.dev/id/chunk/40fe7c24-903a-49b6-9cfa-c97404641dc2, https://agentic-knowledge-base.dev/id/chunk/a0d074b3-52e3-4233-a75d-696cd28faef4, https://agentic-knowledge-base.dev/id/chunk/045a2d31-d37b-411e-8d97-92d9611a0eab]}
---
**자극** — 부류의 자극은 리비전을 고정한 채 union 구성이 다른 지표 도구 둘 이상을 돌려 이름이 같은 수치를 나란히 뽑는 것이다. actor는 지표를 내는 세션이고 action은 `//kg:metrics`와 `//kg:link_candidates`처럼 입력 집합이 다른 타깃을 같은 리비전에서 실행해 같은 이름의 수치를 대조하는 것이다. 순서는 리비전 고정 → 도구 실행 둘 → 같은 이름의 수치 대조이고, `keep()`은 리비전과 청크 집합, 그리고 두 실행 사이에 바뀌지 않는 그래프 파일들이다.

변수는 ODD 속성 둘이다. `id:cond-build-system`(빌드 체계)이 어느 타깃이 어느 그래프를 입력으로 받는지를 가르고, `id:cond-dependency-lock`(의존성 고정)이 파싱과 직렬화의 판본을 가른다. 범위는 logical 높이에서 채운다.
