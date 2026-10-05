---
id: https://agentic-knowledge-base.dev/id/chunk/ea6fd215-ad82-40c5-b9f9-68e6f11f59e3
type: artifact
level: executable
title_ko: 질의 sources-empty (tools/verify-queries)
title: query sources-empty in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/sources-empty.rq` 다. 10줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 출처(sources) 빈 청크 — 어디서 왔는지 없는 지식은 실패다 (노트 2.5절·2.12절)
# 결과 행 하나 = 위반 하나.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?chunk WHERE {
  ?chunk a ?cls .
  ?cls rdfs:subClassOf* agt:Chunk .
  FILTER NOT EXISTS { ?chunk prov:wasDerivedFrom ?src }
}
```
<!-- 인용 끝 -->
