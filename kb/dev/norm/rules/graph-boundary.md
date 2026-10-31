---
id: https://agentic-knowledge-base.dev/id/chunk/a3c10c2f-5f85-4602-a43f-ce9358ec9cb6
type: norm
level: logical
title_ko: docs/rules.md 절 — 그래프 안과 밖
title: docs/rules.md section — Inside and outside the graph
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:33:38+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4ae2bbc4-2198-4191-b626-091c3aecdb23
heading: 그래프 안과 밖
depth: 2
---
검사 대상인 지식과 검사 대상이 아닌 문서를 가르는데, 소통 기록과 지식을 섞으면 통제 어휘 검사가 무의미해지기
때문이다. 지식은 `kb/{ontology,odd,dev,vv}/`와 `kg/`에 있고, 문서는 `docs/`와 `.claude/`에 있다.
문서는 결정을 복사하지 않고 **IRI로 인용**한다. 복사하면 이중 관리가 되고, 원본과 사본이 어긋나는
순간 어느 쪽이 원본인지 알 수 없어지기 때문이다 ([p4-projection-as-query](../../decision/p4-projection-as-query/conclusion.md)).
