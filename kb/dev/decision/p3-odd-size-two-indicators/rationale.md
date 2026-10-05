---
id: https://agentic-knowledge-base.dev/id/chunk/93d8f258-42a5-45b8-904d-9d0b36d0748d
type: decision
level: logical
title_ko: 참조되지 않는 조건은 과대의 신호이고 가정을 못 적는 항목은 과소의 신호다
title: An unreferenced condition signals oversize; an item that cannot state its assumption signals undersize
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-05T23:21:44+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e14838e7-3b70-4325-84b9-d5b69377bc39
---
**근거** — ODD가 작으면 파생물(스코프·가정·시나리오)이 참조할 속성이 부족해 지식을 만들 수 없다. 크면 커버리지 분모가 커져 같은 시나리오 집합의 커버리지가 떨어지고 대조·유지 비용이 는다(p8-coverage-metrics). 참조되지 않는 조건이 과대의 신호이고 가정을 못 적는 항목이 과소의 신호다. 두 신호를 지표로 재면 ODD를 늘릴 때와 줄일 때가 갈린다. 판정 기준이 없으면 ODD는 한 방향으로만 자란다.
