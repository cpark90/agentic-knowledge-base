---
id: https://agentic-knowledge-base.dev/id/chunk/9f6433f5-842d-42ab-8c1f-8a98344d143d
type: artifact
level: executable
title_ko: 질의 link-state-class-mismatch (tools/verify-queries)
title: query link-state-class-mismatch in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016, https://agentic-knowledge-base.dev/id/chunk/55535378-f5cd-4f01-a5ce-54d438529104]
---
**질의** — `tools/verify-queries/link-state-class-mismatch.rq` 다. 10줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 상태와 클래스 불일치 — linkState 가 candidate 인데 agt:ConfirmedLink 이거나 confirmed 인데 agt:CandidateLink 다
# (link-ontology: CandidateLink·ConfirmedLink 는 linkState 의 클래스 표현, 9.4절). 후보 개체가 확정으로 오인되는 것을 막는다
# (p10-extracted-references-are-candidates). 결과 행 하나 = 위반 하나 (링크, 상태). 첫 실행(2026-09-19, 확정 577 · 후보 cites): 0.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT ?link ?state WHERE {
  ?link a agt:Link ; agt:linkState ?state .
  { ?link a agt:ConfirmedLink . FILTER(?state != "confirmed") }
  UNION
  { ?link a agt:CandidateLink . FILTER(?state != "candidate") }
}
```
<!-- 인용 끝 -->
