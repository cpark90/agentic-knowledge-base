---
id: https://agentic-knowledge-base.dev/id/chunk/ba003973-ba31-4f98-8af2-8958c13a979d
type: requirement
level: functional
pattern: event-driven
title_ko: 확률 모델이 확률을 내면 체계는 그 출력을 확정 지식과 게이트로 검사하여야 한다
title: When the probabilistic model emits probabilities, the system shall check its output against settled knowledge and gates
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/comp-req-accumulation
---
**요구** — 확률적 지식 모델이 링크·결정 후보·질의의 답에 확률을 내면, 체계는 그 출력을 확정 항목과 게이트로 검사하여야 한다.

- **이해관계자**: 업체 · 검증자 · **관심사**: 본 적 없는 질의에 답하되 근거로 되짚을 수 있는 지식
- **출처**: 유저 지시 2026-10-22, 유저 답 Q88(a·b·d) · Q89-a

질의의 답은 분포로 내고 그 근거로 지식을 인용한다(Q88-d). 확정의 권한은 r-011의 개정이 정한 대로 증거 기록 규칙과 게이트에 남고, 확률은 그 곁에 병기된다(Q87-b, Q90-a).

**폐기** — 별도의 학습 모델을 전제로 한 요구였고, 유저가 2026-10-24에 그 전제를 지웠다(Q-0063#Q156, Q156-b). 질의에 대한 답의 분포(Q88-d)는 믿음 정도에서 유도한 분포로 읽고, 요구를 두지 않는다(Q-0063#Q154).
