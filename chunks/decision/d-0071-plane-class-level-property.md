---
id: https://agentic-knowledge-base.dev/id/chunk-d0071
type: decision
level: concrete
title_ko: plane은 하위 클래스, level은 속성
title: Plane as subclass, level as property
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — plane은 `agt:Chunk`의 **하위 클래스**로 두고(`agt:DecisionChunk`,
`agt:ContractChunk`, `agt:SchemaChunk`, `agt:ArtifactChunk`,
`agt:AnnotationChunk`, `agt:MemoryChunk`), level은 **속성**
`agt:hasLevel`로 둔다. 값은 `agt:functional`…`agt:executable` 다섯 개체
중 하나다.

**근거** (노트 4.2절)
- plane을 클래스로 두는 이유는 **plane마다 다른 제약(shape)을 붙이기
  위해서**다. 모듈형 문서의 정보 유형(concept / task / reference)이 topic의
  특수화이듯, plane은 청크의 특수화다.
- level을 속성으로 두어도 충분한 이유는 **같은 청크가 level을 바꾸는 일이
  없기** 때문이다. 사다리 전이는 기존 청크의 level을 갱신하는 것이 아니라
  새 청크를 만들고 `refines` 링크를 남긴다.

**청크 개체의 최소 선언** — 타입(plane 클래스) 1, `agt:hasLevel` 1,
`rdfs:label` 한/영 각 1, `agt:lineCount`. 이 넷이 head 그래프의 내용이다.
