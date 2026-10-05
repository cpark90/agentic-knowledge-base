---
id: https://agentic-knowledge-base.dev/id/chunk/ecf1f527-8c7b-4523-a1d4-4ede18f8806d
type: decision
level: concrete
title_ko: 규범 문서 규약 — 주석은 라벨과 장식을 달고 해소 상태를 가지며 blocking만 게이트를 막는다
title: Normative-document conventions — A comment carries a label and a decoration, holds a resolution state, and only blocking stops the gate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be
---
**규약** — `p7-commentary-form`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `annotation`은 주석이다. 첫 줄이 `<라벨> (<장식>): <요지>`이고 라벨 일곱(`praise`·`nitpick`·`suggestion`·`issue`·`question`·`thought`·`chore`)과 장식 셋(`blocking`·`non-blocking`·`if-minor`)은 닫힌 어휘다. 이어서 `대상:`(IRI, `targets`와 일치) · `본문:`(4문장 이하) · `제안:`(선택) · `해소:`(`열림`·`해소`·`기각` + 한 줄 이유)를 적는다. `issue (blocking)`이면서 `해소: 열림`인 것만 게이트를 막는다.
