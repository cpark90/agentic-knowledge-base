---
id: https://agentic-knowledge-base.dev/id/chunk/a574bc7c-f3c3-4d44-9b47-7e6dc3cd16c2
type: decision
level: concrete
title_ko: 규범 문서 규약 — 인터프리터는 hci를 일반화해 외부 대상과 orchestrator 사이의 소통을 맡고 hci는 그 유저 대상 하위 역할이다
title: Normative-document conventions — The interpreter generalizes hci to carry communication between external parties and the orchestrator, and hci is its user-facing sub-role
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9fef5341-55b1-4fda-8a93-e5ffdfbfcf83
---
**규약** — `p11-interpreter-generalizes-hci`의 결론을 규범 문서에 싣는 문장이다. 역할 표의 interpreter 행과 hci 행은 `p7-dev-roles-and-scopes`의 규약이 원본이다.

규약: **지식 베이스 밖의 대상은 interpreter를 거쳐 지식 베이스와 소통한다.** interpreter는 세션 하나로 외부 대상 셋을 맡고 대상은 메시지의 `origin`으로 가르며, 유저 대상 몫은 하위 역할 hci가 같은 세션에서 맡는다.
규약: [지킴] **외부 대상의 쓰기는 후보 제안까지다.** 외부 대상은 저장소 파일을 쓰지 않고, interpreter가 그 쓰기 요청을 후보 제안으로 정제해 orchestrator에 넘긴다.
규약: 외부에서 온 후보는 유저가 미리 정한 범위 안에서 orchestrator가 확정하고 결과를 유저에게 보고한다. interpreter는 확정하지 않으며, 위임 범위는 뒤 단계의 결정이 정한다.
