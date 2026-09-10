---
id: https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a
type: requirement
level: functional
title_ko: 편집은 게이트가 판정한다
title: The gate judges every proposed edit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 에이전트가 편집을 제안하면, 하네스는 검사 게이트로 판정하여 실행 가능한 전이로 바꾸거나 근거를 들어 거부하여야 한다.

- **이해관계자**: 에이전트 · **관심사**: 구조적 통제
- **출처**: 노트 1.6절(행동 사영)·6.7절·1.1절

사람의 한 줄 검토는 성립하지 않으므로 판정은 에이전트 밖의 규칙과 shape가 한다.
