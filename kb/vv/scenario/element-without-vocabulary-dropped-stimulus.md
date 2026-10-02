---
id: https://agentic-knowledge-base.dev/id/chunk/4add0b57-4550-4459-9513-179a53525343
type: decision
level: abstract
title_ko: 시나리오 자극 — 어휘에 슬롯이 없는 요소를 담은 소스의 반영
title: Scenario stimulus — reflecting a source that carries an element with no slot in the vocabulary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/b055c55f-c77b-421f-8cc0-d1e832f7b207]
part_of: https://agentic-knowledge-base.dev/id/composite/886c9bad-f13a-48af-bd5e-aa6afa92a572
composite: {id: https://agentic-knowledge-base.dev/id/composite/886c9bad-f13a-48af-bd5e-aa6afa92a572, title_ko: 어휘에 슬롯이 없는 요소를 담은 소스의 반영, title: Reflecting a source that carries an element with no slot in the vocabulary, ordered: [https://agentic-knowledge-base.dev/id/chunk/4add0b57-4550-4459-9513-179a53525343, https://agentic-knowledge-base.dev/id/chunk/40b0436b-4cd7-4fc2-abce-c2daa47e5b18, https://agentic-knowledge-base.dev/id/chunk/013324e4-24e4-4e3e-8fd9-49379692450c]}
---
**자극** — 부류의 자극은 방출기가 아는 요소 집합 밖의 요소를 소스에 넣고 방출을 돌린 뒤 산출물에서 그 요소를 찾는 것이다. actor는 소스를 저작하는 에이전트이고 action은 알려진 키·실체 집합 밖의 요소를 하나 더해 head 그래프를 생성하는 것이다. 순서는 어휘 밖 요소 저작 → 방출 실행 → 소스 전수와 방출 전수의 대조이고, `keep()`은 그 요소를 뺀 나머지 frontmatter와 방출기가 읽는 어휘 목록이다.

변수는 ODD 속성 둘이다. `id:cond-language-policy`(언어 정책)가 요소 이름의 허용 범위를 가르고, `id:cond-repo-layout`(저장소 구조)이 그 요소가 어느 모듈의 어휘에 속해야 하는지를 가른다. 범위는 logical 높이에서 채운다.
