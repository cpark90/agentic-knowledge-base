---
id: https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93
type: requirement
level: functional
title_ko: 하네스는 읽기·쓰기 집합을 기록한다
title: The harness records read and write sets
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
---
**요구** — 에이전트의 편집이 일어나면, 하네스는 읽기 집합과 쓰기 집합을 기록하여 링크를 편집의 부산물로 구축하여야 한다.

- **이해관계자**: 에이전트 · **관심사**: 링크 구축
- **출처**: 노트 10.3절·1.6절

링크를 만들 수 있던 순간에 만들지 않으면 남는 것은 사후 복원뿐이고, 복원은 본질적으로 부정확하다.
