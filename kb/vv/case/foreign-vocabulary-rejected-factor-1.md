---
id: https://agentic-knowledge-base.dev/id/chunk/90e003d5-92eb-5220-b85d-cdb05fc96ece
type: schema
level: concrete
title_ko: 미정의 술어 agt:unknownPredicate를 담은 임시 그래프가 FAIL [vocab]로 거부되고 커밋된 그래프는 gate_test를 통과한다
title: A temporary graph carrying the undefined predicate agt:unknownPredicate is rejected as FAIL [vocab] and committed graphs pass gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:54:21+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f2618270-3e11-40c7-b5d0-36c828923ff0]
verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f693dd9b-a550-5b20-b56c-a59628b0552d]
---
**케이스** — 온톨로지 밖 술어 하나만을 어기는 데이터 그래프와 커밋된 그래프 전체를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 이름은 `vv-vocab-kg.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape와 writer 검사를 만족시키고 어기는 것은 미정의 술어 한 줄뿐이다.

```yaml
files:
  vv-vocab-kg.ttl: |-
    @prefix agt: <https://agentic-knowledge-base.dev/agt/> .
    @prefix id:  <https://agentic-knowledge-base.dev/id/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    id:chunk-vv-vocab-sample a agt:ContractChunk , agt:InterfaceSignature ;
        rdfs:label "vocabulary sample"@en ; rdfs:label "어휘 표본"@ko ;
        agt:hasLevel agt:logical ; agt:tokenCount 1 ; agt:status "draft" ;
        agt:bodySlot "합격 기준" ; agt:bodySlot "판정식" ; agt:bodySlot "등급" ;
        agt:generatedBy "vnv/claude-opus-5" ; agt:assertionLocation "kb/vv/criteria/vv-vocab-sample.md" ;
        agt:unknownPredicate "x" .
```

**기대** — 출력에 `FAIL [vocab]`와 미정의 술어의 IRI가 있고 종료 코드가 1이다. 양성 실행 `//kg:gate_test`는 PASS다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [vocab]"
      - "온톨로지에 정의되지 않은 agt: 술어 https://agentic-knowledge-base.dev/agt/unknownPredicate"
  - exit: 0
```

**실행 명령** — `python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-vocab-kg.ttl}}; bazel test //kg:gate_test`

**표본 근거** — `sampling:factor` · seed `1` · 시나리오 `foreign-vocabulary-rejected` · 요인 `agt:outOfVocabularyPredicate`. 값은 `predicate=unknownPredicate`이고 판정 부류는 `reject`(keep 밖)다.
