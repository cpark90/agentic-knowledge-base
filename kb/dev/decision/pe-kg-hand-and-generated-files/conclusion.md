---
id: https://agentic-knowledge-base.dev/id/chunk/ad0722e8-b65d-47ed-8940-f0082997a7d2
type: decision
level: concrete
title_ko: 청크 head는 생성하고 손으로 쓰는 지식그래프 TTL 셋은 청크가 아닌 개체만 한/영 라벨과 배너를 갖춰 담는다
title: Chunk heads are generated, and the three hand-written knowledge graph TTL files hold only non-chunk entities, with ko/en labels and a banner
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:10:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3b6eaa94-2497-48bd-96c7-2b84963394d7
composite: {id: https://agentic-knowledge-base.dev/id/composite/3b6eaa94-2497-48bd-96c7-2b84963394d7, title_ko: 지식그래프 파일 — 손과 생성, title: Knowledge graph files — hand-written and generated}
---
**결론** — 지식그래프 A-Box는 생성 파일과 손 파일로 나뉜다. 청크의 head는 손으로 쓰지 않는다.

| 담는 것 | 위치 | 손/생성 |
|---|---|---|
| chunk head | `bazel-bin/kg/chunks-kg.ttl`. 청크 파일의 frontmatter에서 `//kg:chunks_kg`가 만든다 | 생성 |
| 복합체 | `kg/composite-kg.ttl` | 손 |
| 가정 · 출처 문서 | `kg/base-kg.ttl` | 손 |
| 역할 · 스코프 · 채널 · 하네스 (입력) | `kg/catalog-kg.ttl` | 손 |

- 손 TTL 셋은 청크가 아닌 개체만 담는다. 가정·출처 문서·복합체·역할·스코프·채널·하네스다.
- 개체마다 `rdfs:label`을 한/영 하나씩 단다.
- 파일 상단 배너에 그 파일이 담는 개체 종류와 손으로 쓰지 않는 것을 적는다.
- 조건과 ODD의 위치는 `pe-odd-is-openodd`가 정한다. 개체 IRI의 꼴은 `p0-entity-iri-forms`가 정한다.
