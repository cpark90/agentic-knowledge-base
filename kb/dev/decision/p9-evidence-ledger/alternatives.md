---
id: https://agentic-knowledge-base.dev/id/chunk/aa5949c4-b69d-4388-be81-f640d3a57169
type: decision
level: logical
title_ko: 수치 신뢰도와 확률 합산의 기각
title: Rejecting numeric confidence and probabilistic aggregation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/05abd2cf-de1b-4aa2-9559-10cb0f868dab
---
**대안** — 링크에 0~1 신뢰도를 두고 증거를 확률로 합산하는 안(이 저장소 `agt:confidence`, `dependency-graph-design.md` §2.3). 기각·폐기 — 캘리브레이션 불가, 재판정 불가. 선호는 종류 서열에서 파생된다 (노트 9.11절, 유저 결정 2026-09-10 Q8).

**대안** — 반박이 있어도 지지가 많으면 확정하는 안(다수결). 기각 — 반례 하나는 지지 여럿을 이긴다. ±공존은 사람 큐다 (노트 9.11절).
