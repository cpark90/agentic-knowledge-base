---
id: https://agentic-knowledge-base.dev/id/chunk/9a4c0545-1d19-4b5d-b3ed-1d04ddb3984c
type: decision
level: logical
title_ko: 질문이 등록되지 않으면 무엇이 첨가인지 판정할 기준이 없다
title: Without a registered question there is no criterion for what counts as padding
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f7ac1b83-2f07-479d-a1ac-dfa68858e15f
---
**근거** — 42줄 상한은 분량을 제한하지만 그 안에 무엇이 들어가야 하는지는 말하지 않는다. 슬롯 표지는 이미 쓰이고 있으나 각 표지가 무슨 질문에 답하는지는 어디에도 등록돼 있지 않았다(2026-09-22 실측 — `profile-development-shapes.ttl`의 `sh:property`가 1개, 전부 청크 수준이다). 등록이 없으면 "이 문장이 여기 있어야 하는가"를 판정할 수 없고, 리뷰는 취향이 된다.

질문을 등록하면 세 가지가 기계 판정 또는 판정자 판정의 대상이 된다. 슬롯 밖의 답은 옮길 자리가 정해지고, 메타 문장은 어느 질문에도 답하지 않으므로 지워지며, 채움은 "실질적으로 답하는가"로 갈린다.

첨가를 막는 것이 42줄 상한을 실제로 살린다. 상한이 있어도 채움이 그 예산을 먹으면 답이 들어갈 자리가 줄어든다. 예산은 상한이지 목표가 아니다.

목록 규칙의 근거는 표시용 번호가 소스에 있으면 안 된다는 것이다. 항목을 지우거나 끼워 넣을 때 손 번호는 어긋나고, 그 어긋남은 내용의 변경이 아닌데도 `contentHash`를 바꾼다. 항목 9와 중첩 2는 복합체의 직접 부분 상한 9와 같은 수치이고 근거도 같다 — 한눈에 세어지는 크기다.
