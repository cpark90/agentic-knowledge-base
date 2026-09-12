---
id: https://agentic-knowledge-base.dev/id/chunk/17415ccd-8911-48bc-87dd-ce547417ac77
type: decision
level: logical
title_ko: 분해해야 42줄 4~5개 계산이 성립하는지 알 수 있다
title: Only a breakdown shows whether 42x4-5 actually holds
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ee6bf20f-7b60-4ee8-8681-af13f995682d
---
**근거** (노트 1.1·1.4절) — 200줄 밖은 에이전트에게 없는 것과 같다. 그래서 무엇을
보게 할지가 곧 무엇을 판단하게 할지이고, 조망 단위(42줄 청크 4~5개)가 정해져
있어야 무엇이 들어오고 무엇이 빠졌는지 셀 수 있다.

그러나 200줄에는 하네스 지시·툴 출력·대화 이력도 실린다. 예산을 분해하지 않으면
"42줄 청크 4~5개"라는 계산이 실제로 성립하는지 알 수 없다 — 분해표가 있어야 각
항목의 통제 수단이 정해지고, 실측(17번 미해결)이 어느 항목을 재야 하는지가
정해진다.
