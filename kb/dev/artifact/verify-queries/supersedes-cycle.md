---
id: https://agentic-knowledge-base.dev/id/chunk/4b5dd9a4-f6cd-4e97-9e2c-db216d3ee0d1
type: artifact
level: executable
title_ko: 질의 supersedes-cycle (tools/verify-queries)
title: query supersedes-cycle in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/supersedes-cycle.rq` 다. 8줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 순환 대체 — agt:supersedes 연쇄가 자기 자신에 닿는다 (노트 7.4절, 8.11절)
# owl:TransitiveProperty(ladder-ontology) 를 켠 뒤의 건전성 조건이다. 이행 폐포가 자기 자신에 닿으면 대체 사슬에
# 옛것과 새것의 구분이 없어지고 suspect 유도가 끝나지 않는다. 같은 plane 검사는 defs/kb.bzl 이 분석 시점에 한다.
# 결과 행 하나 = 위반 하나. 첫 실행(2026-09-26, supersedes 135): 0.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT DISTINCT ?chunk WHERE {
  ?chunk agt:supersedes+ ?chunk .
}
```
<!-- 인용 끝 -->
