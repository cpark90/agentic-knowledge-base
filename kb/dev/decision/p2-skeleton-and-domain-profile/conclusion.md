---
id: https://agentic-knowledge-base.dev/id/chunk/93a15ba6-326d-4e40-ac54-f76736f46001
type: decision
level: concrete
title_ko: 프로파일은 코어를 확장만 하는 온톨로지 모듈이다
title: A profile is an ontology module that only extends the skeleton
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0056, https://agentic-knowledge-base.dev/id/chunk-d0057, https://agentic-knowledge-base.dev/id/chunk-d0021]
part_of: https://agentic-knowledge-base.dev/id/composite/f28573cc-2a81-4db9-9497-160a41fdd56d
composite: {id: https://agentic-knowledge-base.dev/id/composite/f28573cc-2a81-4db9-9497-160a41fdd56d, title_ko: 도메인 중립 코어와 도메인 프로파일, title: Domain-neutral skeleton and domain profiles}
---
**결론** — 체계는 **도메인 중립 코어**과 **도메인 프로파일**로 나뉜다. 코어는 작업 종류와 무관한 것이고, 프로파일은 그것을 특정 작업 종류에 맞게 채운 것이다.

| 코어가 정하는 것 | 프로파일이 채우는 것 |
|---|---|
| plane 여섯과 각각의 판정 방식 | 각 plane의 청크가 무엇인가, 판정 도구는 무엇인가 |
| level 다섯 단계 | 각 단계의 assertion 형식 |
| 경계 조건 3갈래와 둘째 수준 | 셋째 수준 이하의 조건 개념 |
| 결함 요인 3갈래 · 링크 타입 | 도메인 고유 하위 유형 · 링크 양 끝의 프로파일 클래스 |
| 42줄 상한 · 앵커 해석 방식 | plane별 오버라이드와 "줄"의 단위 · 실제 해석기 |

**프로파일은 온톨로지 모듈이다.** `profile/<domain>`에 두고 코어 모듈을 import하며, **코어 클래스의 하위 클래스와 shape만 추가한다. 코어를 수정하는 프로파일은 검사 실패다.**

한 프로젝트는 프로파일을 여럿 가질 수 있다 — 개발 프로젝트에도 문서 작성 작업이 있다. 청크는 프로파일 클래스 하나에 속하되 **링크는 프로파일을 넘는다.** 참조 프로파일은 `development`이고, 부록 D가 다른 프로파일의 템플릿이다.
