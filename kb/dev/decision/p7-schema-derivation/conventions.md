---
id: https://agentic-knowledge-base.dev/id/chunk/6b872dfb-2c83-4c26-849a-71e0dda6235a
type: decision
level: concrete
title_ko: 규범 문서 규약 — 스키마는 결정에서 파생되어 계약을 제약하고 변경은 호환성 검사를 거친다
title: Normative-document conventions — Schemas derive from decisions, constrain contracts, and changes pass a compatibility check
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d7435609-eefb-48a3-bab6-2cab0f56476e
---
**규약** — `p7-schema-derivation`의 결론을 규범 문서에 싣는 문장이다.

규약: 스키마 | `decision`에서 `derives-from`, `contract`를 `constrains`. 비호환 변경 = 새 IRI + `supersedes`
규약: 스키마 확정 | 호환성 판정 → `wasRevisionOf` 또는 새 IRI + `supersedes` | `schema_compat`(미구현)
