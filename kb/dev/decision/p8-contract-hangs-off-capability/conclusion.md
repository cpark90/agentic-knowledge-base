---
id: https://agentic-knowledge-base.dev/id/chunk/3bd73a17-5b74-43ac-947d-15f500f2c6ca
type: decision
level: concrete
title_ko: 계약은 구현이 아니라 능력에 매단다
title: A contract hangs off the capability, not the implementation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0181-contract-hangs-off-capability.md, id: https://agentic-knowledge-base.dev/id/chunk-d0181, title_ko: "계약은 구현이 아니라 능력에 매단다", title: "Contracts hang off the capability, not the implementation"}, {resource: git:aeb0a58:chunks/decision/d-0190-verifiable-spec-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0190, title_ko: "대안 — 검증 가능한 명세", title: "Alternatives — specification as verifiable contract"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0181, https://agentic-knowledge-base.dev/id/chunk-d0190]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bc99c810-3637-44a9-b446-350ceb648180
composite: {id: https://agentic-knowledge-base.dev/id/composite/bc99c810-3637-44a9-b446-350ceb648180, title_ko: 능력에 매다는 계약, title: Contract attached to the capability}
---
**결론** — 산출물의 합격 기준인 계약은 그것을 실현한 **구현이 아니라 명세 쪽 능력(capability)**에 매단다. 그래서 어느 구현이 그 능력을 실현하든 판정 기준이 같아지고, 구현 교체가 판정 결과를 바꿀 수 없다.
