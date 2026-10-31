---
id: https://agentic-knowledge-base.dev/id/chunk/eaf61cb9-4317-42cf-b29a-75c6db72428f
type: decision
level: concrete
title_ko: 필수 술어는 모든 레시피를 측정한 교집합이고 shape는 연합의 하위 저장소까지 검증하므로 최소에 머문다
title: Required predicates are the measured intersection of all recipes, and shapes stay minimal because they also validate downstream repositories
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0019-recipe-required-core.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:24:06+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:24:06+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/62ae5796-417d-448f-a95a-5c028891aef7
---
**근거** — 출처는 harness-concrete `RECIPE_STANDARD`의 §0과 §1이다.

- 필수와 선택의 구분은 발명이 아니라 **모든 레시피를 측정한 교집합**이다. 측정한 레시피는 처음에 53개였고 2026-09의 재측정에서 58개였다. 모든 레시피를 덮는 술어가 단단한 코어(hard core)가 되고, 대부분을 덮는 술어가 규약의 요구가 된다. 표준이 먼저 있고 데이터가 따르는 것이 아니라 그 반대다.
- shape의 minCount를 규약 수준까지 올리지 않는 이유는 같은 shape가 연합 CI에서 하위 저장소의 데이터까지 검증하기 때문이다. 상한선을 shape에 넣으면 정당한 축소 프로파일까지 깨지므로, 강한 요구는 규약과 린터의 층에 둔다.
- 표준은 바닥이지 천장이 아니다. 그래서 원천이 제공하면 잘 타입된 다른 바인딩을 얼마든지 더 실을 수 있다.

이 저장소에서는 검사 게이트(6.7절)와 스타일 규약(STYLEGUIDE의 [지킴]과 [권장])의 이층 구조가 같은 원리다. shape는 최소를 맡고 규약은 측정에서 온 요구를 맡는다.
