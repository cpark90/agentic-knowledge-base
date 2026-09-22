---
id: https://agentic-knowledge-base.dev/id/chunk/1ef46f34-e0ff-4996-bad4-ee3340ec290a
type: requirement
level: functional
pattern: event-driven
title_ko: 반복되는 관측은 요구·결정·기준·규칙을 거쳐 온톨로지 어휘로 승격될 수 있어야 한다
title: A repeated observation must be promotable through requirements, decisions, criteria and rules into ontology vocabulary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
---
**검증 목표** — 일반화가 네 전이이고 마지막 전이가 온톨로지에 닿으며 용어 제안은 승인 큐를 거친다는 결정이 승격 경로의 존재로 성립한다는 것이 보여져야 한다. 관측이 반복 패턴인지의 판단과 승인은 사람의 몫이다.

- **이해관계자**: 업체 · **관심사**: 축적과 재사용

**무엇을 관측하면 성립하는가**

- 관측이 memory plane 에 append-only 로 쌓인다(`kb/dev/memory/`·`kb/vv/run/`, 케이스 `observations-append-only`).
- `term_propose` 가 관측에서 뽑은 개념 후보를 검사(상위 개념 실재·라벨 중복 없음·정의 존재·케밥 ID)해 `kb/ontology/proposals/` 에 두고, 승인 전에는 그래프에 들어가지 않는다(`//kb/ontology:modules` 밖).
- 승인된 제안이 확장 모듈로 옮겨지고 `prov:wasDerivedFrom` 으로 관측에 연결된다.
- 승격의 목적지 넷(요구·logical 기준·결정·규칙) 중 하나가 된 관측이 있다.

판정의 원본은 `tools/term_propose.py`, `kb/ontology/proposals/README.md`, `kb/dev/decision/p6-ascent-generalization/conclusion.md` 다.
