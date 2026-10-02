---
id: https://agentic-knowledge-base.dev/id/chunk/14414342-1e2f-4f00-a100-8c18642d0ebd
type: requirement
level: functional
pattern: ubiquitous
title_ko: 본문이 토큰 상한(저작 산문 1,092·artifact·memory 2,856)을 넘는 청크는 거부되어야 한다
title: A chunk whose body exceeds the token limit (authored prose 1,092; artifact/memory 2,856) must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T20:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
---
**검증 목표** — 청크의 본문이 토큰 상한(저작 산문 1,092 · `artifact`·`memory` 2,856)을 넘지 않는다는 결정이 청크 검사와 shape 두 곳에서 강제된다는 것이 보여져야 한다. 상한을 넘는 것은 청크가 아니라 분할 대상이다(p1-chunk-unit-is-tokens).

- **이해관계자**: 에이전트 · 감사 역할 · **관심사**: 작업 집합이 컨텍스트 예산 안에 드는 것

**무엇을 관측하면 성립하는가**

- 본문 토큰 수가 plane 상한을 넘는 `.md` 청크를 `chunk_lint`에 넣으면 `FAIL [chunk]`로 거부된다. frontmatter와 앞뒤 빈 줄은 세지 않는다. 계수기는 고정된 `o200k_base`다.
- 같은 청크의 head 그래프는 `agt:tokenCount`가 상한을 넘어 plane별 `…Chunk` shape(`token-budget-shapes.ttl`)에 걸린다.
- 커밋된 청크 전부가 plane 상한 이하이고 `//chunks:lint_test`·`//kb/dev:lint_test`·`//kg:gate_test`가 PASS다.

상한의 원본은 `tools/kb_lib.py`의 `BODY_TOKEN_LIMITS`와 `kb/ontology/shapes/token-budget-shapes.ttl`의 `sh:maxInclusive`다. 게이트 id는 `chunk`·`token-budget`이다.
