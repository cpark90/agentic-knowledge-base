---
id: https://agentic-knowledge-base.dev/id/chunk/149d6c23-b665-4569-9b2d-98241152cb97
type: decision
level: concrete
title_ko: 컨텍스트 팩이 조립의 입력 전부이고 템플릿 출처가 복원을 보장한다
title: The context pack is the whole input to composition, and template provenance keeps it recoverable
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0015-composition-workflow.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:13:15+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:13:15+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/16438f48-86f5-4fd8-a6b6-f971064cf38e
---
**근거** — 출처는 harness-concrete `CLAUDE.md`의 조립 워크플로와 harness-functional의 옛 `docs/DESIGN.md`다.

- 컨텍스트 팩은 조립에 필요한 입력 전부가 되도록 설계되어 있다. 팩의 capability 결핍 목록이 메워야 할 것을 명시한다.
- 템플릿 출처를 남기는 것은 손실 내성의 온톨로지판이다. 그래서 어디서 왔는지 복원할 수 있다.
