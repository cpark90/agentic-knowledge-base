---
id: https://agentic-knowledge-base.dev/id/chunk/0fc69c06-f72c-43c4-b621-ba5e8c735948
type: decision
level: concrete
title_ko: 한 도메인을 담는 라이브러리와 유닛 열거 import와 부품 복제는 택하지 않는다
title: A domain-bearing library, per-unit imports and copied parts are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0186-recipe-standard-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:21:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:21:21+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/34c7f15b-534a-47b4-813a-16c2edda3703
---
**대안** — 원천(harness-concrete `RECIPE_STANDARD.md`와 `docs/recipes-design.md`)이 대비한 안 셋을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 중립 부품 라이브러리가 한 도메인의 개체를 담는다 | lpranging 모델링은 중립 부품 원칙에 따라 라이브러리에서 퇴역했고 예시 레시피 `recipes/lpranging/`로 옮겨졌다(recipes-design.md "Repo renames") |
| 레시피가 core 유닛을 하나씩 열거해 import한다 | 새 core 유닛이 레시피의 폐포를 조용히 깨뜨릴 수 있으므로 union 루트 하나만 import한다(recipes-design.md "What a single recipe unit contains" 1) |
| 중앙 부품을 레시피에 복제한다 | 복제는 drift이므로 IRI로 재사용한다(RECIPE_STANDARD §1, §2) |
