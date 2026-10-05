---
id: https://agentic-knowledge-base.dev/id/chunk/de249b57-d514-4501-aa52-f713281e1d5c
type: artifact
level: executable
title_ko: 질의 confirmed-without-evidence (tools/verify-queries)
title: query confirmed-without-evidence in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/confirmed-without-evidence.rq` 다. 9줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 지지 없는 확정 — 구축(+) 또는 실행(+) 증거 없이 confirmed인 링크 (노트 9.11절 증거 기록 규칙, 10.4절)
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT ?link WHERE {
  ?link a agt:Link ; agt:linkState "confirmed" .
  FILTER NOT EXISTS {
    ?link agt:hasEvidence ?e . ?e agt:polarity "+" ; agt:evidenceKind ?k .
    FILTER(?k IN (agt:constructionRecord, agt:runResult))
  }
}
```
<!-- 인용 끝 -->
