---
id: https://agentic-knowledge-base.dev/id/chunk/ea187469-7c81-46b7-92b7-bbe049abbe65
type: contract
level: logical
title_ko: 축적은 어휘 밖 술어 0 과 본문의 개념 사용 수치를 두 시점에서 비교해 사람이 확인한다
title: Accumulation is confirmed by a person comparing zero foreign predicates and the concept-usage figures at two points in time
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-22T19:06:46+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/92fbd9bd-9e1f-4f97-b6e9-1661d59d794d]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. 기계가 내는 값은 `foreign_predicates = 0`(게이트)과 `usesConcept 수`·`CQ-28 고립 개념 수`·`CQ-35 개념별 사용처 수`(뷰)이고, 축적의 판정은 두 시점 `t₀ < t₁` 에서 `usesConcept(t₁) ≥ usesConcept(t₀)` 이고 고립 개념이 늘지 않았는지를 사람이 본다.

**확인 절차**

1. `bazel test //kg:gate_test` 가 PASS 인지 본다. `vocab` 위반 0 이 전제다.
1. `bazel build //kg:metrics //kg:cq` 를 돌려 `agt:usesConcept` 수(2026-09-21 실측 164)와 CQ-28·CQ-35 의 행 수를 적는다.
1. 이전 실행 기록 또는 이전 리비전의 같은 수치와 비교한다. 개념 사용이 늘고 고립 개념이 늘지 않았으면 성립이다.
1. 판단을 관측(memory plane)으로 남긴다.

**등급** — C 다. 수치는 기계가 내지만 판정은 사람의 비교다.

케이스를 두지 않는다. 시점 비교는 실행 명령 하나로 판정되지 않고, 한 시점의 수치만으로 통과를 선언하면 공허하다. 판정의 원본은 `tools/metrics.py`·`tools/cq-queries/CQ-28.rq`·`CQ-35.rq` 와 이 절차다.
