---
id: https://agentic-knowledge-base.dev/id/chunk/32d8d4d5-4249-45cf-89f4-040a59826ee7
type: artifact
level: executable
title_ko: 음성 자극이 거부되는지 판정하는 검증기는 defs/tests/negative.bzl 의 failure_test 다
title: The verifier that judges whether a negative stimulus is rejected is failure_test in defs/tests/negative.bzl
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/4d943c83-e888-4840-a503-9163282182fd, https://agentic-knowledge-base.dev/id/chunk/0885d278-bf9d-44cc-9484-adc96e64f47f, https://agentic-knowledge-base.dev/id/chunk/e82398f4-7be6-404a-9a64-b8c359a9180f, https://agentic-knowledge-base.dev/id/chunk/dd9f88e7-0282-4093-9ac5-70acd9a8e409, https://agentic-knowledge-base.dev/id/chunk/23f7dfe7-7344-434c-96b5-e9f9f6f73dd6, https://agentic-knowledge-base.dev/id/chunk/e0f0c405-96b7-48cc-8ad3-4a6effe070db, https://agentic-knowledge-base.dev/id/chunk/6c4f4fc7-bf82-4c93-9b78-58b6a8be2563, https://agentic-knowledge-base.dev/id/chunk/7e69ba96-e363-4ed0-bea1-2ef9602cbeae, https://agentic-knowledge-base.dev/id/chunk/3a93bc97-0661-4051-877b-55ffd4669809]
restored: [https://agentic-knowledge-base.dev/id/chunk/4d943c83-e888-4840-a503-9163282182fd, https://agentic-knowledge-base.dev/id/chunk/0885d278-bf9d-44cc-9484-adc96e64f47f, https://agentic-knowledge-base.dev/id/chunk/e82398f4-7be6-404a-9a64-b8c359a9180f, https://agentic-knowledge-base.dev/id/chunk/dd9f88e7-0282-4093-9ac5-70acd9a8e409, https://agentic-knowledge-base.dev/id/chunk/23f7dfe7-7344-434c-96b5-e9f9f6f73dd6, https://agentic-knowledge-base.dev/id/chunk/e0f0c405-96b7-48cc-8ad3-4a6effe070db, https://agentic-knowledge-base.dev/id/chunk/6c4f4fc7-bf82-4c93-9b78-58b6a8be2563, https://agentic-knowledge-base.dev/id/chunk/7e69ba96-e363-4ed0-bea1-2ef9602cbeae, https://agentic-knowledge-base.dev/id/chunk/3a93bc97-0661-4051-877b-55ffd4669809]
generated: {by: vnv/claude-opus-5, at: 2026-09-22T23:44:00+09:00}
---
**검증기** — 음성 자극이 실제로 거부되는지 판정하는 검증기는 `defs/tests/negative.bzl` 의 `failure_test` 다. skylib 의 `analysistest` 로 고정물 타깃을 분석 시점에 실패시키고 그 실패를 통과로 읽는다.

**적용하는 기준** — `target_under_test` 의 분석이 실패해야 하고 실패 메시지가 `expected` 문구를 담아야 한다. 종료 코드만 보는 판정과 달리 문구를 대조하므로 규칙의 문구가 바뀌면 이 검증기가 먼저 걸린다.

**덮는 축** — plane 단방향 · 수준 허용표 · `supersedes` 같은 plane · `verifies` 주어 · 결정의 부분 수준 · `serves` 대상 · KB 를 가로지르는 링크의 일곱이다. 위반 고정물은 `defs/tests/` 안에만 있고 지식 패키지에 두지 않는다.

**검증 대응물** — 없음. 같은 `executable` 수준의 개발 항목이 없어 `verifies` 를 달 수 없다.
