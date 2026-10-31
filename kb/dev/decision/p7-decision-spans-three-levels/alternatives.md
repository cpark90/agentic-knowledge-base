---
id: https://agentic-knowledge-base.dev/id/chunk/87912c85-9a5e-4d3a-a410-b092a59b2735
type: decision
level: logical
title_ko: 수준 통합 단위 지식은 기각되고 전 결정 abstract 강제는 -space 도입까지 보류된다
former_title_ko: ["수준 통합 청크는 기각되고 전 결정 abstract 강제는 -space 도입까지 보류된다", "수준 통합 지식 항목은 기각되고 전 결정 abstract 강제는 -space 도입까지 보류된다"]
title: Single-chunk decisions are rejected; mandatory abstract chunks are deferred until -space arrives
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-30T16:05:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:33:38+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/9acf3e73-f933-4260-9b42-432825013b6c
---
**대안** — 한 결정을 수준 구분 없는 하나의 결정(ADR 한 장)으로 두는 안(이 저장소의 옛 결정 트리이고, 지금은 git 역사에만 있다). 기각 — 변수·후보·값의 판정이 섞여 게이트가 수준별로 실패를 잡을 수 없고, `refines` 연쇄가 결정 안에서 끊긴다 (노트 7.2절, 6.8절).

**대안** — 모든 결정에 abstract 변수를 강제하는 안. 보류 — 후보가 하나뿐인 결정에서는 빈 단위 지식이 되므로 `-space`가 있을 때만 만든다 (유저 결정 2026-09-10, Q1(a)). `-space`가 도입되면(도입 5단계) 재검토한다.
