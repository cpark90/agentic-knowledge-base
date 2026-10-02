---
id: https://agentic-knowledge-base.dev/id/chunk/40b0436b-4cd7-4fc2-abce-c2daa47e5b18
type: decision
level: abstract
title_ko: 시나리오 요인 — 어휘에 슬롯이 없는 요소의 반영이 노출하는 현상
title: Scenario factors — the phenomenon exposed by reflecting an element with no slot in the vocabulary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/elementWithoutVocabularyDropped]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/886c9bad-f13a-48af-bd5e-aa6afa92a572
---
**요인** — 노출하려는 현상은 `agt:elementWithoutVocabularyDropped`(P19) 하나다. 등급은 S3·E2·D3이고 인과는 `agt:coverageImpact`다. 빠진 요소는 커버리지의 분모에도 오르지 않으므로 탈락이 커버리지를 높게 보이게 한다.

주입하는 한정자는 `agt:missingQualifier` 하나다. 요소의 어휘가 틀린 것이 아니라 없는 것이 이 부류의 결함 형태다. 어휘 밖 술어를 쓴 그래프는 `vocab` 검사가 이미 거부하므로 이 부류가 자극하는 자리는 검사가 보지 않는 둘, 곧 frontmatter 키와 실체 표다.

기여하는 검증 목표는 `kb/vv/goal/element-without-vocabulary-dropped.md`(`https://agentic-knowledge-base.dev/id/chunk/b055c55f-c77b-421f-8cc0-d1e832f7b207`)다. 표본 근거는 참조 저장소 `../harness-functional`의 실패 R3이며 그 저장소는 내용의 원천이고 빌드 의존이 아니다.
