---
id: https://agentic-knowledge-base.dev/id/chunk/bd30d659-57db-4c01-a4f4-8f8f9b4d4969
type: decision
level: abstract
title_ko: 후보 결정의 자리 변수를 abstract 결정으로 두는 근거
title: Why the variable of where candidate decisions sit is an abstract decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:45:22+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:56:56+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/97f58cf4-62e3-42d5-9f8a-eab5b8eddcce
---
**근거** — 결정의 abstract는 결정 변수 선언이다(`p6-plane-level-occupancy`, `p7-decision-spans-three-levels`). 설계 공간의 확정 후보는 출발 항목을 head에서 `refines`해야 한다(`p9-candidate-storage`). 그런데 앞의 출발 `p9-candidate-storage` 결론은 concrete라 어떤 결정도 그것을 `refines`할 수 없었다. 이 변수를 abstract로 떼어 출발로 두면 확정 결론(concrete)이 위 수준을 정제하는 규칙을 지킨다(Q85-a, Q92-a, Q93-c).
