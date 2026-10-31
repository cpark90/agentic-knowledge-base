---
id: https://agentic-knowledge-base.dev/id/chunk/17b2eb03-21df-428a-88b1-3eb575903186
type: decision
level: concrete
title_ko: 레시피는 중립 부품의 조립 명세다
title: A recipe is an assembly specification over neutral parts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0018-recipe-assembly-spec.md, id: https://agentic-knowledge-base.dev/id/chunk-d0018, title_ko: "레시피는 중립 부품의 조립 명세다", title: "A recipe is an assembly spec over neutral parts"}, {resource: git:aeb0a58:chunks/decision/d-0186-recipe-standard-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0186, title_ko: "대안 — 레시피 표준", title: "Alternatives — recipe standard"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0018, https://agentic-knowledge-base.dev/id/chunk-d0186]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/34c7f15b-534a-47b4-813a-16c2edda3703
composite: {id: https://agentic-knowledge-base.dev/id/composite/34c7f15b-534a-47b4-813a-16c2edda3703, title_ko: 레시피는 조립 명세, title: Recipe as an assembly specification}
---
**결론** — 중앙 라이브러리와 레시피의 역할을 나눈다. 중앙은 일반화된 도메인 독립 부품만 담는 **중립 부품 라이브러리**로 두며, 그 부품은 guardrail과 pattern, workflow, prompt, tool, capability, concept다. 반면 부품이 어떻게 조합되어 쓰이는가는 레시피가 담는다. 레시피는 중앙 부품을 IRI로 참조해 완성물 하나를 조립하는 **조립 명세**이며, 자기 전문화에 필요한 도메인 특수 바인딩만 로컬로 선언한다.
