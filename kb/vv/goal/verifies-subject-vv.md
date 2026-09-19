---
id: https://agentic-knowledge-base.dev/id/chunk/98edd71a-023c-446e-a26f-c24bc834a4b5
type: requirement
level: functional
pattern: ubiquitous
title_ko: 개발 KB 청크가 주어인 verifies 링크는 거부되어야 한다
title: A verifies link whose subject is a development-KB chunk must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
---
**검증 목표** — `verifies` 링크의 주어가 V&V KB의 청크뿐이라는 결정이 패키지 경계로 강제된다는 것이 보여져야 한다. 개발 산출물이 자기를 검증했다고 주장하는 링크는 저장소에 들어올 수 없다.

- **이해관계자**: 검증 역할 · 감사 역할 · **관심사**: 검증의 독립성

**무엇을 관측하면 성립하는가**

- `kb/dev` 밖의 개발 패키지에서 `verifies`를 가진 타깃이 분석 시점에 실패한다.
- `verifies`의 대상이 `kb/dev` 패키지가 아니면 실패한다.
- `verifies`의 주어와 대상은 같은 수준이어야 하고 다르면 실패한다.
- 커밋된 `verifies` 링크의 주어는 전부 `kb/vv` 패키지에 있고 `bazel test //...`가 PASS다.

판정의 원본은 `defs/kb.bzl`의 `_check_links`이고 주어 라벨의 패키지 접두어 `kb/vv`와 대상의 `kb/dev`를 본다.
