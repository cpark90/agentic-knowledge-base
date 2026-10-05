---
id: https://agentic-knowledge-base.dev/id/chunk/a1cac39e-5291-44af-9f2d-9a3ef3de9f26
type: decision
level: logical
title_ko: 옛 채널은 닫는 사슬이 길어 항목이 쌓였고 수신함과 질문지는 완료를 수신자의 한 동작으로 만든다
title: The old channel piled up items behind a long closing chain; inboxes and questionnaires make completion a single act by the receiver
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-04T11:51:45+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/bb2307b6-884f-43ba-bee6-7b1185c43e3a
---
**근거** — 옛 채널의 실측(2026-10-03)이 출발점이다. 항목 111건 가운데 열린 것은 넷이었다. 넷은 유저 판단 대기 1, 판정지 1, 진행 중인 인수인계 2다. 그런데 인수 기록 38건이 `answered`에서, 중계된 질문 9건이 `relayed`에서 멈춰 있었다. 발신자가 `closed`로 바꿔야 hci가 지울 수 있고, 지우는 순서가 인수 기록·인수인계·유저 항목의 사슬을 따라야 했기 때문이다. 닫는 동작이 세 역할에 나뉘어 있어 아무도 닫지 않았다.

수신함은 완료를 **수신자의 한 동작**으로 만든다. `done`으로 표시하면 보관된다. 그 동작의 조건이 짝의 실재다. `result` 없는 `task`와 `answer` 없는 `question`은 닫히지 않는다. 시간으로 완료를 가정하지 않는다는 옛 규칙이 그대로 남고 사슬은 한 단계가 된다.

질문지는 `p12-user-feedback-space-file`의 연장이다. 유저는 파일을 편집해 결정하고 답의 원문이 파일에 남는다. 선택지·비용·권장안을 형식으로 두는 까닭은 한 줄 질문으로는 답을 받지 못한다는 유저 지적(2026-09-02)이다.

hci가 수행하지 않는다는 유저 교정(2026-09-11)은 단일 작성자와 종류별 방향으로 기계화된다. `task`는 hci만, `result`는 orchestrator만 보낸다. developer·vnv는 세션을 유지하지 않아 수신함을 읽을 주체가 없다. 그들의 자리는 hand-back이다.

채널 메시지를 git 밖에 두는 까닭은 소멸성이다. 기록으로 남는 것은 질문지(답의 원문)와 지식 베이스(승격된 결론)와 git 이력이다.

한 메시지 한 주제와 IRI·조건 id·`file:line` 참조는 2026-09-01 첫 채널부터 있던 규칙이고 새 채널이 그대로 잇는다. 옛 규칙은 항목 하나를 반영·승인의 단위로 두었다. 지식을 링크로 가리키는 까닭은 채널이 그래프 밖이라 링크가 유일한 연결이기 때문이다(같은 날의 `STYLEGUIDE.md` 원문). 채널 경로를 인용원으로 쓰지 않는 규칙과 면제를 `docs/waivers.md`에 선언하는 규칙은 2026-09-12 유저가 채택한 수렴 규칙이다. 그날 결정 하나가 채널 항목을 원본으로 인용해 그 항목을 정리하지 못했고, 면제는 도구 코드에 숨어 있었다.

`KNOWLEDGE.md`를 두지 않는 까닭은 이 저장소가 만드는 것이 그 자리이기 때문이다. 한 파일은 종류·수준·상태를 가르지 못하고 토큰 상한을 넘는다.

허가 신호에 채팅 알림을 더한 근거는 2026-10-03~04 사이클의 관찰이다(Q24-b). 유저가 답을 적고 채팅으로 알렸으나 태깅하지 않은 일이 네 번 있었고 그때마다 반영이 늦어졌다. 채팅 알림은 유저만 할 수 있으므로 허가의 주체는 그대로 유저다. 유저가 직접 태깅하는 길도 그대로 열려 있다.
