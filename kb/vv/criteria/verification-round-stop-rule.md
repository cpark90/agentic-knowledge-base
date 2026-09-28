---
id: https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333
type: contract
level: abstract
title_ko: 연속한 두 라운드의 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않는다
title: If the new-defect count does not fall across two consecutive rounds, no further round is opened
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78]
---
**합격 기준** — 기준 종류는 정지 규칙이다. 라운드 `n`의 신규 결함 수를 `new(n)`이라 할 때 `new(n) >= new(n-1)` 이면 라운드 `n+1`을 열지 않고 채널로 되돌리는 것이 합격이다.

**확인 절차**

- 실행 기록(`kb/vv/run/`)에서 연속한 두 라운드를 고르고 각 라운드의 `fail` 케이스와 새로 열린 판정 주석을 합해 `new(n)`을 센다.
- `new(n) >= new(n-1)` 인데 다음 라운드가 열렸으면 불합격이다. 열리지 않았고 그 이유가 판정 주석으로 남았으면 합격이다.
- 라운드 경계는 실행 기록의 `generated.at` 으로 가른다. 같은 리비전의 재실행은 같은 라운드로 센다.

**등급** — C다. 라운드 경계와 신규 결함의 셈이 사람 판단이고 실행 기록이 두 건뿐이라 표본이 없다.

미확정: 신규 결함 수를 기계가 세는 수단이 없다. 수단이 서면 이 기준을 logical로 올리고 판정식을 쓴다.
