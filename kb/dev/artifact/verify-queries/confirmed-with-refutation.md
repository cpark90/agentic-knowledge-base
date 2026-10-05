---
id: https://agentic-knowledge-base.dev/id/chunk/bdecbee2-b7cb-4a9e-b43d-0c7764709f68
type: artifact
level: executable
title_ko: 질의 confirmed-with-refutation (tools/verify-queries)
title: query confirmed-with-refutation in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/confirmed-with-refutation.rq` 다. 6줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 반박된 확정 — (−) 증거가 있는데 여전히 confirmed인 링크. 실행(−)은 invalid, 그 밖의 (−)는 사람 큐 (노트 9.11절)
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT ?link ?k WHERE {
  ?link a agt:Link ; agt:linkState "confirmed" ;
        agt:hasEvidence ?e . ?e agt:polarity "-" ; agt:evidenceKind ?k .
}
```
<!-- 인용 끝 -->
