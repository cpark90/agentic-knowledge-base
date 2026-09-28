---
id: https://agentic-knowledge-base.dev/id/chunk/f0fdfa51-3dd6-4e7f-adee-88b3ad41b93a
type: requirement
level: functional
pattern: ubiquitous
title_ko: 순서 있는 복합체(co:List)의 색인 정합성은 shape가 강제해야 한다
title: The index consistency of an ordered composite (co:List) must be enforced by a shape
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T05:10:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
---
**검증 목표** — 결정 p4-composite-order-is-declared는 순서가 뜻을 갖는 복합체만 선언 청크의 `composite:`에 `ordered`를 적고 생성기가 `co:List`·`co:index`를 방출한다고 정한다. 색인이 1..n 연속·중복 없음이고 `co:itemContent`가 `agt:hasDirectPart`와 같은 집합이라는 정합성은 이 저장소에서 처음 쓰는 `sh:sparql` shape(`composite-order-shapes.ttl`)가 판정한다. pySHACL의 `sh:sparql` 잠금이 바뀌면 조용히 통과할 수 있으므로, shape 쪽에 고정물이 있어야 회귀를 잡는다.

- **이해관계자**: 에이전트 · 감사 역할 · **관심사**: 순서 선언의 정합성

**무엇을 관측하면 성립하는가**

- 색인에 구멍이 있는(예 1,3) `co:List`가 거부된다.
- 색인이 중복인(예 1,1) `co:List`가 거부된다.
- `co:itemContent`가 `agt:hasDirectPart` 밖을 가리키는 `co:List`가 거부된다.
- 위 셋을 만족시키는 정합한 `co:List`는 통과한다.

판정의 원본은 `kb/ontology/shapes/composite-order-shapes.ttl`과 `tools/validate.py`의 `check_shacl`이다.
