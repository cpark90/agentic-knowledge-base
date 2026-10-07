---
id: https://agentic-knowledge-base.dev/id/chunk/e815eab2-4c4b-41dc-8b57-6617bb76e566
type: requirement
level: functional
pattern: ubiquitous
title_ko: 제안된 편집은 게이트가 판정하여 통과시키거나 근거를 들어 거부해야 한다
title: A proposed edit must be judged by a gate that passes it or rejects it with a reason
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-06T11:23:25+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-06T11:23:25+09:00}]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
---
**검증 목표** — 게이트가 다섯 실행 계층(shape·verify·analysis·test·human)에 배치되고 실패는 `draft`에 머물러 전파되지 않는다는 결정이 기계 게이트로 실제 편집을 판정한다는 것이 보여져야 한다. 판정은 에이전트 밖의 규칙과 shape가 한다.

- **이해관계자**: 에이전트 · 감사 역할 · **관심사**: 구조적 통제

**무엇을 관측하면 성립하는가**

- analysis 실행 계층: 수준 허용표·plane 순서·`supersedes` plane·`verifies` 주어·복합체 수준을 어긴 타깃이 분석 시점에 실패하고 메시지에 규칙과 절 번호가 있다.
- shape·verify 실행 계층: head 그래프가 SHACL shape·통제 어휘·안티패턴 질의를 통과한다. `//kg:gate_test`가 PASS다.
- test 실행 계층: 청크 검사(`//kb/dev:lint_test`)가 본문 토큰 상한·역할 표지·산문을 판정한다.
- 거부 메시지는 `FAIL [<게이트 id>] <위치>: <규칙>` 형식이라 실패가 곧 수정 방향이다.

판정의 원본은 `defs/kb.bzl`의 `_check_residency`·`_check_links`, `tools/validate.py`, `tools/chunk_lint.py`다.
