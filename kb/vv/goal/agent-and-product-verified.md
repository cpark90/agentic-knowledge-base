---
id: https://agentic-knowledge-base.dev/id/chunk/cbcb6272-8151-49d5-b868-71be8559ba2e
type: requirement
level: functional
pattern: ubiquitous
title_ko: 검증 대상은 만들어지는 제품과 만드는 에이전트 둘이어야 한다
title: The verification targets must be both the product being made and the agent making it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-24T11:20:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
---
**검증 목표** — 검증 대상이 둘이고 두 대상의 검증 사슬이 별개라는 결정이 V&V KB 의 실제 사슬로 성립한다는 것이 보여져야 한다. 제품 쪽 사슬은 개발 요구에서 파생되고 에이전트 쪽 사슬은 카탈로그 역할의 책임에서 파생된다. 두 사슬을 가르는 것은 `verifies` 도착점의 종류가 아니라 그 도착점이 정한 것의 종류다.

- **이해관계자**: 검증자 · **관심사**: 검증 대상

**무엇을 관측하면 성립하는가**

- 제품 검증: 검증 목표가 개발 요구를 `derivesFrom` 하고 케이스가 산출물의 기준을 정한 결정을 `verifies` 한다 (감사 `검증 현황` 절).
- 에이전트 검증: 검증 목표가 카탈로그 역할(`id:role-*`)의 책임에서 파생되고 케이스가 역할·스코프·작업 집합을 정한 결정을 `verifies` 한다.
- 두 사슬의 `verifies` 도착점은 **둘 다 개발 KB 청크**다. A-Box 개체는 `ChunkInfo` 도 수준도 없어 도착점이 될 수 없다 (`defs/kb.bzl` `_check_links`).
- 에이전트 쪽 합격 기준은 이미 도는 게이트다 — shape 통과·`refines` 완주·게이트 통과율이다.

판정의 원본은 `tools/weave.py` 의 `render_audit`, `kb/dev/decision/p8-agent-verification-target/conclusion.md`·`p8-agent-vv/conclusion.md` 다.
