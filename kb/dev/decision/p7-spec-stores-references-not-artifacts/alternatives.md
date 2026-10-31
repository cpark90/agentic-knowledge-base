---
id: https://agentic-knowledge-base.dev/id/chunk/f97fc9f8-73ec-4a87-85fb-5a8c2894be79
type: decision
level: concrete
title_ko: 레시피가 구체 빌드 문서를 직접 저장하는 안은 택하지 않는다
title: A recipe storing concrete build documents directly is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0189-spec-content-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:10:57+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:10:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/959d935b-e16d-4955-acf0-12c81c12e8aa
---
**대안** — 원천(harness-concrete `docs/recipes-design.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 레시피가 구체 빌드 문서(도구 코드, 표준 문서, 스킬 본문)를 직접 저장한다 | 원천은 그것을 vendoring이라 부르고, 구현은 참조되어 빌드에서 재생성될 뿐 명세에 저장하지 않는다고 정한다(recipes-design "What a recipe stores", ODR INV-1) |
