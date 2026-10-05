---
id: https://agentic-knowledge-base.dev/id/chunk/f2362b25-fce0-54e1-94ae-a453b7178fe9
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 자기 참조 supersedes 하나를 더한 그래프의 검증
title: Logical scenario stimulus — validating a graph with one self-referencing supersedes added
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4eb68c72-d1c3-51c4-8bdf-22980bbad1a7
composite: {id: https://agentic-knowledge-base.dev/id/composite/4eb68c72-d1c3-51c4-8bdf-22980bbad1a7, title_ko: 자기 참조 supersedes 하나를 더한 그래프의 검증, title: Validating a graph with one self-referencing supersedes added, ordered: [https://agentic-knowledge-base.dev/id/chunk/f2362b25-fce0-54e1-94ae-a453b7178fe9, https://agentic-knowledge-base.dev/id/chunk/31504c97-ea87-5ab7-927a-ce70abf4a4d9, https://agentic-knowledge-base.dev/id/chunk/24aea9bf-bdc2-5076-baaf-213f5acda2a0]}
---
**자극** — actor는 그래프를 저작하는 에이전트이고 action은 커밋된 그래프 전체에 자기 자신을 가리키는 대체 링크 트리플 하나를 담은 임시 그래프를 더해 verify 질의를 도는 것이다. 순서는 임시 그래프 저작 → `validate` 실행 → `//kg:gate_test` 실행이다. `keep()`은 shape·출처·쓰기 권한을 만족시키는 나머지 개체다. 변수는 링크 종류 `relation` 하나이고 ODD 속성 `id:cond-repo-layout`(저장소 구조)에 매인다. keep은 값 `supersedes` 하나다.

```yaml
keep:
  relation: {odd: "id:cond-repo-layout", values: ["supersedes"]}
cover:
  - {rule: equivalence, vars: [relation]}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/b2b7a878-a500-4352-976a-e7cdd6ca1d8b
  verifies: [https://agentic-knowledge-base.dev/id/chunk/0ea16a47-6e97-451e-bc6a-93c9154824d6]
  title_ko: "자기 참조 ${relation} 하나가 이행 질의로 거부되고 위반을 뺀 그래프는 gate_test를 통과한다"
  title: "A self-referencing ${relation} is rejected by the transitivity query, and the graph without it passes gate_test"
  summary: "`${relation}` 이행 공리를 자기 참조 트리플 하나로 어기는 임시 그래프를 자극으로 쓴다."
  stimulus: "임시 파일 하나다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape를 만족시키고 어기는 것은 자기 자신을 가리키는 링크 하나뿐이다."
  files:
    vv-${relation}-cycle.ttl: |
      @prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . @prefix prov: <http://www.w3.org/ns/prov#> .
      id:chunk-vv-${relation}-cycle-sample a agt:ArtifactChunk , agt:FunctionArtifact ; rdfs:label "${relation} cycle sample"@en ; rdfs:label "${relation} 순환 표본"@ko ; agt:hasLevel agt:concrete ; agt:tokenCount 1 ; agt:status "draft" ; agt:generatedBy "vnv/claude-sonnet-5" ; agt:assertionLocation "kb/vv/case/vv-${relation}-cycle-sample.md" ; prov:wasDerivedFrom id:doc-system-notes ; agt:${relation} id:chunk-vv-${relation}-cycle-sample .
  command: "bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-${relation}-cycle.ttl}}; bazel test //kg:gate_test"
  accept:
    prose: "그래프가 먼저 생성된다. 음성 명령은 질의 이름 `${relation}-cycle.rq`를 내고 종료 코드 1이다. 양성 `//kg:gate_test`는 PASS다."
    expect:
      - {exit: 0}
      - {exit: 1, contains: ["FAIL [verify] tools/verify-queries/${relation}-cycle.rq"]}
      - {exit: 0}
```
