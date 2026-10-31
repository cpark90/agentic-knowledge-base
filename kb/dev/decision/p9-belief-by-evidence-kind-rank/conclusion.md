---
id: https://agentic-knowledge-base.dev/id/chunk/8b6a4563-17d3-4c5c-a9a1-ea46f0babdbc
type: decision
level: logical
title_ko: 믿음 정도는 증거 종류의 서열에 정한 가중을 극성대로 더해 [0,1]로 접는 점수다
title: Degree of belief is a score folding rank weights of evidence kinds by polarity into [0,1]
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:51:33+09:00}
layer: methodology
composite: {id: https://agentic-knowledge-base.dev/id/composite/16f7371f-4f26-4563-989c-40a59c4822ea, title_ko: 증거 종류 서열 가중 믿음 정도, title: Belief weighted by evidence-kind rank}
part_of: https://agentic-knowledge-base.dev/id/composite/16f7371f-4f26-4563-989c-40a59c4822ea
---
**결론** — 증거 항목마다 종류의 서열(`p10-link-judgement-evidence`)에 정한 가중을 주고, 극성대로 더하거나 빼서 [0,1]로 접은 점수를 믿음 정도로 둔다. 보정 없이 순위를 주는 규칙이다.
