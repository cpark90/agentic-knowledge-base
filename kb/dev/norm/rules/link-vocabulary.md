---
id: https://agentic-knowledge-base.dev/id/chunk/a06e708f-6ada-466d-b887-e1226ae6b7f7
type: norm
level: logical
title_ko: docs/rules.md 절 traceability의 이어짐 — 링크 어휘의 확장 규칙과 링크 키의 두 무리
title: docs/rules.md traceability section continued — link vocabulary extension and the two groups of link keys
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:17:27+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/608085a2-2251-4b82-8ccc-a5c7e6e71766
continues: true
---
**링크 어휘의 확장 규칙** — 새 관계는 위 세 족 가운데 하나의 **잎으로만** 더하고 족을 새로 만들지 않는다(유저 승인 2026-09-23,
링크 견고성 E). 잎은 `rdfs:subPropertyOf`로 족에 속하고, 게이트가 부모 트리플을 함께 생성하므로 족 단위 질의는
새 잎을 자동으로 본다. 잎의 이름은 `docs/references.md` §추적성의 추적성 관계 분류에서 가져오고 지어내지 않으며,
`overlapsWith`가 그렇게 가져온 이름이다. 후보 생성기는 추적 매트릭스에 칸이 없는 쌍을 만나면 `relatedTo`가 아니라 `overlapsWith`로
낸다. 인용은 겹침의 표지이고 칸 없는 참조는 참조 링크로 확정되지 않기 때문이다. 다만 칸이 생기면 그 칸의 잎으로 올린다.

frontmatter 링크 키는 두 무리로 나뉜다. 첫째 무리는 Bazel `deps`가 되는 네 키 `refines`와 `serves`, `supersedes`, `verifies`다.
둘째 무리는 그래프 트리플과 링크 개체만 되는 나머지 키 `satisfies`와 `constrains`, `derivesFrom`, `allocates`, `generates`,
`overlapsWith`다. 대칭 속성은 `deps`가 되면 순환이 생기므로 둘째 무리에만 든다.
