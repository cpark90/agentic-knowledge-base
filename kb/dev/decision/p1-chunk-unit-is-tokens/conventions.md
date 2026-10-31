---
id: https://agentic-knowledge-base.dev/id/chunk/f920fa6c-0a5a-497a-b83f-22c234c1bf09
type: decision
level: concrete
title_ko: 규범 문서 규약 — 단위 지식의 단위는 토큰이고 상한은 예산 5,418의 1/5인 1,092 토큰(42의 26배)이다
title: Normative-document conventions — The chunk unit is tokens, and the limit is 42×26 = 1,092 tokens — one fifth of the 5,418-token budget
former_title_ko: ["규범 문서 규약 — 지식 항목의 단위는 토큰이고 상한은 예산 5,418의 1/5인 1,092 토큰(42의 26배)이다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/128d439b-0863-41e3-8eb3-7c090e7f1742
---
**규약** — `p1-chunk-unit-is-tokens`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **본문은 토큰 상한 이하다.** 상한은 저작 산문이 42의 26배인 1,092, `artifact`와 `memory`의 인용이 42의 68배인 2,856이고, 계수기는 고정된 `o200k_base`다(2026-10-01, 그 전에는 42줄). 단위는 컴포넌트별 절이 정의한다.
규약: [지킴] 본문은 토큰 상한 1,092 이하다. `@prefix`·주석·빈 줄은 제외한다.
규약: [지킴] 본문은 토큰 상한인 저작 산문 1,092와 인용 2,856 이하이고, frontmatter와 앞뒤 빈 줄은 제외한다. 주제는 하나이며 라벨만 보고 본문을 예측할 수 있어야 한다.
규약: 상한 오버라이드 | 저작 산문 1,092 토큰 · `artifact`와 `memory`의 인용 2,856 | 채움(단위는 토큰이고 값은 `BODY_TOKEN_LIMITS`에 있다, 2026-10-01)
