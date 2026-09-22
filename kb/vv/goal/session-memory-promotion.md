---
id: https://agentic-knowledge-base.dev/id/chunk/c7aaa3bd-826c-425b-9d0d-76d009002ae6
type: requirement
level: functional
pattern: event-driven
title_ko: 세션의 시행착오는 memory plane 에 남고 승격 규칙에 따라 주제 plane 으로 올라가야 한다
title: A session's trial and error must remain in the memory plane and rise to a topic plane under the promotion rule
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
---
**검증 목표** — 단기기억은 memory plane 에 두고 장기기억은 주제 plane 으로 승격하며 승격 규칙은 체계가 고정하지 않는 입력이라는 결정이 두 층의 존재와 승격 사례로 성립한다는 것이 보여져야 한다. 승격 규칙이 입력이므로 언제 무엇을 올리는지는 프로젝트가 정하고 사람이 확인한다.

- **이해관계자**: 에이전트 · **관심사**: 일반화

**무엇을 관측하면 성립하는가**

- memory plane 이 실재하고 concrete 에만 산다(`kb/dev/memory/`·`kb/vv/run/`, 수준 허용표 `memory: [concrete]`).
- 도구가 실행 결과를 관측으로 남긴다(`assume_check --record`·`vv_run --record`, 케이스 `observations-append-only`).
- 관측에서 올라간 결정·요구가 있고 그 청크가 `sources` 또는 `prov:wasDerivedFrom` 으로 관측을 가리킨다.
- orchestrator 의 write plane 에 `memory` 가 있어 세션·판정 관측을 남길 수 있다(`kg/catalog-kg.ttl`).

판정의 원본은 `defs/kb.bzl` 의 `RESIDENCY`, `tools/assume_check.py`·`tools/vv_run.py` 의 `--record`, `kb/dev/decision/p11-memory-promotion-rule/conclusion.md` 다.
