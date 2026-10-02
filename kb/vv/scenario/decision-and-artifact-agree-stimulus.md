---
id: https://agentic-knowledge-base.dev/id/chunk/fb826dc5-88fa-4bbb-bf98-7536fc095df7
type: decision
level: abstract
title_ko: 시나리오 자극 — 결정 본문과 산출물이 어긋난 편집
title: Scenario stimulus — an edit that makes the decision body and the artefact disagree
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-links-only-interaction, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a]
part_of: https://agentic-knowledge-base.dev/id/composite/65c71b3f-efa7-47bb-b4fa-f7b491e99078
composite: {id: https://agentic-knowledge-base.dev/id/composite/65c71b3f-efa7-47bb-b4fa-f7b491e99078, title_ko: 결정 본문과 산출물이 어긋난 편집, title: An edit that makes the decision body and the artefact disagree, ordered: [https://agentic-knowledge-base.dev/id/chunk/fb826dc5-88fa-4bbb-bf98-7536fc095df7, https://agentic-knowledge-base.dev/id/chunk/6aca2592-1d64-42f7-b6df-f4437224c90a, https://agentic-knowledge-base.dev/id/chunk/5e0b0569-58c0-4450-83b6-62841414f57e]}
---
**자극** — 부류의 자극은 결정 결론의 본문을 고치고 그 결론을 `satisfies` 하는 산출물과 결론의 라벨은 고치지 않는 것이다. actor는 결정 결론을 편집하는 에이전트이고 action은 본문만 고치고 라벨·산출물은 그대로 두는 것이다. 순서는 본문 편집 → 라벨·산출물 방치이고, `keep()`은 편집 뒤에도 유지되는 라벨과 `satisfies` 링크다.

변수는 ODD 속성 둘이다. `id:cond-repo-layout`(저장소 구조 — 한 청크는 한 파일이고 링크가 `deps` 다)이 어긋남이 빌드 그래프에 보이는지를 가르고, `id:cond-language-policy`(언어 정책 — 라벨은 한·영 1:1)가 라벨 검사의 대상 범위를 가른다.
