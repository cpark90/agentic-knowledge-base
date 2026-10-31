---
id: https://agentic-knowledge-base.dev/id/chunk/a5643dfc-04dd-48e8-997a-47ae456bef7f
type: decision
level: concrete
title_ko: 카탈로그로 IRI를 파일로 해석해 union을 조립한다
title: The union is assembled by resolving IRIs to files through a catalog
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0156-catalog-resolved-union.md, id: https://agentic-knowledge-base.dev/id/chunk-d0156, title_ko: "카탈로그로 IRI를 파일로 해석해 union을 조립한다", title: "Assemble the union by resolving IRIs through a catalog"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0156]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5beca94e-efeb-4e6c-89a7-12c3fa80103e
composite: {id: https://agentic-knowledge-base.dev/id/composite/5beca94e-efeb-4e6c-89a7-12c3fa80103e, title_ko: 카탈로그로 조립하는 union, title: Catalog-resolved union}
---
**결론** — 여러 저장소에 나뉜 그래프는 **import 선언과 카탈로그**로 하나의 union으로 조립하고, 카탈로그는 문서 IRI를 로컬 파일로 해석한다. root 문서에서 import를 따라간 폐포가 곧 union이며, 디렉토리 glob도 submodule도 조립 수단으로 쓰지 않는다.
