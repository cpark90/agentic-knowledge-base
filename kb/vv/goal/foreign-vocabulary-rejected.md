---
id: https://agentic-knowledge-base.dev/id/chunk/50af6125-94e4-4d69-8181-df29db77451d
type: requirement
level: functional
pattern: ubiquitous
title_ko: 온톨로지에 없는 술어로 쓴 그래프는 거부되어야 한다
title: A graph written with a predicate the ontology does not define must be rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
---
**검증 목표** — 온톨로지 밖의 어휘로 쓴 지식이 이 체계에 존재하지 않는다는 결정이 통제 어휘 검사로 강제된다는 것이 보여져야 한다. 데이터 그래프의 술어는 온톨로지 정의 또는 등록된 표준 어휘 안에 있어야 한다.

- **이해관계자**: 개발 역할 · 온톨로지 편집 역할 · **관심사**: 어휘가 조용히 갈라지지 않는 것

**무엇을 관측하면 성립하는가**

- 온톨로지에 정의되지 않은 `agt:` 술어를 가진 데이터 그래프를 검사에 넣으면 `FAIL [vocab]`로 거부된다.
- 등록되지 않은 네임스페이스의 술어도 `FAIL [vocab]`로 거부된다.
- 커밋된 그래프 전부의 술어가 온톨로지 안에 있고 `//kg:gate_test`가 PASS다.

검사의 원본은 `tools/validate.py`의 `check_vocab`이고 입력은 head 그래프·시드 그래프·ODD 그래프다.
