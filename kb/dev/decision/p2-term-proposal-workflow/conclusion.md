---
id: https://agentic-knowledge-base.dev/id/chunk/4754eb68-ad27-45ad-912c-0385087cd063
type: decision
level: concrete
title_ko: 에이전트가 제안하고 컴파일러가 거르고 사람이 승인한다
title: The agent proposes, the compiler filters, a human approves
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-27T10:05:05+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-27T10:05:05+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
part_of: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b
composite: {id: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b, title_ko: 용어 제안 워크플로, title: Term proposal workflow}
---
**결론** — 일반화(6.3절)이 온톨로지에 닿을 때의 절차. OBO 진영에서 운영되는 흐름의 구조를 쓰고, 입력과 검사는 이 저장소의 도구가 맡는다(Q175-a).

1. 에이전트가 관측에서 개념 후보를 뽑아 `term_propose`의 명령행 인자로 준다 — ID · 종류 · 라벨 ko/en · 정의(속 + 종차) · 상위 개념 · 기여하는 역량 질문 · 근거 관측 둘 이상
1. `term_propose`가 상위 개념 실재, 항·라벨 중복, 정의 형식, 케밥 ID, 근거 실재를 검사하고, 통과한 것만 제안 TTL `kb/ontology/proposals/<id>-proposal.ttl`로 써서 **유저 승인 큐**에 올린다. 근거는 `prov:wasDerivedFrom`으로 제안에 함께 적힌다
1. 승인되면 **코어가 아닌 확장 모듈**에 새 파일로 옮긴다
1. 옮긴 파일은 모듈의 일부로 **2.5절 온톨로지 검사 3단계**를 받는다

**제안은 승인되어 모듈 파일이 되면서 다른 지식과 같은 규칙을 받는다.** 승인 큐는 `//kb/ontology:modules` 밖이어서 큐의 제안 TTL에는 게이트가 걸리지 않고, 큐에서는 `term_propose`의 검사가 라벨 ko/en과 정의, 근거를 강제한다. 모듈로 옮긴 뒤에는 토큰 상한(`//kb/ontology:chunk_lint_test`)과 라벨·정의 검사(`//kg:gate_test`), 논리 정합성(`//kg:reason_test`)이 걸린다. 제안 TTL은 이름 붙은 그래프의 4분 구조를 갖지 않는다.

**에이전트는 신뢰할 수 없는 센서다.** 제안은 하되 판정하지 않는다. 판정은 컴파일러(기계)와 승인자(사람)의 몫이며, 이것이 1.5절 "검사 게이트는 에이전트 밖"의 온톨로지판이다.
