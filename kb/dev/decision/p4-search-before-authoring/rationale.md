---
id: https://agentic-knowledge-base.dev/id/chunk/47d4c9d1-69c8-474e-b3e9-f055f3e988fe
type: decision
level: concrete
title_ko: 섞인 노드는 재사용과 검색과 예산을 함께 해치고 같은 뜻의 노드 둘이 곧 drift다
title: Mixed nodes hurt reuse, retrieval and budgeting at once, and two nodes with one meaning are drift
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0160-search-before-authoring.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:40:17+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:40:17+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/54ecc54e-24cd-420e-b5c9-4405958c87ec
---
**근거** — 출처는 harness-functional `ONTOLOGYSTYLE`의 §1이다.

- 여러 정책이나 페르소나를 한 노드에 섞으면 재사용과 검색, 예산 계산이 한꺼번에 나빠진다. 그 노드의 절반만 필요해도 통째로 실어야 하고, 검색은 두 주제가 섞인 텍스트에 대해 어느 쪽으로도 정확히 맞지 않는다.
- **같은 뜻의 노드를 둘 만드는 것이 곧 drift다**(`p6-three-failure-mode-defences`). 검색이 그 drift의 1차 방어이며, 저작 도구가 검색을 저작 흐름의 **첫 단계**로 두어야 실제로 지켜진다. 규칙만 적어 두면 새로 만드는 쪽이 언제나 더 빠르기 때문이다.
- 서술 길이 상한(`p1-node-text-token-band`)을 넘는 노드는 대개 단일 책임 위반의 증상이다. 상한은 이 규칙의 기계적 대리 지표이고, 초과의 처방은 자르기가 아니라 분해다.
- **영리한 모델링을 경계한다.** 스키마가 금지하지 않았다는 것이 써도 된다는 뜻은 아니다. 그래서 등록된 관용 패턴을 먼저 따르고, 벗어나야 한다면 그 노드나 커밋에 사유를 한 문장 남기며, 말없이 머지하지 않는다.
