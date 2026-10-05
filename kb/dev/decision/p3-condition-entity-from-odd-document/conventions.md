---
id: https://agentic-knowledge-base.dev/id/chunk/bd9fefc0-ad33-468c-8a21-702ed59ef821
type: decision
level: concrete
title_ko: 규범 문서 규약 — 조건은 ODD 문서의 속성으로 저작하고 id:cond-<slug>로 ODD에 등록되며 명시 제외는 검토 시점과 이유를 갖는다
title: Normative-document conventions — Conditions are authored as ODD document properties, registered on the ODD as id:cond-<slug>, and explicit exclusions carry a review date and a reason
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a42db8cd-3f7e-443f-bb88-61ac79945d82
---
**규약** — `p3-condition-entity-from-odd-document`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 조건 개체는 `id:cond-<slug>`다. 타입은 `agt:StaticElement` / `agt:EnvironmentalCondition` / `agt:DynamicElement`의 3분류 중 하나다.
규약: [지킴] 조건은 ODD 개체의 `agt:hasCondition` 목록에 등록한다. 등록 없는 조건을 만들지 않는다.
규약: [지킴] 검토했으나 밖에 두는 것은 **명시 제외**로 기록한다. ODD 문서의 `EXCLUSIONS_REVIEWED`에 `concept`·`reviewed`(YYYY-MM)·`reason`을 적고, 그래프의 `agt:excludes` 서식은 `"<대상> — reviewed YYYY-MM, 이유: <근거>"`다.
