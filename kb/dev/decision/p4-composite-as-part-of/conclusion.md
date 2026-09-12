---
id: https://agentic-knowledge-base.dev/id/chunk/047c5c56-2b6c-4f8b-993e-32f3a35fd1d6
type: decision
level: concrete
title_ko: 복합체는 표준 part-of와 순서 컬렉션으로 쓴다
title: Composites use standard part-of and an ordered collection
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0073]
part_of: https://agentic-knowledge-base.dev/id/composite/85fcc7f3-446f-46d6-b386-693544fefe6e
composite: {id: https://agentic-knowledge-base.dev/id/composite/85fcc7f3-446f-46d6-b386-693544fefe6e, title_ko: 복합체 — 표준 부분-전체 관계, title: Composite as standard parthood}
---
**결론** — **복합체(`agt:Composite`)** 는 청크 또는 다른 복합체를 부분으로 갖는
개체다. **assertion 그래프가 없다** — 라벨과 순서 있는 부분 목록이 전부다.

- 부분-전체는 **상위 온톨로지의 `part-of`** 를 쓴다.
- **순서는 표준 순서 컬렉션 어휘로 쓴다.** 순서가 필요한 복합체(케이스 열,
  절차, 논증)는 Collections Ontology의 `co:List`를 겸하며 각 부분이
  `co:index`를 갖는다.
- 순서가 없는 복합체(스키마의 필드 집합)는 `part-of`만 쓴다.
