---
id: https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93
type: requirement
level: functional
pattern: event-driven
title_ko: 에이전트는 하네스의 도구로 읽기·쓰기 집합을 기록한다
title: The agent records read and write sets through the harness tools
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-03T18:33:13+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-03T19:53:33+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-req-agent
---
**요구** — 에이전트의 편집이 일어나면, 에이전트는 하네스의 도구로 읽기 집합과 쓰기 집합을 기록하여 링크를 편집의 부산물로 구축하여야 한다. 기록은 하네스 도구의 부산물이고 에이전트의 자기 보고가 아니다.

- **이해관계자**: 에이전트 · **관심사**: 링크 구축
- **출처**: 노트 10.3절·1.6절, 유저 답 Q17-b(2026-10-03)

링크를 만들 수 있던 순간에 만들지 않으면 남는 것은 사후 복원뿐이고, 복원은 본질적으로 부정확하다.
