---
id: https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef
type: requirement
level: functional
title_ko: 입력은 명시되고 버전 관리된다
title: Inputs are explicit and versioned
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
---
**요구** — 체계는 카탈로그·실행 모드·승격 규칙 등 밖에서 오는 입력을 온톨로지 어휘로 명시하고 버전으로 관리하여야 한다.

- **이해관계자**: 업체 · 운영 · **관심사**: 재구성 가능성
- **출처**: 노트 11.1절 · 11.7절 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

입력이 암묵적이면 체계가 왜 그렇게 구성됐는지 재구성할 수 없고, 앞 입력이 바뀔 때 뒤 입력의 재검토 범위를 계산할 수 없다.
