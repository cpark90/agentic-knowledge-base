---
id: https://agentic-knowledge-base.dev/id/chunk-d0125
type: decision
level: concrete
title_ko: 개발 프로파일의 역할별 plane 권한
title: Plane permissions per role in the development profile
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 참조 프로파일(소프트웨어 개발)의 에이전트 카탈로그를 아홉 역할로
정하고, 각 역할의 plane 권한을 아래로 고정한다.

**근거** (노트 9.2절)
- **orchestrator** — 설계 반영, 구현 관리, dispatch. `decision`(RW), 나머지 R.
- **design** — 설계 전용. `decision`(RW) + **T-Box와 ODD 편집 권한**,
  `schema`·`contract`(R).
- **developer** — 모듈 구현. `artifact`(RW), `contract`·`schema`(R).
- **verification & validation** — 검증·평가. `artifact`(R), 시나리오(R),
  `annotation`(W).
- **inspection** — dispatch, git 관리. 전 plane R.
  **inspection worker** — 조사 전용, 수정 금지. 읽기 전용.
- **research** — 외부 조사. 외부 전용.
- **claim** — 사용성 개선 주장. `decision` 제안만.
- **audit** — 감사. 전 plane R + 실행 기록.

**write 권한이 겹치지 않는다** — `decision`은 orchestrator·design,
`artifact`는 developer, `annotation`은 V&V. 9.2절 "설계/구현/운영 독립
분리"의 구체형이며, 9.6절 입력 검증이 이 비겹침을 검사한다.
