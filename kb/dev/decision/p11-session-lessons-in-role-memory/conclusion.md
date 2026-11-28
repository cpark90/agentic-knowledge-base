---
id: https://agentic-knowledge-base.dev/id/chunk/e45a0f86-ddc6-48ae-8b82-d710629e04ed
type: decision
level: concrete
title_ko: 세션 교훈은 그래프 밖의 역할 메모리에 둔다
title: Session lessons stay in role memory outside the graph
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T15:54:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/812a5dca-20bc-4adc-a1a5-5d14700e9420]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/44c28dd9-af7d-4c91-a832-00a5eb7af95d
composite: {id: https://agentic-knowledge-base.dev/id/composite/44c28dd9-af7d-4c91-a832-00a5eb7af95d, title_ko: 역할 메모리의 세션 교훈, title: Session lessons in role memory}
---
**결론** — 세션 교훈을 지금처럼 역할 메모리(`.claude/agent-memory/<역할>/`, 그래프 밖)에 둔다. 파일은 옮기지 않고, orchestrator의 교훈은 저장소 밖 Claude 메모리에 둔다. 그래프 안으로 들어오는 것은 승격된 표준 규칙이다.
