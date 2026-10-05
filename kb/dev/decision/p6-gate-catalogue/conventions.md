---
id: https://agentic-knowledge-base.dev/id/chunk/289a4661-984b-4486-8fde-3ea1279e6b96
type: decision
level: concrete
title_ko: 규범 문서 규약 — 게이트는 다섯 실행 계층에 배치되며 실패는 draft에 머물러 전파되지 않는다
title: Normative-document conventions — Gates sit on five execution layers; a failure stays in draft and does not propagate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/33c8a1a1-fc90-4ce7-83a9-20c607a7c163
---
**규약** — `p6-gate-catalogue`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 게이트 도구는 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용을 낸다. 메시지가 곧 수정 안내다.
규약: **게이트 실패 대응.** FAIL 메시지의 인용이 수정 방향이다. 게이트가 틀렸다고 판단되면 게이트를 고치지 말고 채널에 `question`을 보낸다. shape 약화는 유저 승인 사항이다.
