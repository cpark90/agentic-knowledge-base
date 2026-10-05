---
id: https://agentic-knowledge-base.dev/id/chunk/ca72384d-b350-55b7-a940-56236c261fdd
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 색인 구멍과 중복을 가진 순서 있는 복합체의 검증
title: Logical scenario stimulus — validating ordered composites carrying an index gap and a duplicate index
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ef62777d-3412-55e0-8cdb-e6b05f3b630b
composite: {id: https://agentic-knowledge-base.dev/id/composite/ef62777d-3412-55e0-8cdb-e6b05f3b630b, title_ko: 색인 구멍과 중복을 가진 순서 있는 복합체의 검증, title: Validating ordered composites carrying an index gap and a duplicate index, ordered: [https://agentic-knowledge-base.dev/id/chunk/ca72384d-b350-55b7-a940-56236c261fdd, https://agentic-knowledge-base.dev/id/chunk/b4f9eed2-8ae3-5e5d-a4c1-c281292c2246, https://agentic-knowledge-base.dev/id/chunk/0c458191-3f66-59fb-9e40-7ee8d6f79041]}
---
**자극** — actor는 복합체를 저작하는 에이전트이고 action은 색인이 1..n 연속이 아닌 `co:List` 둘을 순서 shape로 검사하는 것이다. 순서는 임시 그래프 저작 → 자극마다 `validate` 실행이다. `keep()`은 부분 수·dangling 규칙을 만족시키는 나머지 개체다. 변수는 색인 결함 `index_defect` 하나이고 ODD 속성 `id:cond-repo-layout`(저장소 구조)에 매인다. keep은 구멍과 중복을 한 케이스에 담는 값 하나다.

```yaml
keep:
  index_defect: {odd: "id:cond-repo-layout", values: ["gap-and-duplicate"]}
cover:
  - {rule: equivalence, vars: [index_defect]}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02
  verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
  title_ko: "색인 구멍·중복이 순서 shape의 첫 sh:sparql로 거부된다"
  title: "An index gap and a duplicate index are each rejected by the order shape's first sh:sparql"
  summary: "색인 구멍(1,3)·색인 중복(1,1) 둘로 shape의 첫 `sh:sparql`(색인 정합)을 돌린다."
  stimulus: "임시 파일 둘이다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙은 만족시키고 어기는 것은 색인 규칙 하나뿐이다."
  files:
    vv-order-gap.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
      id:vv-order-gap a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-gap-p1 , id:vv-order-gap-p2 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p1 ] , [ co:index "3"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p2 ] .
      id:vv-order-gap-p1 a agt:Chunk .
      id:vv-order-gap-p2 a agt:Chunk .
    vv-order-dup.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
      id:vv-order-dup a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-dup-p1 , id:vv-order-dup-p2 ; co:item [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p1 ] , [ co:index "1"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p2 ] .
      id:vv-order-dup-p1 a agt:Chunk .
      id:vv-order-dup-p2 a agt:Chunk .
  command: "python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-gap.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-dup.ttl}}"
  accept:
    prose: "구멍·중복 자극 둘 모두 첫 `sh:sparql`(색인 정합) 하나로 종료 코드 1이다."
    expect:
      - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속", "FAIL [validate] — 1건"]}
      - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속", "FAIL [validate] — 1건"]}
```
