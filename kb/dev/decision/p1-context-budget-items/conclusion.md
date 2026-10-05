---
id: https://agentic-knowledge-base.dev/id/chunk/9ef516f3-4b21-4a67-ad86-df15c950fa35
type: decision
level: concrete
title_ko: 컨텍스트 예산 5,418 토큰은 항목별로 분해해 통제하고 지식 본문은 잔여로 둔다
title: The 5,418-token context budget is decomposed into items, each controlled separately, and the knowledge body gets the remainder
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T01:13:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T01:13:52+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4b1cecd2-e105-480b-93fd-c5d769657b22
composite: {id: https://agentic-knowledge-base.dev/id/composite/4b1cecd2-e105-480b-93fd-c5d769657b22, title_ko: 토큰 단위 컨텍스트 예산의 항목 분해, title: Item breakdown of the token context budget}
---
**결론** — 컨텍스트 예산 5,418 토큰(`p1-chunk-unit-is-tokens`)은 전부 지식에 쓰이지 않는다. 예산을 **항목별로 분해해** 항목마다 다른 수단으로 통제하고, **지식 청크 본문은 잔여**로 둔다. 이 결정은 deprecated 결정 `p1-context-budget-breakdown`의 분해를 토큰 단위로 승계한다.

| 항목 | 예상 소비 | 통제 수단 |
|---|---|---|
| 하네스 지시 (역할·규칙) | 고정 | 짧게 — 온톨로지 어휘로 압축 |
| 작업 집합 (노트 0.5절) | 라벨 목록 + 펼친 청크 | 스코프가 상한 |
| 툴 출력 | 가변, 위험 | 노트 5.3절 읽기 응답 형태로 제한 |
| 대화 이력 | 누적 | 실행 모드(노트 11.3절)로 주기적 비우기 |
| 지식 청크 본문 | **남는 것** | 해당 없음 |

청크 상한(저작 산문 1,092 · 인용 2,856)과 예산 5,418의 값은 `p1-chunk-unit-is-tokens`가 정한다. 이 결정은 그 값을 바꾸지 않고 예산 안의 몫을 나눈다.

미확정: 항목별 실제 소비의 토큰 실측은 공간 `https://agentic-knowledge-base.dev/id/chunk/3ab6d43d-0193-4275-bb9f-5246da93b88a`의 현재 상태에 있다 — 항목별 상한은 정하지 않았다(Q62-a).
