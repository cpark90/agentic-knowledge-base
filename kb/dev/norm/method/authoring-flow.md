---
id: https://agentic-knowledge-base.dev/id/chunk/9adc9618-34fd-4767-92ab-eb2922b639c1
type: norm
level: logical
title_ko: docs/method.md 절 — 개발 KB의 저작 흐름과 완료 절차
title: docs/method.md section — the development KB authoring flow and completion procedures
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:16:36+09:00}
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
**저작 흐름 8단계**는 아래 순서로 진행한다. 요구마다 독립적으로 정제하고, 요구 사이의 순서는
`depends-on`과 ODD 시간 제약이 정한다 ([`p7-authoring-flow`](../../decision/p7-authoring-flow/conclusion.md)).

1. 요구 작성 단계에서는 유저와 design이 요구를 쓴다.
1. 형식화 단계에서는 `decision` 지식 종류로 정제 수준이 추상인 항목을 쓰고 `serves` 링크를 단다.
1. 계약 선언 단계에서는 `contract` 지식 종류로 추상 수준의 계약을 선언한다.
1. 전개 단계에서는 논리 수준에서 `decision`의 `-space`와 `contract`의 사후조건, `schema`를 쓴다.
1. 확정 단계에서는 design과 유저가 체크박스 피드백으로 고르고 `-space`를 `resolved`로 닫는다.
1. 스키마 확정 단계에서는 스키마를 확정한다.
1. 구현 단계에서는 developer가 `artifact` 지식 종류로 구현한다.
1. 리뷰 단계에서는 `annotation` 지식 종류로 리뷰를 남긴다.
