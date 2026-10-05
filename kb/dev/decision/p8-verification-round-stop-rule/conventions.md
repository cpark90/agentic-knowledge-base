---
id: https://agentic-knowledge-base.dev/id/chunk/a3dad389-efdd-480a-8b27-f327483e1bbd
type: decision
level: concrete
title_ko: 규범 문서 규약 — 검증 라운드는 종료 사유를 단 명시 기록이고 정지 규칙은 그 기록 사이의 신규 결함 수로 판정한다
title: Normative-document conventions — A verification round is an explicit record with an end reason, and the stop rule is judged on the new defects between records
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1da87f55-7c99-4879-831b-613ea302dc21
---
**규약** — `p8-verification-round-stop-rule`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 라운드는 `vv_run --round stop-rule|budget|complete`가 남기는 기록 `kb/vv/run/round-<UTC>.md`다(번호·구간 안 신규 결함 수·종료 사유). 종료 사유는 `agt:RoundEndReason`의 개체 셋 중 하나다. 신규 결함 수 new(n)은 직전 기록 시각 뒤부터 기록 n 시각까지 저작된 살아 있는 판정 주석(`process:judge` 제외)의 수다. new(n) ≥ new(n−1)이면 다음 라운드를 열지 않고 채널로 되돌리며, 기록 n+1이 정지 규칙이 아닌 사유로 닫히면 verify 질의 `round-stop-rule-violated`(`//kg:gate_test`)가 위반으로 낸다. `//kg:audit`는 기록으로 구간을 자르고 기록이 없으면 날짜로 자른다(유저 답 Q39-c, 2026-10-04).
