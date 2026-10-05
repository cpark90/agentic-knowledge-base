---
id: https://agentic-knowledge-base.dev/id/chunk/ffacb879-a5c4-4ecc-8e50-c0751aec665b
type: contract
level: logical
title_ko: 드리프트 테스트 종류가 방향별로 남김없이 분류되고 지식이 원본인 종류와 지식을 읽는 게이트가 PASS 하며 승격 사례가 하나 이상이다
title: Every drift-test kind is classified by direction, the kinds whose source is knowledge and the gates that read knowledge pass, and at least one promotion exists
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T13:27:34+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/df934d56-8cc4-4f5f-8cbd-7ae5b6bb89f0]
---
**합격 기준** — 기준 종류는 **불변식**이다. 드리프트 테스트 종류 집합 `D` 는 `defs/knowledge.bzl` 의 매크로 `kb_<종류>_drift_test` 가 낸 타깃의 종류다. `D` 를 방향으로 나눈다. `K = {build, norms}` 는 지식 → 하네스, `V = {case}` 는 지식 → V&V KB 의 케이스, `T = {extract, skills}` 는 도구 코드 → 청크·skill 이다. 판정은 `D ∖ (K ∪ V ∪ T) = ∅` 이고 아래 네 식이 모두 성립하는 것이다.

**판정식**

- 생성 부분: `bazel query 'attr(generator_function, "^kb_(build|norms)_drift_test$", //...)'` 가 `//:build_drift_test`·`//:norms_drift_test` 를 내고 두 테스트와 `//:gendoc_test` 가 PASS 다.
- 게이트 입력: `bazel query 'deps(//kg:gate_test) intersect set(//kb/ontology:modules //kb/ontology:shapes //kb/odd:odd)'` 가 셋을 모두 내고 `//kg:gate_test` 가 PASS 다.
- 승격: `grep -rhE 'prov:wasDerivedFrom .*<https://agentic-knowledge-base.dev/id/chunk/' kb/ontology --include='*.ttl'` 의 행 수가 1 이상이다.
- 역방향 공백: `bazel query 'attr(generator_function, "^kb_[a-z]+_drift_test$", //...) except attr(generator_function, "^kb_(build|norms|case|extract|skills)_drift_test$", //...)'` 가 빈 결과다.

생성 뷰는 트리에 사본이 없어 바이트 비교 대신 형태 게이트 `gendoc` 이 본다. 게이트 입력 식은 어휘·shape·ODD 가 도구 코드가 아니라 지식 파일에서 읽힌다는 구조 증거이고, 개념 하나로 수용 범위가 바뀌는 음성 표본은 기준 `foreign-vocabulary-rejected` 가 갖는다. 승격 식은 확장 모듈의 용어가 `prov:wasDerivedFrom` 으로 청크 IRI(관측·판정 주석)를 가리키는 수를 센다. 승인 대기 제안은 `bazel query 'labels(srcs, //kb/ontology:proposals)'` 가 낸다. 역방향 공백 식에서 분류된 종류 가운데 도구 코드를 생성 쪽에 두는 것이 없으므로 지식 → 도구 코드 경로가 없다는 사실이 분류 표로 드러난다. 새 종류가 생기면 잔여가 비지 않아 불합격이고 분류가 먼저 정해진다.

**등급** — B 다. 판정은 기계가 하되 드리프트 테스트의 재생성 비용이 있다. 승격 수와 잔여 질의는 A 다.

**미확정의 처리** — 목표의 `미확정:` 인 경계를 닫지 않는다. 경계를 드리프트 테스트를 가진 생성 부분으로 좁혀 그 안의 성립만 판정한다. 드리프트 테스트가 없는 하네스 부분(손으로 쓴 도구 코드·부팅 스크립트)이 지식에서 생성되어야 하는가는 판정 밖이다. 그래서 PASS 는 부분 성립의 범위를 보일 뿐 요구 `r-029-harness-self-improvement` 의 성립이 아니다. 잔여 질의가 경계의 이동을 불합격으로 드러낸다.

판정의 원본은 `defs/knowledge.bzl` 의 드리프트 매크로 다섯과 `BUILD.bazel` 의 선언이다.
