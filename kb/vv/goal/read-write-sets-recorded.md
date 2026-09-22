---
id: https://agentic-knowledge-base.dev/id/chunk/c486fdea-7d86-4618-a361-4a9415e7ff4a
type: requirement
level: functional
pattern: event-driven
title_ko: 편집의 읽기 집합과 쓰기 집합은 하네스가 기록하고 링크는 그 부산물이어야 한다
title: The harness must record the read set and the write set of an edit, and links must be their by-product
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93]
---
**검증 목표** — 링크가 편집 연산의 부산물이라는 결정(구축이 기본, 복원은 예외)이 쓰기 집합의 기계 검사와 읽기 집합의 인수인계로 성립한다는 것이 보여져야 한다. 쓰기 집합은 카탈로그의 역할 × plane 권한이고 읽기 집합은 작업 집합 뷰에서 펼친 청크다.

- **이해관계자**: 에이전트 · **관심사**: 링크 구축

**무엇을 관측하면 성립하는가**

- 카탈로그(`kg/catalog-kg.ttl`)가 역할마다 `agt:reads`·`agt:writes`·`agt:writesIn` 을 갖고 CQ-24 가 역할 × 권한 행으로 낸다.
- 청크의 `generated.by` 역할이 그 KB·plane 의 쓰기 권한이 없으면 `writer` 검사가 거부한다. 쓰기 집합이 기록되어 있어야 이 판정이 성립한다.
- 작업 집합 뷰의 펼친 청크(`<!-- iri: … -->`)가 읽기 집합이고 `handoff` 가 그것을 새 청크의 `sources` 로 옮긴다. `chunk2kg` 는 frontmatter 링크마다 `agt:Link` 와 구축 기록 증거를 방출한다.
- `metrics` 의 구축 비율(구축 링크 대 복원 링크)이 구축이 기본임을 수치로 보인다.

판정의 원본은 `tools/validate.py` 의 `check_catalog`·`check_writer`, `tools/handoff.py`, `tools/chunk2kg.py` 다.
