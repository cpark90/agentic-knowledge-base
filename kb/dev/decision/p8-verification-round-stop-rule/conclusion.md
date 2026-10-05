---
id: https://agentic-knowledge-base.dev/id/chunk/a7816e3d-024c-488d-9054-075440f4cb8b
type: decision
level: concrete
title_ko: 검증 라운드는 종료 사유를 단 명시 기록이고 정지 규칙은 그 기록 사이의 신규 결함 수로 판정한다
title: A verification round is an explicit record with an end reason, and the stop rule is judged on the new defects between records
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1da87f55-7c99-4879-831b-613ea302dc21
composite: {id: https://agentic-knowledge-base.dev/id/composite/1da87f55-7c99-4879-831b-613ea302dc21, title_ko: 검증 라운드의 기록과 정지 규칙, title: Verification round records and the stop rule}
---
**결론** — 라운드 경계는 날짜가 아니라 명시 기록이다(유저 답 Q39-c, 2026-10-04).

| 항목 | 정의 |
|---|---|
| 라운드 기록 | `vv_run --round stop-rule\|budget\|complete`가 남기는 `kb/vv/run/round-<UTC>.md`다. 실행 기록과 같은 자리의 append-only 관측이고 라운드 번호·구간 안 신규 결함 수·종료 사유를 담는다 |
| 종료 사유 | 개념 `agt:RoundEndReason`의 개체 셋 — `agt:roundEndedByStopRule`·`agt:roundEndedByBudget`·`agt:roundEndedByCompletion`. 기록 본문이 하나를 인용한다 |
| 신규 결함 수 new(n) | 직전 기록 시각 뒤부터 기록 n 시각까지 저작된 살아 있는 판정 주석의 수다. `process:judge`의 판정 결과 주석은 뺀다 |
| 정지 규칙 | 연속한 두 라운드에서 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않고 채널로 되돌린다. new(n) ≥ new(n−1)인데 기록 n+1이 정지 규칙이 아닌 사유로 닫히면 위반이다 |

위반은 verify 질의 `round-stop-rule-violated`(`//kg:gate_test`)가 판정한다. 감사 `//kg:audit`는 라운드 기록으로 구간을 자르고, 기록이 없으면 판정 주석의 `prov:generatedAtTime` 날짜로 자른다(호환).
