---
id: https://agentic-knowledge-base.dev/id/chunk/6493de12-ad0f-474a-828b-bdf1965a8968
type: decision
level: logical
title_ko: 네 질의가 링크 모델의 역량 질문이다
title: The four queries are the link model's competency questions
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/03b399d7-2688-4588-bfed-7942e0e30aab
---
**근거** (노트 9.7·9.13절) — 이 넷은 링크 모델의 역량 질문(2.7절)이다. 링크 타입과 카디널리티는 이 질의들이 답을 낼 수 있도록 고른 것이고, 답이 안 나오는 질의가 생기면 TIM에 빈 곳이 있다는 신호다.

넷 모두 한 방향으로 저장된 링크 위에서 성립한다 — 역방향("무엇이 이 결정을 충족하는가")은 질의가 만들어 내므로 두 벌을 저장할 필요가 없다 (9.2절). 커버리지 질의는 존재하지 않는 링크를 세는 것이므로 `FILTER NOT EXISTS` 형태가 기본이다.
