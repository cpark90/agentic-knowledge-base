---
id: https://agentic-knowledge-base.dev/id/chunk/24bf5c57-22a5-411f-8bdb-a4be933fb5e7
type: requirement
level: functional
pattern: ubiquitous
title_ko: 확정된 지식은 확률 모델의 학습 데이터와 검증 기준으로 내보낼 수 있어야 한다
title: Settled knowledge shall be exportable as training data and validation reference for a probabilistic model
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}
part_of: https://agentic-knowledge-base.dev/id/comp-req-accumulation
---
**요구** — 체계는 확정된 항목·링크·관측을 확률적 지식 모델의 학습 데이터와 그 출력을 검사하는 기준으로 내보낼 수 있어야 한다.

- **이해관계자**: 업체 · **관심사**: 표 형식의 지식에서 확률로 답하는 지식으로
- **출처**: 유저 지시 2026-10-22("위키가 타뷸러 방식의 모델이라하면 딥러닝기반 방식으로 확률적인 지식의 모델링을 하는것이 목적"), 유저 답 Q87-a·Q89-a

확정된 지식 베이스는 모델을 대신하지 않고 모델의 재료이자 기준이 된다. 내보내는 단위와 형식은 결정이 정한다.

**폐기** — 별도의 학습 모델을 전제로 한 요구였고, 유저가 2026-10-24에 그 전제를 지웠다(Q-0063#Q156, Q156-b). 출처의 Q87-a는 hci의 오독으로 폐기됐다(Q-0063#Q154).
