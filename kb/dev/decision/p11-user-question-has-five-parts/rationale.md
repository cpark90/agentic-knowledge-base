---
id: https://agentic-knowledge-base.dev/id/chunk/c4b3dc7c-af9c-40d5-990c-eeaa896051d0
type: decision
level: logical
title_ko: 한 문장 질문으로는 유저가 항목의 내용을 파악하지 못했고 유저의 결정은 배경과 선택지를 담은 리포트에서 나온다
title: A one-sentence question did not let the user grasp the item, and the user decides from a report carrying background and options
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/85053389-9f78-4781-9357-d559a7b7ed90
---
**근거** — 출발점은 유저 지적(2026-09-02)이다. 원문은 "한문장의 짧은 질문으로는 해당 항목에 대한 내용파악이 힘든것같아."이다. 그때 미결 항목 문서의 한 줄 항목은 답을 받지 못했다. hci 역할 메모리는 다섯 요소가 2026-09-04에 규범 문서와 채널 규약에 반영됐다고 적는다.

노트 12.2절이 같은 방향을 정한다. 유저는 적은 선택지 중 고르지 않고 리포트를 받아 피드백을 입력해 결정한다. 리포트가 제공할 것은 결정할 항목과 배경, 선택지, 결정의 기록이다. 다섯 요소는 그 배경을 셋(질문의 어려움·이미 정해진 것·현재 상태)으로 나누고 선택지에 답이 가르는 것을 붙인 형태다.

요소별 이유로 확인한 것은 둘이다. 이미 정해진 것을 적는 까닭은 이미 답한 것을 다시 묻지 않기 위해서다. 현재 상태를 실측으로 적는 까닭은 문서에 적힌 수치가 낡아 있기 때문이다(hci 역할 메모리, 2026-09-04).

2026-10-03 채널 개편(`p11-harness-two-channels`)은 이 규약을 바꾸지 않고 옛 항목 형식에서 질문지 형식으로 옮겼다. 그 결정의 근거도 2026-09-02 지적을 인용한다. 별도 결정으로 두는 까닭은 시행 시점과 대상이 다르기 때문이다 — 이 규약은 채널 형식보다 앞서 시행됐고 채널이 바뀌어도 남는다.
