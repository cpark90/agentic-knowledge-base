---
id: https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3
type: requirement
level: functional
title_ko: 명명과 표기는 결정론적이다
title: Naming and notation are deterministic
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
---
**요구** — 체계는 같은 내용이 같은 바이트로 직렬화되고 이름·라벨이 규칙으로 정해지도록 하여야 한다.

- **이해관계자**: 업체 · 리뷰어 · **관심사**: diff의 의미
- **출처**: 노트 4.2절 · 4.3절 · 4.9절 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

정규화가 없으면 diff가 의미 없는 변경으로 오염되어 리뷰와 해시 기반 재판정이 모두 흔들린다.
