---
id: https://agentic-knowledge-base.dev/id/chunk/556b1d8b-17e2-4999-a7cf-12a2cb5e23d0
type: decision
level: concrete
title_ko: 저작 UI는 단일 진실 공급원을 우회하지 않는다
title: The authoring UI does not bypass the single source of truth
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0163-authoring-ui-shares-the-gate.md, id: https://agentic-knowledge-base.dev/id/chunk-d0163, title_ko: "저작 UI는 SSOT를 우회하지 않는다", title: "The authoring UI never forks the source of truth"}, {resource: git:aeb0a58:chunks/decision/d-0187-authoring-discipline-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0187, title_ko: "대안 — 저작 규율", title: "Alternatives — authoring discipline"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0163, https://agentic-knowledge-base.dev/id/chunk-d0187]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/4f30d4af-1a70-4db1-9bf3-1b2fe3bd8b5b
composite: {id: https://agentic-knowledge-base.dev/id/composite/4f30d4af-1a70-4db1-9bf3-1b2fe3bd8b5b, title_ko: 게이트를 공유하는 저작 UI, title: Authoring UI sharing the gate}
---
**결론** — 사람용 편집 도구는 상태를 자기 저장소로 fork하지 않는다. 에이전트가 읽고 쓰는 **같은 파일**을 단일 진실 공급원으로 쓰고, 저장은 에이전트가 통과하는 것과 **같은 검증 게이트**를 타며, 편집 폼은 스키마로 구속한다.
