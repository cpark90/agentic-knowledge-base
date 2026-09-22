---
id: https://agentic-knowledge-base.dev/id/chunk/d72a3063-801a-4ec0-977c-f2f75550f5c0
type: requirement
level: functional
pattern: event-driven
title_ko: 프로젝트의 운영 조건은 판정 방법을 가진 조건들의 ODD 문서 하나로 명세되어야 한다
title: The operating conditions of a project must be specified in one ODD document of conditions with check methods
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
---
**검증 목표** — ODD 가 프로젝트당 하나의 실제 문서이고 모든 조건이 객관적 판정 방법과 등급을 동반한다는 결정이 저장 구조와 ODD 게이트로 강제된다는 것이 보여져야 한다. 원본은 OpenODD 문서 하나이고 TTL·택소노미는 생성물이다.

- **이해관계자**: 프로젝트 · **관심사**: 경계와 갱신

**무엇을 관측하면 성립하는가**

- `kb/odd/` 의 OpenODD 문서는 `project-odd.yml` 하나이고 `//kb/odd:odd` 의 `srcs` 는 그 파일과 생성 택소노미뿐이다.
- 모든 조건에 `CHECKS.<속성>` 의 `grade`·`method` 가 있고, 없으면 `odd2kg` 가 생성을 거부한다.
- 생성 그래프의 모든 `agt:Condition` 이 `agt:checkMethod`·`agt:verificationGrade` 를 갖고 ODD 개체가 조건을 하나 이상 갖는다(`condition-shapes.ttl`).
- `bazel test //kb/odd:gate_test` 가 PASS 다.

판정의 원본은 `kb/odd/BUILD.bazel` 의 `kb_odd_kg`, `tools/odd2kg.py`, `kb/ontology/shapes/condition-shapes.ttl` 이다.
