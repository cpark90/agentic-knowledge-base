---
id: https://agentic-knowledge-base.dev/id/chunk/d8ec49ca-9a20-4402-b47f-9affa7c93d32
type: decision
level: logical
title_ko: 관계를 지어내면 표준 질의가 이 그래프를 지나친다
title: Bespoke relations make standard queries miss this graph
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ad815628-628e-40a9-a3da-05db0480bb7e
---
**근거** (노트 2.8절) — 개념에 적용한 0.0절 표준어 원칙이 관계에도 그대로 적용된다. 관계를 지어내면 외부 도구와 외부 온톨로지의 질의가 이 그래프를 지나친다.

`subPropertyOf`로 매다는 것이 실질적 이득이다 — 2.9절 RL 프로파일이 `subPropertyOf`를 전파하므로, `ro:realizes`로 물으면 `agt:satisfies` 트리플이 추론으로 함께 걸린다. 매달지 않으면 고유 관계는 표준 세계에서 보이지 않는 섬이 된다.

셋만 고유로 남는 것은 이 체계가 추적성에 고유한 부분이 그 셋뿐이라는 뜻이다. 그보다 많아지면 표준 검토가 부족했다는 신호다.
