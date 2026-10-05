---
id: https://agentic-knowledge-base.dev/id/chunk/51bc815c-46a8-468c-83df-bd3339d34bc6
type: artifact
level: executable
title_ko: 질의 imported-chain-confirmed (tools/verify-queries)
title: query imported-chain-confirmed in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/imported-chain-confirmed.rq` 다. 13줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 신뢰 전파 위반 — 확정 상태인데 파생 연쇄 전체가 origin:imported (노트 2.12절)
# 연쇄 어딘가에 사람 검토(verifiedBy human:*)나 designed/observed 출처가 있어야 한다.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?chunk WHERE {
  ?chunk agt:status "stable" ; agt:taggedWith ?t .
  ?t agt:inTagCategory agt:originCategory .
  FILTER NOT EXISTS { ?chunk agt:verifiedBy ?v . FILTER(STRSTARTS(?v, "human:")) }
  FILTER NOT EXISTS {
    ?chunk (prov:wasDerivedFrom)* ?anc .
    ?anc agt:taggedWith ?dt . FILTER(?dt != ?t)
  }
}
```
<!-- 인용 끝 -->
