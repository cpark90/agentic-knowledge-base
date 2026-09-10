---
id: https://agentic-knowledge-base.dev/id/chunk-d0073
type: decision
level: concrete
title_ko: 구성체는 표준 part-of와 순서 컬렉션으로 쓴다
title: Composites use standard part-of and ordered collections
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 구성체(`agt:Composite`)는 청크 또는 다른 구성체를 부분으로 갖는
개체다. **assertion 그래프가 없고**, 라벨과 순서 있는 부분 목록이 전부다.
`agt:Chunk`와 disjoint하며 둘 다 `agt:KnowledgeItem`의 하위 클래스다.

**근거** (노트 4.5절)
- 부분-전체는 **상위 온톨로지의 `part-of`** 를 쓴다. 이행성·반대칭성 공리가
  이미 정의되어 있어 "A가 B의 부분이고 B가 C의 부분이면 A는 C의 부분"이
  추론된다. 지어내면 이 공리를 다시 써야 한다 (표준어 우선).
- **순서는 표준 순서 컬렉션 어휘로 쓴다.** `part-of`는 순서를 모르므로,
  순서가 필요한 구성체(시나리오, 절차, 논증)는 Collections Ontology의
  `co:List`를 겸하고 각 부분이 `co:index`를 갖는다.
- 순서가 없는 구성체(스키마의 필드 집합)는 `part-of`만 쓴다 — 순서를
  요구하지 않는 것에 순서를 붙이면 거짓 정보가 생긴다.

**본문이 없다는 것이 요점이다.** 구성체는 조립 지시일 뿐이고 내용은 전부
부분 청크에 있다. 그래서 42줄 제한이 구성체에는 적용되지 않는다.
