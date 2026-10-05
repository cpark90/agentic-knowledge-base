---
id: https://agentic-knowledge-base.dev/id/chunk/96b4093f-7859-4db2-9cd8-13913f515e10
type: decision
level: concrete
title_ko: 영문 라벨에는 한글을 섞지 않고 용어 치환은 한글 필드만 대상으로 한다
title: English labels carry no Hangul, and term substitution touches only the Korean fields
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f0b99b6e-b385-4a1a-a879-a46b0b5c8faa
composite: {id: https://agentic-knowledge-base.dev/id/composite/f0b99b6e-b385-4a1a-a879-a46b0b5c8faa, title_ko: 라벨 언어 — 영문 라벨의 한글 금지, title: Label language — no Hangul in English labels}
---
**결론** — 영문 라벨(`title`)에 한글을 섞지 않는다(유저 결정 2026-09-12). 한글 라벨(`title_ko`)에는 한글이 있어야 한다. 복합체 선언의 `title`·`title_ko`도 같은 규칙을 따른다. 용어 치환은 한글 필드(`title_ko`·본문)만 대상으로 한다.

`chunk2kg`가 head 그래프를 생성하면서 위반을 거부한다. 판정은 한글 음절·자모의 정규식 하나다. 생성기가 곧 검사기이므로 위반은 `//kg:chunks_kg` 빌드에서 실패한다.
