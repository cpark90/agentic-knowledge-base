---
id: https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393
type: decision
level: concrete
title_ko: 청크의 단위는 토큰이고 상한은 예산 5,418의 1/5인 42×26 = 1,092 토큰이다
title: The chunk unit is tokens, and the limit is 42×26 = 1,092 tokens — one fifth of the 5,418-token budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/de38da18-3de5-4b30-86d6-af112ca9659c]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-01T20:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/128d439b-0863-41e3-8eb3-7c090e7f1742
composite: {id: https://agentic-knowledge-base.dev/id/composite/128d439b-0863-41e3-8eb3-7c090e7f1742, title_ko: 청크의 단위는 토큰이다, title: The chunk unit is tokens}
---
**결론** — 청크 크기의 단위는 줄이 아니라 **토큰**이다(유저 답 2026-10-01 — "42의 배수로, 공개 토크나이저 하나를 의존성으로 고정"). 계수기는 `tiktoken` `o200k_base`(어휘 파일 sha256 고정, ODD 조건 `cond-tokenizer-lock`)다.

| 항목 | 값 | 도출 |
|---|---|---|
| 컨텍스트 예산 | **5,418 토큰 = 42×129** | 저작 산문(요구·결정 879)의 줄당 토큰 중앙 27.09 × 200줄 — 옛 결정의 200줄을 같은 계수기로 환산 |
| 청크 상한(저작 산문) | **1,092 토큰 = 42×26** | 예산 ÷ 5 = 1,084 → 가장 가까운 42의 배수. 한 번에 4~5개를 조망한다는 옛 근거 그대로 |
| 청크 상한(`artifact`·`memory`) | **2,856 토큰 = 42×68** | 코드의 줄당 토큰 14.3 × 200줄 — "청크 하나가 컨텍스트 한 창을 넘지 않는다"(옛 200줄 상한의 환산) |

근거를 **예산 ÷ 5**로 고른 까닭: 42줄은 처음부터 "200줄의 약 1/5"로 도출됐고, 그 도출을 토큰으로 옮기면 1,092다. 참조 저장소의 재결정 260(≈ 42×6)은 다른 계수기·다른 창의 수이며 그것을 쓰면 저작 산문의 43%(426)를 쪼개야 한다 — 숫자가 아니라 도출이 규칙이다. 1,092에서 초과는 저작 산문 3 · 코드 52(2,856에서는 6)다.

줄 상한(42·200)은 전부 폐지되고 게이트는 토큰(`agt:tokenCount`)으로 판정한다. 분할은 `p10-split-keeps-work-identity`를 따른다. 노트 938·949·641행의 "줄"은 유저 의도대로 정정한다 — 기획 원본의 오기록이다.
