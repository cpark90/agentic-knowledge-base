---
id: https://agentic-knowledge-base.dev/id/chunk/475d2733-e7b8-4b2f-beaa-f369ea22bd73
type: decision
level: concrete
title_ko: 조건은 정적 요소·환경 조건·동적 요소 세 갈래이고 둘째 수준은 제안 큐를 거쳐 코어에 더한다
title: Conditions branch into static elements, environmental conditions and dynamic elements, and the second level grows in the core through the proposal queue
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/870158d1-2a3e-4b89-b721-7afb4d7a095d]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4f241f3b-cc00-43cb-b95e-bf55e145270e
composite: {id: https://agentic-knowledge-base.dev/id/composite/4f241f3b-cc00-43cb-b95e-bf55e145270e, title_ko: 경계 조건은 3갈래이고 둘째 수준은 제안 큐로 확장하며 판정 등급을 갖는다, title: Boundary conditions have three branches, a second level extended through the proposal queue, and decidability grades}
---
**결론** — 스코프와 가정이 언급하는 조건은 최상위에서 세 갈래다. 이 분류는 온톨로지 `related/` 모듈의 최상위 개념이다.

- **정적 요소** — 작업 기간 동안 변하지 않는 구조. 언어·런타임, 빌드·패키징 체계, 저장소 구조, 아키텍처 스타일, 코딩 규약, 라이선스·규제 정책
- **환경 조건** — 작업 밖에서 주어지며 변할 수 있는 조건. 의존성 버전, 인프라 자원, 외부 서비스, 연결성, 자원 예산, 시간, 규제·컴플라이언스 상태
- **동적 요소** — 작업 중 움직이는 행위자와 산출물. 활성 에이전트, 유저, 동시 변경, 미해소 스레드, 데이터 볼륨·트래픽, 외부 행위자, **시간 제약**

둘째 수준은 코어 `related/condition`에 두고 ODD(3.2절)의 모든 속성이 그중 하나에 속하게 한다. **둘째 수준은 확장 가능하다.** 새 둘째 수준 조건 개념은 `term-propose`로 `kb/ontology/proposals/`에 제안하고, 승인되면 코어 `related/condition`에 더한다(유저 답 Q11-b, 2026-10-03). 셋째 수준 이하는 프로젝트별로 두고 도메인 프로파일이 더한다(`p2-skeleton-and-domain-profile`). 이 경계는 바뀌지 않는다.

**모든 조건은 객관적 판정 방법을 갖는다.** "인프라가 정상이다"는 조건이 아니고 "헬스체크 엔드포인트가 200을 반환한다"가 조건이다. 판정 방법이 없는 조건은 6.5절 `unverified`로만 존재한다. 판정 등급(3.9절)은 A 기계 즉시 판정에서 D 판정 불가까지이고, C·D가 많은 갈래는 판정 방법을 개선하거나 ODD에서 빼고 가정으로 내린다.

이 결정은 `p0-condition-taxonomy`를 대체한다. 바뀐 것은 둘째 수준의 고정 하나다.
