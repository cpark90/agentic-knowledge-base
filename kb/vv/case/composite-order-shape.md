---
id: https://agentic-knowledge-base.dev/id/chunk/34d4c769-f5ee-4412-ba43-94d915cea156
type: schema
level: concrete
title_ko: 색인 구멍·중복·itemContent 이탈 셋이 shape 하나로 거부되고 정합한 co:List는 통과한다
title: An index gap, a duplicate index and an itemContent outside hasDirectPart are each rejected by the shape, and a consistent co:List passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T05:10:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02]
verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
---
**케이스** — 색인 구멍(1,3)·색인 중복(1,1)·itemContent가 hasDirectPart 밖인 최소 `co:List` 셋과 정합한 통제 하나로 shape를 돌린다. shape 쪽 고정물이 없어 `sh:sparql` 잠금 변경을 조용히 통과할 위험을 이 케이스가 메운다.

**자극** — 임시 파일 넷. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙(부분 수·라벨 없는 최소 개체의 vocab·dangling)은 만족시키고 어기는 것은 색인 규칙 또는 부분 집합 규칙 하나뿐이다.

```yaml
files:
  vv-order-gap.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-gap a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-gap-p1 , id:vv-order-gap-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p1 ] , [ co:index \"3\"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p2 ] .\nid:vv-order-gap-p1 a agt:Chunk .\nid:vv-order-gap-p2 a agt:Chunk .\n"
  vv-order-dup.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-dup a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-dup-p1 , id:vv-order-dup-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p1 ] , [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p2 ] .\nid:vv-order-dup-p1 a agt:Chunk .\nid:vv-order-dup-p2 a agt:Chunk .\n"
  vv-order-outside.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-outside a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-outside-p1 , id:vv-order-outside-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p1 ] , [ co:index \"2\"^^xsd:positiveInteger ; co:itemContent id:vv-order-outside-p3 ] .\nid:vv-order-outside-p1 a agt:Chunk .\nid:vv-order-outside-p2 a agt:Chunk .\nid:vv-order-outside-p3 a agt:Chunk .\n"
  vv-order-control.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-control a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-control-p1 , id:vv-order-control-p2 , id:vv-order-control-p3 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p1 ] , [ co:index \"2\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p2 ] , [ co:index \"3\"^^xsd:positiveInteger ; co:itemContent id:vv-order-control-p3 ] .\nid:vv-order-control-p1 a agt:Chunk .\nid:vv-order-control-p2 a agt:Chunk .\nid:vv-order-control-p3 a agt:Chunk .\n"
expect:
  - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속·중복 없음이 아니거나 부분 집합(agt:hasDirectPart)과 개수가 다르다", "FAIL [validate] — 1건"]}
  - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속·중복 없음이 아니거나 부분 집합(agt:hasDirectPart)과 개수가 다르다", "FAIL [validate] — 1건"]}
  - {exit: 1, contains: ["FAIL [shacl]", "순서 항목이 가리키는 것이 이 복합체의 직접 부분이 아니다", "FAIL [validate] — 1건"]}
  - {exit: 0}
```

**기대** — 구멍·중복 자극은 첫 `sh:sparql`(색인 정합) 하나로, itemContent 이탈 자극은 둘째 `sh:sparql`(부분 집합 일치)로 종료 코드 1이다. 통제는 종료 코드 0이다.

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-gap.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-dup.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-outside.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-control.ttl}}`

**표본 근거** — 구멍·중복은 첫 `sh:sparql`(n≠hi 또는 n≠items·contents·parts)만 건드리고, itemContent 이탈은 둘째 `sh:sparql`(부분 집합 일치)만 건드린다. 최소성은 실험으로 확인했다 — 자극마다 어긴 트리플만 빼면 같은 명령이 종료 0이다(2026-09-29 실측).
