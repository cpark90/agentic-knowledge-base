---
id: https://agentic-knowledge-base.dev/id/chunk/65b29e82-58ca-4539-afa0-6d3aedc87aff
type: decision
level: concrete
title_ko: 노드 서술 텍스트는 130에서 260 token 대역에 두고 상한만 기계적으로 강제한다
title: Node description text sits in a 130 to 260 token band and only the upper bound is enforced mechanically
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0016-node-text-budget.md, id: https://agentic-knowledge-base.dev/id/chunk-d0016, title_ko: "노드 서술 텍스트는 130–260 token 대역에 두고 상한만 기계적으로 강제한다", title: "Node description text stays in a 130-260 token band, with only the upper bound enforced"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0016]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/403c7a1c-fe4f-48d4-932d-b9cc39517dcc
composite: {id: https://agentic-knowledge-base.dev/id/composite/403c7a1c-fe4f-48d4-932d-b9cc39517dcc, title_ko: 노드 서술 텍스트의 토큰 대역, title: Token band for node description text}
---
**결론** — 검색 단위로 뷰에 실리는 노드의 서술 텍스트 합은 260 token을 넘지 않는다. 측정치는 문자 수를 4로 나눈 값이고, 외부 토크나이저에 의존하지 않아 결정론적이다. 목표 대역은 130에서 260 token이며, 하한은 권고이고 상한만 기계적으로 강제한다.
