---
id: https://agentic-knowledge-base.dev/id/chunk/86e2ac76-b4a0-4183-a400-474f74113e80
type: decision
level: concrete
title_ko: 규범 문서 규약 — 작업은 셀프체크를 통과해야 끝나고 셀프체크는 게이트 전체 PASS와 원본이 바뀐 생성물의 재생성이다
title: Normative-document conventions — Work ends only after the self-check, which is a passing full gate run and the regeneration of every output whose source changed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3e29e698-8ef5-4fe2-ac1b-867e596a5179
---
**규약** — `p6-self-check-before-completion`의 결론을 규범 문서에 싣는 문장이다.

규약: **지식 파일을 고치면 `bazel test //...` 를 돌린다.** 실패하면 고친 파일을 수정한다. shape·게이트 코드를 약화시키지 않는다.
