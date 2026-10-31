---
id: https://agentic-knowledge-base.dev/id/chunk/a589cdf9-9e75-4233-858c-eb2dae890647
type: decision
level: concrete
title_ko: 계약을 선택된 구현 후보에 매다는 안은 택하지 않는다
title: Attaching the contract to the selected implementation candidate is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0190-verifiable-spec-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:05:23+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:05:23+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bc99c810-3637-44a9-b446-350ceb648180
---
**대안** — 원천(harness-concrete `docs/odr-contract-verify.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 계약을 선택된 구현 후보에 매단다 | 계약을 능력에 매달아야 판정 기준이 명세에서만 오고(INV-3), 다른 후보로 다시 묶어도 판정이 바뀌지 않는다(INV-4). contract-demo 레시피의 후보 교체에서 계약별 판정이 같게 나왔다("Where the VERIFY axis lives"와 "Level 4") |
