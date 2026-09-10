---
id: https://agentic-knowledge-base.dev/id/chunk/acd3f19b-bb9e-448f-acf3-ac227733c8ab
type: decision
level: concrete
title_ko: 개발 프로파일의 카탈로그는 아홉 역할이고 설계·구현·운영이 write를 나눈다
title: The development profile catalog has nine roles and splits write across design, build, and operations
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7, https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0125]
part_of: https://agentic-knowledge-base.dev/id/composite/4dbb535c-ea05-4b67-accf-29c2ef7f6ee3
composite: {id: https://agentic-knowledge-base.dev/id/composite/4dbb535c-ea05-4b67-accf-29c2ef7f6ee3, title_ko: 개발 프로파일의 역할별 plane 권한, title: Plane permissions per role in the development profile}
---
**결론** — 참조 프로파일(소프트웨어 개발)의 에이전트 카탈로그를 아홉 역할로
정하고 plane 권한을 아래로 고정한다.

- **orchestrator** — 설계 반영·구현 관리·dispatch. `decision`(RW), 나머지 R
- **verification & validation** — 검증·확인. `artifact` 검증 역할(RW),
  `requirement`·`decision` logical 기준(R), `annotation`(W)
- **design** — 설계 전용. `decision`(RW) + **T-Box와 ODD 편집 권한**,
  `schema`·`contract`(R)
- **developer** — 모듈 구현. `artifact`(RW), `contract`·`schema`(R)
- **research** — 외부 조사. 외부 전용
- **inspection** — dispatch·git 관리. 전 plane R
- **inspection worker** — 조사 전용, 수정 금지. 읽기 전용
- **claim** — 사용성 개선 주장. `decision` 제안만
- **audit** — 감사. 전 plane R + 실행 기록

**설계 / 구현 / 운영은 독립 분리한다** — 세 영역의 역할이 같은 write scope를
갖지 않는다.
