---
id: https://agentic-knowledge-base.dev/id/chunk/176c6a81-7351-4d81-a71d-129a48c42b96
type: decision
level: concrete
title_ko: 그림은 번호 없는 캡션 한 줄로 시작하고 다이어그램은 소스 펜스로 둔다
title: A figure opens with one unnumbered caption line, and a diagram is kept as a source fence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/97352110-2d95-4c45-ad01-1d9302b08656
composite: {id: https://agentic-knowledge-base.dev/id/composite/97352110-2d95-4c45-ad01-1d9302b08656, title_ko: 그림 — 캡션과 소스 펜스, title: Figures — caption and source fence}
---
**결론** — 그림 규칙은 셋이다(유저 승인 2026-09-22). 문서와 청크에 함께 걸리므로 `STYLEGUIDE.md` §0에 둔다.

- 그림은 캡션 한 줄로 시작하고 캡션에 번호를 쓰지 않는다. 번호는 표시용이라 소스에 두지 않는다.
- 다이어그램은 소스 펜스(`mermaid`·`svg`·`plantuml`)로 둔다. 이미지 파일은 소스가 없을 때만 쓴다.
- 기호·색의 뜻이 자명하지 않으면 "읽는 법"을 명사구 셋 이하로 붙인다. 이 항목은 권장이다.

셋 다 검사 수단이 없는 규약이고 리뷰가 잡는다.
