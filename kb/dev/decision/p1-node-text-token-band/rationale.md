---
id: https://agentic-knowledge-base.dev/id/chunk/73b8a4b9-da3e-4b0b-9491-faacaccea2b2
type: decision
level: concrete
title_ko: 검색 정밀도의 최적대에서 온 값이고 초과는 단일 책임 위반의 신호다
title: The band comes from the retrieval-precision optimum, and exceeding it signals a single-responsibility violation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0016-node-text-budget.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:15:56+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/403c7a1c-fe4f-48d4-932d-b9cc39517dcc
---
**근거** — 출처는 harness-functional `ONTOLOGYSTYLE`의 §1c다.

- 이 값은 검색 정밀도의 최적대가 100에서 200 단어(약 130에서 260 BPE token)라는 실증에서 왔다.
- 초과는 그 노드가 두 가지 이상을 말하고 있다는 단일 책임 위반의 신호다. 그래서 노드를 분해하거나, 같은 대상의 대안 서술이면 별도 노드로 분리한다.
- 텍스트를 지닌 노드에는 토큰 추정치를 반드시 붙인다. 추정치가 빠지면 뷰 예산이 부정확해져 context rot 방어가 샌다. 또한 뷰 비용인 추정치와 런타임 관측량은 별개의 축이므로 섞지 않는다. 섞으면 팩이 조용히 잘리며, 이것은 실제로 발생한 결함이다.

이 규칙은 단위 지식의 토큰 상한(`p1-chunk-unit-is-tokens`)과 뿌리가 같은 예산 규칙이고, 그 상한의 옛 단위는 42줄이었다. 단위 지식의 상한은 조망 단위이고 130에서 260 token은 검색 정밀도 단위이며, 둘 다 한 단위에 한 주제를 크기로 강제한다.
