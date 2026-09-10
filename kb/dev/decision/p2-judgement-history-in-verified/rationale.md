---
id: https://agentic-knowledge-base.dev/id/chunk/e11c495f-94e3-4baa-bd8e-644700bb601c
type: decision
level: logical
title_ko: 판정을 버리면 재판정이 매번 처음부터 시작하고 판정자를 측정할 수 없다
title: Discarded judgements make re-judgement start from zero and leave the judge unmeasured
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/eec68e02-3a0a-459a-9357-0c6cb85e8267
---
**근거** (노트 2.12절) — 판정 결과를 통과/실패의 일회 신호로 쓰면 두 가지를 잃는다. 재판정할 때 이전 판정과 비교할 대상이 없고, 판정자가 시간에 따라 달라졌는지 측정할 재료가 없다. 판정자가 학습된 것이면 후자가 특히 문제다 — 드리프트를 관측하지 못하면 판정 자체의 신뢰가 근거 없이 유지된다.

누적 위치가 청크 head인 이유는 판정이 청크에 대한 것이고, head가 이미 상태·출처를 싣는 자리이기 때문이다.

**필드를 새로 만들지 않는다** — 유저 결정 C6에 따라 노트의 `trust`는 OKF `verified` 목록과 같은 것으로 확정되었다. 같은 개념에 두 이름을 두는 것은 0.0절 동음·이명 회피 위반이며, 2.10절 "동의어를 별개 클래스로"가 잡아야 할 결함이다.
