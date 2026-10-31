---
id: https://agentic-knowledge-base.dev/id/chunk/51d32aac-c242-4615-a0dc-b651565bddde
type: decision
level: concrete
title_ko: 언어모델은 후보와 선호 순서를 제안하고 판정할 뿐 확정하지 않으며 선호의 기본은 증거 기록의 종류 서열이다
title: The language model proposes candidates and preference order and judges, but never settles; default preference comes from the ledger kind ranking
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-10-24T17:17:21+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/a6dd335e-3bb8-41b4-9c4c-2745b90b5188, title_ko: 언어모델의 자리, title: The place of the language model}
part_of: https://agentic-knowledge-base.dev/id/composite/a6dd335e-3bb8-41b4-9c4c-2745b90b5188
---
**결론** — 언어모델의 확률적 추론은 다음 세 곳에만 쓴다. 이것이 2.5절 "에이전트는 센서"의 링크판이다.

1. **후보를 제안한다.** 제안은 증거 기록에 종류 `proposal`과 극성 지지로 적히고, 확정 근거가 아니다.
1. 후보가 여럿일 때 **선호 순서를 제안한다.** 제안은 9.9절의 부분순서를 따르고 이유 문자열을 반드시 붙인다.
1. **판정한다.** 판정은 `p8-judge-session-agreement`의 규칙대로 한다. 세션 둘이 답하고, 임계는 일치율이며, 기계 환원이 먼저다. 판정 결과는 증거 기록에 종류 "판정"으로 확신도와 함께 적히고, 확정 근거가 아니다.

확정과 기각, 상태 전이는 지금처럼 증거 기록 규칙이 한다. 이 결정은 링크와 후보의 처리에 걸린다.

선호는 증거 기록에서 파생될 수 있다. 지지 증거의 종류 서열로 후보를 정렬한 것이 기본 선호다. 서열은 구축, 실행, 동시 편집, 공동 커버, 판정, 임베딩, 세션의 차례이고, 언어모델의 제안은 기본 선호를 덮지 못한다(노트 9.11절). 기본 선호에서 순서가 없는 두 후보는 믿음 정도가 먼저 동률을 깨고, 믿음 정도가 같거나 없으면 언어모델의 제안이 깬다(`p9-preference-partial-order`). 이 저장소의 증거 종류는 `agt:proposal`과 `agt:judgement`이고, `agt:counterfactualTest`는 폐기했다(Q10, 유저 결정 Q-0056 Q118-a).
