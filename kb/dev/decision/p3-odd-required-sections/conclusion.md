---
id: https://agentic-knowledge-base.dev/id/chunk/00deb95f-2fe6-42a3-aaa2-648cf1794ce5
type: decision
level: concrete
title_ko: ODD는 일곱 절과 속성별 판정 방법으로 쓴다
title: The ODD has seven sections and a check per property
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0059]
part_of: https://agentic-knowledge-base.dev/id/composite/80a7e3df-fc4f-452e-94fc-4acead84d77b
composite: {id: https://agentic-knowledge-base.dev/id/composite/80a7e3df-fc4f-452e-94fc-4acead84d77b, title_ko: ODD 문서의 내용 구조, title: Required structure of the ODD document}
---
**결론** — 파일명은 `project-odd`, 표기는 0.4절 명세 형식(mode / include / exclude / conditional)이다. 다음 절을 갖는다.

| 절 | 내용 | 필수 |
|---|---|---|
| 식별 | 대상 시스템, 버전, 책임 에이전트, 상위 ODD | 예 |
| 정적 요소 | 작업 기간 동안 변하지 않는 구조 | 예 |
| 환경 조건 | 작업 밖에서 주어지며 변할 수 있는 조건 | 예 |
| 동적 요소 | 작업 중 움직이는 행위자와 산출물 | 예 |
| 명시 제외 | 설계 범위 밖임을 명시적으로 적은 것 | 예 |
| 조건부 규정 | "X이면 Y" 형태의 부가 조건 | 선택 |
| 판정 방법 | 위 모든 속성의 관측 수단 | 예 |

정적·환경·동적의 각 속성은 **값 또는 범위**와 **`check:` 판정 수단**을 함께 적는다 (예: `database = PostgreSQL 15..16  check: SELECT version()`). 명시 제외는 검토 시점과 이유를 적는다.
