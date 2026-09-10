---
id: https://agentic-knowledge-base.dev/id/chunk/870158d1-2a3e-4b89-b721-7afb4d7a095d
type: decision
level: concrete
title_ko: 조건의 3갈래 분류와 둘째 수준 고정
title: Three condition branches with a fixed second level
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0030]
part_of: https://agentic-knowledge-base.dev/id/composite/7d50713a-5c4d-485d-8a46-a36172a1b114
composite: {id: https://agentic-knowledge-base.dev/id/composite/7d50713a-5c4d-485d-8a46-a36172a1b114, title_ko: 경계 조건은 3갈래와 둘째 수준까지 고정하고 판정 등급을 갖는다, title: Boundary conditions are fixed to three branches and a second level with decidability grades}
---
**결론** — 스코프와 가정이 언급하는 조건은 최상위에서 세 갈래다. 이 분류는
온톨로지 `related/` 모듈의 최상위 개념이다.

- **정적 요소** — 작업 기간 동안 변하지 않는 구조. 언어·런타임, 빌드·패키징
  체계, 저장소 구조, 아키텍처 스타일, 코딩 규약, 라이선스·규제 정책
- **환경 조건** — 작업 밖에서 주어지며 변할 수 있는 조건. 의존성 버전, 인프라
  자원, 외부 서비스, 연결성, 자원 예산, 시간, 규제·컴플라이언스 상태
- **동적 요소** — 작업 중 움직이는 행위자와 산출물. 활성 에이전트, 유저, 동시
  변경, 미해소 스레드, 데이터 볼륨·트래픽, 외부 행위자, **시간 제약**

둘째 수준까지를 `related/condition`에 고정하고 ODD(3.2절)의 모든 속성이 그중
하나에 속하게 한다. 셋째 수준 이하는 프로젝트별로 둔다.

**모든 조건은 객관적 판정 방법을 갖는다.** "인프라가 정상이다"는 조건이
아니고 "헬스체크 엔드포인트가 200을 반환한다"가 조건이다. 판정 방법이 없는
조건은 6.5절 `unverified`로만 존재한다. 판정 등급(3.9절) C 이상이 대부분이어야
하며, C·D가 많은 갈래는 판정 방법을 개선하거나 ODD에서 빼고 가정으로 내린다.
