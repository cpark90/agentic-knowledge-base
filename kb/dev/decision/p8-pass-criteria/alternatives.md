---
id: https://agentic-knowledge-base.dev/id/chunk/8b4bb7eb-ae79-42cc-a425-ca13529d58be
type: decision
level: logical
title_ko: 테스트 케이스 안 기준의 기각
former_title_ko: ["케이스 안 기준의 기각"]
title: Rejecting criteria embedded in cases
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/14433614-5dd7-4df3-b32c-2422a25daef3
---
**대안** — 합격 기준을 시나리오·테스트 케이스 안에 두는 안. 기각 — 자극과 판정을 한 단위 지식에 두면 기준 변경이 테스트 케이스 변경으로 보여 같은 자극에 대한 판정 강화가 이력에서 사라진다. 기준은 V&V `contract` logical의 별도 단위 지식이고 `verifies` 속성으로 바인딩된다 (8.11절).
