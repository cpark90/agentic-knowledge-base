---
id: https://agentic-knowledge-base.dev/id/chunk/c24d4d9d-6c00-41f7-965e-2749fe65f546
type: decision
level: concrete
title_ko: 규범 문서 규약 — 입력도 shape로 검사한다
title: Normative-document conventions — Inputs are validated by shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792
---
**규약** — `p11-input-validation-shapes`의 결론을 규범 문서에 싣는 문장이다.

규약: 역할별 `agt:maxConcurrent`의 합은 ODD 동적 요소(`id:cond-concurrent-agents`) 안이어야 한다. 그 한도는 현재 5 이하다. 역할을 추가하면 ODD 한도도 함께 검토한다. **이 검사는 `//kg:gate_test`의 `catalog`가 한다**(2026-09-13) ([`docs/tools.md` §게이트 밖](../../../../docs/tools.md#게이트-밖--규약으로-남은-것)).
