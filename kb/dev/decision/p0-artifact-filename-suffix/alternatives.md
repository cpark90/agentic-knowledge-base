---
id: https://agentic-knowledge-base.dev/id/chunk/b6492fc9-43d1-441d-aa1b-6cbfca385155
type: decision
level: logical
title_ko: 청크 고유 접미사와 functional 전용 파일 안의 기각
title: Rejecting a chunk-specific suffix and a dedicated functional file
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0af48edc-840f-49e8-ad8b-60dfb331854d
---
**대안** — 청크에도 고유 접미사를 주는 안. 기각 — 청크의 본문은 plane마다
형식이 달라(4.12절) 하나의 접미사로 묶으면 본문의 확장자가 가려지고, 도구가
파일을 열기 전에는 무엇인지 알 수 없게 된다.

**대안** — functional 단계를 별도 파일로 두는 안. 기각 — functional은 어휘를
서술적으로 쓴 것이라 온톨로지와 내용이 겹치고, 두 곳에 두면 어긋난 시점을 알
방법이 없다.

**대안** — 성격을 파일명이 아니라 파일 안 메타데이터로만 표시하는 안. 기각 —
게이트가 파일을 열어야 판정할 수 있어 스코프 선별이 읽기 이후로 밀린다.
