---
id: https://agentic-knowledge-base.dev/id/chunk/85e89cfb-0bb3-475e-9788-9f9f6468ab95
type: decision
level: concrete
title_ko: 규범 문서 규약 — 소통은 유저 질문지와 수신함 메시지 두 채널로 하고 결론은 지식 베이스에 남긴다
title: Normative-document conventions — Communication runs on two channels, user questionnaires and inbox messages, and conclusions stay in the knowledge base
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:44:41+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/bb2307b6-884f-43ba-bee6-7b1185c43e3a
---
**규약** — `p11-harness-two-channels`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 에이전트 채널은 단일 작성자라서 `to_orchestrator/`에는 interpreter(하위 역할 hci 포함)만, `to_interpreter/`에는 orchestrator만 쓴다. 쓰기는 `harness/scripts/send.sh`로, 상태 전이는 수신자가 `harness/scripts/mark.sh`로 한다.
규약: [지킴] 메시지 하나에는 주제 하나만 담고, `task` 하나가 반영 단위이므로 큰 작업은 쪼개어 보낸다.
규약: [지킴] `status` 어휘는 채널마다 달라 섞지 않는다. 메시지는 `new→read→in_progress→done | blocked`, 질문지는 `open→answered→closed`다. `answered`는 유저가 쓰며, hci 세션에서 답을 알린 경우에는 hci가 대신 쓴다.
규약: [지킴] `task`는 배경, 목표, 완료조건, 제약, 파급효과, 확인 못 한 것의 필수 절 여섯을 갖춘다. `result`·`answer`는 `re`로 원 메시지를 가리키고 `result` 없는 `task`는 `done`이 될 수 없다.
규약: [지킴] 메시지와 질문지는 지식을 **식별자**(결정 slug, `agt:`, `id:`, IRI, 조건 id, `file:line`)로 가리키고, slug와 `agt:`, `id:` 옆에는 그 한글 이름을 함께 적는다(Q-0052 Q103 답). 게이트 `channel`이 판정한다.
규약: [지킴] 채널·질문지 경로는 소멸하므로 본문 인용원이 되지 못하고 근거는 질문 번호로 적는다. 면제는 코드가 아니라 `docs/waivers.md`에 선언한다(2026-09-12).
규약: **유저와의 상세 소통은 hci만 한다.** orchestrator는 유저 판단이 필요하거나 문제·특이사항이 생기면 직접 묻지 않고 에이전트 채널에 `question` 등을 보낸다. hci는 유저 결정을 유저 채널의 **파일 질문지**로 받는다. 프로토콜 원본은 [`harness/README.md`](../../../../harness/README.md)다.
규약: 세션으로 도는 두 역할은 지침 파일을 갖고 스크립트로 띄운다(`harness/agents/interpreter.md`·`harness/agents/orchestrator.md`, `harness/scripts/run-interpreter.sh`·`harness/scripts/run-orchestrator.sh`).
규약: 유저가 hci 세션에서 조사나 구체화, 제안을 요청한다. orchestrator의 `question`도 interpreter 수신함으로 들어온다.
규약: hci가 검토·구체화하고 조사도 직접 한다. 유저 결정이 필요한 지점은 유저 채널의 **질문지** `Q-<번호>.md`로 묻는다.
규약: 유저가 질문지에 답을 적고 `status: answered`로 태깅하면 반영이 허가된다. hci 세션에서 답을 알리면 hci가 대신 태깅한다. hci는 그 답을 `task`·`answer`·`knowledge` 메시지로 정제해 orchestrator에 보낼 뿐 수행하지 않으며, `//harness:channel_lint_test`와 writer 검사가 이를 강제한다.
규약: orchestrator가 담당 쓰기 지식 종류의 역할로 반영하고, `bazel test //...` 통과를 확인한 뒤 무엇을 어디에 썼는지 `result` 메시지로 돌려준다. 결론은 지식으로 남긴다.
규약: hci가 유저에게 결과를 보고하고 질문지를 `closed`로 닫아 유저 채널의 `archive/`로 옮긴다.
규약: [지킴] **유저에게 결정은 항상 파일 질문지로 요청한다.** 채팅에는 질문지를 만들었다는 안내와 요지만 쓰고, 유저가 채팅으로 먼저 답하면 hci가 그 답을 질문지에 원문으로 옮겨 적는다.
규약: **메시지는 흐르고 지식 베이스는 남는다.** 소통의 결론은 채널이 아니라 온톨로지와 ODD, 지식으로 승격한다. 하네스의 `KNOWLEDGE.md`에 쌓일 지식을 이 저장소는 지식 베이스에 남긴다([`harness/README.md` §지식 축적](../../../../harness/README.md#지식-축적)).
