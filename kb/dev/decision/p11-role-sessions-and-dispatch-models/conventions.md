---
id: https://agentic-knowledge-base.dev/id/chunk/1bc3ec94-dbfc-47d9-a62b-1d7cf9b56afc
type: decision
level: concrete
title_ko: 규범 문서 규약 — 세션 역할은 부팅 스크립트로 띄우고 스크립트 없는 세션은 orchestrator이며 dispatch는 opus 또는 sonnet으로 역할 표와 스코프를 브리핑한다
title: Normative-document conventions — Session roles start from launch scripts, a session without one is the orchestrator, and dispatch runs on opus or sonnet with a briefing of the role table and scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-05T20:19:26+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T20:19:34+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/04ec773f-bf28-4ae8-a8d6-5fc4012dff58
---
**규약** — `p11-role-sessions-and-dispatch-models`의 결론을 규범 문서에 싣는 문장이다.

규약: 스크립트 없이 띄운 세션은 orchestrator다.
규약: dispatch는 **opus 또는 sonnet 모델**로 한다(유저 지시 2026-09-26·2026-10-03). 설계 판단과 새 구조는 opus, 규약이 정해진 기계적 반영은 sonnet이다.
규약: [지킴] 수신 감시(`harness/scripts/watch.sh <역할>`)는 도구의 백그라운드 실행으로 하나만 띄운다. 메시지를 처리한 턴의 끝마다 감시가 살아 있는지 확인하고 없으면 다시 건다. 감시가 0이 아닌 코드로 끝나면 수신함을 한 번 직접 읽은 뒤 다시 건다. 역할 세션은 백그라운드 셸 회수를 끈 환경으로 띄운다(`harness/scripts/run-hci.sh`·`harness/scripts/run-orchestrator.sh`).
