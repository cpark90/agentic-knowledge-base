---
id: https://agentic-knowledge-base.dev/id/chunk/dcefca6d-9de7-40d2-b9c3-25de51743e47
type: schema
level: concrete
title_ko: 자기 참조 hasDirectPart 하나가 복합체 비순환 질의로 거부되고 위반을 뺀 그래프는 gate_test를 통과한다
title: A self-referencing hasDirectPart is rejected by the composite acyclicity query, and the graph without it passes gate_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T20:40:00+09:00}
specializationOf: https://agentic-knowledge-base.dev/id/chunk/66c029ba-ccd2-433b-bcab-5727b26fff9f
---
**케이스** — composite 비순환 공리를 자기 참조 트리플 하나로 어기는 임시 그래프를 자극으로 쓴다. refines 비반사는 원 청크 `id:chunk/66c029ba-ccd2-433b-bcab-5727b26fff9f`(`acyclic-relation-axioms`)가 맡는다 — 사슬(`refines`·`verifies`)도 그 청크에 있다. 이 조각은 `specializationOf`로 거기를 가리킨다(p10-split-keeps-work-identity).

**자극** — 임시 파일 하나다. 경로는 검증기가 정한다. 커밋하지 않는다. 개체는 shape를 만족시키고 어기는 것은 자기 자신을 가리키는 링크 하나뿐이다.

```yaml
files:
  vv-composite-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> . @prefix id: <https://agentic-knowledge-base.dev/id/> .\nid:composite-vv-cycle-sample a agt:Composite ; agt:hasDirectPart id:composite-vv-cycle-sample .\n"
expect:
  - exit: 0
  - exit: 1
    contains: ["FAIL [verify] tools/verify-queries/composite-cycle.rq"]
  - exit: 0
```

**기대** — 그래프가 먼저 생성된다. 음성 명령은 질의 이름 `composite-cycle.rq`를 내고 종료 코드 1이다. 양성 `//kg:gate_test`는 PASS다.

**실행 명령** — `bazel build //kg:chunks_kg //kb/odd:odd; python3 tools/validate.py --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --verify-queries tools/verify-queries --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl {{vv-composite-cycle.ttl}}; bazel test //kg:gate_test`

**표본 근거** — 자극은 composite 비순환 공리만 건드린다. 개체는 나머지 규칙(shape·출처·쓰기 권한)을 만족시켜 어기는 것이 자기 참조 트리플 하나뿐이다. 최소성은 실험으로 확인했다 — 자기 참조만 빼거나 다른 기존 노드로 돌리면 같은 명령이 종료 0이다(2026-09-26). 음성 명령의 기대에서 `FAIL [validate] — N건`을 빼는 까닭은 데이터가 커밋된 그래프 전체(`kg/*-kg.ttl` 포함)라 이 자극과 무관한 기존 위반이 섞일 수 있어서다 — 기대는 이 자극이 내는 특정 질의 이름만 본다. 자극 셋을 한 파일에 담던 원 케이스는 본문 토큰 상한을 초과해 셋으로 나눴다(2026-10-01).
