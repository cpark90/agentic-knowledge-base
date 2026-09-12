---
id: https://agentic-knowledge-base.dev/id/chunk/4754eb68-ad27-45ad-912c-0385087cd063
type: decision
level: concrete
title_ko: 에이전트가 제안하고 컴파일러가 거르고 사람이 승인한다
title: The agent proposes, the compiler filters, a human approves
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
part_of: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b
composite: {id: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b, title_ko: 용어 제안 워크플로, title: Term proposal workflow}
---
**결론** — 일반화(6.3절)이 온톨로지에 닿을 때의 절차. OBO 진영에서 운영되는 흐름을 그대로 쓴다.

1. 에이전트가 관측 청크에서 개념 후보를 뽑아 **ROBOT template 행**으로 쓴다 — ID · 라벨 ko/en · 정의(속 + 종차) · 상위 클래스 · 기여하는 역량 질문
2. template → OWL 변환. **2.5절 3계층 검사**
3. 통과한 것만 **유저 승인 큐**로
4. 승인되면 **코어가 아닌 확장 모듈**에 병합하고, `prov:wasDerivedFrom`으로 관측 청크에 연결

**template 행이 곧 청크다** — 42줄 안, 라벨 필수, 4분 구조. 온톨로지 확장 제안이 다른 지식과 같은 규칙을 따른다.

**에이전트는 신뢰할 수 없는 센서다.** 제안은 하되 판정하지 않는다. 판정은 컴파일러(기계)와 승인자(사람)의 몫이며, 이것이 1.5절 "검사 게이트는 에이전트 밖"의 온톨로지판이다.
