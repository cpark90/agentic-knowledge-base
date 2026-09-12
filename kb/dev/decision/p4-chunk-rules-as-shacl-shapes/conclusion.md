---
id: https://agentic-knowledge-base.dev/id/chunk/f7ac5761-e5da-4a34-8beb-f661f8164328
type: decision
level: concrete
title_ko: 청크의 규칙은 SHACL shape으로 쓴다
title: Chunk rules are written as SHACL shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0072]
part_of: https://agentic-knowledge-base.dev/id/composite/19abf7d7-e6fe-406a-be99-f9de153f4e95
composite: {id: https://agentic-knowledge-base.dev/id/composite/19abf7d7-e6fe-406a-be99-f9de153f4e95, title_ko: 청크의 규칙 — SHACL shape, title: Chunk rules as SHACL shapes}
---
**결론** — 구조적 글쓰기의 원칙을 **SHACL shape**으로 쓴다. 6.7절 검사 게이트가
이 shape으로 청크를 검사한다.

| 원칙 | shape |
|---|---|
| **청킹** — 작은 단위 | `agt:lineCount` ≤ 42 |
| **관련성** — 한 주제 | plane 클래스 정확히 1, `agt:hasLevel` 정확히 1 |
| **라벨링** — 이름 필수 | `rdfs:label` 최소 1, 한/영 각 1 (0.6절) |
| **일관성** — 어휘 통일 | assertion의 모든 술어가 온톨로지에 존재 |

```
agt:ChunkShape a sh:NodeShape ;
  sh:targetClass agt:Chunk ;
  sh:property [ sh:path agt:lineCount ; sh:maxInclusive 42 ] ;
  sh:property [ sh:path agt:hasLevel ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path rdfs:label ; sh:minCount 2 ] .
```

plane별 shape는 `agt:ChunkShape`를 **상속하고 추가 제약을 더한다** —
`agt:ArtifactChunk`는 심볼 ID 필수, `agt:DecisionChunk`는 결론·근거·대안 중
하나의 역할 태그 필수.
