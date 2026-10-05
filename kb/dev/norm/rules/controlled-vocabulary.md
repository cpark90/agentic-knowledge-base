---
id: https://agentic-knowledge-base.dev/id/chunk/b1e2fe77-9471-4ed7-9f22-bb1acb6a4aaa
type: norm
level: logical
title_ko: docs/rules.md 절 — 통제 어휘
title: docs/rules.md section — Controlled vocabulary
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
heading: 통제 어휘
depth: 3
---
데이터의 술어는 `agt:` 온톨로지 또는 등록된 표준 어휘(rdf·rdfs·owl·xsd·skos·sh·prov·
dcterms·co·obo) 안이어야 한다. prov·skos 용어는 W3C 원문에 실재해야 한다. 원문은 `MODULE.bazel`의
`http_file`로 해시 고정한 `@prov_o`·`@skos`다. 게이트가 원문과 대조한다 (2026-09-12). `agt:` 접두어인데
온톨로지에 없으면 오타 또는 무단 어휘 생성이고, 등록되지 않은 네임스페이스면 어휘 우회다. 둘을 다른
메시지로 구분해 보고한다 ([p0-agt-namespace](../../decision/p0-agt-namespace/conclusion.md)). 목록의 단일 정의처는 `tools/kb_lib.py`다.
