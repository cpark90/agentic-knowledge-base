---
id: https://agentic-knowledge-base.dev/id/chunk/d3a36010-25a1-417b-b2e7-875ccc6955ce
type: decision
level: concrete
title_ko: 링크의 증거는 극성 있는 항목의 증거 기록이고 확률로 합산하지 않으며 상태 전이 규칙이 증거 기록을 읽는다
title: Link evidence is a ledger of signed entries, never summed into a probability; transition rules read the ledger
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395]
composite: {id: https://agentic-knowledge-base.dev/id/composite/05abd2cf-de1b-4aa2-9559-10cb0f868dab, title_ko: 증거 기록, title: The evidence ledger}
part_of: https://agentic-knowledge-base.dev/id/composite/05abd2cf-de1b-4aa2-9559-10cb0f868dab
---
**결론** — 후보에는 증거 항목의 목록이 붙는다. 항목 = (종류, 참조, 극성). 종류는 10.8절 근거 유형 + 실행, 극성은 지지(+)/반박(−). **확률로 합산하지 않는다.** 상태 전이 규칙이 증거 기록을 읽는다 (노트 9.11절):

| 규칙 | 조건 | 결과 |
|---|---|---|
| 확정 가능 | 구축(+) 또는 실행(+) 하나 이상 **and** 반박 없음 **and** `when` 참 **and** 다른 후보 전부 eliminated | 확정 제안 |
| 보류 | 임베딩·세션 공동 읽기(+)만 | open — 확정 근거 부족 (10.4절) |
| 반박 | 실행(−) 하나 이상 | 후보면 eliminated(`eliminated_by: run`), 확정이면 invalid |
| 충돌 | 같은 후보에 (+)와 (−) 공존 | open 유지 + 유저 큐. 자동 해소 금지 |

**실행 증거가 특별하다.** verifier의 통과는 `verifies`뿐 아니라 그것이 검증하는 `satisfies` 후보에도 (+)를, 실패는 (−)를 적는다 — V&V 결과가 개발 KB 후보의 증거로 흘러드는 유일한 경로이며, 링크가 아니라 증거 기록 항목이라 방향 규칙(8.5절)을 깨지 않는다. 확정 링크도 증거 기록을 유지한다 — "왜 아직 유효한가"에 마지막 확정 시각이 아니라 **마지막 지지 증거**로 답한다. 이 저장소: `agt:Evidence`(kind·ref·polarity), `agt:confidence` 폐기, 증거 기록 규칙은 verify 질의 (2026-09-10).
