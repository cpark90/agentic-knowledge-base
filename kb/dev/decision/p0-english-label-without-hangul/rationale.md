---
id: https://agentic-knowledge-base.dev/id/chunk/9efb465d-672a-4f5e-acfd-7bc863b636eb
type: decision
level: logical
title_ko: 용어 치환이 영문 라벨 여섯에 한글을 넣었고 기존 검사는 청크 frontmatter의 언어를 보지 않았다
title: A term substitution put Hangul into six English labels, and no existing check looked at the language of chunk frontmatter
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f0b99b6e-b385-4a1a-a879-a46b0b5c8faa
---
**근거** — 2026-09-12 실측이 출발점이다. `verifier`를 `검증기`로 바꾼 용어 치환이 영문 라벨에도 적용되어 청크 여섯의 `title`에 한글이 들어갔다. 온톨로지 `@en` 라벨과 문서에는 오염이 없었다.

같은 실측이 기존 검사가 놓친 까닭을 적는다. `validate`의 라벨 검사는 온톨로지 용어만 보고 청크 frontmatter를 보지 않았다. `consistency`는 라벨의 중복과 형식만 보고 언어를 보지 않았다.

라벨은 한/영 1:1이고 영문은 영어다(`p0-notation-format`, 노트 0.6절). 라벨은 청크의 인터페이스이므로(`p4-label-is-the-interface`) 라벨 오염은 인터페이스 오염이다. 유저는 생성기 검사의 추가와 `STYLEGUIDE.md`의 규약 한 줄을 함께 골랐다. 복합체 선언으로의 확장은 같은 날 뒤따랐다.
