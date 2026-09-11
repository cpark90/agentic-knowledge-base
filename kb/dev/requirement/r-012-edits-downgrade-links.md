---
id: https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd
type: requirement
level: functional
title_ko: 변경은 링크를 재판정 대상으로 만든다
title: Edits downgrade affected links to suspect
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
---
**요구** — 산출물이 변경되면, 체계는 그 항목을 끝으로 하는 링크를 suspect로 내려 재검증 시점에서 일괄 재판정하여야 한다.

- **이해관계자**: 프로젝트 · **관심사**: 경계와 갱신
- **출처**: 노트 10.6절

오도하는 링크는 없는 링크보다 해롭다 — 붕괴를 상태로 관리한다.
