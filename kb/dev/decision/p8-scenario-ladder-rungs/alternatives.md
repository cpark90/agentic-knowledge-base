---
id: https://agentic-knowledge-base.dev/id/chunk/8066865c-a0c4-4bcd-a509-27abb002a366
type: decision
level: logical
title_ko: 선택적 검증 대응물과 ODD 밖 변수의 기각
title: Rejecting optional rungs and out-of-ODD variables
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T20:16:58+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T20:17:35+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/0ef3233e-c6aa-434b-a0ef-350c857e690e
---
**대안** — 검증 대응물을 선택으로 두어 V&V가 개발 뒤에 오게 하는 안. 기각 — 같은 높이의 대응물이 없으면 개발 게이트가 다음 높이로 못 내려간다. 이것이 의도된 압력이다 (8.3절, 8.19절).

**대안** — verify 질의를 "주어가 기준이거나 기준을 `refines`한다"로 넓혀 기준마다 같은 높이의 결정을 `verifies`하게 하는 안(Q30-a). 기각 (유저 결정 2026-10-04, Q30-b) — 기준 38마다 새 링크가 필요하고 기준이 검증 주어와 바인딩 속성을 겸해 `p8-pass-criteria`의 "기준은 `verifies` 링크의 속성"과 어긋난다. 기준 → 목표 `refines`가 같은 대응을 이미 남긴다.

**대안** — 시나리오 변수를 ODD 밖 속성에서도 잡는 안. 기각 — 게이트가 거부한다. ODD 밖 자극은 `odd:outside` 태그로만 존재하고 커버리지에 들지 않는다 (8.3절).
