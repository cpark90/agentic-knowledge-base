---
id: https://agentic-knowledge-base.dev/id/chunk/ef27a2a6-bdb2-4c5b-bd95-d7198b3c9359
type: artifact
level: executable
title_ko: 질의 composite-cycle (tools/verify-queries)
title: query composite-cycle in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/composite-cycle.rq` 다. 6줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 순환 복합체 — agt:hasDirectPart 연쇄가 자기 자신에 닿는다 (노트 4.5절, rules §2 비순환)
# 결과 행 하나 = 위반 하나. 첫 실행(2026-09-13, 복합체 230): 0.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT DISTINCT ?composite WHERE {
  ?composite a agt:Composite ; agt:hasDirectPart+ ?composite .
}
```
<!-- 인용 끝 -->
