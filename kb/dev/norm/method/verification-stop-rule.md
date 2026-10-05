---
id: https://agentic-knowledge-base.dev/id/chunk/6b073d14-5780-416a-af16-5b54897193ab
type: norm
level: logical
title_ko: docs/method.md 절 검증의 이어짐 — 라운드 정지 규칙
title: docs/method.md verification section continued — the round stop rule
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4
continues: true
items: [p8-verification-round-stop-rule#1]
---
**정지 규칙**(유저 승인 2026-10-01, 목표 `verification-round-stop-rule` stable) — 연속한 두 라운드에서 신규 결함 수가 줄지 않으면 다음
라운드를 열지 않고 채널로 되돌린다. 라운드의 정의는 처음에 판정 주석의 `prov:generatedAtTime` 날짜였고, 유저 답 Q39-c(2026-10-04)가
그것을 종료 사유를 단 명시 기록으로 바꿨다. 날짜 정의 아래의 첫 적용은 2026-10-01 orchestrator 세션이다 — 2·4·2·2·2에서 두 번 성립해
라운드를 열지 않았다.
