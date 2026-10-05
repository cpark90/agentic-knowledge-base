---
id: https://agentic-knowledge-base.dev/id/chunk/d8b9e328-92ba-5536-a7fc-c4224e8fd0e7
type: schema
level: concrete
title_ko: 자기 참조 hasDirectPart 하나가 복합체 비순환 질의로 거부되고 위반을 뺀 그래프는 gate_test를 통과한다
title: A self-referencing hasDirectPart is rejected by the composite acyclicity query, and the graph without it passes gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b2b7a878-a500-4352-976a-e7cdd6ca1d8b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/0ea16a47-6e97-451e-bc6a-93c9154824d6]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/a3b9da01-17aa-52c7-9aa5-26bd2daa02c7]
---
**케이스** — `composite` 비순환 공리를 자기 참조 트리플 하나로 어기는 임시 그래프를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape를 만족시키고 어기는 것은 자기 자신을 가리키는 링크 하나뿐이다.

```yaml
files:
  vv-composite-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> .\nid:composite-vv-cycle-sample a agt:Composite ; agt:hasDirectPart id:composite-vv-cycle-sample .\n"
```

**기대** — 그래프가 먼저 생성된다. 음성 명령은 질의 이름 `composite-cycle.rq`를 내고 종료 코드 1이다. 양성 `//kg:gate_test`는 PASS다.

```yaml
expect:
  - exit: 0
  - exit: 1
    contains:
      - "FAIL [verify] tools/verify-queries/composite-cycle.rq"
  - exit: 0
```

**실행 명령** — `bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-composite-cycle.ttl}}; bazel test //kg:gate_test`

**표본 근거** — `sampling:equivalence` · seed `1` · 시나리오 `acyclic-relation-axioms-composite`. 값은 `relation=composite`이고 판정 부류는 `accept`(keep 안)다.
