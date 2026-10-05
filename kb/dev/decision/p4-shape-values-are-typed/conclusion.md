---
id: https://agentic-knowledge-base.dev/id/chunk/81346f76-4da4-45f0-bbb2-421ab78efc30
type: decision
level: concrete
title_ko: 값을 갖는 property shape는 형을 달고 닫힌 값 목록은 온톨로지 정의의 서술과 일치시킨다
title: A property shape over values declares a type, and a closed value list matches the ontology definition
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c1a7b38a-801d-4968-9c9f-d8db75756183
composite: {id: https://agentic-knowledge-base.dev/id/composite/c1a7b38a-801d-4968-9c9f-d8db75756183, title_ko: shape 값의 형, title: Typed shape values}
---
**결론** — 값을 갖는 property shape에는 형을 단다(유저 승인 2026-09-23, 자연어 모호성 항목 M5).

- 문자열·정수는 `sh:datatype`, 개체는 `sh:class`, 참조는 `sh:nodeKind sh:IRI`로 단다.
- 범위가 있으면 `sh:minInclusive`·`sh:maxInclusive`를 단다.
- 닫힌 집합이면 `sh:in`을 단다. `sh:in`의 원천은 온톨로지 정의의 서술과 일치시킨다(권장).

형이 없는 값은 문자열로 남아 "이상·이하·약"이 산문에 머문다. 이 규약을 판정하는 게이트는 없다. 리뷰 규범이다.
