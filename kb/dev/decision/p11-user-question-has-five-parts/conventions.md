---
id: https://agentic-knowledge-base.dev/id/chunk/3f183688-089d-4fe1-8e1b-e856a619af30
type: decision
level: concrete
title_ko: 규범 문서 규약 — 유저 판단을 요청하는 질문은 다섯 요소와 선택지별 비용·권장안을 갖춘다
title: Normative-document conventions — A question asking for the user's judgement carries five parts, a cost per option, and a recommendation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-26T23:15:18+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:40:02+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-26T23:15:18+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90
---
**규약** — `p11-user-question-has-five-parts`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 유저 판단을 요청하는 질문은 **다섯 가지**를 갖춘다. 다섯 가지는 왜 어려운가를 포함한 질문과 이미 정해진 것, 측정치인 현재 상태, 답이 가르는 것, 선택지다. 한 줄 질문은 답을 받지 못한다. 선택지마다 비용을 적고 `**권장:**`으로 권장안을 붙인다(유저 지적 2026-09-02).

규약: [지킴] 유저에게 묻는 것은 확정 권한과 방향, 비용이 큰 선택, 새 파일, 검사의 약화로 좁히고, 구현 선택은 orchestrator가 정해 `result`에 적는다. 선택지마다 끝에 "권한·방향: 바꾼다" 또는 "권한·방향: 그대로"를 적는다(Q-0060#Q140).

규약: [지킴] 새 파일 질문의 예외는 판정 기록 하나다. 링크 후보 뷰에 새로 든 판정 없는 후보는 묻지 않고 판정해 판정 로그와 결과 주석을 기록한다. 한 번에 새 기록이 50개를 넘으면 판정 전에 묻고, 기록 수와 판정 결과는 매번 `result`로 알린다(Q-0074#Q170).
