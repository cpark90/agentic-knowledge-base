---
id: https://agentic-knowledge-base.dev/id/chunk-d0008
type: decision
level: concrete
title_ko: ODD가 경계의 기반이다
title: ODD is the foundation of boundaries
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 프로젝트의 운영 조건을 ODD 문서 하나에 명세하고, 스코프·가정·
시나리오·설계 공간·커버리지·하네스 경계를 전부 ODD에서 파생시킨다.
ODD에 없는 속성을 참조하는 파생물은 검사 게이트가 거부한다 — 대응은
ODD 확장 또는 파생물 기각뿐이며, 그냥 통과는 없다.

**근거** (노트 Part III, 3.3절)
- 스코프가 무엇의 부분집합인지, 가정이 판정 가능한 명제인지, 시나리오가
  설계 범위 안인지, 커버리지의 분모가 무엇인지 — 전부 ODD 없이는 정의
  불가다.
- 모든 조건은 객관적 판정 방법을 가져야 실행 시 대조(3.5절)가 가능하다.
  "인프라가 정상이다"가 아니라 "헬스체크가 200을 반환한다"가 조건이다.
- 명시 제외 절이 필수다 — 적지 않은 것과 검토 후 제외한 것을 구분해야
  다음 검토자가 같은 검토를 반복하지 않는다.

**구조** (0.4절, ISO 34503) — 조건은 정적 요소 / 환경 조건 / 동적 요소
3분류, 명세는 mode / include / exclude / conditional 네 문장으로 쓴다.
