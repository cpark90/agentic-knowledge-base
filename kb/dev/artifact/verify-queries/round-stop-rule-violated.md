---
id: https://agentic-knowledge-base.dev/id/chunk/d7b21ca0-5e2c-4f71-9a2c-86a9052af424
type: artifact
level: executable
title_ko: 질의 round-stop-rule-violated (tools/verify-queries)
title: query round-stop-rule-violated in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/round-stop-rule-violated.rq` 다. 44줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 정지 규칙 위반 — 라운드 n 의 신규 결함 수가 라운드 n−1 의 것 이상인데 라운드 n+1 기록이 정지 규칙이 아닌 사유로 닫혔다 (V&V 기준 verification-round-stop-rule, 유저 답 Q39-c)
# 라운드 기록 = vv_run(process:vv_run)의 관측 중 본문이 종료 사유(agt:RoundEndReason) 하나를 인용한 것(agt:usesConcept). 라운드 순서는 prov:generatedAtTime 이다.
# 신규 결함 수 new(n) = 직전 라운드 기록 시각 뒤 ~ 라운드 n 기록 시각까지 저작된 살아 있는 판정 주석(agt:AnnotationChunk) 중
# 판정 결과 주석(process:judge)이 아닌 것의 수다. 첫 라운드의 구간은 첫 기록 시각까지 전부다. 기록이 셋 미만이면 대상 0 이다.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?next ?reason ?newPrev ?newCur WHERE {
  { SELECT ?prev (COUNT(DISTINCT ?c) AS ?newPrev) WHERE {
      ?prev a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?pr ; prov:generatedAtTime ?tp .
      ?pr a agt:RoundEndReason .
      OPTIONAL {
        ?c a agt:AnnotationChunk ; prov:generatedAtTime ?tc ; agt:generatedBy ?gc ; agt:status ?sc .
        FILTER(?gc != "process:judge" && ?sc != "deprecated" && ?tc <= ?tp)
        FILTER NOT EXISTS {
          ?q a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?qr ; prov:generatedAtTime ?tq .
          ?qr a agt:RoundEndReason .
          FILTER(?tc <= ?tq && ?tq < ?tp)
        }
      }
    } GROUP BY ?prev }
  { SELECT ?cur (COUNT(DISTINCT ?d) AS ?newCur) WHERE {
      ?cur a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?cr ; prov:generatedAtTime ?tr .
      ?cr a agt:RoundEndReason .
      OPTIONAL {
        ?d a agt:AnnotationChunk ; prov:generatedAtTime ?td ; agt:generatedBy ?gd ; agt:status ?sd .
        FILTER(?gd != "process:judge" && ?sd != "deprecated" && ?td <= ?tr)
        FILTER NOT EXISTS {
          ?s a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?sr ; prov:generatedAtTime ?ts .
          ?sr a agt:RoundEndReason .
          FILTER(?td <= ?ts && ?ts < ?tr)
        }
      }
    } GROUP BY ?cur }
  ?prev prov:generatedAtTime ?t1 .
  ?cur prov:generatedAtTime ?t2 .
  ?next a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?reason ; prov:generatedAtTime ?t3 .
  ?reason a agt:RoundEndReason .
  FILTER(?t1 < ?t2 && ?t2 < ?t3 && ?newCur >= ?newPrev && ?reason != agt:roundEndedByStopRule)
  FILTER NOT EXISTS {
    ?x a agt:MemoryChunk ; agt:generatedBy "process:vv_run" ; agt:usesConcept ?xr ; prov:generatedAtTime ?tx .
    ?xr a agt:RoundEndReason .
    FILTER((?t1 < ?tx && ?tx < ?t2) || (?t2 < ?tx && ?tx < ?t3))
  }
}
```
<!-- 인용 끝 -->
