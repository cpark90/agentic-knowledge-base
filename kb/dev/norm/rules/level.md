---
id: https://agentic-knowledge-base.dev/id/chunk/73572326-f442-4f1f-b7dc-2abb6864f428
type: norm
level: logical
title_ko: docs/rules.md 절 — level, 정제 수준과 지식 종류별 허용 수준 표
title: docs/rules.md section — level, refinement levels and the occupancy table
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:08+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
heading: level — 정제 수준과 지식 종류별 허용 수준 표
depth: 3
form: table
columns: [plane, 허용 level]
items: [p6-plane-level-occupancy#1, p6-plane-level-occupancy#2, p6-plane-level-occupancy#3, p6-plane-level-occupancy#4, p6-plane-level-occupancy#5, p6-plane-level-occupancy#6, p6-plane-level-occupancy#7]
---
v3가 `level` 키를 **정제 수준**으로 재정의했다 (노트 6.4절). 다섯 수준은 요구만 있는 `functional`,
형식 문장만 있고 도메인이 없는 `abstract`, 후보와 제약을 담는 `logical`, 확정된 개체를 담는 `concrete`, 동작만 남은
`executable`이고, 이 다섯 단계는 유지하며 건너뛰지 않는다.

**모든 지식 종류가 모든 정제 수준에 놓일 수 있는 것은 아니다.** 그래서 지식 종류별 허용 수준 표를 SHACL로 강제한다
(`kb/ontology/shapes/residency-shapes.ttl`).
