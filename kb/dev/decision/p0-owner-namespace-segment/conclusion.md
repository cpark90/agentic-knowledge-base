---
id: https://agentic-knowledge-base.dev/id/chunk/d99ab099-4192-4021-a7f6-7876f5954b69
type: decision
level: concrete
title_ko: 개체 이름공간을 소유자 세그먼트로 나눈다
title: The entity namespace is split by an owner segment
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0158-owner-namespace-segment.md, id: https://agentic-knowledge-base.dev/id/chunk-d0158, title_ko: "개체 이름공간을 소유자 세그먼트로 나눈다", title: "Partition the entity namespace by owner segment"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0158]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c6b1526b-31e7-41f3-9f13-9cc419803e2d
composite: {id: https://agentic-knowledge-base.dev/id/composite/c6b1526b-31e7-41f3-9f13-9cc419803e2d, title_ko: 소유자 세그먼트로 나눈 개체 이름공간, title: Entity namespace split by owner segment}
---
**결론** — 독립 저장소가 각자 개체를 민팅하는 연합에서는 개체 IRI에 **소유자 세그먼트**를 넣어 `…/id/<owner>/<slug>` 꼴로 민팅한다. 공용 중립 부품용 세그먼트 하나를 예약하고, 저장 형식에서는 prefix 바인딩으로만 표현해 노드 본문의 이름은 slug 그대로 둔다.
