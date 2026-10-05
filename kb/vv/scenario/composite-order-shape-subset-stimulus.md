---
id: https://agentic-knowledge-base.dev/id/chunk/ab0a4767-66e3-571f-8004-46c538f04234
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 직접 부분 밖을 가리키는 순서 항목을 가진 복합체의 검증
title: Logical scenario stimulus — validating an ordered composite whose item points outside its direct parts
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/3dd16af0-6fda-5dab-930f-94602d130ec2
composite: {id: https://agentic-knowledge-base.dev/id/composite/3dd16af0-6fda-5dab-930f-94602d130ec2, title_ko: 직접 부분 밖을 가리키는 순서 항목을 가진 복합체의 검증, title: Validating an ordered composite whose item points outside its direct parts, ordered: [https://agentic-knowledge-base.dev/id/chunk/ab0a4767-66e3-571f-8004-46c538f04234, https://agentic-knowledge-base.dev/id/chunk/93cd59d3-752e-5089-90a6-24f03b464e89, https://agentic-knowledge-base.dev/id/chunk/829c7a86-50b2-59d4-a80e-9c24bae0921e]}
---
**자극** — actor는 복합체 저작자이고 action은 항목이 직접 부분 밖을 가리키는 `co:List`와 통제를 순서 shape로 검사하는 것이다. 순서는 저작 → 자극마다 `validate`다. `keep()`은 색인 정합이다. 변수 `item_target`은 ODD 속성 `id:cond-repo-layout`에 매이고 keep은 값 하나다.

```yaml
keep:
  item_target: {odd: "id:cond-repo-layout", values: ["outside-parts"]}
cover:
  - {rule: equivalence, vars: [item_target]}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02
  verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
  title_ko: "itemContent가 hasDirectPart 밖인 co:List가 순서 shape의 둘째 sh:sparql로 거부되고 정합한 co:List는 통과한다"
  title: "A co:List whose itemContent lies outside hasDirectPart is rejected by the order shape's second sh:sparql, and a consistent co:List passes"
  summary: "itemContent가 직접 부분 밖인 자극 하나와 정합한 통제 하나로 shape의 둘째 `sh:sparql`(부분 집합 일치)을 돌린다."
  stimulus: "임시 파일 둘이다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙은 만족시키고 어기는 것은 부분 집합 규칙 하나뿐이다."
  files:
    vv-order-outside.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
      id:vv-order-outside a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-outside-p1 , id:vv-order-outside-p2 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p1 ] , [ co:index "2"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p3 ] .
      id:vv-order-outside-p1 a agt:Chunk .
      id:vv-order-outside-p2 a agt:Chunk .
      id:vv-order-outside-p3 a agt:Chunk .
    vv-order-control.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
      id:vv-order-control a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-control-p1 , id:vv-order-control-p2 , id:vv-order-control-p3 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p1 ] , [ co:index "2"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p2 ] , [ co:index "3"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p3 ] .
      id:vv-order-control-p1 a agt:Chunk .
      id:vv-order-control-p2 a agt:Chunk .
      id:vv-order-control-p3 a agt:Chunk .
  command: "python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-outside.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-control.ttl}}"
  accept:
    prose: "itemContent 이탈 자극은 둘째 `sh:sparql`(부분 집합 일치) 하나로 종료 코드 1이다. 통제는 종료 코드 0이다."
    expect:
      - {exit: 1, contains: ["FAIL [shacl]", "순서 항목이 가리키는 것이 이 복합체의 직접 부분이 아니다", "FAIL [validate] — 1건"]}
      - {exit: 0}
```
