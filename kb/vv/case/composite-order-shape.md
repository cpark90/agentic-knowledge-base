---
id: https://agentic-knowledge-base.dev/id/chunk/34d4c769-f5ee-4412-ba43-94d915cea156
type: schema
level: concrete
title_ko: 색인 구멍·중복이 순서 shape의 첫 sh:sparql로 거부되고 정합한 co:List는 통과한다
title: An index gap and a duplicate index are each rejected by the order shape's first sh:sparql, and a consistent co:List passes
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T20:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/a6673077-7796-4803-afe1-299d79fc4d02]
verifies: [https://agentic-knowledge-base.dev/id/chunk/b7ef890e-af82-442e-8cf4-091412f49c2e]
---
**케이스** — 색인 구멍(1,3)·색인 중복(1,1) 둘로 shape의 첫 `sh:sparql`(색인 정합)을 돌린다. 정합한 통제와 둘째 `sh:sparql`(부분 집합 일치)은 분할 조각 `id:chunk/4d76d4b0-24d7-42e8-9928-c6c4cd092831`(`composite-order-shape-subset`)이 맡는다 — 본문 토큰 상한 초과로 자극마다 나눈 분할이고, 통제 하나가 두 `sh:sparql`을 모두 만족시켜 그 조각의 양성 실행이 겸한다(p10-split-keeps-work-identity).

**자극** — 임시 파일 둘. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 나머지 규칙(부분 수·라벨 없는 최소 개체의 vocab·dangling)은 만족시키고 어기는 것은 색인 규칙 하나뿐이다.

```yaml
files:
  vv-order-gap.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-gap a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-gap-p1 , id:vv-order-gap-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p1 ] , [ co:index \"3\"^^xsd:positiveInteger ; co:itemContent id:vv-order-gap-p2 ] .\nid:vv-order-gap-p1 a agt:Chunk .\nid:vv-order-gap-p2 a agt:Chunk .\n"
  vv-order-dup.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix co: <http://purl.org/co/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\nid:vv-order-dup a agt:Composite , co:List ; agt:hasDirectPart id:vv-order-dup-p1 , id:vv-order-dup-p2 ; co:item [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p1 ] , [ co:index \"1\"^^xsd:positiveInteger ; co:itemContent id:vv-order-dup-p2 ] .\nid:vv-order-dup-p1 a agt:Chunk .\nid:vv-order-dup-p2 a agt:Chunk .\n"
expect:
  - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속", "FAIL [validate] — 1건"]}
  - {exit: 1, contains: ["FAIL [shacl]", "순서 색인이 1..n 연속", "FAIL [validate] — 1건"]}
```

**기대** — 구멍·중복 자극 둘 모두 첫 `sh:sparql`(색인 정합) 하나로 종료 코드 1이다.

**실행 명령** — `python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-gap.ttl}}; python3 tools/validate.py --ontology kb/ontology/entity/knowledge-item/property-ontology.ttl kb/ontology/profile/development/plane-substance-ontology.ttl --shapes kb/ontology/shapes/composite-order-shapes.ttl --data {{vv-order-dup.ttl}}`

**표본 근거** — 구멍·중복은 첫 `sh:sparql`만 건드린다. 최소성은 실험으로 확인했다 — 자극마다 어긴 트리플만 빼면 같은 명령이 종료 0이다(2026-09-29 실측). `--ontology`의 `plane-substance-ontology.ttl`은 `element-drop`(b) 대조를 대칭차 공집합으로 둬 자극의 결과를 가리지 않게 한다(2026-10-01 실측). 자극 넷을 한 파일에 담던 원 케이스는 본문 토큰 상한을 초과해 둘로 나눴다 — 이 조각이 uuid를 승계하고 통제·둘째 `sh:sparql`은 `composite-order-shape-subset`이 잇는다(2026-10-01).
