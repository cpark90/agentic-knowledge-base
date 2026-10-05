---
id: https://agentic-knowledge-base.dev/id/chunk/39eef88f-75b6-50ec-9f75-d6e35d9ae77a
type: schema
level: concrete
title_ko: 자기 참조 refines 하나가 비반사 질의로 거부되고 위반을 뺀 그래프는 gate_test를 통과한다
title: A self-referencing refines is rejected by the irreflexivity query, and the graph without it passes gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:35:51+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b2b7a878-a500-4352-976a-e7cdd6ca1d8b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/0ea16a47-6e97-451e-bc6a-93c9154824d6]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/b17f109e-e309-5a1d-9b80-e909e85b1294]
---
**케이스** — `refines` 비반사 공리를 자기 참조 트리플 하나로 어기는 임시 그래프를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape를 만족시키고 어기는 것은 자기 자신을 가리키는 링크 하나뿐이다.

```yaml
files:
  vv-refines-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . @prefix prov: <http://www.w3.org/ns/prov#> .\nid:chunk-vv-refines-cycle-sample a agt:ArtifactChunk , agt:FunctionArtifact ; rdfs:label \"refines cycle sample\"@en ; rdfs:label \"refines 순환 표본\"@ko ; agt:hasLevel agt:concrete ; agt:tokenCount 1 ; agt:status \"draft\" ; agt:generatedBy \"vnv/claude-sonnet-5\" ; agt:assertionLocation \"kb/vv/case/vv-refines-cycle-sample.md\" ; prov:wasDerivedFrom id:doc-system-notes ; agt:refines id:chunk-vv-refines-cycle-sample .\n"
```

**기대** — 그래프가 먼저 생성된다. 음성 명령은 질의 이름 `refines-cycle.rq`를 내고 종료 코드 1이다. 양성 `//kg:gate_test`는 PASS다.

```yaml
expect:
  - exit: 0
  - exit: 1
    contains:
      - "FAIL [verify] tools/verify-queries/refines-cycle.rq"
  - exit: 0
```

**실행 명령** — `bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-refines-cycle.ttl}}; bazel test //kg:gate_test`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `acyclic-relation-axioms`. 값은 `relation=refines`이고 판정 부류는 `accept`(keep 안)다.
