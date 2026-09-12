---
id: https://agentic-knowledge-base.dev/id/chunk/6a32ff4f-beb8-4013-b563-bf9c283d96a5
type: decision
level: logical
title_ko: 셋을 섞으면 무효화 범위가 흐려진다
title: Conflating the three blurs the scope of invalidation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/82fb12dd-6188-4e06-bae7-e86e699ac5fe
---
**근거** (노트 9.3절) — 셋은 수명과 파급이 다르다. 공리를 고치면 온톨로지 전체의 링크가 재검토 대상이 되고, 제약을 완화하면 그 설계 공간의 후보 집합만 늘며, 가정이 깨지면 `assumes`를 타고 그 가정에 선 항목만 무효화된다 (6.5절).

셋을 한 곳에 섞어 적으면 "무엇이 깨졌을 때 무엇을 다시 보아야 하는가"를 답할 수 없다. 위치를 분리하는 것이 전수조사 없는 무효화의 전제다.
