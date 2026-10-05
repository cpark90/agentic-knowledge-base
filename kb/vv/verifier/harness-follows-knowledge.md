---
id: https://agentic-knowledge-base.dev/id/chunk/270dd91e-f97d-48be-a902-5f0dc19b51b8
type: artifact
level: executable
title_ko: 드리프트 테스트 종류의 분류 잔여가 비고 지식이 원본인 두 드리프트 테스트와 형태 게이트·어휘 게이트가 PASS 한다
title: The residue of the drift-test kind classification is empty and the two drift tests whose source is knowledge, the form gate and the vocabulary gate pass
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ffacb879-a5c4-4ecc-8e50-c0751aec665b]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T13:27:34+09:00}
layer: process
---
**검증기** — 드리프트 테스트 매크로가 낸 타깃 집합과 지식 파일을 입력으로 받는 게이트를 자극으로 쓴다. 임시 자극을 만들지 않고 커밋된 트리를 읽는다.

**자극** — 분류 표와 게이트 입력 셋이다.

```yaml
kinds:       {knowledge-to-harness: [build, norms], knowledge-to-vv: [case], tool-to-chunk: [extract], tool-to-skill: [skills]}
gate_inputs: [//kb/ontology:modules, //kb/ontology:shapes, //kb/odd:odd]
```

**기대** — 첫 질의는 분류 잔여가 비어 `Empty results` 를 낸다. 둘째 질의는 지식이 원본인 드리프트 테스트 둘을 낸다. 셋째 질의는 게이트 입력 셋을 모두 낸다. 테스트 넷은 PASS 다.

```yaml
expect:
  - exit: 0
    contains: ["Empty results"]
  - exit: 0
    contains: ["//:build_drift_test", "//:norms_drift_test"]
  - exit: 0
    contains: ["//kb/ontology:modules", "//kb/ontology:shapes", "//kb/odd:odd"]
  - exit: 0
```

**실행 명령** — `bazel query 'attr(generator_function, "^kb_[a-z]+_drift_test$", //...) except attr(generator_function, "^kb_(build|norms|case|extract|skills)_drift_test$", //...)'; bazel query 'attr(generator_function, "^kb_(build|norms)_drift_test$", //...)'; bazel query 'deps(//kg:gate_test) intersect set(//kb/ontology:modules //kb/ontology:shapes //kb/odd:odd)'; bazel test //:build_drift_test //:norms_drift_test //:gendoc_test //kg:gate_test`

**판정 범위** — 기준의 네 식 가운데 생성 부분·게이트 입력·역방향 공백을 실행한다. 승격 수는 `grep` 이라 실행기의 허용 목록 밖이어서 두지 않는다. 그 수는 기준이 인용한 명령으로 따로 얻는다.

**검증 대응물** — 없음. 판정 대상이 생성기 하나가 아니라 드리프트 테스트 종류의 집합이라 `executable` 개발 항목 하나에 대응하지 않는다.
