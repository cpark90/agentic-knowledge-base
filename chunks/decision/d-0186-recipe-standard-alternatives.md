---
id: https://agentic-knowledge-base.dev/id/chunk-d0186
type: decision
level: concrete
title_ko: 대안 — 레시피 표준
title: Alternatives — recipe standard
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:56+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-recipe-standard
---
**대안** — 묶음의 세 결정마다 원천(harness-concrete `RECIPE_STANDARD.md`·`docs/recipes-design.md`)이 대비한 안을 적는다.

- d-0018(조립 명세): 중립 부품 라이브러리가 한 도메인의 개체를 담는 배치는 기각이다. lpranging 모델링은 중립 부품 원칙에 따라 라이브러리에서 퇴역했고 예시 레시피 `recipes/lpranging/`로 옮겨졌다(recipes-design.md "Repo renames").
- d-0018(조립 명세): 레시피가 core 유닛을 하나씩 열거해 import하는 안도 기각이다. 새 core 유닛이 레시피의 폐포를 조용히 깨뜨릴 수 있어 union 루트 하나만 import한다(recipes-design.md "What a single recipe unit contains" 1).
- d-0018(조립 명세): 중앙 부품을 레시피에 복제하는 안은 drift이므로 IRI로 재사용한다(RECIPE_STANDARD §1·§2).
- d-0019(규약 ⊇ shape): 대안 없음. RECIPE_STANDARD §0–1은 shape가 강제하는 술어와 규약만 요구하는 술어를 실측으로 나누어 적을 뿐, 두 층을 다르게 배치하는 안을 후보로 비교하지 않는다.
- d-0020(source-gating): 실행 거동 축을 전수 100%로 채우려고 원천에 없던 시나리오·실패 정책을 지어내는 안은 기각이다. 원천은 그것을 정직한 과소 반영보다 나쁘다고 적고, 결손은 수용 사유를 기록한 결과로 둔다(RECIPE_STANDARD §0·§2).
