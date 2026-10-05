---
id: https://agentic-knowledge-base.dev/id/chunk/552a1329-8c1a-40ec-b1a6-b23d0ba545ff
type: annotation
level: executable
title_ko: 추적 매트릭스의 빈 칸 verifies contract→decision 은 logical 결정의 검증 대응물이 없는 실제 누락이고 지금 게이트가 그 칸을 막는다
title: The empty TIM cell verifies contract to decision is a real gap leaving logical decisions without a verification counterpart, and the current gate blocks the cell
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T13:21:50+09:00}
---
issue (non-blocking): 빈 칸 `verifies`:contract→decision 은 실제 누락이다 — 사다리 결정은 logical 높이의 `verifies` 를 필수로 두는데 그 주어가 될 합격 기준을 게이트가 거부한다

대상: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946

본문: `p8-scenario-ladder-rungs` 는 logical 논리 시나리오(합격 기준 판정식) ↔ 범위·제약을 `verifies` **필수**로 두고 TIM 절의 주석도 "logical 기준 → 결정"을 적는다. 2026-10-04 실측에서 `verifies` 는 concrete 케이스 → concrete 결정과 executable 검증기 → 산출물뿐이고(같은 level 강제) logical 기준 38 의 `verifies` 는 0 이라 logical 결정 청크 514 는 어느 V&V 청크의 `verifies` 대상도 아니다. 기준에 `verifies` 를 달면 기준은 검증 목표(`RequirementChunk`)를 `refines` 하므로 verify 질의 `verifies-without-criteria` 가 거부한다. `p8-pass-criteria` 의 "기준은 `verifies` 링크의 속성으로 바인딩된다"는 기준을 주어가 아니라 바인딩으로 읽게 하므로 두 결정과 게이트가 한 칸에서 어긋난다.

제안: (a) 질의를 "주어가 기준이거나 기준을 refines 한다"로 넓혀 기준이 같은 높이의 결정을 `verifies` 하게 하거나 (b) 사다리 결정의 logical 행을 "기준이 케이스의 `verifies` 에 바인딩된다"로 고치고 TIM 의 이 칸을 지운다. 어느 쪽이든 결정 변경이라 orchestrator 를 거쳐 유저 승인이 필요하다.

해소: 열림
