---
id: https://agentic-knowledge-base.dev/id/chunk/db979862-55e5-49d2-a35f-da151fe77d39
type: decision
level: logical
title_ko: 전체 컨텍스트 전달의 기각과 병렬 시도의 조건
title: Rejecting full-context dispatch; the condition for parallel attempts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/7e1f24c0-e217-46a1-8599-5fd5ac39e486
---
**대안** — dispatch 대상에게 전체 컨텍스트를 넘기는 안. 기각 — 적용 범위가 무엇을 볼지 이미 정해 두었으므로 적용 범위로 거른 작업 집합만 넘긴다. 요약을 매번 사람이 재단하면 그 재단이 인지 결함의 원인이 된다 (11.3절).

**대안(미확정)** — 같은 작업을 여러 에이전트가 병렬로 시도하고 최선을 고르는 모드(`[안]`). 원시 궤적끼리 비교·선택은 성립하지 않는다 — 비교·선택·재사용의 단위는 구조화 요약이다 (11.3절).
