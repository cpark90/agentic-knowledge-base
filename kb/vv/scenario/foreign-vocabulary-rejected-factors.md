---
id: https://agentic-knowledge-base.dev/id/chunk/64545f36-8857-570c-8a83-8e9286bedd20
type: decision
level: logical
title_ko: 논리 시나리오 요인 — 미정의 agt 술어 하나를 담은 그래프의 검증이 노출하는 현상
title: Logical scenario factors — the phenomena exposed by validating a graph that carries one undefined agt predicate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f9c229ee-0c23-5dae-9cf3-62910f2054c9
---
**요인** — 노출하려는 현상은 `agt:outOfVocabularyPredicate` 하나다. `agt:` 접두어를 쓴 술어는 접두어 검사로 걸러지지 않으므로 온톨로지 정의 대조만이 잡는다. 표본 근거는 요인 주입 하나다. 변수 `predicate`에 keep 밖 값 `unknownPredicate`를 주입해 케이스 하나를 낸다. 기대에서 `FAIL [validate] — N건`을 빼는 까닭은 데이터가 커밋된 그래프 전체라 무관한 기존 위반이 섞일 수 있어서다. 기여하는 검증 목표는 `kb/vv/goal/foreign-vocabulary-rejected.md`(`https://agentic-knowledge-base.dev/id/chunk/50af6125-94e4-4d69-8181-df29db77451d`)다.
