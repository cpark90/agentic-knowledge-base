---
id: https://agentic-knowledge-base.dev/id/chunk/0d2a6a36-d0d1-4c55-b4b8-2e8ff8f540f3
type: requirement
level: functional
pattern: event-driven
title_ko: 프로젝트가 끝나면 어휘·공리·ODD 코어·결함 어휘·교훈이 다음 프로젝트로 넘어가야 한다
title: When a project ends, vocabulary, axioms, the ODD core, the defect vocabulary and lessons must carry over to the next project
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d]
---
**검증 목표** — 프로젝트를 넘는 것이 어휘·제약·ODD 코어이고 청크는 넘지 않는다는 결정이 두 번째 프로젝트에서 실제로 성립한다는 것이 보여져야 한다. 이 저장소에는 두 번째 프로젝트가 없어 관측은 재사용 대상의 분리 여부에 그친다.

- **이해관계자**: 업체 · **관심사**: 축적과 재사용

**무엇을 관측하면 성립하는가**

- 온톨로지 코어 모듈과 프로젝트 확장 모듈이 디렉토리로 갈라져 있다(`kb/ontology/` 의 모듈 구조, `//kb/ontology:modules`).
- ODD 문서가 코어(택소노미 생성)와 프로젝트 조건으로 갈라져 있다(`kb/odd/project-odd.yml` 의 `TAXONOMY` 는 `related/condition` 에서 생성).
- 청크 재사용 경로가 없다. 그래프 입력은 이 저장소의 청크뿐이다(케이스 `chunk-bound-to-project-odd`).
- 다음 프로젝트를 시작할 때 온톨로지·ODD 코어를 복사하고 청크는 복사하지 않는 절차를 사람이 수행하고 확인한다.

판정의 원본은 `kb/ontology/BUILD.bazel` 의 모듈 목록, `kb/odd/BUILD.bazel` 의 `kb_taxonomy`, `kb/dev/decision/p12-cross-project-reuse/conclusion.md` 의 표다.
