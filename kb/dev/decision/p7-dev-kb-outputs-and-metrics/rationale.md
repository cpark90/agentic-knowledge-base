---
id: https://agentic-knowledge-base.dev/id/chunk/e56f2c76-bbbe-46a6-abd8-95d068289a4a
type: decision
level: logical
title_ko: 산출은 전부 뷰이고 지표는 전부 질의다
title: Every output is a projection and every metric a query
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f44b4776-de6f-44bf-893b-72ce88179fdb
---
**근거** (노트 7.8절, 4.6절, 12.3절) — 코드·문서·ADR·보고가 저장물이 아니라 뷰이어야 청크가 유일한 원본으로 남는다(4.6절). 지표 여섯은 전부 그래프 질의로 나오며, 12.3절의 선택 규칙("낮으면 무엇을 고치는가")을 만족한다 — 완주율·귀속률은 정제 하네스, 완결률은 설계 진행, 체류 시간은 유저 피드백, 선행률·기록률은 게이트.
