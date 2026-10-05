---
id: https://agentic-knowledge-base.dev/id/chunk/b8725acf-20d3-4b17-8c6f-afd9da8df2f4
type: decision
level: concrete
title_ko: 규범 문서의 절 청크는 orchestrator가 쓰고 생성기는 developer가 쓴다
title: Section chunks of the normative documents are written by the orchestrator, and the generator by the developer
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1129e152-2ac3-4104-94c7-9642040ca3a3
composite: {id: https://agentic-knowledge-base.dev/id/composite/1129e152-2ac3-4104-94c7-9642040ca3a3, title_ko: 규범 문서 절 청크의 저작 역할, title: Authoring role for normative-document section chunks}
---
**결론** — `norm` plane의 쓰기 역할은 orchestrator다(2026-10-04). 규범 문서의 절 청크(`agt:DocumentSectionChunk`)는 orchestrator가 쓴다.

| 대상 | 쓰는 역할 | 근거 자리 |
|---|---|---|
| 절 청크(`kb/dev/norm/`) | orchestrator | `kg/catalog-kg.ttl`의 `id:role-orchestrator` `agt:writes` |
| 결정의 `conventions.md` | orchestrator | 결정 plane의 쓰기 역할(`p7-dev-roles-and-scopes`) |
| 생성기 `tools/gen_norms.py` | developer | `artifact` plane(`p12-norm-documents-from-section-chunks`) |

- 게이트 `writer`가 이것을 판정한다. `generated.by`의 역할이 `norm` plane을 쓸 수 없으면 FAIL이다. 다른 역할이 만든 절 청크는 orchestrator의 `verified`(인수)가 있어야 통과한다.
- 카탈로그와 역할 표(`AGENTS.md`)는 같은 커밋에서 바꾼다(`p7-dev-roles-and-scopes`).
