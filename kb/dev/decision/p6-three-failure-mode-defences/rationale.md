---
id: https://agentic-knowledge-base.dev/id/chunk/ff29ad03-15d9-4391-99f6-b9077470925c
type: decision
level: concrete
title_ko: 세 실패 모드는 독립된 축이어서 방어선도 겹치지 않게 둔다
title: The three failure modes are independent axes, so their defences do not overlap
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0014-three-failure-modes.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:10:31+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:10:31+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/ea65a62f-fb81-43aa-878a-09fcb883fdfd
---
**근거** — 출처는 harness-functional의 옛 `docs/DESIGN.md`이고, 그 원본은 이 승격으로 제거됐다.

- 고아는 예외가 아니라 빌드 실패다. 그래서 새 노드는 같은 커밋 안에서 그래프에 연결한다. 노드 지역 규칙인 shape가 놓치는 섬은 도달성 BFS가 잡고, 연결됐지만 빌드할 수 없는 상태는 capability 짝 맞춤이 잡는다.
- drift는 손실만큼 정상적인 위험으로 다룬다. 근사 동의어 클래스와 타입 없는 간선이 바로 이 방어선이 막으려는 것이다. 예를 들어 "RAG"와 "Document retrieval"은 한 노드의 우선 라벨과 대체 라벨이지 두 노드가 아니다.
- 셋은 독립된 축이므로 방어선도 겹치지 않게 둔다. 따라서 하나의 게이트로 셋을 다 막으려 하지 않는다.
