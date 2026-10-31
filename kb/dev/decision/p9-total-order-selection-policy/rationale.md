---
id: https://agentic-knowledge-base.dev/id/chunk/4b77a857-6942-4a5c-a66b-2728b5f63026
type: decision
level: concrete
title_ko: 기계가 소비하는 선호는 전순서여야 같은 입력에서 같은 답이 나온다
title: A preference consumed by a machine must be a total order to give the same answer for the same input
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0176-deterministic-selection-policy.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:51:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:51:27+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/edb7941d-bfc4-43d0-84ce-b2201e7fddb1
---
**근거** — 출처는 harness-concrete `docs/odr-bind-lock.md`의 "Selection policy" 절이다.

- 선호는 후보를 기각하지 않고 순서만 정한다(`p9-preference-partial-order`). 그 순서를 사람이 아니라 기계가 소비하려면 순서가 **전순서**여야 한다. 부분순서로는 동점에서 답이 갈리기 때문이다.
- 그래서 마지막 동점 처리(tiebreak)는 반드시 전순서인 키로 두며, 그 키는 값이고 그다음은 후보 식별자의 오름차순이다. 집합이나 해시의 순회 순서에 기대는 선택은 같은 입력에서 다른 답을 내므로 재현성을 깬다.
- 값 비교 규칙 자체도 고정한다. 버전 문자열은 구분자로 쪼개 숫자 구간을 숫자로 비교한다(`1.10.0 > 1.9.0`). 사전식 비교는 사람이 기대하는 순서와 어긋나기 때문이다.
- 정책은 지역이 전역을 덮는다. 항목별 정책이 구성물 기본 정책보다, 구성물 기본 정책이 체계 기본값보다 앞선다. 그래야 한 항목만 고정하려고 전체 기본값을 바꾸지 않는다.
