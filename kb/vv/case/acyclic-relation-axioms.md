---
id: https://agentic-knowledge-base.dev/id/chunk/66c029ba-ccd2-433b-bcab-5727b26fff9f
type: schema
level: concrete
title_ko: 자기 참조 refines·supersedes·hasDirectPart 각각이 대응 질의 하나로만 거부되고 위반을 뺀 그래프는 gate_test를 통과한다
title: Self-referencing refines, supersedes and hasDirectPart are each rejected by exactly one query, and the graph without the violation passes gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-26T00:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b2b7a878-a500-4352-976a-e7cdd6ca1d8b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/0ea16a47-6e97-451e-bc6a-93c9154824d6]
---
**케이스** — 성질 공리 셋(refines 비반사·supersedes 이행·composite 비순환)을 자기 참조 트리플 하나씩으로 어기는 임시 그래프 셋과 커밋된 그래프 전체를 자극으로 쓴다.

**자극** — 임시 파일 셋. 경로는 검증기가 정한다. 커밋하지 않는다. 개체마다 shape를 만족시키고 어기는 것은 자기 자신을 가리키는 링크 하나뿐이다.

```yaml
files:
  vv-refines-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . @prefix prov: <http://www.w3.org/ns/prov#> .\nid:chunk-vv-refines-cycle-sample a agt:ArtifactChunk , agt:FunctionArtifact ; rdfs:label \"refines cycle sample\"@en ; rdfs:label \"refines 순환 표본\"@ko ; agt:hasLevel agt:concrete ; agt:lineCount 1 ; agt:status \"draft\" ; agt:generatedBy \"vnv/claude-sonnet-5\" ; agt:assertionLocation \"kb/vv/case/vv-refines-cycle-sample.md\" ; prov:wasDerivedFrom id:doc-system-notes ; agt:refines id:chunk-vv-refines-cycle-sample .\n"
  vv-supersedes-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . @prefix prov: <http://www.w3.org/ns/prov#> .\nid:chunk-vv-supersedes-cycle-sample a agt:ArtifactChunk , agt:FunctionArtifact ; rdfs:label \"supersedes cycle sample\"@en ; rdfs:label \"supersedes 순환 표본\"@ko ; agt:hasLevel agt:concrete ; agt:lineCount 1 ; agt:status \"draft\" ; agt:generatedBy \"vnv/claude-sonnet-5\" ; agt:assertionLocation \"kb/vv/case/vv-supersedes-cycle-sample.md\" ; prov:wasDerivedFrom id:doc-system-notes ; agt:supersedes id:chunk-vv-supersedes-cycle-sample .\n"
  vv-composite-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> .\nid:composite-vv-cycle-sample a agt:Composite ; agt:hasDirectPart id:composite-vv-cycle-sample .\n"
expect:
  - exit: 0
  - exit: 1
    contains: ["FAIL [verify] tools/verify-queries/refines-cycle.rq", "FAIL [validate] — 1건"]
  - exit: 1
    contains: ["FAIL [verify] tools/verify-queries/supersedes-cycle.rq", "FAIL [validate] — 1건"]
  - exit: 1
    contains: ["FAIL [verify] tools/verify-queries/composite-cycle.rq", "FAIL [validate] — 1건"]
  - exit: 0
```

**기대** — 그래프 두 개가 먼저 생성된다. 세 음성 명령은 각자 하나의 질의 이름과 `FAIL [validate] — 1건`을 내고 종료 코드 1이다. 양성 `//kg:gate_test`는 PASS다.

**실행 명령** — `bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-refines-cycle.ttl}}; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-supersedes-cycle.ttl}}; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-composite-cycle.ttl}}; bazel test //kg:gate_test`

**표본 근거** — 세 자극은 서로 다른 공리를 검사하므로 하나로 줄이지 않는다. 각 개체는 나머지 규칙(shape·출처·쓰기 권한)을 만족시켜 어기는 것이 자기 참조 트리플 하나뿐이다. 최소성은 실험으로 확인했다 — 자기 참조만 빼거나 다른 기존 노드로 돌리면 같은 명령이 종료 0이다(2026-09-26).
