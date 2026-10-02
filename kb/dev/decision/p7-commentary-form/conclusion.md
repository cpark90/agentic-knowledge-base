---
id: https://agentic-knowledge-base.dev/id/chunk/c0b7f63a-353e-4fdf-9389-961b6f3e130c
type: decision
level: concrete
title_ko: 주석은 라벨과 장식을 달고 해소 상태를 가지며 blocking만 게이트를 막는다
title: A comment carries a label and a decoration, holds a resolution state, and only blocking stops the gate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-26T15:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be
composite: {id: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be, title_ko: 주석의 형식, title: The form of a comment}
---
**결론** — `annotation` 청크는 주석이다. 첫 줄이 `<라벨> (<장식>): <요지>`이고 라벨과 장식은 닫힌 어휘다. 표기의 원천은 Conventional Comments다.

| 라벨 | 뜻 |
|---|---|
| `praise` | 잘된 것을 짚는다 |
| `nitpick` | 사소하고 취향에 가깝다 |
| `suggestion` | 이렇게 바꾸자 |
| `issue` | 문제가 있다 |
| `question` | 뜻을 묻는다 |
| `thought` | 행동을 요구하지 않는 생각이다 |
| `chore` | 절차상 해야 할 잡일이다 |

장식은 셋이다. `blocking`은 해소 전에는 진행할 수 없다, `non-blocking`은 진행해도 된다, `if-minor`는 비용이 작으면 하라는 뜻이다.

슬롯은 다섯이다. 첫 줄 · `대상:`(검증·리뷰 대상 IRI, `targets`와 일치) · `본문:`(4문장 이하) · `제안:`(선택) · `해소:`(`열림`·`해소`·`기각` + 한 줄 이유)다.

**`issue (blocking)`이면서 `해소: 열림`인 주석만 게이트를 막는다.** 나머지는 기록이다. 판정 도구는 해소 상태의 존재만 보고 내용을 보지 않는다(`p5-verification-tools-per-plane`).
