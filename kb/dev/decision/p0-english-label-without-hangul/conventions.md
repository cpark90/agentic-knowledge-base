---
id: https://agentic-knowledge-base.dev/id/chunk/cc18d62b-65d8-4be5-88ad-ed3a50c208f9
type: decision
level: concrete
title_ko: 규범 문서 규약 — 영문 라벨에는 한글을 섞지 않고 용어 치환은 한글 필드만 대상으로 한다
title: Normative-document conventions — English labels carry no Hangul, and term substitution touches only the Korean fields
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:18:25+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:18:25+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f0b99b6e-b385-4a1a-a879-a46b0b5c8faa
---
**규약** — `p0-english-label-without-hangul`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 영문 라벨인 `title`에는 한글을 섞지 않고, 용어 치환은 한글 필드인 `title_ko`와 본문만 대상으로 한다. `chunk2kg`는 `title`에 든 한글과 `title_ko`에 한글이 없는 경우를 거부한다(유저 결정 2026-09-12).
