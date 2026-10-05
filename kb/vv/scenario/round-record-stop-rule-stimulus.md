---
id: https://agentic-knowledge-base.dev/id/chunk/482e5340-b183-5f66-adea-4ccf1931b159
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 신규 결함이 줄지 않은 두 라운드 뒤 셋째 라운드 기록의 정지 규칙 판정
title: Logical scenario stimulus — judging the stop rule on a third round record after two rounds whose new defects did not fall
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:16:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/90e4464e-15dc-5cdc-9105-ba97d62261a8
composite: {id: https://agentic-knowledge-base.dev/id/composite/90e4464e-15dc-5cdc-9105-ba97d62261a8, title_ko: 신규 결함이 줄지 않은 두 라운드 뒤 셋째 라운드 기록의 정지 규칙 판정, title: Judging the stop rule on a third round record after two rounds whose new defects did not fall, ordered: [https://agentic-knowledge-base.dev/id/chunk/482e5340-b183-5f66-adea-4ccf1931b159, https://agentic-knowledge-base.dev/id/chunk/de11ca60-357f-597b-a28a-b4d22359c830, https://agentic-knowledge-base.dev/id/chunk/ec96760a-2ac4-5171-b341-e40143ce058a]}
---
**자극** — actor는 라운드를 닫는 세션이고 action은 라운드 기록 셋과 판정 주석 둘을 담은 임시 그래프를 verify 질의로 판정하는 것이다. 라운드 경계는 명시 라운드 기록이고(유저 답 Q39-c) 라운드 1·2의 신규 결함은 1·1이다. 순서는 결함 → 라운드 1 → 결함 → 라운드 2 → 라운드 3이다. `keep()`은 앞 두 기록과 주석이다. 변수는 라운드 3의 종료 사유 `reason` 하나이고 ODD 속성 `id:cond-build-system`(빌드 체계)에 매인다. keep은 `roundEndedByStopRule` 이다.

```yaml
keep:
  reason: {odd: "id:cond-build-system", values: ["roundEndedByStopRule"], reject: ["roundEndedByCompletion"]}
cover:
  - {rule: equivalence, vars: [reason]}
  - {rule: factor, var: reason, factors: {"agt:unknownStopCondition": roundEndedByCompletion}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333
  verifies: [https://agentic-knowledge-base.dev/id/chunk/a7816e3d-024c-488d-9054-075440f4cb8b]
  title_ko: "신규 결함이 1·1로 줄지 않은 뒤 라운드 3을 ${reason} 로 닫은 기록을 verify 질의로 판정한다"
  title: "Judging with the verify queries a record that closes round 3 by ${reason} after new defects of 1 and 1"
  summary: "라운드 기록 셋과 판정 주석 둘의 그래프가 자극이다."
  stimulus: "임시 파일 하나이고 경로는 검증기가 정한다. 라운드 기록은 종료 사유 하나를 `agt:usesConcept` 로 인용한다."
  files:
    vv-rounds.ttl: |
      @prefix a: <https://agentic-knowledge-base.dev/agt/> . @prefix i: <https://agentic-knowledge-base.dev/id/> . @prefix p: <http://www.w3.org/ns/prov#> . @prefix x: <http://www.w3.org/2001/XMLSchema#> .
      i:vv-d1 a a:AnnotationChunk ; a:generatedBy "vnv/c" ; a:status "draft" ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime "2026-01-01T01:00:00Z"^^x:dateTime .
      i:vv-d2 a a:AnnotationChunk ; a:generatedBy "vnv/c" ; a:status "draft" ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime "2026-01-01T03:00:00Z"^^x:dateTime .
      i:vv-r1 a a:MemoryChunk ; a:generatedBy "process:vv_run" ; a:usesConcept a:roundEndedByCompletion ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime "2026-01-01T02:00:00Z"^^x:dateTime .
      i:vv-r2 a a:MemoryChunk ; a:generatedBy "process:vv_run" ; a:usesConcept a:roundEndedByCompletion ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime "2026-01-01T04:00:00Z"^^x:dateTime .
      i:vv-r3 a a:MemoryChunk ; a:generatedBy "process:vv_run" ; a:usesConcept a:${reason} ; p:wasDerivedFrom i:doc-vv-profile-hazards ; p:generatedAtTime "2026-01-01T05:00:00Z"^^x:dateTime .
  command: "python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --verify-queries tools/verify-queries --data {{vv-rounds.ttl}}"
  accept:
    prose: "라운드 3이 정지 규칙으로 닫혀 위반 행이 없고 종료 0이다."
    expect:
      - {exit: 0, contains: ["PASS [validate]"]}
  reject:
    prose: "라운드 3이 정지 규칙이 아닌 사유로 닫혀 정지 규칙 질의가 행 하나를 내고 종료 1이다."
    expect:
      - {exit: 1, contains: ["FAIL [verify] tools/verify-queries/round-stop-rule-violated.rq", "FAIL [validate] — 1건"]}
```
