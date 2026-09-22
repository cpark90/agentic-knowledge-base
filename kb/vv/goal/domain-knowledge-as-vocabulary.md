---
id: https://agentic-knowledge-base.dev/id/chunk/92fbd9bd-9e1f-4f97-b6e9-1661d59d794d
type: requirement
level: functional
pattern: ubiquitous
title_ko: 분야 지식은 에이전트가 활용할 수 있는 어휘와 그 위의 항목으로 축적되어야 한다
title: Domain knowledge must accumulate as vocabulary usable by agents and as items built on it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
---
**검증 목표** — 온톨로지가 다섯 수준 전부의 어휘이고 어휘 밖 지식은 체계에 존재하지 않는다는 결정이 축적의 형태로 성립한다는 것이 보여져야 한다. 축적은 시간에 걸친 판단이라 기계 판정 하나로 닫히지 않는다.

- **이해관계자**: 업체 · **관심사**: 축적과 재사용

**무엇을 관측하면 성립하는가**

- 데이터의 술어가 전부 `agt:` 온톨로지 또는 등록 표준 어휘 안이다(`vocab` 검사, 케이스 `foreign-vocabulary-rejected`).
- 청크 본문이 온톨로지 개념을 쓴다. `metrics` 의 `agt:usesConcept` 수와 CQ-35(개념 검색)가 그 수치다.
- 정의되었으나 쓰이지 않는 개념(CQ-28)이 줄고 본문에서 쓰이는 개념이 는다.
- 새 개념은 온톨로지 모듈에 파일 하나로 추가되고 한/영 라벨·정의를 갖는다(`labels` 검사).

판정의 원본은 `tools/validate.py` 의 `check_vocab`·`check_labels`, `tools/cq-queries/CQ-28.rq`·`CQ-35.rq`, `tools/metrics.py` 다. 어휘가 재사용 가능한 형태로 자라는지는 사람이 두 시점의 수치를 비교해 판단한다.
