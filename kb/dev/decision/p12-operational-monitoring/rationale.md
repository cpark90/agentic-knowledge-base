---
id: https://agentic-knowledge-base.dev/id/chunk/7f4f027a-2720-45cf-9ad8-dfdb16d8558d
type: decision
level: logical
title_ko: ODD 안팎의 갈림이 대응 주체를 가르고 커버 밖은 자동 대응하지 않는다
title: Inside or outside the ODD decides who responds; uncovered anomalies are never auto-handled
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f2acea7a-db49-4239-aa5f-eef954055e55
---
**근거** (노트 12.5절)

- **ODD 안이면 결함, 밖이면 이탈**이라는 갈림이 대응 주체를 가른다. 결함은
  체계 안에서 요인 분류와 Runbook으로 처리되고, 이탈은 유저의 판단이 필요한
  경계 변경이다.
- 사전 케이스의 커버리지 한계는 7.7절에서 이미 인정한 것이다. 커버되지 않은
  이상에 자동 대응을 시도하면 근거 없는 배정이 된다 — 그 이상은 어휘의 공백
  이거나 케이스의 공백이라 고를 후보 자체가 없다.
- 새 orchestrator의 스코프를 "이상 지점의 plane과 그 상위"로 고정하는 이유 —
  단방향 영향 규칙(5.2절)상 원인이 아래에 있을 수 없다.
