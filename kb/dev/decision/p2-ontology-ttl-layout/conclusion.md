---
id: https://agentic-knowledge-base.dev/id/chunk/7eed55e6-6ffa-43fe-a74d-156d6717e60e
type: decision
level: concrete
title_ko: 온톨로지 TTL 파일은 배너·prefix·개념 블록 순이고 개념 블록의 술어 순서는 고정이다
title: An ontology TTL file runs banner, prefixes, then concept blocks, and predicates in a concept block follow a fixed order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/aa03212b-6699-4c65-bbc8-0f9836401c6d
composite: {id: https://agentic-knowledge-base.dev/id/composite/aa03212b-6699-4c65-bbc8-0f9836401c6d, title_ko: 온톨로지 TTL 파일의 서식, title: Ontology TTL file layout}
---
**결론** — 손으로 쓰는 온톨로지 TTL 파일(`kb/ontology/**/*-ontology.ttl`)은 한 꼴로 쓴다.

- **파일 구조**는 상단 배너 주석 1줄(주제) → `@prefix` 블록 → 개념 블록들의 순이다.
- **`@prefix` 순서**는 agt → owl → rdfs → skos → xsd다.
- **개념 블록의 술어 순서**는 `a` → `rdfs:subClassOf`/`owl:disjointWith` → `rdfs:domain` → `rdfs:range` → `rdfs:label`(en, ko 순) → `skos:definition`이다.

이 꼴을 판정하는 게이트는 없다. 리뷰 규범이다. 게이트 `canon`(`tools/canonicalize.py`)의 정규형은 이 꼴과 다르고 손으로 쓴 온톨로지 파일에 걸려 있지 않다(2026-10-03 BUILD 실측).
