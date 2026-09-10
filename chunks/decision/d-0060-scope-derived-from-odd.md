---
id: https://agentic-knowledge-base.dev/id/chunk-d0060
type: decision
level: concrete
title_ko: 하네스는 ODD에서 스코프를 잘라낸다
title: The harness carves scopes out of the ODD
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 하네스는 ODD에서 스코프를 잘라낸다. 스코프는 ODD 속성을
`inherit`하고 plane 권한을 `include`할 뿐이며, **ODD에 없는 속성을 스코프에
새로 쓸 수 없다.**

**근거** (노트 3.4절)
- `inherit`는 전부(`static.*`)일 수도 일부(`environment.database`)일 수도
  있고, `include plane`은 read/write로 권한을 주며 조건부로도 줄 수 있다
  ("대상 결정의 level이 concrete이면 interface plane 쓰기 허용").
- 에이전트의 situation(0.5절)은 scene을 이 스코프로 거른 것이다. 따라서
  **에이전트가 볼 수 있는 조건은 ODD 속성 중 스코프가 inherit한 것뿐이며**
  나머지는 그 에이전트에게 존재하지 않는다.
- 스코프가 ODD 밖 속성을 쓸 수 있으면 "무엇의 부분집합인가"가 무너지고,
  하네스마다 경계를 따로 정의하게 된다.
