---
id: https://agentic-knowledge-base.dev/id/chunk/ad544be2-8940-47c2-b038-9639b32b88c5
type: decision
level: logical
title_ko: 선호에 의한 기각과 수치 등급의 기각
title: Rejecting elimination by preference and numeric grades
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-10-24T02:22:01+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4
---
**대안** — 선호로 후보를 기각하는 안은 기각한다. 선호는 후보가 여럿 남았을 때 보여 주는 순서만 정하고, 기각은 제약이 한다(9.9절).

**대안** — 선호를 수치 등급으로 두는 안은 기각한다. 수치 등급을 두면 캘리브레이션 문제가 그대로 돌아오므로, 순서의 원본은 부분순서와 이유 문자열이고 믿음 정도는 순서가 없는 두 후보의 동률만 깬다(9.2절, 9.9절, Q109-b).

**대안** — 믿음 정도로 부분순서를 덮는 안은 기각한다. 믿음 정도는 아직 보정되지 않아 이유 문자열이 붙은 순서를 덮을 근거가 없으므로, 동률 깨기에만 쓴다(Q109-b).
