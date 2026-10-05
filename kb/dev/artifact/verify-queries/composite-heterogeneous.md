---
id: https://agentic-knowledge-base.dev/id/chunk/a2e8caea-4359-4d47-b6a5-ece7bbe10a54
type: artifact
level: executable
title_ko: 질의 composite-heterogeneous (tools/verify-queries)
title: query composite-heterogeneous in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/composite-heterogeneous.rq` 다. 27줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 이질 복합체 — 부분들의 plane 이 서로 다르거나, 결정 밖 복합체의 부분 수준이 서로 다르다 (노트 4.5절 동질성, rules §2)
# 결과 행 하나 = 위반 하나 (복합체, 부분, 다른 부분). plane 은 부분의 agt:Chunk 하위 클래스로 본다.
# 수준 검사는 결정 복합체(부분이 agt:DecisionChunk)를 뺀다 — 결론 concrete·근거/대안 logical 이 설계다
# (p7-decision-spans-three-levels, 유저 결정 2026-09-10 Q1(a)); 그 세 부분의 수준 허용은 kb_decision 이 분석 시점에 본다.
# 예외를 결정 복합체로 **한정한 채 둔다**(2026-09-29, 결정 밖 복합체 반영). 근거는 둘이다. 첫째, 수준을 섞는 설계는
# 결정 하나뿐이다 — kb_decision 만 부분마다 수준을 받고(part_levels), 결정 밖 복합체의 규칙 kb_composite 는 묶음 전체에
# plane·level 을 한 쌍만 받으므로 이질 복합체를 만들 수 없다. 둘째, 생성 시점에도 tools/gen_build.py 의 _check_bundle 이
# 부분들의 frontmatter 가 그 한 쌍에 일치할 때만 규칙을 생성한다. 그래서 일반 복합체의 동질성은 구조로 보장되고 이 질의가
# 남아서 판정하는 것은 손으로 쓴 복합체(kg/composite-kg.ttl)와 생성 경로 밖의 트리플이다. 예외가 부분의 클래스
# (agt:DecisionChunk)로 걸리므로 decision plane 의 일반 복합체는 수준 검사를 비껴간다 — 그 자리를 _check_bundle 이 메운다.
# 첫 실행(2026-09-13, 복합체 230): 수준까지 전부에 걸면 결정 복합체 188/188 이 걸려 규칙을 의심했고 범위를 좁혔다
# (p6-mass-fail-suspects-the-rule). plane 이질 0 · 결정 밖 수준 이질 0 (손으로 쓴 복합체 42 포함).
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?composite ?part ?other WHERE {
  ?composite a agt:Composite ; agt:hasDirectPart ?part , ?other .
  FILTER(STR(?part) < STR(?other))
  {
    ?part a ?c1 . ?other a ?c2 .
    ?c1 rdfs:subClassOf agt:Chunk . ?c2 rdfs:subClassOf agt:Chunk .
    FILTER(?c1 != ?c2)
  } UNION {
    ?part agt:hasLevel ?l1 . ?other agt:hasLevel ?l2 .
    FILTER(?l1 != ?l2)
    FILTER NOT EXISTS { ?part a agt:DecisionChunk }
  }
}
```
<!-- 인용 끝 -->
