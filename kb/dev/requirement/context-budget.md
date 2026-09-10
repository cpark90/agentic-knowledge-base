---
id: https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a
type: requirement
level: functional
title_ko: 작업 집합은 컨텍스트 예산 안에 든다
title: Worksets fit within the context budget
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
---
**요구** — 체계는 역할별 작업 집합이 컨텍스트 예산(약 200줄, 42줄 청크 4~5개) 안에 들도록 유지하여야 한다.

- **이해관계자**: 업체 · 에이전트 운영 · **관심사**: 컨텍스트 예산
- **출처**: 노트 1.4절 · 14.1절 2단계 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

예산을 넘는 작업 집합은 라벨 목록 우선 읽기와 스코프의 효과를 없애며, 1단계 통과 조건(같은 작업의 토큰 감소)이 이것을 잰다.
