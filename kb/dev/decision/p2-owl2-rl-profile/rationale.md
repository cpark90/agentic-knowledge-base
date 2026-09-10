---
id: https://agentic-knowledge-base.dev/id/chunk/428cb843-a4fb-4e74-a63b-5768f433d744
type: decision
level: logical
title_ko: 게이트는 실시간이므로 추론 비용에 상한이 있어야 한다
title: A real-time gate needs a bounded reasoning cost
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4863dfa7-90c7-471e-b5ac-84e0ca2011c8
---
**근거** (노트 2.9절) — 검사 게이트는 편집마다 도는 실시간 경로다. 추론 비용의 상한이 정해져 있지 않으면 게이트의 응답 시간이 그래프 크기에 따라 예측 불가능해지고, 결국 게이트를 끄게 된다.

RL이 이 체계가 실제로 쓰는 추론 — 이행적 `part_of`, `subPropertyOf` 전파(2.8절), 규칙 기반 결함 추론 — 을 전부 덮는다. 같은 엔진으로 `defect-rules`를 돌리므로 추론 스택이 하나다.
