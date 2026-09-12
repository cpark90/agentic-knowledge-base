---
id: https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af
type: requirement
level: functional
title_ko: dispatch는 작업 집합만 전달한다
title: Dispatch passes only the workset
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 에이전트가 dispatch되면, 하네스는 지식 베이스 전체가 아니라 역할 스코프 × level 창으로 거른 작업 집합만 전달하여야 한다.

- **이해관계자**: 에이전트 · **관심사**: 좁은 관측
- **출처**: 노트 0.5절·10.3절·1.6절(관측 사영)

무엇을 보게 할지가 곧 무엇을 판단하게 할지다 — 관측 함수를 우연에 맡기지 않는다.
