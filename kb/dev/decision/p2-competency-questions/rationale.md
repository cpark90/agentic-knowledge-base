---
id: https://agentic-knowledge-base.dev/id/chunk/a6d691f9-0dd6-4bc3-8dc3-bbf299b3563f
type: decision
level: logical
title_ko: 질의로 답할 수 없는 개념은 늘기만 하고 검사되지 않는다
title: Concepts no query can use only accumulate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5f6eadd5-ef4f-47cb-8128-f72cca5e8575
---
**근거** (노트 2.7절) — 온톨로지에 "무엇이 빠졌는가"를 판정할 기준이 없으면 개념은 늘기만 한다. 역량 질문은 온톨로지 공학의 표준 관행이고, 이 체계에서는 두 방향으로 쓰인다 — 충분성 검사(질문에 답하지 못하면 개념이 모자란다)와 과설계 검사(어느 질문에도 기여하지 않으면 개념이 남는다, 2.10절).

각 질문이 질의 하나로 답해야 한다는 제약이 어휘를 실용에 묶는다. 답이 여러 질의의 조합이나 사람의 해석을 요구하면 그 개념은 아직 형식화되지 않은 것이다.

CQ19·CQ20은 r-008 정제 완주와 r-009 후방 추적 귀속을 온톨로지 요구로 옮긴 것이다. 추적 매트릭스의 빈 칸(CQ7)이 그 답을 눈으로 보여준다.
