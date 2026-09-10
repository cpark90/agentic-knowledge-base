---
id: https://agentic-knowledge-base.dev/id/chunk/a4678d28-76ed-48df-84de-db8421a8718e
type: decision
level: concrete
title_ko: 청크 IRI가 앵커다 — 드리프트가 청크 안에 갇힌다
title: The chunk IRI is the anchor; drift is confined inside the chunk
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0077]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2184c3-67a9-4745-b0c3-65e8c3f69fd6
composite: {id: https://agentic-knowledge-base.dev/id/composite/5e2184c3-67a9-4745-b0c3-65e8c3f69fd6, title_ko: 청크 IRI가 앵커다, title: The chunk IRI is the anchor}
---
**결론** — **청크 IRI가 앵커다.** 링크(Part X)의 양 끝은 `agt:KnowledgeItem`
IRI이고, plane별 식별자는 IRI를 실제 저장 위치로 해석하는 수단일 뿐이다.

**앵커 드리프트가 청크 안으로 갇힌다.** 링크는 IRI를 가리키므로 본문 편집은
링크에 영향을 주지 않는다. 청크가 **분할·병합될 때만** — 즉 IRI가 새로
생기거나 사라질 때만 — 링크가 `suspect`가 된다. 분할·병합은
`prov:wasDerivedFrom`으로 옛 IRI와 이어져 추적된다.

같은 앵커가 다른 메커니즘에도 쓰인다 — 가정(6.5절) `assumes`의 출발점이 청크
IRI여서 가정 입도 문제가 청크 분할 문제로 환원되고, 시간 정체성(2.6절)은 청크
IRI가 지속하고 본문 버전이 `prov:wasRevisionOf`로 이어져 별도 정체성 링크가
필요 없으며, 상승(6.3절)은 관측 → 패턴 → 개념 청크의 각 단계가
`prov:wasDerivedFrom`이다.
