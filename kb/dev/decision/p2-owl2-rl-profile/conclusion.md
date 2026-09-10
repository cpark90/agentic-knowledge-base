---
id: https://agentic-knowledge-base.dev/id/chunk/bcf9106c-2d8a-4866-89ad-e40d05489672
type: decision
level: concrete
title_ko: 검사 게이트와 무효화 전파는 RL 안에서 동작한다
title: Gate and invalidation propagation run inside RL
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0054]
part_of: https://agentic-knowledge-base.dev/id/composite/4863dfa7-90c7-471e-b5ac-84e0ca2011c8
composite: {id: https://agentic-knowledge-base.dev/id/composite/4863dfa7-90c7-471e-b5ac-84e0ca2011c8, title_ko: 추론은 OWL 2 RL로 제한한다, title: Limit reasoning to the OWL 2 RL profile}
---
**결론** — 어떤 추론을 허용할지 정해야 검사와 질의의 비용이 예측된다. **OWL 2 RL을 채택한다.** 규칙 기반, 다항 시간이며 `part-of` 이행성과 `subPropertyOf` 전파를 준다. `defect-rules`와 같은 엔진을 쓴다.

**검사 게이트(6.7절)와 무효화 전파(6.5절)는 RL 프로파일 안에서 동작해야 한다.** 그 밖의 추론은 배치로 돌린다.
