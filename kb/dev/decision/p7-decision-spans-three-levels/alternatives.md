---
id: https://agentic-knowledge-base.dev/id/chunk/87912c85-9a5e-4d3a-a410-b092a59b2735
type: decision
level: logical
title_ko: 수준 통합 청크와 전 결정 abstract 강제의 기각
title: Rejecting single-chunk decisions and mandatory abstract chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/9acf3e73-f933-4260-9b42-432825013b6c
---
**대안** — 한 결정을 수준 구분 없는 하나의 결정 청크(ADR 한 장)로 두는 안(이 저장소의 옛 `chunks/decision/`). 기각 — 변수·후보·값의 판정이 섞여 게이트가 수준별로 실패를 잡을 수 없고, `refines` 연쇄가 결정 안에서 끊긴다 (노트 7.2절, 6.8절).

**대안** — 모든 결정에 abstract 변수 청크를 강제하는 안. 보류 — 후보가 하나뿐인 결정에서는 빈 청크가 되므로 `-space`가 있을 때만 만든다 (유저 결정 2026-09-10, Q1(a)). `-space`가 도입되면(도입 5단계) 재검토한다.
