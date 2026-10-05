---
id: https://agentic-knowledge-base.dev/id/chunk/917d1355-b82f-41c8-8c0f-fa634c9eeb37
type: artifact
level: executable
title_ko: defs/tests의 위반 고정물 다섯이 각자의 규칙 문구로 실패하고 //kg:gate_test·//kb/dev:lint_test가 PASS다
title: The five violating fixtures in defs/tests fail with their own rule text and //kg:gate_test and //kb/dev:lint_test pass
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/47ee0dfa-f035-4220-a756-a447df307de9]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T00:49:09+09:00}
layer: process
---
**검증기** — 다섯 실행 계층 중 기계 계층 넷을 대표 게이트 하나씩으로 자극한다.

**자극** — `defs/tests/BUILD.bazel`의 `manual` 고정물 다섯과 커밋된 저장소 전체다.

```yaml
analysis:     [bad_residency, bad_plane_dir, bad_supersedes, bad_verifies, bad_decision_levels]   # 규칙 하나씩 위반
shape+verify: //kg:gate_test         # head·시드·참조·ODD 그래프 + shape + verify 질의
test:         //kb/dev:lint_test     # 본문 토큰 상한 · 결정 역할 표지 · 산문
```

**기대** — 다섯 음성 시험이 PASS다. 각 고정물의 분석 실패 메시지가 `수준 허용표 위반 (6.4절)`·`plane 단방향 위반 (5.2절)`·`supersedes 는 같은 plane 안에서만 (7.4절)`·`verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)`·`plane decision 는 level executable 에 살 수 없다`를 담는다. `//kg:gate_test`·`//kb/dev:lint_test`가 PASS다.

**실행 명령** — `bazel test //defs/tests:residency_test //defs/tests:plane_direction_test //defs/tests:supersedes_plane_test //defs/tests:verifies_subject_test //defs/tests:decision_levels_test //kg:gate_test //kb/dev:lint_test`

**판정 범위** — 고정물 다섯은 `defs/kb.bzl`의 분석 시점 규칙 전부에 하나씩 대응하므로 analysis 계층은 전수다. shape·verify·test 계층은 게이트 하나씩으로 대표하고 각 게이트의 세부 분기는 다른 사슬(`residency-matrix`·`chunk-42-lines`·`foreign-vocabulary-rejected`·`criteria-before-verifies`)이 갖는다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p6-gate-catalogue` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
