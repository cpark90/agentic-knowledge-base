---
id: https://agentic-knowledge-base.dev/id/chunk/b79a0835-5b59-4d17-a11e-3799daea778b
type: decision
level: logical
title_ko: 서비스 층의 범위 변수를 abstract 결정으로 두는 근거
title: Why the variable of the service layer's reach is an abstract decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/23f8d9d8-ce9f-42c2-8f69-3f39abc5e09a
---
**근거** — 결정의 abstract 정제 수준은 결정 변수의 선언이다(`p6-plane-level-occupancy`, `p7-decision-spans-three-levels`). 결정 `p9-candidate-storage`에 따라 설계 공간의 확정 후보는 출발 항목을 head에서 `refines`해야 하는데, 앞의 출발인 `p0-service-is-a-three-layer-wiki`의 결론은 concrete라 어떤 결정도 그것을 `refines`할 수 없었다. 그래서 이 변수를 abstract 결론으로 떼어 출발로 두고, 그 concrete 결론이 이 결론을 정제하게 한다. 유저는 확정이 생길 때 만든다는 Q93-c를 바꿔 이 결정을 지금 만들기로 했다(유저 결정 Q-0055 Q112-b, 2026-10-24).

이 결론이 정제하는 요구 `r-001`에는 V&V 검증 목표 `domain-knowledge-as-vocabulary`가 있다. 따라서 게이트 `rung-before-descent`가 기능 수준에서 추상 수준으로 내려가는 정제에 요구하는 대응물을 갖춘다.
