---
id: https://agentic-knowledge-base.dev/id/chunk/6a1f743e-95a2-4413-ba48-81c316af6eb0
type: decision
level: logical
title_ko: 수준마다 판정이 다르므로 청크가 다르다
title: Different judgements per level require different chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/9acf3e73-f933-4260-9b42-432825013b6c
---
**근거** (노트 7.2절, 6.2절, 9.10절) — abstract는 변수의 선언이 온톨로지 어휘만 쓰는가로, logical은 후보에 범위·제약·배제 근거가 있는가로, concrete는 표본 근거와 배제 근거가 있는가로 판정된다 (6.8절 게이트). 판정이 다른 것을 한 청크에 두면 한 수준의 실패가 다른 수준을 `draft`로 끌어내린다. `refines`로 잇기 때문에 전방 추적 커버리지(7.1절)이 결정 안에서도 계산된다.

이 저장소가 abstract 청크를 `-space` 있는 결정에만 두는 이유 — 변수 선언은 후보가 여럿일 때 의미가 있고(9.10절 변수 하나 = 파일 하나), 후보가 하나뿐인 결정에 빈 abstract를 강제하면 자립성 없는 청크가 늘어난다 (4.13절 파편화).
