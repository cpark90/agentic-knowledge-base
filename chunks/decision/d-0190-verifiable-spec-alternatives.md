---
id: https://agentic-knowledge-base.dev/id/chunk-d0190
type: decision
level: concrete
title_ko: 대안 — 검증 가능한 명세
title: Alternatives — specification as verifiable contract
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:56+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-verifiable-spec
---
**대안** — 묶음의 두 결정마다 원천(harness-concrete `docs/odr-contract-verify.md`)이 대비한 안을 적는다.

- d-0181(능력에 매단다): 계약을 선택된 구현 후보에 매다는 안은 기각이다. 계약을 능력에 매달아야 판정 기준이 명세에서만 오고(INV-3), 다른 후보로 다시 묶어도 판정이 바뀌지 않는다(INV-4). contract-demo 레시피의 후보 교체에서 계약별 판정이 같게 나왔다("Where the VERIFY axis lives"·"Level 4").
- d-0182(검증 가능한 계약): 그래프 검증(`validate.py`)만으로 명세를 검증된 것으로 보는 안은 기각이다. 그래프가 잘 형성되었다는 것은 산출물이 능력의 계약을 만족한다는 것을 보이지 않으므로 명세→산출 방향의 판정기(`verify_contract.py`)를 둔다(문서 머리 절).
