---
id: https://agentic-knowledge-base.dev/id/chunk/ac713f19-e6d1-57c6-8be7-67acfab19db6
type: schema
level: concrete
title_ko: 색인 구멍·중복이 순서 shape의 첫 sh:sparql로 거부된다
title: An index gap and a duplicate index are each rejected by the order shape's first sh:sparql
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02]
verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ca72384d-b350-55b7-a940-56236c261fdd]
---
**케이스** — 색인 구멍(1,3)·색인 중복(1,1) 둘로 shape의 첫 `sh:sparql`(색인 정합)을 돌린다.

**자극** — 임시 파일 둘이다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙은 만족시키고 어기는 것은 색인 규칙 하나뿐이다.

```yaml
files:
  vv-order-gap.ttl: |
    @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    id:vv-order-gap a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-gap-p1 , id:vv-order-gap-p2 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p1 ] , [ co:index "3"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p2 ] .
    id:vv-order-gap-p1 a agt:Chunk .
    id:vv-order-gap-p2 a agt:Chunk .
  vv-order-dup.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-dup a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-dup-p1 , id:vv-order-dup-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p1 ] , [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p2 ] .\nid:vv-order-dup-p1 a agt:Chunk .\nid:vv-order-dup-p2 a agt:Chunk .\n"
```

**기대** — 구멍·중복 자극 둘 모두 첫 `sh:sparql`(색인 정합) 하나로 종료 코드 1이다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [shacl]"
      - "순서 색인이 1..n 연속"
      - "FAIL [validate] — 1건"
  - exit: 1
    contains:
      - "FAIL [shacl]"
      - "순서 색인이 1..n 연속"
      - "FAIL [validate] — 1건"
```

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-gap.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-dup.ttl}}`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `composite-order-shape`. 값은 `index_defect=gap-and-duplicate`이고 판정 부류는 `accept`(keep 안)다.
