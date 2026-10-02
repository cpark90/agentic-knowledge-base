---
id: https://agentic-knowledge-base.dev/id/chunk/ee329895-169a-4bf2-bd1a-94dcc44345e3
type: schema
level: concrete
title_ko: 미정의 술어 agt:unknownPredicate를 담은 임시 그래프가 FAIL [vocab]로 거부되고 커밋된 그래프는 gate_test를 통과한다
title: A temporary graph carrying the undefined predicate agt:unknownPredicate is rejected as FAIL [vocab] and committed graphs pass gate_test
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T20:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f2618270-3e11-40c7-b5d0-36c828923ff0]
verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2]
restored: [https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2]
---
**케이스** — 온톨로지 밖 술어 하나만을 어기는 데이터 그래프와 커밋된 그래프 전체를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 이름은 `vv-vocab-kg.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 라벨·수준·상태·생성자·슬롯을 갖춰 shape와 writer 검사를 만족시키고 어기는 것은 미정의 술어 한 줄뿐이다. 검사는 게이트와 같은 입력(온톨로지 모듈·shape·ODD·데이터)에 이 파일 하나를 `--data`로 더해 돌린다.

```yaml
files:
  vv-vocab-kg.ttl: |
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

**기대** — 출력에 `FAIL [vocab]`와 미정의 술어의 IRI가 있고 종료 코드가 1이다. 미정의 술어 한 줄을 빼면 같은 명령이 PASS다. 양성 실행 `//kg:gate_test`는 PASS다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [vocab]"
      - "온톨로지에 정의되지 않은 agt: 술어 https://agentic-knowledge-base.dev/agt/unknownPredicate"
  - exit: 0
```

**실행 명령** — `python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-vocab-kg.ttl}}; bazel test //kg:gate_test`

**표본 근거** — 이 자극이 어기는 규칙은 하나다. `agt:` 접두어를 쓴 술어는 접두어 검사로 걸러지지 않으므로 온톨로지 정의 대조만이 잡고, 그것이 통제 어휘의 핵심 분기다. 최소성은 실험으로 확인했다 — 미정의 술어 한 줄만 뺀 같은 그래프가 같은 명령에서 종료 0 으로 PASS 이므로 종료 코드와 `contains` 문구가 같은 규칙을 가리킨다(2026-09-23, `p8-minimal-negative-stimulus`). 미등록 네임스페이스 분기는 접두어만으로 판정되어 표본을 따로 두지 않는다. 음성 명령의 기대에서 `FAIL [validate] — N건`을 빼는 까닭은 데이터가 커밋된 그래프 전체(`kg/*-kg.ttl` 포함)라 이 자극과 무관한 기존 위반이 섞일 수 있어서다 — 기대는 `FAIL [vocab]`와 그 술어 IRI만 본다. 고정물의 `agt:lineCount`는 `agt:tokenCount`로 바꿨다 — 크기의 단위가 토큰으로 바뀌어 `lineCount`는 `agt:ChunkShape`의 `tokenCount` 최소 카디널리티를 채우지 못하고 별개의 위반을 낸다(2026-10-01, p1-chunk-unit-is-tokens).
