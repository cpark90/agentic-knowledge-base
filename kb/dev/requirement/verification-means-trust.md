---
id: https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207
type: requirement
level: functional
title_ko: 검증 수단 자체의 신뢰도를 잰다
title: The trustworthiness of verification means is measured
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
---
**요구** — 체계는 합격 기준이 실제로 거르는지(변이 검출률)와 판정자가 믿을 만한지(정확도·판별력·캘리브레이션)를 측정하여야 한다.

- **이해관계자**: 업체 · V&V · **관심사**: 기준과 판정자의 질
- **출처**: 노트 8.6절 · 8.14절 · 8.26절 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

아무것도 거르지 않는 기준도 통과하고 드리프트한 판정자도 판정한다. 검증 수단이 검증되지 않으면 통과는 공허하다.
