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
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be
composite: {id: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be, title_ko: 주석의 형식, title: The form of a comment}
---
**결론** — `annotation` 지식 종류에 드는 것은 주석이다. 첫 줄이 `<라벨> (<장식>): <요지>`이고 라벨과 장식은 닫힌 어휘다. 표기의 원천은 Conventional Comments다.

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

**게이트** `blocking-comment`(노트 7.7절, 실행 계층 test) — `chunk_lint`가 판정한다(2026-09-22). 대상은 살아 있는 `type: annotation` 단위 지식이고 `deprecated`·`invalidated` 주석은 기록이라 막지 않는다. 해소는 저작자가 대상을 고친 뒤 `해소: 해소 — <이유>`로 바꾸거나, 받지 않기로 했으면 `해소: 기각 — <이유>`로 바꾸는 것이다. 면제는 `docs/waivers.md`(축 `파일`)에 선언한다.

**게이트** `verify`(노트 7.7절 주석의 수준 상속) — 주석의 `hasLevel`이 `targets` 대상 어느 것의 수준과도 다르면 verify 질의 `comment-level-not-inherited`가 거부한다(2026-09-26). 대상이 여럿이면 그중 하나와 같을 때 통과한다. 해소는 vnv가 주석의 수준을 대상에 맞추는 것이다.
