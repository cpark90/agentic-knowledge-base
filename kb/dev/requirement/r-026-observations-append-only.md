---
id: https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d
type: requirement
level: functional
title_ko: 관측은 append-only 실행 기록이다
title: Observations are append-only run records
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 검증이 실행되면, 체계는 관측을 실행 기록(Run)으로 concrete 수준에 append-only 저장하여야 한다.

- **이해관계자**: 검증자 · **관심사**: 관측
- **출처**: 노트 0.5절 / 구조도 관측

관측은 이미 일어난 것이라 고칠 수 없다 — 시간은 실행 기록과 wasRevisionOf가 운반한다.
