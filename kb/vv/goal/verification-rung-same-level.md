---
id: https://agentic-knowledge-base.dev/id/chunk/6ee940e6-b69f-4f62-93e2-924829542e3f
type: requirement
level: functional
pattern: event-driven
title_ko: 개발 높이마다 같은 높이의 검증 대응물이 있어야 하고 없는 요구는 감사가 세어야 한다
title: Each development height must have a verification counterpart at the same height, and requirements lacking one must be counted by the audit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2]
---
**검증 목표** — 시나리오 계층이 개발 계층과 같은 높이를 갖고 functional 에서는 검증 목표의 `derives-from` 이 필수라는 결정이 분석 시점 규칙과 감사 수치로 성립한다는 것이 보여져야 한다.

- **이해관계자**: 검증자 · **관심사**: 완주

**무엇을 관측하면 성립하는가**

- `verifies` 는 같은 수준끼리만 허용되고 어긋나면 분석 시점에 실패한다(`defs/kb.bzl` 의 `verifies 는 같은 수준끼리 (8.3절 검증 대응물)`).
- `verifies` 의 주어는 V&V KB 청크뿐이고 고정물 `bad_verifies` 가 `verifies 의 주어는` 으로 실패한다.
- `bazel build //kg:audit` 의 `검증 현황` 절이 `검증 대응물이 있는 요구: n/d = p.p% (목표 100.0%)` 와 `검증 대응물 없는 요구 N건` 목록을 낸다.
- 같은 절이 사슬(목표 → 기준 → 케이스) 수를 세어 목표만 있고 케이스가 없는 요구를 드러낸다.

판정의 원본은 `defs/kb.bzl` 의 `_check_links`, `defs/tests/BUILD.bazel` 의 `verifies_subject_test`, `tools/weave.py` 의 `render_audit` 이다.
