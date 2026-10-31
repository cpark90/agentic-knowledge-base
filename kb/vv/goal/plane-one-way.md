---
id: https://agentic-knowledge-base.dev/id/chunk/63c4c14d-87eb-4caf-ad0f-704265706505
type: requirement
level: functional
pattern: ubiquitous
title_ko: 하위 지식 종류를 refines 하는 링크는 거부되어야 한다
former_title_ko: ["하위 plane을 refines 하는 링크는 거부되어야 한다"]
title: A refines link pointing at a lower plane must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-24T22:56:06+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
---
**검증 목표** — 상위 지식 종류만 하위 지식 종류에 영향을 준다는 결정이 링크의 구조 판정으로 강제된다는 것이 보여져야 한다. 지식 종류 순서는 requirement → decision → contract·schema → artifact → annotation → memory다.

- **이해관계자**: 개발 역할 · 감사 역할 · **관심사**: 변화 속도가 빠른 지식이 느린 지식을 끌고 가지 않는 것

**무엇을 관측하면 성립하는가**

- 결정이 계약을 `refines` 하는 타깃이 분석 시점에 실패한다. 수준 검사는 통과하는 입력이어야 지식 종류 검사만 판정된다.
- `refines`·`serves`의 대상은 더 높은 수준이어야 하고, 같은 수준이거나 낮은 수준이면 실패한다.
- 커밋된 모든 링크는 순서를 지키며 `bazel test //...`가 PASS다.

순서의 원본은 `defs/kb.bzl`의 `PLANES`이고 판정은 `_check_links`가 한다.
