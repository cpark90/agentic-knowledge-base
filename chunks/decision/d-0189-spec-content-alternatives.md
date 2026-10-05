---
id: https://agentic-knowledge-base.dev/id/chunk-d0189
type: decision
level: concrete
title_ko: 대안 — 명세가 담는 것
title: Alternatives — what a specification carries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:56+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T21:15:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-spec-content
---
**대안** — 묶음의 세 결정마다 원천(harness-concrete `docs/recipes-design.md`·`docs/composition-methodology.md`)이 대비한 안을 적는다.

- d-0183(참조만 담는다): 레시피가 구체 빌드 문서(도구 코드·표준 문서·스킬 본문)를 직접 저장하는 안은 기각이다. 원천은 그것을 vendoring이라 부르고, 구현은 참조되어 빌드에서 재생성될 뿐 명세에 저장하지 않는다고 정한다(recipes-design "What a recipe stores", ODR INV-1).
- d-0184(도달 범위): 해석되지 않는 참조를 빌드 실패로 처리하는 안은 기각이고 `.ref` 스텁으로 강등한다(recipes-design 같은 절). 저장소 상대 참조와 외부 참조는 기각 관계가 아니다. 원천은 두 형태를 모두 쓰며(lpranging은 저장소 상대, 수입 코퍼스 레시피 50개는 외부) 각 레시피 README가 고른 형태와 이유를 적게 한다.
- d-0185(조율 방식): 체계 전역에 조율 방식 하나를 고정하는 안은 기각이다. 하네스가 채널을 고르거나 선언하므로 전역 위상이 강제되지 않고, orchestrator-workers와 peer-mesh가 공존한다. 새 방식을 TBox 변경으로 들이는 안도 기각이고, 패턴과 채널 개체 한 쌍과 그것을 문 하네스를 더한다(composition-methodology "Coordination topology").
