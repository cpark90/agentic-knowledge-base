---
id: https://agentic-knowledge-base.dev/id/chunk/4137bc99-bfe1-4503-8ddb-83b9c7564180
type: norm
level: logical
title_ko: docs/method.md 절 조회의 이어짐 — 컨텍스트 예산과 작업 집합 조립 알고리즘
title: docs/method.md retrieval section continued — the context budget and the workset assembly algorithm
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/8fb872fb-34de-4823-8019-358e4f069652
continues: true
---
작업 집합의 조립 알고리즘은 결정
[`p0-workset-anchor-neighbourhood`](../../decision/p0-workset-anchor-neighbourhood/conclusion.md)가 정하고,
첫 형태는 `workset`이며 [`tools.md`](../../../../docs/tools.md)에 있다. 알고리즘은 앵커를 고르고, 이웃으로 확장하고,
우선순위를 매긴 뒤 예산 안에 패킹한다. 예산 상한식은 `Δ = m·k·1,092`이고, 앵커 수 m과 이웃 수 k, 단위 지식의
토큰 상한을 곱한 값이다. 예산은 42와 129의 곱인 5,418 토큰이다.
