---
id: https://agentic-knowledge-base.dev/id/chunk/68c71368-de19-47b0-9237-4a6acf194aff
type: decision
level: logical
title_ko: 저장된 상태는 낡지만 평가된 상태는 낡지 않는다
title: A stored state goes stale; an evaluated state cannot
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0b7abe3a-c03e-434f-b53b-b9d9d936a388
---
**근거** (노트 9.11절, 6.5절, 6.10절) — 상태를 저장하면 조건이 바뀌어도 상태가 그대로 남아 링크 붕괴(오래된 링크가 구조를 오도)가 일어난다. 상태가 조건의 평가 결과이면 ODD 속성·가정이 바뀌는 순간 재판정 경계에서 자동으로 suspect·eliminated가 된다 — 전수조사 없는 무효화(요구 3)의 링크판이다. `assumes`·스코프 conditional·`when`을 한 메커니즘으로 보면 세 규칙이 아니라 한 평가기만 있으면 된다. ODD 밖 참조를 거부하는 것은 조건부 링크가 ODD 안에서만 조건부이기 때문이다.
