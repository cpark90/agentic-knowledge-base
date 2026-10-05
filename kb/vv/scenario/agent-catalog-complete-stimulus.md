---
id: https://agentic-knowledge-base.dev/id/chunk/fb74eba0-91b3-5fba-816c-011a4f37ca11
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 대응 스코프 없는 역할 하나를 가진 하네스의 검증
title: Logical scenario stimulus — validating a harness holding one role without its matching scope
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:54:21+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/3d83dc02-81cc-4d4f-98bb-fc4ffa44840a]
restored: [https://agentic-knowledge-base.dev/id/chunk/3d83dc02-81cc-4d4f-98bb-fc4ffa44840a]
part_of: https://agentic-knowledge-base.dev/id/composite/4ee07222-bd78-5edf-a40f-de853056fa4d
composite: {id: https://agentic-knowledge-base.dev/id/composite/4ee07222-bd78-5edf-a40f-de853056fa4d, title_ko: 대응 스코프 없는 역할 하나를 가진 하네스의 검증, title: Validating a harness holding one role without its matching scope, ordered: [https://agentic-knowledge-base.dev/id/chunk/fb74eba0-91b3-5fba-816c-011a4f37ca11, https://agentic-knowledge-base.dev/id/chunk/07a91c11-d4bb-50b8-bb7a-fed3f2b0ddfd, https://agentic-knowledge-base.dev/id/chunk/5213e007-142d-5440-b854-1444da04bd07]}
---
**자극** — actor는 카탈로그를 저작하는 에이전트이고 action은 커밋된 그래프 전체에 역할 하나를 가진 하네스를 더해 카탈로그 완전성 검사를 도는 것이다. 순서는 임시 하네스 저작 → `validate` 실행 → `//kg:gate_test` 실행이다. `keep()`은 한영 라벨·`agt:reads`·`agt:executionMode`·`agt:maxConcurrent`를 갖춘 역할이다. 변수는 역할에서 빠진 요소 `missing` 하나이고 ODD 속성 `id:cond-repo-layout`(저장소 구조 — 카탈로그는 `kg/catalog-kg.ttl`이다)에 매인다. keep은 `none`이고 keep 밖 값은 `scope`다.

```yaml
keep:
  missing: {odd: "id:cond-repo-layout", values: ["none"], reject: ["scope"]}
cover:
  - {rule: factor, var: missing, factors: {"agt:roleSpecificationViolation": scope}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/081e9e28-c736-49bc-84ea-6d41f0a1c44a
  verifies: [https://agentic-knowledge-base.dev/id/chunk/18537e8d-b957-4704-add4-639d90f323e5, https://agentic-knowledge-base.dev/id/chunk/acd3f19b-bb9e-448f-acf3-ac227733c8ab]
  title_ko: "대응 스코프 없는 역할 하나를 가진 하네스가 FAIL [catalog]로 거부되고 커밋된 카탈로그는 gate_test를 통과한다"
  title: "A harness holding one role without its matching scope is refused with FAIL [catalog] while the committed catalog passes gate_test"
  summary: "카탈로그 완전성 하나만을 어기는 하네스(빠진 요소 `${missing}`)와 커밋된 카탈로그 전체를 자극으로 쓴다."
  stimulus: "임시 파일 하나다. 이름은 `vv-catalog-kg.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 역할은 나머지 세 갈래와 shape를 만족시키고 어기는 것은 대응 스코프의 부재 하나뿐이다."
  files:
    vv-catalog-kg.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix id:  <https://agentic-knowledge-base.dev/id/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\nid:h-vv-catalog-sample a agt:Harness ;\n    rdfs:label \"catalog sample harness\"@en ; rdfs:label \"카탈로그 표본 하네스\"@ko ;\n    agt:hasRole id:role-vv-catalog-sample .\nid:role-vv-catalog-sample a agt:Role ;\n    rdfs:label \"catalog sample role\"@en ; rdfs:label \"카탈로그 표본 역할\"@ko ;\n    agt:reads agt:DecisionChunk ;\n    agt:executionMode agt:dispatch ;\n    agt:maxConcurrent 0 ."
  command: "bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-catalog-kg.ttl}} --waivers docs/waivers.md; bazel test //kg:gate_test"
  reject:
    prose: "그래프 두 개가 먼저 생성되고 음성 명령은 `FAIL [catalog]`와 없는 스코프의 이름을 내며 거부는 그 하나이고 종료 코드가 1이다. 양성 실행 `//kg:gate_test`는 PASS다."
    expect:
      - {exit: 0}
      - {exit: 1, contains: ["FAIL [catalog]", "역할 id:role-vv-catalog-sample 에 대응 스코프 id:scope-vv-catalog-sample 가 없다", "FAIL [validate] — 1건"]}
      - {exit: 0}
```
