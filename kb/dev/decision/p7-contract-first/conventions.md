---
id: https://agentic-knowledge-base.dev/id/chunk/01c7e26a-4a80-418b-8631-0d8ed12e6079
type: decision
level: concrete
title_ko: 규범 문서 규약 — 계약이 구현보다 먼저 확정되고 논리 수준의 계약이 V&V 기준의 직접 재료다
title: Normative-document conventions — Contracts are fixed before implementation, and contract logical is the direct material of V&V criteria
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:18:59+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5957a996-1394-4279-8e3c-31b55c586f62
---
**규약** — `p7-contract-first`의 결론을 규범 문서에 싣는 문장이다.

규약: 계약 우선 | 추상 수준의 `contract`가 구현보다 먼저 확정되고, 계약이 없는 구현은 정제가 끊긴 것이다. 논리 수준의 계약인 사후조건이 V&V 기준의 재료다
규약: 계약 선언에서 구현으로 | 시그니처를 먼저 선언하고, CEL로 쓴 사후조건이 V&V 기준의 재료가 된다 | `contract_check`(미구현)
