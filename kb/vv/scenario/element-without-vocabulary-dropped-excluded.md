---
id: https://agentic-knowledge-base.dev/id/chunk/013324e4-24e4-4e3e-8fd9-49379692450c
type: decision
level: abstract
title_ko: 시나리오 배제 자극 — 어휘에 슬롯이 없는 요소의 반영에서 다루지 않는 것
title: Scenario excluded stimuli — what reflecting an element with no slot in the vocabulary does not cover
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T06:20:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/886c9bad-f13a-48af-bd5e-aa6afa92a572
---
**배제 자극** — 다루지 않는 자극은 셋이다.

- 어휘 밖 `agt:` 술어를 담은 데이터 그래프는 이 부류가 다루지 않는다. `vocab` 검사가 이미 거부하고 그 자리는 부류 `foreign-vocabulary-rejected`가 덮는다.
- 사람이 어휘를 먼저 확장한 뒤의 반영은 다루지 않는다. 확장 신호가 올라간 경로에서는 탈락이 성립하지 않는다.
- 방출기가 아는 요소인데 shape가 없어 검사되지 않는 경우는 다른 부류가 덮는다. 이 부류는 슬롯의 부재만 자극하고 검사의 부재는 자극하지 않는다.
