---
id: https://agentic-knowledge-base.dev/id/chunk/13c1f8a2-edd5-4ee1-a3a1-0124a13174c7
type: decision
level: concrete
title_ko: 운영 모니터링은 체계에서 분류·경계·절차·스코프를 받는다
title: Operational monitoring draws classification, boundary, procedure, and scope from the system
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0147]
part_of: https://agentic-knowledge-base.dev/id/composite/f2acea7a-db49-4239-aa5f-eef954055e55
composite: {id: https://agentic-knowledge-base.dev/id/composite/f2acea7a-db49-4239-aa5f-eef954055e55, title_ko: 운영 모니터링이 체계에서 받는 것, title: What operational monitoring draws from the system}
---
**결론** — 전체 시스템을 모니터링하는 에이전트가 이상 신호를 보내면 문제
지점에 orchestrator를 하네스와 함께 생성해 해결하게 한다. 그 구조의 **지식
측면**을 체계가 공급한다.

- 이상 신호의 분류 — `defect` 어휘(인지·상호작용·실행 요인)
- 설계 범위 판정 — ODD 모니터링(3.5절). 밖이면 ODD 이탈, 안이면 결함
- 대응 절차 — `agt:Runbook`. 결함 요인에 `대응` 링크
- 새 orchestrator의 스코프 — 이상 지점 청크가 속한 plane과 그 상위
- 사후 기록 — 관측 청크 → 일반화

**사전 케이스가 모든 이상을 커버한다는 전제는 성립하지 않는다.** 커버되지 않은
이상은 ODD 이탈로 처리하고 유저에게 넘긴다.
