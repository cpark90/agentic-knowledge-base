---
id: https://agentic-knowledge-base.dev/id/chunk/32d8d4d5-4249-45cf-89f4-040a59826ee7
type: artifact
level: executable
title_ko: 음성 자극이 거부되는지 판정하는 검증기는 defs/tests/negative.bzl 의 failure_test 다
title: The verifier that judges whether a negative stimulus is rejected is failure_test in defs/tests/negative.bzl
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/e1cc9b56-b318-4f5a-8c98-4af5e9a655e7, https://agentic-knowledge-base.dev/id/chunk/797958ea-3a61-41d1-9a10-d12f1c4d69b3, https://agentic-knowledge-base.dev/id/chunk/47ee0dfa-f035-4220-a756-a447df307de9, https://agentic-knowledge-base.dev/id/chunk/193f0438-c6bc-4e78-979d-152cfbf97323, https://agentic-knowledge-base.dev/id/chunk/68faa51d-47c8-48fb-9cb1-589f793d31a6, https://agentic-knowledge-base.dev/id/chunk/56b4c449-63d5-4f3c-8b25-2983028beab8, https://agentic-knowledge-base.dev/id/chunk/2b1a11cb-160a-45fe-a5cb-4f86f8a42271, https://agentic-knowledge-base.dev/id/chunk/100e3c7b-9fd4-4b43-bc2a-6068e15bbd27, https://agentic-knowledge-base.dev/id/chunk/2a7d49b7-e29a-4609-acc5-81608e38324a]
restored: [https://agentic-knowledge-base.dev/id/chunk/e1cc9b56-b318-4f5a-8c98-4af5e9a655e7, https://agentic-knowledge-base.dev/id/chunk/797958ea-3a61-41d1-9a10-d12f1c4d69b3, https://agentic-knowledge-base.dev/id/chunk/47ee0dfa-f035-4220-a756-a447df307de9, https://agentic-knowledge-base.dev/id/chunk/193f0438-c6bc-4e78-979d-152cfbf97323, https://agentic-knowledge-base.dev/id/chunk/68faa51d-47c8-48fb-9cb1-589f793d31a6, https://agentic-knowledge-base.dev/id/chunk/56b4c449-63d5-4f3c-8b25-2983028beab8, https://agentic-knowledge-base.dev/id/chunk/2b1a11cb-160a-45fe-a5cb-4f86f8a42271, https://agentic-knowledge-base.dev/id/chunk/100e3c7b-9fd4-4b43-bc2a-6068e15bbd27, https://agentic-knowledge-base.dev/id/chunk/2a7d49b7-e29a-4609-acc5-81608e38324a]
generated: {by: vnv/claude-opus-5, at: 2026-10-04T20:20:54+09:00}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ff058e5b-5ef1-474e-b392-3948fb4f04c7
---
**검증기** — 음성 자극이 실제로 거부되는지 판정하는 검증기는 `defs/tests/negative.bzl` 의 `failure_test` 다. skylib 의 `analysistest` 로 고정물 타깃을 분석 시점에 실패시키고 그 실패를 통과로 읽는다.

**적용하는 기준** — `target_under_test` 의 분석이 실패해야 하고 실패 메시지가 `expected` 문구를 담아야 한다. 종료 코드만 보는 판정과 달리 문구를 대조하므로 규칙의 문구가 바뀌면 이 검증기가 먼저 걸린다.

**덮는 축** — plane 단방향 · 수준 허용표 · `supersedes` 같은 plane · `verifies` 주어 · 결정의 부분 수준 · `serves` 대상 · KB 를 가로지르는 링크의 일곱이다. 위반 고정물은 `defs/tests/` 안에만 있고 지식 패키지에 두지 않는다.

**검증 대응물** — 없음. 같은 `executable` 수준의 개발 항목이 없어 `verifies` 를 달 수 없다.
