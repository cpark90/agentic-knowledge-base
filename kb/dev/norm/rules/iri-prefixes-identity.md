---
id: https://agentic-knowledge-base.dev/id/chunk/ce184703-4fba-4899-b344-6d074d799e70
type: norm
level: logical
title_ko: docs/rules.md 절 개체 IRI 접두사의 이어짐 — IRI는 불투명하게 유지한다
title: docs/rules.md entity IRI prefix section continued — IRIs stay opaque
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
continues: true
---
IRI는 불투명하게 유지한다. 라벨이나 경로가 바뀌어도 IRI가 유지되어야 시간 정체성이
성립한다. 그래서 v3부터 uuid다 (유저 결정 Q1). 사람이 읽는 이름은 IRI가 아니라
`rdfs:label`이고, 내용 버전은 `agt:contentHash`다.
