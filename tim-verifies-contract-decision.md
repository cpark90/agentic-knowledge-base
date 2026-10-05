issue (non-blocking): 빈 칸 `verifies`:contract→decision 은 실제 누락이다 — 사다리 결정은 logical 높이의 `verifies` 를 필수로 두는데 그 주어가 될 합격 기준을 게이트가 거부한다

대상: https://agentic-knowledge-base.dev/id/chunk/1a5c517a-088b-47c7-b29a-b4a044c84946

본문: `p8-scenario-ladder-rungs` 는 logical 논리 시나리오(합격 기준 판정식) ↔ 범위·제약을 `verifies` **필수**로 두고 TIM 절의 주석도 "logical 기준 → 결정"을 적는다. 2026-10-04 실측에서 logical 기준 38 의 `verifies` 는 0 이고 `verifies` 38 은 전부 concrete 케이스 → concrete 결정이라(같은 level 강제) logical 결정 514 는 어느 V&V 청크의 `verifies` 대상도 아니다. 기준에 `verifies` 를 달면 기준은 검증 목표(`RequirementChunk`)를 `refines` 하므로 verify 질의 `verifies-without-criteria` 가 거부한다. `p8-pass-criteria` 의 "기준은 `verifies` 링크의 속성으로 바인딩된다"는 기준을 주어가 아니라 바인딩으로 읽게 하므로 두 결정과 게이트가 한 칸에서 어긋난다.

제안: (a) 질의를 "주어가 기준이거나 기준을 refines 한다"로 넓혀 기준이 같은 높이의 결정을 `verifies` 하게 하거나 (b) 사다리 결정의 logical 행을 "기준이 케이스의 `verifies` 에 바인딩된다"로 고치고 TIM 의 이 칸을 지운다. 어느 쪽이든 결정 변경이라 orchestrator 를 거쳐 유저 승인이 필요하다.

해소: 열림
