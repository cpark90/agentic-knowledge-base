---
id: https://agentic-knowledge-base.dev/id/chunk/fe5f0125-8adf-4cbe-b020-ff9484db8cde
type: decision
level: logical
title_ko: V&V 프로파일 없이는 검증 목표를 파생할 부류가 없다
title: Without a V&V profile there are no classes to derive verification goals from
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d834336a-9ec4-465b-b0e4-f44bc557677f
---
**근거** (노트 2.11절 `[확정]`, 8.21절) — 노트가 순서의 이유를 직접 적는다. V&V 프로파일 없이는 검증 목표를 파생할 부류가 없다.

- 위험 분석의 G5 산출물이 시나리오 부류이고, 시나리오는 부류에서 시작한다(`p8-risk-analysis-profile` 대안 청크). 부류가 없으면 시나리오가 어느 요인을 노출하려는지의 근거가 없다.
- 개발이 먼저 진행되고 V&V 실체가 뒤따르면 개발 결정에 대응할 검증 목표가 그 사이에 비어 있다. 나란히 수행하는 것이 노트가 허용하는 가장 늦은 시점이다.
- 두 부분을 같은 프로파일의 부분으로 두는 이유는 두 실체가 같은 도메인을 기술하기 때문이다. 개발 실체는 무엇을 만드는가를, V&V 실체는 그것이 어떻게 실패하는가를 담는다.
