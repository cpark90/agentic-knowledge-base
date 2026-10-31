---
id: https://agentic-knowledge-base.dev/id/chunk/b8033cb3-5883-44dc-b70e-9a31fd55c7d6
type: decision
level: concrete
title_ko: 자동 선택은 전순서 정책으로 결정한다
title: Automatic selection is decided by a total-order policy
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0176-deterministic-selection-policy.md, id: https://agentic-knowledge-base.dev/id/chunk-d0176, title_ko: "자동 선택은 전순서 정책으로 결정한다", title: "Automatic choice needs a total-order selection policy"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0176]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/edb7941d-bfc4-43d0-84ce-b2201e7fddb1
composite: {id: https://agentic-knowledge-base.dev/id/composite/edb7941d-bfc4-43d0-84ce-b2201e7fddb1, title_ko: 결정론적 선택 정책, title: Deterministic selection policy}
---
**결론** — 후보가 여럿 남은 채로도 산출을 내야 하는 무인 경로에서는 사람의 선택을 기다리지 않고 **전순서(total order) 선택 정책**으로 하나를 고른다. 정책은 조건 필터와 우선 등급, 값 비교, 안정 식별자의 차례로 적용되어 항상 유일한 답을 낸다.
