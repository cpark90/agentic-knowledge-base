---
id: https://agentic-knowledge-base.dev/id/chunk/ba70473f-98c1-4146-bdef-558c114c884d
type: decision
level: concrete
title_ko: 규범 문서 규약 — 그림은 번호 없는 캡션 한 줄로 시작하고 다이어그램은 소스 펜스로 둔다
title: Normative-document conventions — A figure opens with one unnumbered caption line, and a diagram is kept as a source fence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/97352110-2d95-4c45-ad01-1d9302b08656
---
**규약** — `p0-figure-caption-and-source`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **그림은 캡션 한 줄로 시작하고 캡션에 번호를 쓰지 않는다.** 번호는 표시용이라 소스에 두지 않는다 — 항목을 넣고 뺄 때 어긋나기 때문이다(목록 규칙과 같은 이유다).
규약: [지킴] 다이어그램은 **소스 펜스**(`mermaid`·`svg`·`plantuml`)로 둔다. 이미지 파일은 소스가 없을 때만 쓴다. 소스는 고칠 수 있고 diff 가 읽히지만 이미지는 둘 다 아니다.
규약: [권장] 기호·색의 뜻이 자명하지 않으면 "읽는 법"을 명사구 셋 이하로 붙인다.
