---
id: https://agentic-knowledge-base.dev/id/chunk/9adc9618-34fd-4767-92ab-eb2922b639c1
type: norm
level: logical
title_ko: docs/method.md 절 — 개발 KB의 저작 흐름과 완료 절차
title: docs/method.md section — the development KB authoring flow and completion procedures
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1471db95-dd63-42f0-8759-b3d76584253a
composite: {id: https://agentic-knowledge-base.dev/id/composite/1471db95-dd63-42f0-8759-b3d76584253a, title_ko: docs/method.md의 development 절 묶음, title: docs/method.md development section group, part_of: https://agentic-knowledge-base.dev/id/composite/c040ba95-dc6c-4c10-af69-8d0d4c0cf6ec, ordered: [https://agentic-knowledge-base.dev/id/chunk/9adc9618-34fd-4767-92ab-eb2922b639c1, https://agentic-knowledge-base.dev/id/chunk/40f2e9c7-36a2-4c5f-ba32-f06eca745ead]}
heading: 저작 흐름과 완료
depth: 2
form: table
columns: [절차, 입력 → 산출, 게이트, 결정]
link_column: 결정
items: [p6-transition-gates#2, p9-candidate-storage#4, p7-contract-first#2, p7-schema-derivation#2, p7-dev-kb-completion#2]
---
**저작 흐름 8단계**는 요구 작성(유저+design) → 형식화(`decision` abstract, `serves`) → 계약
선언(`contract` abstract) → 전개(`decision` logical `-space` / `contract` logical 사후조건 /
`schema` logical) → 확정(design+유저, 체크박스 피드백, `-space` resolved) → 스키마 확정 →
구현(developer, `artifact`) → 리뷰(`annotation`)다
([`p7-authoring-flow`](../../decision/p7-authoring-flow/conclusion.md)). 요구마다 독립적으로
정제하고, 요구 간 순서는 `depends-on`과 ODD 시간 제약이 정한다.
