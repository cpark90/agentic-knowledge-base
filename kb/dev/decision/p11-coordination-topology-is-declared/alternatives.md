---
id: https://agentic-knowledge-base.dev/id/chunk/835dd3bd-865f-4e18-8bf7-c515966d43e1
type: decision
level: concrete
title_ko: 전역 조율 방식 하나와 TBox 변경으로 방식을 들이는 안은 택하지 않는다
title: A single global topology and adding topologies through TBox changes are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0189-spec-content-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:16:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:16:35+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/2c1f938b-829d-4a41-b29b-b82d166d0ab5
---
**대안** — 원천(harness-concrete `docs/composition-methodology.md`)이 대비한 안 둘을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 체계 전역에 조율 방식 하나를 고정한다 | 하네스가 채널을 고르거나 선언하므로 전역 위상이 강제되지 않고, orchestrator-workers와 peer-mesh가 공존한다(composition-methodology "Coordination topology") |
| 새 방식을 TBox 변경으로 들인다 | 패턴과 채널 개체 한 쌍과 그것을 문 하네스를 더하는 것으로 충분하다(같은 절) |
