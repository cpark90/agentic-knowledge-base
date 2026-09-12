---
id: https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2
type: decision
level: concrete
title_ko: plane은 Chunk의 하위 클래스이고 level은 속성이다
title: Plane is a subclass of Chunk and level is a property
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0071]
part_of: https://agentic-knowledge-base.dev/id/composite/db06bc97-7100-4ad3-bad0-83fb1c876e1c
composite: {id: https://agentic-knowledge-base.dev/id/composite/db06bc97-7100-4ad3-bad0-83fb1c876e1c, title_ko: plane과 level의 온톨로지 표현, title: Ontological form of plane and level}
---
**결론** — **plane은 `agt:Chunk`의 하위 클래스다.** 일곱 개다.

```
agt:Chunk
  ├── agt:RequirementChunk   (plane = requirement, level = functional 고정)
  ├── agt:DecisionChunk      ├── agt:ContractChunk
  ├── agt:SchemaChunk        ├── agt:ArtifactChunk
  ├── agt:AnnotationChunk    └── agt:MemoryChunk
```

**level은 속성이다.** `agt:hasLevel`의 값은 다섯 개체 `agt:functional` …
`agt:executable` 중 하나다. 청크 개체의 최소 선언은 타입(plane 클래스),
`agt:hasLevel`, 한/영 `rdfs:label`, `agt:lineCount`다.
