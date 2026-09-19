---
id: https://agentic-knowledge-base.dev/id/chunk/83c1bb49-81f0-4f0e-a6f9-56b3a2f66924
type: requirement
level: functional
pattern: ubiquitous
title_ko: 수준 허용표 밖의 plane·level 조합은 거부되어야 한다
title: A plane-level pair outside the allowed-level matrix must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
---
**검증 목표** — 각 plane이 정해진 level 구간에만 거주한다는 결정이 게이트로 강제된다는 것이 보여져야 한다. 수준 허용표 밖의 조합을 가진 청크는 저장소에 들어올 수 없다.

- **이해관계자**: 개발 역할 · 감사 역할 · **관심사**: 판정 방식이 다른 지식이 섞이지 않는 것

**무엇을 관측하면 성립하는가**

- `requirement` plane에 `functional` 밖의 level을 붙인 타깃이 분석 시점에 실패한다.
- 결정 복합체의 세 부분 중 하나라도 `decision`의 허용 구간(abstract·logical·concrete) 밖이면 복합체 전체가 실패한다.
- 저장소에 커밋된 모든 청크는 같은 검사를 통과한다. `bazel test //...`가 PASS다.

허용표의 원본은 `defs/kb.bzl`의 `RESIDENCY`와 `kb/ontology/shapes/residency-shapes.ttl`이고 둘은 같은 내용이다.
