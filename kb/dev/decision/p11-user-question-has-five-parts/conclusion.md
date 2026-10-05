---
id: https://agentic-knowledge-base.dev/id/chunk/e107e7d2-8fad-48ba-bfd7-543754aa7c58
type: decision
level: concrete
title_ko: 유저 판단을 요청하는 질문은 다섯 요소와 선택지별 비용·권장안을 갖춘다
title: A question asking for the user's judgement carries five parts, a cost per option, and a recommendation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90
composite: {id: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90, title_ko: 유저 판단 질문의 다섯 요소, title: Five parts of a user judgement question}
---
**결론** — 유저에게 판단을 요청하는 질문은 다섯 요소를 갖춘다(유저 지적 2026-09-02). 한 줄 질문은 답을 받지 못한다.

| 요소 | 내용 |
|---|---|
| 질문 | 무엇이 정해지지 않았는가와 왜 어려운가 |
| 이미 정해진 것 | 관련 결정과 그 결론. 이미 답한 것을 다시 묻지 않는다 |
| 현재 상태 | 저장소 실물로 본 상태. 파일과 수치는 실측이다 |
| 답이 가르는 것 | 선택지마다 고르면 무엇이 바뀌는가 |
| 선택지 | 둘에서 넷. 각각의 비용을 적는다 |

선택지 뒤에 `**권장:**`으로 추천과 근거 한 줄을 붙인다. 지식은 이름이 아니라 IRI·조건 id·`file:line`으로 가리킨다.

2026-10-03부터 이 질문의 자리는 유저 채널의 질문지다. 앞의 두 요소는 머리 인용 블록에 모아 적어도 된다. orchestrator의 `question`이 유저 판단을 요구할 때도 같은 다섯 절을 쓴다(`harness/README.md`의 type 표). 게이트 `channel`은 질문지의 `답:` 줄만 판정하고 다섯 요소는 hci가 질문지를 쓸 때 지킨다.
