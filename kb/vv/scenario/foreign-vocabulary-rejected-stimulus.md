---
id: https://agentic-knowledge-base.dev/id/chunk/f693dd9b-a550-5b20-b56c-a59628b0552d
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 미정의 agt 술어 하나를 담은 그래프의 검증
title: Logical scenario stimulus — validating a graph that carries one undefined agt predicate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:54:21+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f9c229ee-0c23-5dae-9cf3-62910f2054c9
composite: {id: https://agentic-knowledge-base.dev/id/composite/f9c229ee-0c23-5dae-9cf3-62910f2054c9, title_ko: 미정의 agt 술어 하나를 담은 그래프의 검증, title: Validating a graph that carries one undefined agt predicate, ordered: [https://agentic-knowledge-base.dev/id/chunk/f693dd9b-a550-5b20-b56c-a59628b0552d, https://agentic-knowledge-base.dev/id/chunk/64545f36-8857-570c-8a83-8e9286bedd20, https://agentic-knowledge-base.dev/id/chunk/deb69f00-2898-584c-9c6a-bfd7f32fa282]}
---
**자극** — actor는 그래프를 저작하는 에이전트이고 action은 커밋된 그래프 전체에 온톨로지에 없는 `agt:` 술어 한 줄을 가진 개체 하나를 더해 검증하는 것이다. 순서는 임시 그래프 저작 → `validate` 실행 → `//kg:gate_test` 실행이다. `keep()`은 라벨·수준·상태·생성자·슬롯을 갖춘 개체다. 변수는 술어의 지역 이름 `predicate` 하나이고 ODD 속성 `id:cond-repo-layout`(저장소 구조 — 어휘는 `kb/ontology/`의 모듈이다)에 매인다. keep은 정의된 술어 `bodySlot`이다.

```yaml
keep:
  predicate: {odd: "id:cond-repo-layout", values: ["bodySlot"], reject: ["unknownPredicate"]}
cover:
  - {rule: factor, var: predicate, factors: {"agt:outOfVocabularyPredicate": unknownPredicate}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/f2618270-3e11-40c7-b5d0-36c828923ff0
  verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
  title_ko: "미정의 술어 agt:${predicate}를 담은 임시 그래프가 FAIL [vocab]로 거부되고 커밋된 그래프는 gate_test를 통과한다"
  title: "A temporary graph carrying the undefined predicate agt:${predicate} is rejected as FAIL [vocab] and committed graphs pass gate_test"
  summary: "온톨로지 밖 술어 하나만을 어기는 데이터 그래프와 커밋된 그래프 전체를 자극으로 쓴다."
  stimulus: "임시 파일 하나다. 이름은 `vv-vocab-kg.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape와 writer 검사를 만족시키고 어기는 것은 미정의 술어 한 줄뿐이다."
  files:
    vv-vocab-kg.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix id:  <https://agentic-knowledge-base.dev/id/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\nid:chunk-vv-vocab-sample a agt:ContractChunk , agt:InterfaceSignature ;\n    rdfs:label \"vocabulary sample\"@en ; rdfs:label \"어휘 표본\"@ko ;\n    agt:hasLevel agt:logical ; agt:tokenCount 1 ; agt:status \"draft\" ;\n    agt:bodySlot \"합격 기준\" ; agt:bodySlot \"판정식\" ; agt:bodySlot \"등급\" ;\n    agt:generatedBy \"vnv/claude-opus-5\" ; agt:assertionLocation \"kb/vv/criteria/vv-vocab-sample.md\" ;\n    agt:${predicate} \"x\" ."
  command: "python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-vocab-kg.ttl}}; bazel test //kg:gate_test"
  reject:
    prose: "출력에 `FAIL [vocab]`와 미정의 술어의 IRI가 있고 종료 코드가 1이다. 양성 실행 `//kg:gate_test`는 PASS다."
    expect:
      - {exit: 1, contains: ["FAIL [vocab]", "온톨로지에 정의되지 않은 agt: 술어 https://agentic-knowledge-base.dev/agt/${predicate}"]}
      - {exit: 0}
```
