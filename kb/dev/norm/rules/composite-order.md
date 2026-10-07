---
id: https://agentic-knowledge-base.dev/id/chunk/8ac23bae-1974-460b-b125-6471de3e5212
type: norm
level: logical
title_ko: docs/rules.md 절 복합체의 이어짐 — 순서는 선언에서만 나온다
title: docs/rules.md composite section continued — order comes only from the declaration
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e2326375-ac83-490d-ab30-09a01c5f73f0
continues: true
---
**순서는 선언에서만 나온다** ([`p4-composite-order-is-declared`](../../decision/p4-composite-order-is-declared/conclusion.md) —
유저 승인 2026-09-29 — 결정도 예외 없이, 도구 반영 같은 날). 선언 청크의 `composite:`에 `ordered: [<부분 IRI>…]`가 있으면 `kb_composite`·`gen_build`가
`part_iris`를 그 순서로 내고 `chunk2kg`가 `<복합체> a agt:Composite, co:List ; co:item [ a co:ListItem ; co:index
"<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ] …`을 방출한다. 없으면 `hasDirectPart`만 낸다 — `hasDirectPart`는 순서와
무관하게 남으므로 순서 트리플은 추가일 뿐이다. 목록이 부분 집합과 어긋나면 생성 시점 `gen-build`와 실행 시점 `chunk2kg`가
거부하고, 색인 1..n 연속·중복 없음·부분 집합과의 일치는 shape `composite-order-shapes`(`sh:sparql` — 이 저장소의 첫
사용)가 판정한다. 판정 단위가 복합체 노드 하나라 verify 실행 계층이 아니라 shape 실행 계층이다. `ordered`는 frontmatter의 메타데이터이므로
더하거나 고쳐도 `generated.at`·`verified`를 건드리지 않는다.
