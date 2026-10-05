---
id: https://agentic-knowledge-base.dev/id/chunk/4137bc99-bfe1-4503-8ddb-83b9c7564180
type: norm
level: logical
title_ko: docs/method.md 절 조회의 이어짐 — 컨텍스트 예산과 작업 집합 조립 알고리즘
title: docs/method.md retrieval section continued — the context budget and the workset assembly algorithm
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:22:52+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/8fb872fb-34de-4823-8019-358e4f069652
continues: true
---
조립 알고리즘은
[`p0-workset-anchor-neighbourhood`](../../decision/p0-workset-anchor-neighbourhood/conclusion.md)
결정이고, 첫 형태는 `workset`([`tools.md`](../../../../docs/tools.md))이다. 알고리즘의 순서는 앵커 → 이웃 확장 →
우선순위 → 예산 패킹이다. 예산 상한식은 Δ = m·k·1,092이고, 앵커 m × 이웃 k × 청크 상한(토큰)이다 — 예산은 5,418 토큰(42×129).
