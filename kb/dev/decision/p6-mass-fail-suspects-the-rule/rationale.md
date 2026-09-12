---
id: https://agentic-knowledge-base.dev/id/chunk/d6713f91-2b82-4d99-a053-c1be4fa6200a
type: decision
level: logical
title_ko: 규칙이 실태와 어긋난 채 게이트가 되면 산출물이 규칙을 따라 왜곡된다
title: When a rule becomes a gate while disagreeing with reality, the artefacts bend to the rule
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T16:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b0647639-f82c-4e20-a9ce-73b4e7fdb748
---
**근거** (노트 6.7절 게이트 총람; 이 저장소 실측 2026-09-12; agrtls `docs_review`·`device_installation`) — 게이트는 강제력이
있어 규칙의 오류를 산출물 전체에 복제한다. 결론 라벨 형식 검사가 결정 청크 전부를 보게 만들어졌을 때 197건이 걸렸고,
그중 168건은 대안 라벨의 명사구 관례였다 — 규칙 원문은 "결론 문장형"이었다. 산출물을 고쳤다면 관례를 깨고 라벨 168건을
다시 썼을 것이다. 그래서 첫 실행의 대량 FAIL은 산출물의 문제가 아니라 규칙의 범위·정의를 되묻는 신호로 다룬다.

배선 안 된 검사를 정상으로 선언하는 것은 같은 이유다 — "trace-check exit 2가 정상이다"라는 한 줄이 없으면 다음 세션이
그것을 결함으로 읽고 고치러 온다. 알려진 비-초록은 기준선이지 부채가 아니며, 부채가 되는 순간을 선언이 가른다.
게이트·보고 구분은 뷰 원칙(4.6절)과 판정 주체(9.8절 — 판정은 사람 또는 승인된 판정자)에서 따라온다.
