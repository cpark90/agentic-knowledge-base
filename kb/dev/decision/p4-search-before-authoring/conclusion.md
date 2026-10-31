---
id: https://agentic-knowledge-base.dev/id/chunk/afc0ae45-1b24-4d30-886c-76cac11671b4
type: decision
level: concrete
title_ko: 만들기 전에 검색하고 노드는 한 가지 책임만 담는다
title: Search before creating, and a node carries a single responsibility
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0160-search-before-authoring.md, id: https://agentic-knowledge-base.dev/id/chunk-d0160, title_ko: "만들기 전에 검색하고 노드는 한 가지 책임만 담는다", title: "Search before authoring, and a node carries one responsibility"}, {resource: git:aeb0a58:chunks/decision/d-0187-authoring-discipline-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0187, title_ko: "대안 — 저작 규율", title: "Alternatives — authoring discipline"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0160, https://agentic-knowledge-base.dev/id/chunk-d0187]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/54ecc54e-24cd-420e-b5c9-4405958c87ec
composite: {id: https://agentic-knowledge-base.dev/id/composite/54ecc54e-24cd-420e-b5c9-4405958c87ec, title_ko: 검색 선행과 단일 책임, title: Search before authoring and single responsibility}
---
**결론** — 한 노드는 한 가지만 담으며, 그 한 가지는 한 페르소나나 한 정책, 한 능력이다. 새 노드를 만들기 전에는 **검색 도구로 같은 것이 이미 있는지 먼저 찾는다**. 그래서 없어서 만드는 것과 못 찾아서 만드는 것을 구분한다.
