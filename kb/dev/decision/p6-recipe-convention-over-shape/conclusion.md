---
id: https://agentic-knowledge-base.dev/id/chunk/81bba3f9-07ee-4c46-b888-4e9380596b59
type: decision
level: concrete
title_ko: 레시피 필수 코어에서는 규약이 shape보다 강하다
title: In the recipe required core, conventions are stronger than shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0019-recipe-required-core.md, id: https://agentic-knowledge-base.dev/id/chunk-d0019, title_ko: "레시피 필수 코어 — 규약이 shape보다 강하다", title: "Recipe required core - convention over SHACL floor"}, {resource: git:aeb0a58:chunks/decision/d-0186-recipe-standard-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0186, title_ko: "대안 — 레시피 표준", title: "Alternatives — recipe standard"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0019, https://agentic-knowledge-base.dev/id/chunk-d0186]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/62ae5796-417d-448f-a95a-5c028891aef7
composite: {id: https://agentic-knowledge-base.dev/id/composite/62ae5796-417d-448f-a95a-5c028891aef7, title_ko: 레시피 필수 코어의 두 층, title: Two layers of the recipe required core}
---
**결론** — 레시피의 필수 형태는 두 층으로 강제한다. shape(SHACL)는 의도와 완결성의 최소만 구조적으로 강제하고, 그 최소는 라벨과, 도메인과 과업, 프롬프트, 워크플로 각각 하나 이상이다. 그 위의 필수 술어 집합은 **플릿 규약**으로 요구하고 린터와 감사, 리뷰가 지킨다. 그 술어는 도구와 guardrail, 모델, capability, 태그 등이다. 규약은 shape를 포함하므로 규약이 항상 더 강한 요구다.
