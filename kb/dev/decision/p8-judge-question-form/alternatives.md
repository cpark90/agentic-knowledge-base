---
id: https://agentic-knowledge-base.dev/id/chunk/00834b82-cb01-4a17-a3a9-8e349e9846b8
type: decision
level: logical
title_ko: 자유 서술 리뷰·단일 임계·즉시 게이트 차단 안은 기각된다
title: Free-form review, a single threshold, and immediate gate blocking are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a5873a98-652e-4341-b229-b3ef6a05e702
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 판정자에게 자유 서술 리뷰를 시킨다 | 재현되지 않고 사람 라벨과 대조할 형식이 없다. `verification-means-trust`의 측정이 성립하지 않는다 |
| 확신도 임계를 하나만 둔다 | 임계 아래를 전부 사람에게 보내면 자동화의 값이 없고, 전부 보류하면 판정이 멈춘다. 오답 비용이 구간마다 다르다 |
| 라벨링 없이 바로 게이트로 차단한다 | 판정자의 정확도를 모르는 채로 지식을 막는다. 게이트 실패는 수정 방향이어야 하는데 근거가 없다 |
| 계산·날짜 검사도 판정자에게 맡긴다 | 확정적으로 판정되는 것을 확률로 바꾼다. 그 검사는 lint와 분석 시점이 이미 정확하게 한다 |
