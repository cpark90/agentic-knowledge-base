---
id: https://agentic-knowledge-base.dev/id/chunk/193f0438-c6bc-4e78-979d-152cfbf97323
type: contract
level: logical
title_ko: 링크·수준 규칙의 변이 고정물 다섯이 전부 기대 문구로 거부되어 검출률이 5/5 다
title: All five mutation fixtures for the link and level rules are rejected with the expected message, giving a detection rate of 5/5
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-22T19:55:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/51822789-fb4e-4062-8bb1-6cc0dda2eee0]
---
**합격 기준** — 기준 종류는 **불변식**이다. `∀ f ∈ fixtures: analysis(f) = FAIL ∧ message(f) ∋ expected(f)` 이고 `detection = |rejected| / |fixtures| = 5/5 = 100.0%` 다.

**판정식**

- 양성: `bazel test //defs/tests:plane_direction_test //defs/tests:residency_test //defs/tests:supersedes_plane_test //defs/tests:verifies_subject_test //defs/tests:decision_levels_test` 가 전부 PASS 다.
- `failure_test` 는 대상이 기대 문구로 실패할 때만 PASS 이므로 PASS 가 곧 거부다.
- 음성: 규칙을 약화해 고정물이 통과하면 해당 `failure_test` 가 `expected` 불일치로 FAIL 이다. 서술 표본이다.
- 측정 밖: 판정자의 정확도·판별력·캘리브레이션은 학습된 판정자가 없어 값이 없다. `없음` 이 정직한 상태다.

**등급** — A 다. 판정은 분석 시점 시험 다섯이고 사람 판단이 없다.

판정의 원본은 `defs/tests/BUILD.bazel` 의 `failure_test` 와 그 `expected` 문구다. 다섯 고정물이 덮는 규칙은 plane 단방향·수준 허용표·supersedes 같은 plane·verifies 주어·결정 부분 수준이고, `serves` 대상·`verifies` 같은 수준·KB 가로지름은 고정물이 없다.
