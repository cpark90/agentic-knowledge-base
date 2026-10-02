---
id: https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333
type: contract
level: abstract
title_ko: 연속한 두 라운드의 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않는다
title: If the new-defect count does not fall across two consecutive rounds, no further round is opened
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-10-01T01:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78]
---
**합격 기준** — 기준 종류는 정지 규칙이다. 라운드 `n`의 신규 결함 수를 `new(n)`이라 할 때 `new(n) >= new(n-1)` 이면 라운드 `n+1`을 열지 않고 채널로 되돌리는 것이 합격이다.

**판정식**

- 실행. `bazel build //kg:audit` 뒤 `bazel-bin/kg/audit.md`의 판정 주석 절이 살아 있는 주석 수·해소 상태 표(열림·해소·기각)·차단 주석 수를 낸다. 실측 2026-10-01에 주석 32 · 열림 23/32 = 71.9% · 해소 8 · 기각 1 · 차단 0이다.
- `new(n)`의 정의. 라운드 경계는 주석의 `prov:generatedAtTime` 날짜이고 `new(n)`은 그 날짜에 저작된 주석 수에서 `generated.by`가 `process:judge`인 판정 결과 주석을 뺀 수다. 판정 결과는 리뷰가 찾은 결함이 아니라 판정자의 응답 기록이라 정지 규칙의 입력이 아니다.
- 음성. 계열은 2(09-22) · 4(09-23) · 2(09-26) · 2(09-29) · 2(09-30)이다. `new(09-29) = new(09-26) = 2`인데 다음 라운드가 열렸고 채널로 되돌린 기록이 없으므로 지금은 **불합격**이다. 판정 결과 20건을 함께 세면 `new(09-29) = 22`이고 판정은 같다.
- 양성. 열림 23 중 게이트를 막는 `issue (blocking)`은 0건이고 그 0은 `chunk_lint`의 `blocking-comment`가 지킨다. 정지 규칙 자체를 막는 게이트는 없으므로 이 기준의 값은 판정 뒤 채널로 간다.

**등급** — B다. 주석 수와 해소 상태가 생성물의 수치이고 명령이 지금 돌아 값이 나온다. A가 아닌 까닭은 라운드별 신규 수를 내는 절이 `audit`에 아직 없어 계열을 손으로 집계한다는 것이다.

미확정: 라운드 경계를 실행 기록으로 가르는 규칙. 실행 기록이 라운드마다 남으면 날짜 대리를 버린다.
