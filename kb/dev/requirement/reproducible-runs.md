---
id: https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e
type: requirement
level: functional
title_ko: 실행은 같은 리비전과 seed에서 재현된다
title: Runs reproduce under the same revision and seed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
---
**요구** — 체계는 같은 리비전·seed·환경에서 검증 실행과 케이스 생성이 같은 결과를 내도록 하여야 한다.

- **이해관계자**: 업체 · V&V · **관심사**: 재현성
- **출처**: 노트 8.12절 · 8.23절 · 8.26절 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

재현되지 않는 검증은 환경 계층에서 강등되고, 재현 실패율이 환경 신뢰도의 지표다. 공백 세션에서 같은 산출물이 나와야 지식이 산출물을 결정한다.
