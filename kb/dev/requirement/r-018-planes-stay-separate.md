---
id: https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4
type: requirement
level: functional
title_ko: 판정 방식이 다른 지식은 섞지 않는다
title: Knowledge with different verification never mixes
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes, https://agentic-knowledge-base.dev/id/doc-structure]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 체계는 판정 방식이 다른 지식(plane)을 한 컨텍스트에 섞지 않아야 하며, 읽기 툴 표면이 plane 할당을 따라야 한다.

- **이해관계자**: 에이전트 · **관심사**: 구조적 통제
- **출처**: 노트 5.1절·5.3절

저장소만 나누고 읽기가 전체를 반환하면 분리는 달성되지 않는다.
