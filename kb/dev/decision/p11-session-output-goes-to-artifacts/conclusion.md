---
id: https://agentic-knowledge-base.dev/id/chunk/016c3cdc-208b-429f-a379-f411b715ecf6
type: decision
level: concrete
title_ko: 상태·결정·주석은 해당 산출물에 쓰고 세션과 채팅에는 무엇을 어디에 썼는지 요점만 남기며 임시 파일은 스크래치패드에 둔다
title: State, decisions and annotations are written to their artifacts, a session or chat keeps only what was written where, and temporary files stay in the scratchpad
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/23cf6ac9-f4b7-498b-88dc-84e70d2d5f8c
composite: {id: https://agentic-knowledge-base.dev/id/composite/23cf6ac9-f4b7-498b-88dc-84e70d2d5f8c, title_ko: 세션 출력의 자리, title: Where session output goes}
---
**결론** — 작업의 내용은 그 종류의 산출물에 쓰고 세션에는 가리키는 요점만 남긴다.

| 내용 | 쓰는 자리 |
|---|---|
| 결정 | `decision` plane |
| 주석 | `annotation` plane |
| 상태 | 그 항목의 산출물(청크의 `status`, 질문지의 `status`) |
| 세션 보고 · `result` 메시지 | 무엇을 어디에 썼는지의 요점 |
| 임시 파일 | 세션의 스크래치패드. 저장소에 두지 않는다 |

- **유저에게 결정을 요청할 때 채팅에는 질문지를 만들었다는 안내와 요지만 쓴다.** 질문의 본문과 선택지는 질문지에 있다(`p11-user-question-has-five-parts`).
- 세션 보고와 `result`는 내용을 되풀이하지 않는다. 산출물의 경로·IRI로 가리킨다.

이 규약을 판정하는 게이트는 없다. 리뷰 규범이다.
