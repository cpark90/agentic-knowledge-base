---
id: https://agentic-knowledge-base.dev/id/chunk/5287133e-f7a3-4913-8aaf-062647cf5491
type: decision
level: concrete
title_ko: 후보 링크와 확정 링크는 A-Box의 개체 클래스다
title: CandidateLink and ConfirmedLink are A-Box individuals
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
part_of: https://agentic-knowledge-base.dev/id/composite/526f1fb6-5721-4b89-b8ac-3955dcbf6a37
composite: {id: https://agentic-knowledge-base.dev/id/composite/526f1fb6-5721-4b89-b8ac-3955dcbf6a37, title_ko: 후보 링크와 확정 링크는 A-Box의 개체 클래스다, title: CandidateLink and ConfirmedLink are A-Box individuals}
---
**결론** — **`agt:CandidateLink`** 와 **`agt:ConfirmedLink`** 를 클래스로 구분한다. **둘 다 A-Box의 개체다.** 구축이든 복원이든 링크는 **후보로 시작한다.**

| 단계 | 동작 | 방식 |
|---|---|---|
| 후보 생성 | 가능한 링크 열거 | 구축: 편집 기록 (9.3절) / 복원: 임베딩 검색 상위 후보 |
| 제약 검사 | TIM 위반 후보 탈락 | 결정론적. plane 제한·카디널리티·단방향 규칙 |
| 판정 | 남은 후보의 성립 여부 | 9.8절 판정 근거. 필요 시 언어모델 분류 |
| 확정 | 후보 → 확정 | 유저 또는 위임된 에이전트의 확인 |

상황별 동작 — 후보 여럿이면 **유지(정상 상태)**, 새 제약이 들어오면 위반 후보 탈락, 하나 남으면 확인 후 승격, 없으면 모순 신호로 상위 plane 재검토.

후보의 가능성 표현과 확정 메커니즘은 Part VIII이 정의하며, 이 결정은 그것을 추적성에 적용한 것이다.
