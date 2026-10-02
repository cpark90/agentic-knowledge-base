---
id: https://agentic-knowledge-base.dev/id/chunk/4d76d4b0-24d7-42e8-9928-c6c4cd092831
type: schema
level: concrete
title_ko: itemContent가 hasDirectPart 밖인 co:List가 순서 shape의 둘째 sh:sparql로 거부되고 정합한 co:List는 통과한다
title: A co:List whose itemContent lies outside hasDirectPart is rejected by the order shape's second sh:sparql, and a consistent co:List passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T20:30:00+09:00}
specializationOf: https://agentic-knowledge-base.dev/id/chunk/34d4c769-f5ee-4412-ba43-94d915cea156
---
**케이스** — itemContent가 직접 부분 밖인 자극 하나와 정합한 통제 하나로 shape의 둘째 `sh:sparql`(부분 집합 일치)을 돌린다. 첫 `sh:sparql`(색인 정합)은 원 청크 `id:chunk/34d4c769-f5ee-4412-ba43-94d915cea156`(`composite-order-shape`)가 맡는다 — 사슬(`refines`·`verifies`)도 그 청크에 있다. 이 조각은 `specializationOf`로 거기를 가리킨다(p10-split-keeps-work-identity).

**자극** — 임시 파일 둘. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙(부분 수·라벨 없는 최소 개체의 vocab·dangling)은 만족시키고 어기는 것은 부분 집합 규칙 하나뿐이다.

```yaml
files:
  vv-order-outside.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-outside a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-outside-p1 , id:vv-order-outside-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p1 ] , [ co:index \"2\"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p3 ] .\nid:vv-order-outside-p1 a agt:Chunk .\nid:vv-order-outside-p2 a agt:Chunk .\nid:vv-order-outside-p3 a agt:Chunk .\n"
  vv-order-control.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-control a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-control-p1 , id:vv-order-control-p2 , id:vv-order-control-p3 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p1 ] , [ co:index \"2\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p2 ] , [ co:index \"3\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p3 ] .\nid:vv-order-control-p1 a agt:Chunk .\nid:vv-order-control-p2 a agt:Chunk .\nid:vv-order-control-p3 a agt:Chunk .\n"
expect:
  - {exit: 1, contains: ["FAIL [shacl]", "순서 항목이 가리키는 것이 이 복합체의 직접 부분이 아니다", "FAIL [validate] — 1건"]}
  - {exit: 0}
```

**기대** — itemContent 이탈 자극은 둘째 `sh:sparql`(부분 집합 일치) 하나로 종료 코드 1이다. 통제는 종료 코드 0이다.

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-outside.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-control.ttl}}`

**표본 근거** — itemContent 이탈은 둘째 `sh:sparql`(부분 집합 일치)만 건드린다. 최소성은 실험으로 확인했다 — 자극의 어긴 트리플만 빼면 같은 명령이 종료 0이다(2026-09-29 실측). `--ontology`에 `plane-substance-ontology.ttl`을 더한 것은 `element-drop`(b) 대조를 대칭차 공집합으로 두어 자극의 결과를 가리지 않게 한다(2026-10-01 실측). 통제 자극은 원 청크의 통제와 같은 내용이다 — 복제는 안전율로 용인한다(rules.md §1).
