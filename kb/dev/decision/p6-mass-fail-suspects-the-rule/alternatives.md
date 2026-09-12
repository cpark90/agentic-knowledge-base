---
id: https://agentic-knowledge-base.dev/id/chunk/1177bea5-def8-4714-96e4-242e2fca39d9
type: decision
level: logical
title_ko: 대량 FAIL을 산출물 정정으로 처리하는 안과 경고를 침묵시키는 안은 기각된다
title: Treating a mass FAIL as artefact repair, and silencing warnings, are both rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T16:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b0647639-f82c-4e20-a9ce-73b4e7fdb748
---
**대안** —

- **대량 FAIL이면 산출물을 전부 고친다** — 기각. 규칙이 틀렸을 때 관례 전체가 규칙을 따라 왜곡되고, 라벨처럼
  인터페이스인 것을 대량으로 바꾸면 검증 표시가 전부 물러난다.
- **비-초록 경고를 도구에서 끈다** — 기각. 침묵은 선언이 아니다 — 경고가 왜 정상인지 기록이 없으면 다음 세션이
  같은 판단을 되풀이하고, 진짜 결함이 섞여 들어와도 묻힌다.
- **게이트 추가 절차를 규약으로만 둔다** — 보류. 절차 자체는 규약이 맞지만 총람 행·id·실패 종류는 도구 형식이라
  기계로 강제된다 — 이 결정은 그 경계를 긋는다.
