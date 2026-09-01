---
iri: https://agentic-knowledge-base.dev/id/chunk-d0059
plane: decision
level: concrete
label_ko: ODD 문서의 절 구성과 속성 표기 형식
label_en: Required sections and attribute notation of the ODD document
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — ODD의 파일명은 `project-odd`이고 0.4절 명세 형식(mode / include /
exclude / conditional)으로 쓴다. 절은 **식별·정적 요소·환경 조건·동적 요소·
명시 제외·판정 방법**이 필수이고, 조건부 규정만 선택이다.

**근거** (노트 3.2절)
- 식별 절이 대상 시스템·버전·책임 에이전트·상위 ODD를 고정한다. 상위 ODD
  참조가 여기 있어야 계층 검사(3.11절)가 성립한다.
- 정적 요소 / 환경 조건 / 동적 요소 세 절은 조건 3분류를 그대로 따르며, 각
  속성에 **값 또는 범위**를 적는다 — 값이 없는 속성은 실행 시 대조의 대상이
  되지 않는다.
- 절 구성이 고정되어야 파생물이 참조할 속성의 위치와 이름이 정해지고, 빠진
  절 자체가 검출 가능한 결함이 된다.

**표기** — 속성 한 줄은 `이름 = 값 또는 범위` + `check:` 판정 수단이다
(`database = PostgreSQL 15..16  check: SELECT version()`). 명시 제외 항목은
검토 시점과 제외 사유를 함께 적고, 조건부 규정은 "X이면 Y" 형태로 쓴다.
