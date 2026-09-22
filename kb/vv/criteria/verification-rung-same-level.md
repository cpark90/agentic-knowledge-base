---
id: https://agentic-knowledge-base.dev/id/chunk/100e3c7b-9fd4-4b43-bc2a-6068e15bbd27
type: contract
level: logical
title_ko: verifies 는 같은 수준끼리만 분석을 통과하고 감사 보고서가 요구별 검증 대응물과 사슬 수를 낸다
title: verifies passes analysis only between equal levels, and the audit report counts verification counterparts and chains per requirement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/6ee940e6-b69f-4f62-93e2-924829542e3f]
---
**합격 기준** — 기준 종류는 **불변식**이다. `∀ (s verifies t): level(s) = level(t) ∧ s ∈ V&V ∧ t ∈ 개발` 이고 `coverage = |{r ∈ req | ∃ goal: goal derivesFrom r}| / |req|` 를 감사가 낸다.

**판정식**

- 양성(주어): `bazel test //defs/tests:verifies_subject_test` 가 PASS 다. 개발 KB 청크가 `verifies` 하는 고정물이 `verifies 의 주어는` 으로 실패할 때만 PASS 다.
- 양성(감사): `bazel build //kg:audit` 이 성공하고 `bazel-bin/kg/audit.md` 의 `검증 현황` 절에 `검증 대응물이 있는 요구(…): **n/d = p.p%** (목표 100.0%)` 와 `사슬: 검증 목표 G · 합격 기준이 달린 목표 C · 케이스까지 이어진 목표 K` 줄이 있다.
- 음성(수준): concrete 케이스가 logical 청크를 `verifies` 하면 `verifies 는 같은 수준끼리 (8.3절 검증 대응물): concrete ≠ logical` 로 분석이 실패한다. 서술 표본이다. 고정물은 없다.
- 관측: 검증 대응물 없는 요구가 있으면 감사가 `검증 대응물 없는 요구 N건:` 아래 슬러그를 나열한다.

**등급** — B 다. 수준 규칙은 분석 시점 판정이고 감사 수치는 관측이다.

판정의 원본은 `defs/kb.bzl` 의 `_check_links` 와 `tools/weave.py` 의 `render_audit` 이다. "대응물이 없으면 다음 높이로 내려가지 못한다" 는 차단 게이트는 없고 감사 수치가 그 자리를 대신한다.
