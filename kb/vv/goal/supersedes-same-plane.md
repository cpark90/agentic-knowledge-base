---
id: https://agentic-knowledge-base.dev/id/chunk/897a67c4-c07c-4674-a845-dd7841db9c17
type: requirement
level: functional
pattern: ubiquitous
title_ko: 다른 plane의 항목을 supersedes 하는 링크는 거부되어야 한다
title: A supersedes link across planes must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
---
**검증 목표** — 결정의 대체가 `supersedes`이고 옛 결정이 같은 plane 안에서 `deprecated`로 남는다는 결정이 링크의 구조 판정으로 강제된다는 것이 보여져야 한다. 대체는 시간축의 관계이므로 plane을 넘지 않는다.

- **이해관계자**: 개발 역할 · 감사 역할 · **관심사**: 변경이 재판정 대상을 정확히 가리키는 것

**무엇을 관측하면 성립하는가**

- `decision` 청크가 `requirement` 청크를 `supersedes` 하는 타깃이 분석 시점에 실패한다.
- 커밋된 `supersedes` 링크는 전부 같은 plane 안에 있고 대상의 상태는 `deprecated`다.
- `bazel test //...`가 PASS다.

판정의 원본은 `defs/kb.bzl`의 `_check_links`이고 `supersedes` 대상의 plane을 주어의 plane과 비교한다.
