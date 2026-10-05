---
id: https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333
type: contract
level: logical
title_ko: 연속한 두 라운드의 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않는다
title: If the new-defect count does not fall across two consecutive rounds, no further round is opened
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:18:12+09:00}
verified: [{by: vnv/claude-opus-5-5, at: 2026-10-04T23:20:47+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78]
---
**합격 기준** — 기준 종류는 정지 규칙이다. 라운드 `n`의 신규 결함 수를 `new(n)`이라 할 때 `new(n) >= new(n-1)` 이면 라운드 `n+1`을 열지 않고 채널로 되돌리는 것이 합격이다.

**판정식**

- 라운드 경계. 경계는 명시 라운드 기록이다(유저 답 Q39-c). `vv_run --round stop-rule|budget|complete`가 `kb/vv/run/round-<UTC>.md`를 남기고 기록 본문이 종료 사유 개념 `agt:RoundEndReason`의 개체 하나를 인용한다.
- `new(n)`의 정의. 직전 라운드 기록 시각 뒤부터 라운드 `n` 기록 시각까지 저작된 살아 있는 판정 주석 수에서 판정 결과 주석(`process:judge`)을 뺀 수다. 첫 라운드는 처음부터 센다.
- 실행. verify 질의 `round-stop-rule-violated`가 `//kg:gate_test`에서 돈다. `new(n) >= new(n-1)`인데 라운드 `n+1` 기록의 종료 사유가 `agt:roundEndedByStopRule`이 아니면 행 하나를 낸다. `bazel-bin/kg/audit.md`의 라운드 절이 같은 정의로 계열을 보인다.
- 음성. 신규 결함 1·1 뒤 라운드 3을 `agt:roundEndedByCompletion`으로 닫은 임시 그래프에서 `validate`가 종료 1과 `FAIL [verify] tools/verify-queries/round-stop-rule-violated.rq`를 내지 않으면 불합격이다. 케이스는 `round-record-stop-rule-equivalence-2`다.
- 통제. 같은 그래프에서 라운드 3을 `agt:roundEndedByStopRule`로 닫으면 종료 0과 `PASS [validate]`다. 케이스는 `round-record-stop-rule-equivalence-1`이고 둘 다 논리 시나리오 `round-record-stop-rule`에서 생성된다.
- 실측 2026-10-04에 두 케이스가 `vv_run`에서 pass이고 고정물 시험 `//defs/tests:round_fixture_{violated,kept,weave}_test`가 PASS다. 저장소의 라운드 기록은 0건이라 질의 대상이 0이고 audit 라운드 절은 날짜 대리로 떨어져 계열 2 · 2 · 2 · 2 · 2 · 1 · 2 · 9를 보인다.

**등급** — A다. 정지 규칙의 판정은 게이트의 verify 질의이고 위반·준수 케이스가 생성기로 서며 사람 판단이 없다. 라운드 기록이 0건인 동안 저장소 자신의 판정은 대상이 없다.
