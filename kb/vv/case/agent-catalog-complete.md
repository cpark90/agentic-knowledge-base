---
id: https://agentic-knowledge-base.dev/id/chunk/d7fd4d10-bf68-4374-8e15-66cd2221c822
type: schema
level: concrete
title_ko: 대응 스코프 없는 역할 하나를 가진 하네스가 FAIL [catalog] 로 거부되고 커밋된 카탈로그는 gate_test 를 통과한다
title: A harness holding one role without its matching scope is refused with FAIL [catalog] while the committed catalog passes gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-24T11:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/081e9e28-c736-49bc-84ea-6d41f0a1c44a]
verifies: [https://agentic-knowledge-base.dev/id/chunk/18537e8d-b957-4704-add4-639d90f323e5, https://agentic-knowledge-base.dev/id/chunk/acd3f19b-bb9e-448f-acf3-ac227733c8ab]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/a02a4db5-cf50-4b19-9a5e-1b101c4e0600]
restored: [https://agentic-knowledge-base.dev/id/chunk/a02a4db5-cf50-4b19-9a5e-1b101c4e0600]
---
**케이스** — 카탈로그 완전성 하나만을 어기는 하네스와 커밋된 카탈로그 전체를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 이름은 `vv-catalog-kg.ttl` 이고 경로는 검증기가 정한다. 커밋하지 않는다. 역할은 한영 라벨·`agt:reads`·`agt:executionMode`·`agt:maxConcurrent` 를 갖춰 나머지 세 갈래와 shape 를 만족시키고 어기는 것은 대응 스코프의 부재 하나뿐이다. 검사는 게이트와 같은 입력에 이 파일 하나를 `--data` 로 더해 돌린다.

```yaml
files:
  vv-catalog-kg.ttl: |
    @prefix agt: <https://agentic-knowledge-base.dev/agt/> .
    @prefix id:  <https://agentic-knowledge-base.dev/id/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    id:h-vv-catalog-sample a agt:Harness ;
        rdfs:label "catalog sample harness"@en ; rdfs:label "카탈로그 표본 하네스"@ko ;
        agt:hasRole id:role-vv-catalog-sample .
    id:role-vv-catalog-sample a agt:Role ;
        rdfs:label "catalog sample role"@en ; rdfs:label "카탈로그 표본 역할"@ko ;
        agt:reads agt:DecisionChunk ;
        agt:executionMode agt:dispatch ;
        agt:maxConcurrent 0 .
```

**기대** — 그래프 두 개가 먼저 생성되고, 음성 명령의 출력에 `FAIL [catalog]` 와 없는 스코프의 이름이 있으며 거부는 그 하나이고 종료 코드가 1 이다. 양성 실행 `//kg:gate_test` 는 PASS 다.

```yaml
expect:
  - exit: 0
  - exit: 1
    contains:
      - "FAIL [catalog]"
      - "역할 id:role-vv-catalog-sample 에 대응 스코프 id:scope-vv-catalog-sample 가 없다"
      - "FAIL [validate] — 1건"
  - exit: 0
```

**실행 명령** — `bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-catalog-kg.ttl}}; bazel test //kg:gate_test`

**표본 근거** — 이 자극이 어기는 규칙은 카탈로그 완전성 하나다. 최소성은 실험으로 확인했다 — 스코프 개체와 `agt:grants` 를 더한 같은 그래프가 같은 명령에서 종료 0 으로 PASS 다(2026-09-24). `agt:grants` 누락은 같은 규칙의 다른 절반이라 표본을 늘리지 않는다. 쓰기 plane 중복과 동시 한도 초과는 커밋된 카탈로그로는 만들 수 없는 값이라 양성 쪽 실측(중복 0 · 합 4 ≤ 5)으로만 관측한다.
