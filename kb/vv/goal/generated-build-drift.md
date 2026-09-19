---
id: https://agentic-knowledge-base.dev/id/chunk/e853e578-c267-4a55-8497-739fa3ed863d
type: requirement
level: functional
pattern: ubiquitous
title_ko: frontmatter와 어긋난 생성 BUILD는 거부되어야 한다
title: A generated BUILD that disagrees with the frontmatter must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
---
**검증 목표** — IRI와 Bazel 라벨의 사상을 `gen_build`가 frontmatter에서 결정론적으로 만든다는 결정이 드리프트 검사로 강제된다는 것이 보여져야 한다. BUILD는 뷰이고 frontmatter가 원본이다.

- **이해관계자**: 개발 역할 · 감사 역할 · **관심사**: 명명과 표기가 결정론적인 것

**무엇을 관측하면 성립하는가**

- 청크의 frontmatter를 고치고 BUILD를 다시 생성하지 않으면 검사 모드가 `FAIL [build-drift]`로 거부한다.
- 손으로 고친 BUILD도 같은 이유로 거부된다.
- 같은 frontmatter에서 생성기를 두 번 돌리면 같은 BUILD가 나온다.
- 커밋된 생성 BUILD 전부가 원본과 일치하고 `//:build_drift_test`가 PASS다.

검사의 원본은 `tools/gen_build.py --check`이고 대조 대상은 `kb/dev/requirement`·`kb/dev/decision`·`kb/dev/memory`·`chunks/decision`·온톨로지 모듈의 BUILD다.
