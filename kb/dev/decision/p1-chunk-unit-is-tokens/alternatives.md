---
id: https://agentic-knowledge-base.dev/id/chunk/be0bbd48-541b-4719-808a-e6b1e9efb5d4
type: decision
level: logical
title_ko: 참조 저장소의 260·근사 630·줄 유지·plane마다 다른 배수는 기각된다
title: The reference repository's 260, the estimated 630, keeping lines, and per-plane multipliers are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-01T20:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/128d439b-0863-41e3-8eb3-7c090e7f1742
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 참조 저장소의 재결정 260 ≈ 42×6 | 다른 계수기·다른 창의 수다. 이 저장소의 도출(예산 ÷ 5)과 무관하고 저작 산문 426개(43%)를 쪼갠다 — 숫자가 도출을 대체한다 |
| hci 근사의 42×15 = 630 | 근사(한글 3자/토큰)가 실측과 1.7배 어긋났다. 111개를 쪼갰을 것이다 |
| 줄을 유지하고 plane별 줄 상한만 둔다 | 줄은 컨텍스트의 단위가 아니다. plane마다 상한의 뜻이 갈리는 문제가 그대로다(산문 42줄 = 1,138토큰, 코드 42줄 = 600토큰) |
| plane마다 다른 배수(요구·결정·V&V 각각) | 저작 산문은 줄당 토큰이 24~33으로 비슷해 한 상한이 맞다. 갈리는 것은 인용(코드·기록)뿐이고 그것만 따로 둔다 |

"42토큰"(글자 그대로)은 검토 대상이 아니다 — 1,644개(99.9%)가 넘는다. 유저 답이 "42의 배수"로 그것을 풀었다.
