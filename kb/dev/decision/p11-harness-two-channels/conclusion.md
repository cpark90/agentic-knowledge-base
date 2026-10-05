---
id: https://agentic-knowledge-base.dev/id/chunk/71481f94-fcc3-4e6e-a18a-639eaa65b5bd
type: decision
level: concrete
title_ko: 소통은 유저 질문지와 수신함 메시지 두 채널로 하고 결론은 지식 베이스에 남긴다
title: Communication runs on two channels, user questionnaires and inbox messages, and conclusions stay in the knowledge base
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-04T12:13:20+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/bb2307b6-884f-43ba-bee6-7b1185c43e3a
composite: {id: https://agentic-knowledge-base.dev/id/composite/bb2307b6-884f-43ba-bee6-7b1185c43e3a, title_ko: 하네스 소통 — 두 채널, title: Harness communication — two channels}
---
**결론** — 유저와 에이전트, 에이전트와 에이전트 사이의 소통은 두 채널이다(유저 지시 2026-10-03, 참조는 strawberry 프로젝트의 하네스). 프로토콜의 원본은 `harness/README.md`이고 게이트 `channel`이 형식을 강제한다.

| 채널 | 누구 사이 | 단위 | 상태 |
|---|---|---|---|
| 유저 채널 | 유저 ↔ hci | 질문지 파일. 질문마다 선택지·권장안·`답:` 줄 | `open → answered → closed` |
| 에이전트 채널 | hci ↔ orchestrator | 번호 메시지. 수신자마다 수신함 하나 | `new → read → in_progress → done`, 막히면 `blocked` |

- **유저의 결정은 파일 질문지로만 받는다.** 채팅으로 온 답도 hci가 질문지에 원문으로 옮긴다. 반영 허가 신호는 유저가 적은 답과 `answered` 태깅이다. 질문지의 `답:` 줄이 채워져 있고 유저가 hci 세션에서 "답 적었어"라고 알리면, 그것을 허가 신호로 삼는다. 이때 hci가 `status: answered`를 대신 적는다(Q24-b, 2026-10-04).
- **수신함은 단일 작성자다.** 보내는 쪽만 쓰고 받는 쪽이 상태를 전이한다. 메시지 종류는 일곱이다. 일곱은 `task`·`question`·`answer`·`result`·`knowledge`·`status`·`ack`다.
- **완료는 짝으로 판정한다.** `task`는 `result`가, `question`은 `answer`가 돌아와야 닫힌다.
- **hci는 수행하지 않는다.** 답을 `task`로 정제해 넘기고, orchestrator가 담당 write plane의 역할을 통해 반영한다. developer·vnv는 채널에 쓰지 않고 hand-back으로 orchestrator에 돌려준다.
- **메시지는 흐르고 지식 베이스는 남는다.** 한 프로젝트의 에이전트들이 하네스의 `KNOWLEDGE.md` 한 파일에 누적하는 것이 이 지식 베이스가 담으려는 지식이다. 그것은 현황·목표·확정된 결정·발견된 제약·작업 결과·열린 질문이다. 결론은 종류별 자리로 승격한다. 채널 경로는 인용원이 될 수 없으므로 근거는 질문 번호로 적는다.
- **한 메시지는 한 주제다.** `task` 하나가 반영의 단위이고 큰 작업은 쪼개어 보낸다. 메시지와 질문지는 지식을 이름이 아니라 IRI·조건 id·`file:line`으로 가리킨다.
- 청크 본문의 채널 경로 인용은 `chunk2kg`가 거부한다. 면제는 코드가 아니라 `docs/waivers.md`에 선언한다.
- 역할 세션은 스크립트로 띄우고 역할마다 지침 파일 하나를 읽는다.

옛 네 lane 채널(유저·에이전트·조사·인수인계)은 이 결정으로 대체된다.
