---
id: https://agentic-knowledge-base.dev/id/chunk/ca541a86-fc8a-4978-b7cd-1bb106d18dcf
type: artifact
level: executable
title_ko: 질의 refines-cycle (tools/verify-queries)
title: query refines-cycle in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/refines-cycle.rq` 다. 8줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 순환 정제 — agt:refines 연쇄가 자기 자신에 닿는다 (노트 6.2절, rules §2 비순환)
# owl:IrreflexiveProperty(ladder-ontology) 의 질의 대응물이다. //kg:gate_test 는 --reason 없이 돌고 pySHACL 의
# rdfs·owlrl 추론은 비반사성 위반을 내지 않으므로(2026-09-26 실측) 공리는 선언이고 판정은 여기서 한다.
# 결과 행 하나 = 위반 하나. 첫 실행(2026-09-26, refines 479): 0 (반사 0 · 길이 2~4 순환 0).
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT DISTINCT ?chunk WHERE {
  ?chunk agt:refines+ ?chunk .
}
```
<!-- 인용 끝 -->
