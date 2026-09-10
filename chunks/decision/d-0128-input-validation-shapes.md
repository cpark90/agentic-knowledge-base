---
id: https://agentic-knowledge-base.dev/id/chunk-d0128
type: decision
level: concrete
title_ko: 입력도 shape로 검사한다
title: Inputs are validated by shapes
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 입력도 청크와 같이 shape로 검사한다. 검사 항목은 네 입력에 대해
아래로 고정한다.

**근거** (노트 9.6절)
- **에이전트 카탈로그** — 모든 역할이 최소 하나의 read plane을 가질 것.
  설계/구현/운영 역할이 같은 write plane을 공유하지 않을 것. 동시 활성
  가능한 합이 ODD 동적 요소 안에 있을 것.
- **태그 어휘** — 태그가 온톨로지 개념일 것. 중복 없음.
- **프로세스 규칙** — 스코프 conditional로 표현 가능할 것. 순환 없음.
- **재판정 경계** — 최소 하나.
- 입력이 온톨로지 어휘로 쓰이므로(9.1절) 청크와 같은 검사 수단을 그대로
  쓴다. 검사 없이 들어온 입력은 그 위의 파생물 전체를 조용히 오염시키며,
  카탈로그의 경우 스코프 전부가 그 오염을 물려받는다.
