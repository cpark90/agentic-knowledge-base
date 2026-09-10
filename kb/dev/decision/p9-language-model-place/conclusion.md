---
id: https://agentic-knowledge-base.dev/id/chunk/51d32aac-c242-4615-a0dc-b651565bddde
type: decision
level: concrete
title_ko: 언어모델은 후보와 선호 순서를 제안할 뿐이고 선호의 기본은 장부의 종류 서열이다
title: The language model only proposes candidates and preference order; default preference comes from the ledger kind ranking
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/a6dd335e-3bb8-41b4-9c4c-2745b90b5188, title_ko: 언어모델의 자리, title: The place of the language model}
part_of: https://agentic-knowledge-base.dev/id/composite/a6dd335e-3bb8-41b4-9c4c-2745b90b5188
---
**결론** — 언어모델의 확률적 추론은 두 곳에만 쓴다 — **후보를 제안**하고(장부에 `kind: proposal`, 극성 +, 확정 근거 아님), 후보가 여럿일 때 **선호 순서를 제안**한다(9.9절 부분순서, 이유 문자열 필수). 확정·기각·상태 전이는 장부 규칙이 한다. 이것이 2.5절 "에이전트는 센서"의 링크판이다.

선호는 장부에서 파생될 수 있다. 지지 증거의 종류 서열(구축 > 실행 > 동시 편집 > 공동 커버 > 임베딩 > 세션)로 후보를 정렬한 것이 기본 선호이고, 언어모델의 제안은 이를 덮지 못하고 동률만 깬다 (노트 9.11절). 이 저장소: 증거 종류 `agt:proposal`, `agt:counterfactualTest` 폐기 (Q10).
