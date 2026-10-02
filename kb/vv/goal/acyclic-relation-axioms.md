---
id: https://agentic-knowledge-base.dev/id/chunk/03335ea8-fe32-45e0-9406-5e8457b81486
type: requirement
level: functional
pattern: ubiquitous
title_ko: refines·supersedes·복합체 부분관계의 성질 공리(비반사·이행·비순환)는 verify 질의가 강제해야 한다
title: The property axioms (irreflexive, transitive, acyclic) of refines, supersedes and the composite part relation must be enforced by verify queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-26T00:30:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
---
**검증 목표** — 온톨로지가 `agt:refines`를 `owl:IrreflexiveProperty`, `agt:supersedes`를 `owl:TransitiveProperty`로, `agt:hasDirectPart`를 비순환으로 선언하지만 pySHACL의 rdfs·owlrl 추론은 이 위반을 보고하지 않는다(2026-09-26 실측). 그래서 판정은 verify 질의가 한다는 것이 보여져야 한다.

- **이해관계자**: 에이전트 · 감사 역할 · **관심사**: 관계의 대수적 건전성

**무엇을 관측하면 성립하는가**

- 자기 자신을 가리키는 `agt:refines` 연쇄를 가진 청크가 `refines-cycle.rq`로 거부된다.
- 자기 자신을 가리키는 `agt:supersedes` 연쇄를 가진 청크가 `supersedes-cycle.rq`로 거부된다.
- 자기 자신을 가리키는 `agt:hasDirectPart` 연쇄를 가진 복합체가 `composite-cycle.rq`로 거부된다.
- 세 질의 중 하나만 어기는 그래프는 정확히 그 질의 이름으로 끝나고, 위반 트리플을 뺀 같은 그래프는 통과한다.

판정의 원본은 `tools/verify-queries/refines-cycle.rq`·`supersedes-cycle.rq`·`composite-cycle.rq`와 `tools/validate.py`의 `check_verify`다.
