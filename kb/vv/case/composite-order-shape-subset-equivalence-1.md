---
id: https://agentic-knowledge-base.dev/id/chunk/56922cd2-8ad3-5608-8ca0-fb31a38a2af7
type: schema
level: concrete
title_ko: itemContent가 hasDirectPart 밖인 co:List가 순서 shape의 둘째 sh:sparql로 거부되고 정합한 co:List는 통과한다
title: A co:List whose itemContent lies outside hasDirectPart is rejected by the order shape's second sh:sparql, and a consistent co:List passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02]
verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ab0a4767-66e3-571f-8004-46c538f04234]
---
**케이스** — itemContent가 직접 부분 밖인 자극 하나와 정합한 통제 하나로 shape의 둘째 `sh:sparql`(부분 집합 일치)을 돌린다.

**자극** — 임시 파일 둘이다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙은 만족시키고 어기는 것은 부분 집합 규칙 하나뿐이다.

```yaml
files:
  vv-order-outside.ttl: |
    @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    id:vv-order-outside a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-outside-p1 , id:vv-order-outside-p2 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p1 ] , [ co:index "2"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p3 ] .
    id:vv-order-outside-p1 a agt:Chunk .
    id:vv-order-outside-p2 a agt:Chunk .
    id:vv-order-outside-p3 a agt:Chunk .
  vv-order-control.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-control a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-control-p1 , id:vv-order-control-p2 , id:vv-order-control-p3 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p1 ] , [ co:index \"2\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p2 ] , [ co:index \"3\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p3 ] .\nid:vv-order-control-p1 a agt:Chunk .\nid:vv-order-control-p2 a agt:Chunk .\nid:vv-order-control-p3 a agt:Chunk .\n"
```

**기대** — itemContent 이탈 자극은 둘째 `sh:sparql`(부분 집합 일치) 하나로 종료 코드 1이다. 통제는 종료 코드 0이다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [shacl]"
      - "순서 항목이 가리키는 것이 이 복합체의 직접 부분이 아니다"
      - "FAIL [validate] — 1건"
  - exit: 0
```

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-outside.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-control.ttl}}`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `composite-order-shape-subset`. 값은 `item_target=outside-parts`이고 판정 부류는 `accept`(keep 안)다.
