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
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-26T23:15:18+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:40:02+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-26T23:15:18+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90
composite: {id: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90, title_ko: 유저 판단 질문의 다섯 요소, title: Five parts of a user judgement question}
---
**결론** — 유저에게 판단을 요청하는 질문은 다섯 요소를 갖춘다(유저 지적 2026-09-02). 한 줄 질문은 답을 받지 못한다.

| 요소 | 내용 |
|---|---|
| 질문 | 무엇이 정해지지 않았는가와 왜 어려운가 |
| 이미 정해진 것 | 관련 결정과 그 결론. 이미 답한 것을 다시 묻지 않는다 |
| 현재 상태 | 저장소 실물로 본 상태. 파일과 수치는 측정이다 |
| 답이 가르는 것 | 선택지마다 고르면 무엇이 바뀌는가 |
| 선택지 | 둘에서 넷. 각각의 비용을 적는다 |

선택지 뒤에 `**권장:**`으로 추천과 근거 한 줄을 붙인다. 지식은 이름이 아니라 IRI·조건 id·`file:line`으로 가리킨다.

2026-10-03부터 이 질문의 자리는 유저 채널의 질문지다. 앞의 두 요소는 머리 인용 블록에 모아 적어도 된다. orchestrator의 `question`이 유저 판단을 요구할 때도 같은 다섯 절을 쓴다(`harness/README.md`의 type 표). 게이트 `channel`은 질문지의 `답:` 줄만 판정하고 다섯 요소는 hci가 질문지를 쓸 때 지킨다.

**묻는 범위** — 유저에게 묻는 것은 확정 권한과 방향, 비용이 큰 선택, 새 파일, 검사의 약화다. 구현 선택은 orchestrator가 정해 `result`에 적고, interpreter가 그것을 보고로 알린다(Q-0060#Q140). 선택지마다 끝에 "권한·방향: 바꾼다" 또는 "권한·방향: 그대로"를 적어, 그 선택지가 확정 권한이나 방향을 바꾸는지 보인다.

**판정 기록의 예외** — 새 파일을 묻는 규칙에는 예외가 하나 있다. 링크 후보 뷰에 새로 든 판정 없는 후보는 묻지 않고 판정해 기록한다. 예외는 판정 도구가 만드는 판정 로그와 결과 주석에 한하고, 그 밖의 새 파일은 만들기 전에 묻는다. 한 번에 생기는 새 기록이 50개를 넘으면 판정을 시작하기 전에 그 수를 세어 묻는다. 기록 수와 판정 결과는 매번 `result`로 알린다(Q-0074#Q170, 2026-10-26).
