---
id: https://agentic-knowledge-base.dev/id/chunk/d0f40d22-48b1-4b99-9cdf-97e6ffb3e272
type: decision
level: concrete
title_ko: 규범 문서 규약 — 값을 갖는 property shape는 형을 달고 닫힌 값 목록은 온톨로지 정의의 서술과 일치시킨다
title: Normative-document conventions — A property shape over values declares a type, and a closed value list matches the ontology definition
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c1a7b38a-801d-4968-9c9f-d8db75756183
---
**규약** — `p4-shape-values-are-typed`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 값을 갖는 property shape 에는 형을 단다 — `sh:datatype`(문자열·정수), `sh:class`(개체), `sh:nodeKind sh:IRI`(참조). 범위가 있으면 `sh:minInclusive`·`sh:maxInclusive`, 닫힌 집합이면 `sh:in` 이다. 형이 없는 값은 문자열로 남아 "이상·이하·약" 이 산문에 머문다(유저 승인 2026-09-23, M5).
규약: [권장] 닫힌 값 목록(`sh:in`)의 원천은 온톨로지 정의의 서술과 일치시킨다.
