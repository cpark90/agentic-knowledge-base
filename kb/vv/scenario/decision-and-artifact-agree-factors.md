---
id: https://agentic-knowledge-base.dev/id/chunk/6aca2592-1d64-42f7-b6df-f4437224c90a
type: decision
level: abstract
title_ko: 시나리오 요인 — 결정 본문과 산출물이 어긋난 편집이 노출하는 현상
title: Scenario factors — the phenomena exposed by an edit that makes the decision body and the artefact disagree
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-mast-failure-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-links-only-interaction, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/reasoningActionMismatch, https://agentic-knowledge-base.dev/agt/labelRot]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/65c71b3f-efa7-47bb-b4fa-f7b491e99078
specializationOf: https://agentic-knowledge-base.dev/id/chunk/fb826dc5-88fa-4bbb-bf98-7536fc095df7
---
**요인** — 노출하려는 현상은 `agt:reasoningActionMismatch`(P16)가 주이고 `agt:labelRot`(P14)이 부다. 앞은 항목 사이의 어긋남이고 뒤는 한 항목 안 라벨과 본문의 어긋남이므로 같은 편집이 둘을 함께 만든다.

주입하는 한정자는 `agt:incorrectQualifier` 하나다. 산출물이 없는 것이 아니라 결정과 다른 것을 하는 것이 이 부류의 결함 형태다. 부류가 주입하는 것은 어긋난 내용이고, 편집이 링크와 라벨을 재판정 대상으로 만드는가를 묻는다.

기여하는 검증 목표는 `kb/vv/goal/decision-and-artifact-agree.md`(`https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a`)다. 결정 본문이 바뀌면 그것을 충족한다고 적힌 산출물이 재판정 대상이 되는가를 이 부류가 자극한다.

미확정: 결정 본문과 산출물의 어긋남을 재는 관측 수단이 없다. 개발 KB의 `artifact`가 3건이라 자극을 걸 표면이 좁다.
