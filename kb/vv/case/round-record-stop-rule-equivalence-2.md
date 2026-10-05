---
id: https://agentic-knowledge-base.dev/id/chunk/46ac80de-c7f6-5a67-a1f9-14e5b550dbff
type: schema
level: concrete
title_ko: 신규 결함이 1·1로 줄지 않은 뒤 라운드 3을 roundEndedByCompletion 로 닫은 기록을 verify 질의로 판정한다
title: Judging with the verify queries a record that closes round 3 by roundEndedByCompletion after new defects of 1 and 1
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:16:12+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333]
verifies: [https://agentic-knowledge-base.dev/id/chunk/a7816e3d-024c-488d-9054-075440f4cb8b]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/482e5340-b183-5f66-adea-4ccf1931b159]
---
**케이스** — 라운드 기록 셋과 판정 주석 둘의 그래프가 자극이다.

**자극** — 임시 파일 하나이고 경로는 검증기가 정한다. 라운드 기록은 종료 사유 하나를 `agt:usesConcept` 로 인용한다.

```yaml
files:
  vv-rounds.ttl: "@prefix a: <https://agentic-knowledge-base.dev/agt/> . @prefix i: <https://agentic-knowledge-base.dev/id/> . @prefix p: <http://www.w3.org/ns/prov#> . @prefix x: <http://www.w3.org/2001/XMLSchema#> .\ni:vv-d1 a a:AnnotationChunk ; a:generatedBy \"vnv/c\" ; a:status \"draft\" ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime \"2026-01-01T01:00:00Z\"^^x:dateTime .\ni:vv-d2 a a:AnnotationChunk ; a:generatedBy \"vnv/c\" ; a:status \"draft\" ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime \"2026-01-01T03:00:00Z\"^^x:dateTime .\ni:vv-r1 a a:MemoryChunk ; a:generatedBy \"process:vv_run\" ; a:usesConcept a:roundEndedByCompletion ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime \"2026-01-01T02:00:00Z\"^^x:dateTime .\ni:vv-r2 a a:MemoryChunk ; a:generatedBy \"process:vv_run\" ; a:usesConcept a:roundEndedByCompletion ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime \"2026-01-01T04:00:00Z\"^^x:dateTime .\ni:vv-r3 a a:MemoryChunk ; a:generatedBy \"process:vv_run\" ; a:usesConcept a:roundEndedByCompletion ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime \"2026-01-01T05:00:00Z\"^^x:dateTime .\n"
```

**기대** — 라운드 3이 정지 규칙이 아닌 사유로 닫혀 정지 규칙 질의가 행 하나를 내고 종료 1이다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [verify] tools/verify-queries/round-stop-rule-violated.rq"
      - "FAIL [validate] — 1건"
```

**실행 명령** — `python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --verify-queries tools/verify-queries --data {{vv-rounds.ttl}}`

**표본 근거** — `sampling:equivalence` · `sampling:factor` · seed `1` · 시나리오 `round-record-stop-rule` · 요인 `agt:unknownStopCondition`. 값은 `reason=roundEndedByCompletion`이고 판정 부류는 `reject`(keep 밖)다.
