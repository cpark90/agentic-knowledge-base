---
id: https://agentic-knowledge-base.dev/id/chunk/45bf2da4-6e02-4e3c-b042-713e94a1e14c
type: contract
level: logical
title_ko: 프로젝트 간 이전은 두 번째 프로젝트를 시작할 때 온톨로지·ODD 코어만 옮겨졌는지 사람이 확인한다
title: Cross-project carry-over is confirmed by a person, when a second project starts, checking that only the ontology and the ODD core were moved
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-22T19:06:46+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/0d2a6a36-d0d1-4c55-b4b8-2e8ff8f540f3]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. 두 번째 프로젝트 `P₂` 에서 `ontology(P₂) ⊇ core(P₁)` 이고 `odd(P₂)` 가 `P₁` 의 택소노미에서 생성되며 `chunks(P₂) ∩ chunks(P₁) = ∅` 인지를 사람이 본다.

**확인 절차**

1. `P₂` 저장소를 만들 때 `kb/ontology/` 의 코어 모듈과 `kb/odd/` 의 택소노미 원천(`related/condition`)만 복사한다.
1. `P₂` 에서 `bazel test //kb/ontology:gate_test //kb/odd:gate_test` 가 PASS 인지 본다.
1. `P₂` 의 `kb/dev/**`·`kb/vv/**` 가 비어 있거나 `P₁` 의 청크 IRI 를 하나도 담지 않는지 `grep` 으로 본다.
1. `P₁` 의 결함 어휘·교훈이 `P₂` 의 온톨로지 확장 모듈에 들어갔는지 본다.

**등급** — D 다. 두 번째 프로젝트가 없어 지금은 판정 자체가 불가능하다.

케이스를 두지 않는다. 이 저장소 안에서 실행할 명령이 없고, 분리 구조의 존재는 케이스 `chunk-bound-to-project-odd` 가 이미 관측한다. 판정의 원본은 `kb/dev/decision/p12-cross-project-reuse/conclusion.md` 의 재사용 표와 이 절차다.
