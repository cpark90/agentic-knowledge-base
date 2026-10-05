---
id: https://agentic-knowledge-base.dev/id/chunk/d0f3d2b1-9533-40a4-acfb-12f318382f7d
type: decision
level: concrete
title_ko: 지속성과 버전을 IRI 구조로 표현한다
title: Persistence and version are expressed in the IRI structure
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-06T01:13:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T01:13:52+09:00}]
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

언제 IRI를 유지하고 언제 새로 만드는가는 분할·병합 공간 `https://agentic-knowledge-base.dev/id/chunk/6fec9aaa-ca14-42fe-98d4-64bc8d15dbe8`이 답했다(`p10-split-keeps-work-identity`, Q57-a).

미확정: 버전 IRI를 쓸 것인가. 상세는 `https://agentic-knowledge-base.dev/id/chunk/dda51e76-7054-460b-ba4d-3bd4c14d4e6f`다(Q62-a).
