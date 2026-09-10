---
id: https://agentic-knowledge-base.dev/id/chunk/d0f3d2b1-9533-40a4-acfb-12f318382f7d
type: decision
level: concrete
title_ko: 지속성과 버전을 IRI 구조로 표현한다
title: Persistence and version are expressed in the IRI structure
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0032]
part_of: https://agentic-knowledge-base.dev/id/composite/eb847899-2640-4bca-955a-7f511528bc1d
composite: {id: https://agentic-knowledge-base.dev/id/composite/eb847899-2640-4bca-955a-7f511528bc1d, title_ko: 불투명 지속 IRI와 해시 버전 IRI, title: Opaque persistent IRI and content-hash version IRI}
---
**결론** — 청크·복합체·링크·가정은 전부 개체이므로 IRI가 필요하다. 지속성과
버전을 IRI 구조로 표현한다.

- **지속 IRI** — `agt:chunk/<uuid>`. 내용과 무관한 불투명 식별자
- **버전 IRI** — `agt:chunk/<uuid>/<content-hash>`. 나노출판 신뢰 가능 IRI
- **온톨로지 버전** — `owl:versionIRI` (표준)
- **사람이 읽는 이름** — IRI가 아니라 `rdfs:label`
