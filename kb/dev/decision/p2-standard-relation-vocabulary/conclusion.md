---
id: https://agentic-knowledge-base.dev/id/chunk/551ff31a-12a5-4bf1-a1bf-65d74e2bde16
type: decision
level: concrete
title_ko: 고유 관계는 subPropertyOf로 표준 관계 아래에 매단다
title: Bespoke relations hang under standard ones via subPropertyOf
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced, https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0053]
part_of: https://agentic-knowledge-base.dev/id/composite/ad815628-628e-40a9-a3da-05db0480bb7e
composite: {id: https://agentic-knowledge-base.dev/id/composite/ad815628-628e-40a9-a3da-05db0480bb7e, title_ko: 관계 어휘도 표준을 쓴다, title: Relations come from standard vocabularies too}
---
**결론** — **관계도 지어내지 않는다.** 상위 온톨로지 계열의 표준 관계 온톨로지(RO)에 있는 것을 우선 쓴다.

- 부분-전체 → `bfo:part_of`
- 출처 → `prov:wasDerivedFrom`
- 실현(역할·기능) → `ro:realizes`
- 참여 → `ro:participates_in` (행위자가 실행에 참여)
- 선행 → `ro:precedes` (시간 제약 어휘, 0.5절)

표준에 없는 것은 셋뿐이다 — **충족·검증·정련**. `agt:satisfies`, `agt:verifies`, `agt:refines`를 둔다.

**고유 관계는 반드시 `rdfs:subPropertyOf`로 표준 관계 아래에 둔다.** `agt:satisfies`는 `ro:realizes`의 특수화다. 표준 관계로 질의하면 고유 관계도 걸린다.
