---
id: https://agentic-knowledge-base.dev/id/chunk/82bd5b30-ee45-4572-9ee0-f6207e625287
type: decision
level: concrete
title_ko: 참조의 도달 범위는 단위별로 명시하는 트레이드오프다
title: Reference reach is a trade-off stated per unit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0184-reference-reach-tradeoff.md, id: https://agentic-knowledge-base.dev/id/chunk-d0184, title_ko: "참조의 도달 범위는 단위별로 명시하는 트레이드오프다", title: "Reference reach is a per-unit, explicitly recorded tradeoff"}, {resource: git:aeb0a58:chunks/decision/d-0189-spec-content-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0189, title_ko: "대안 — 명세가 담는 것", title: "Alternatives — what a specification carries"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0184, https://agentic-knowledge-base.dev/id/chunk-d0189]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/3343eae6-4b88-48c8-abfc-da8bb1af307a
composite: {id: https://agentic-knowledge-base.dev/id/composite/3343eae6-4b88-48c8-abfc-da8bb1af307a, title_ko: 단위마다 기록하는 참조의 도달 범위, title: Reference reach recorded per unit}
---
**결론** — 참조는 두 형태 가운데 하나이고, 단위마다 **어느 쪽을 왜 골랐는지 기록한다.** 내부(저장소 상대) 참조는 어디서나 해석되지만 그 자체가 사본이다. 반면 외부 참조는 명세를 순수하게 유지하지만 원천에 닿는 곳에서만 해석된다. 해석되지 않는 참조는 **실패가 아니라 스텁으로 강등**한다.
