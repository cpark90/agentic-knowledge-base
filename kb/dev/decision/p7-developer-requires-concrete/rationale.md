---
id: https://agentic-knowledge-base.dev/id/chunk/78022ec3-95df-4223-ae18-2fb3b63788a6
type: decision
level: logical
title_ko: 후보가 남은 상태에서의 구현은 근거 없는 배정이다
title: Implementing while candidates remain is an ungrounded assignment
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/fb8de557-6f61-436f-ae39-57f6c7019555
---
**근거** (노트 7.3절, 7.7절, 9.10절) — 결정이 logical에 머물러 있다는 것은 후보가 여럿 남았다는 뜻이고, 그 상태에서 구현하면 developer가 암묵적으로 하나를 고른 것이 된다 — 근거 없는 배정(요구 24)이다. 스코프 conditional은 이를 규약이 아니라 쓰기 권한으로 막는다. 이 conditional은 링크 `when`의 특수형이다 (9.11절).
