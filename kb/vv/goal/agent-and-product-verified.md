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
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
---
**검증 목표** — 검증 대상이 둘이고 두 대상의 검증 청크가 별개이며 `verifies` 의 도착점이 다르다는 결정이 V&V KB 의 실제 사슬로 성립한다는 것이 보여져야 한다. 제품 쪽 사슬은 요구에서 파생되고 에이전트 쪽 사슬은 카탈로그 역할의 책임에서 파생된다.

- **이해관계자**: 검증자 · **관심사**: 검증 대상

**무엇을 관측하면 성립하는가**

- 제품 검증: 검증 목표가 개발 요구를 `derivesFrom` 하고 케이스가 결정을 `verifies` 한다(감사 `검증 현황` 절).
- 에이전트 검증: 검증 목표가 카탈로그 역할(`id:role-*`)의 책임에서 파생되고 그 기준이 shape 통과·`refines` 완주·게이트 통과율·안전 정지 같은 산출물 품질이다.
- 두 사슬의 `verifies` 도착점이 다르다. 제품은 `decision`·`contract`, 에이전트는 하네스·스코프 개체다.
- 2026-09-21 실측은 제품 쪽 사슬만 있다. 에이전트 쪽 검증 목표는 0 이다.

판정의 원본은 `tools/weave.py` 의 `render_audit`, `kb/dev/decision/p8-two-verification-targets/conclusion.md`·`p8-agent-vv/conclusion.md` 다.
