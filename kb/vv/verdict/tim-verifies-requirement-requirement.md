---
id: https://agentic-knowledge-base.dev/id/chunk/8bf294e9-610f-41a0-9939-121b8059c1c9
type: annotation
level: executable
title_ko: 추적 매트릭스의 칸 verifies requirement→requirement 는 functional 사다리가 derivesFrom 으로 묶여 구조상 해당 없었고 허용 칸에서 빠졌다
title: The TIM cell verifies requirement to requirement did not apply by structure, since the functional rung is bound by derivesFrom, and it has left the allowed cells
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T19:40:32+09:00}
---
thought (non-blocking): 칸 `verifies`:requirement→requirement 는 구조상 해당 없었고 허용 칸에서 빠졌다 — functional 높이의 대응은 `derivesFrom` 칸이 맡는다

대상: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946

본문: `p8-scenario-ladder-rungs` 는 functional 검증 목표 ↔ 요구를 `derives-from` **필수**로 묶고 `verifies` 를 logical·concrete·executable 높이에만 둔다. 그 칸 `derivesFrom`:requirement→requirement 는 이미 찼고 2026-10-04 에 검증 목표 `harness-follows-knowledge` 가 더해져 요구 36 전부가 대응물을 갖는다. 검증 목표가 요구를 `verifies` 하면 주어가 합격 기준(`ContractChunk`)을 `refines` 하지 않으므로 verify 질의 `verifies-without-criteria` 가 거부한다. 같은 쌍을 두 링크로 잇는 것은 중복이고 게이트가 그 중복을 막는다.

제안: TIM 표의 이 칸은 사다리 결정과 게이트 어느 쪽과도 맞지 않는 과잉 칸이었다. 유저 결정(Q52-a)이 허용 칸에서 이 칸을 뺐다.

해소: 해소 — 유저 결정 Q52-a 로 `verifies`:requirement→requirement 가 허용 칸에서 빠졌고 그 관계는 `derivesFrom` 칸 `derivesFrom`:requirement→requirement 가 맡는다(Q30-b: functional 검증 목표 ↔ 요구는 derives-from). 허용 칸 채움은 `bazel build //kg:metrics` 의 TIM 줄에서 13/15 이다.
