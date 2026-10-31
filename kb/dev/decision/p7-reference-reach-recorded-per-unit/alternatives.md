---
id: https://agentic-knowledge-base.dev/id/chunk/8cd85968-e7f0-47c4-aa93-4d4c96ab8cf8
type: decision
level: concrete
title_ko: 해석되지 않는 참조를 빌드 실패로 처리하는 안은 택하지 않는다
title: Failing the build on unresolved references is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0189-spec-content-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:13:45+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:13:45+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/3343eae6-4b88-48c8-abfc-da8bb1af307a
---
**대안** — 원천(harness-concrete `docs/recipes-design.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 해석되지 않는 참조를 빌드 실패로 처리한다 | 원천은 그 참조를 `.ref` 스텁으로 강등한다(recipes-design의 같은 절) |

저장소 상대 참조와 외부 참조는 기각 관계가 아니다. 원천은 두 형태를 모두 쓰며(lpranging은 저장소 상대, 수입 코퍼스 레시피 50개는 외부), 각 레시피 README가 고른 형태와 이유를 적게 한다.
