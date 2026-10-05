---
id: https://agentic-knowledge-base.dev/id/chunk/1c2804b6-ea98-4a24-b6ae-18e7ae6fb4a9
type: decision
level: logical
title_ko: 날짜는 세션과 같지 않아 라운드 경계가 성기고 명시 기록만 목표의 관측 셋을 채운다
title: Dates are not sessions, so date boundaries are coarse, and only explicit records meet the goal's observations
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1da87f55-7c99-4879-831b-613ea302dc21
---
**근거** — 정지 규칙 자체는 유저 승인 규범이다(2026-10-01). 그때 라운드의 정의는 판정 주석의 `prov:generatedAtTime` 날짜였다. 첫 적용(2026-10-01 orchestrator 세션)에서 계열 2·4·2·2·2가 정지 규칙을 두 번 성립시켰다.

날짜 대리는 경계가 성기다. 날짜는 세션과 같지 않고 2026-10-04 실측의 실행 기록은 넷뿐이었다. 검증 목표 `verification-round-stop-rule`이 요구하는 관측은 셋이다 — 라운드마다의 신규 결함 수, 멈춘 자리가 규칙이라는 기록, 예산 소진과 정지 규칙의 구분. 날짜 대리는 셋째를 채우지 못한다. 종료 사유를 단 기록은 셋을 모두 채우고 정지 규칙을 그래프 불변식으로 만들어 게이트에 올린다.

유저 답 Q39-c(2026-10-04)가 이 안을 골랐다. 2026-10-01 승인 규범의 날짜 정의는 승인 사항이므로 이 답이 그 규범 개정의 승인을 겸한다.
