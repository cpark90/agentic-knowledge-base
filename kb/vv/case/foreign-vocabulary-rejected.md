---
id: https://agentic-knowledge-base.dev/id/chunk/ee329895-169a-4bf2-bd1a-94dcc44345e3
type: schema
level: concrete
title_ko: 미정의 술어 agt:unknownPredicate를 담은 임시 그래프가 FAIL [vocab]로 거부되고 커밋된 그래프는 gate_test를 통과한다
title: A temporary graph carrying the undefined predicate agt:unknownPredicate is rejected as FAIL [vocab] and committed graphs pass gate_test
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f2618270-3e11-40c7-b5d0-36c828923ff0]
verifies: [https://agentic-knowledge-base.dev/id/chunk/c7e1eccd-8eb4-4af6-8844-6b95cfcff5fb]
---
**케이스** — 온톨로지 밖 술어 하나를 가진 데이터 그래프와 커밋된 그래프 전체를 자극으로 쓴다.

**자극** — 임시 파일 `/tmp/vv-vocab-kg.ttl`이다. 커밋하지 않는다. 검사는 게이트와 같은 입력(온톨로지 모듈·shape·ODD·데이터)에 이 파일 하나를 `--data`로 더해 돌린다.

```turtle
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id:  <https://agentic-knowledge-base.dev/id/> .
id:chunk-vv-vocab-sample a agt:ContractChunk ; agt:unknownPredicate "x" .
```

**기대** — 출력에 `FAIL [vocab] /tmp/vv-vocab-kg.ttl: 온톨로지에 정의되지 않은 agt: 술어 https://agentic-knowledge-base.dev/agt/unknownPredicate`가 있고 종료 코드가 1이다. 파일을 빼면 같은 명령이 PASS다. 양성 실행 `//kg:gate_test`는 PASS다.

**실행 명령** — `bazel run //tools:validate -- --ontology $(ls kb/ontology/*/*/*-ontology.ttl) --shapes kb/ontology/shapes/*.ttl --odd bazel-bin/kb/odd/project-odd.ttl --data bazel-bin/kg/chunks-kg.ttl kg/*-kg.ttl /tmp/vv-vocab-kg.ttl; bazel test //kg:gate_test`

**표본 근거** — `agt:` 접두어를 쓴 술어는 접두어 검사로 걸러지지 않으므로 온톨로지 정의 대조만이 잡는다. 이것이 통제 어휘의 핵심 분기다. 미등록 네임스페이스 분기는 접두어만으로 판정되어 표본을 따로 두지 않는다.
