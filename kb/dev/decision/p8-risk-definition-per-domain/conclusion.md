---
id: https://agentic-knowledge-base.dev/id/chunk/9e62513d-637b-4af9-a025-6bc7d5a50455
type: decision
level: concrete
title_ko: 위험은 상황이 지속될 때 관련 행위자들의 결합된 위험이고 행위자와 피해를 도메인마다 치환한다
title: Risk is the combined risk of the involved actors while the situation persists, with actors and harms substituted per domain
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced, https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b642eb98-5b46-412d-9131-fe6db55108a1
composite: {id: https://agentic-knowledge-base.dev/id/composite/b642eb98-5b46-412d-9131-fe6db55108a1, title_ko: 도메인별 위험의 정의, title: Risk defined per domain}
---
**결론** — 위험 분석(`p8-risk-analysis-profile`)이 쓰는 위험의 정의는 원 정의 하나와 도메인별 치환이다(노트 8.21절 `[확정]`).

- **원 정의** — "상황이 지속될 때 관련 행위자들의 결합된 위험"이다.
- **치환** — 도메인 프로파일마다 행위자와 피해를 정한다. 정의의 형식은 바꾸지 않는다.

| 도메인 | 행위자 | 피해 |
|---|---|---|
| 소프트웨어 | 에이전트·유저·외부 서비스 | 실패·회귀·데이터 손상·추적성 상실 |

`p8-risk-analysis-profile`의 결론은 소프트웨어 치환만 적는다. 이 결정은 그 치환이 어느 정의를 바꾼 것인지를 적는다. 다른 도메인 프로파일은 같은 원 정의에서 자기 행 하나를 더한다.
