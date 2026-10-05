---
id: https://agentic-knowledge-base.dev/id/chunk/8cdc4517-979e-4aa1-809f-b7b5adb1d219
type: artifact
level: executable
title_ko: 질의 verifies-without-criteria (tools/verify-queries)
title: query verifies-without-criteria in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/verifies-without-criteria.rq` 다. 7줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 기준 없는 verifies — 무엇으로 검증했는지 없으면 검증이 아니다 (노트 7.11절)
# 기준 연결 = verifies의 주어가 합격 기준(ContractChunk)을 refines 한다.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT ?s ?o WHERE {
  ?s agt:verifies ?o .
  FILTER NOT EXISTS { ?s agt:refines ?c . ?c a agt:ContractChunk }
}
```
<!-- 인용 끝 -->
