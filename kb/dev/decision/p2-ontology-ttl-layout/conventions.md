---
id: https://agentic-knowledge-base.dev/id/chunk/0afe2600-022d-4122-88f2-7f32432cbf01
type: decision
level: concrete
title_ko: 규범 문서 규약 — 온톨로지 TTL 파일은 배너·prefix·개념 블록 순이고 개념 블록의 술어 순서는 고정이다
title: Normative-document conventions — An ontology TTL file runs banner, prefixes, then concept blocks, and predicates in a concept block follow a fixed order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/aa03212b-6699-4c65-bbc8-0f9836401c6d
---
**규약** — `p2-ontology-ttl-layout`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 파일 구조는 상단 배너 주석 1줄(주제) → `@prefix` 블록(agt → owl → rdfs → skos → xsd 순) → 개념 블록들의 순이다.
규약: [지킴] 개념 블록의 술어 순서는 `a` → `rdfs:subClassOf`/`owl:disjointWith` → `rdfs:domain` → `rdfs:range` → `rdfs:label`(en, ko 순) → `skos:definition`이다.
