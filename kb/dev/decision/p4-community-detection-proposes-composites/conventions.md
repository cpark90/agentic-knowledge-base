---
id: https://agentic-knowledge-base.dev/id/chunk/fda352bc-ca72-4aa2-9d89-71c09fd3aa9b
type: decision
level: concrete
title_ko: 규범 문서 규약 — 커뮤니티 탐지는 복합체 후보를 제안할 뿐이고 채택은 사람이 한다
title: Normative-document conventions — Community detection only proposes composite candidates; adoption is a human decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/165ef75a-d4f3-4de2-aba2-ea3a8efb787a
---
**규약** — `p4-community-detection-proposes-composites`의 결론을 규범 문서에 싣는 문장이다.

규약: **통합이 필요하면** 복합체에 잇는다. 통합이 필요한 때는 함께 읽혀야 이해되거나 순서가 뜻을 가질 때뿐이다. 그렇지 않으면 개별로 둔다 ([rules §2](../../../../docs/rules.md#2-복합체--통합이-필요한-것만)).
규약: 커뮤니티 탐지 | 결정론적 Louvain으로 복합체 후보와 `relatedTo` 후보 — `//kg:communities`. 채택·기각은 사람이 한다
