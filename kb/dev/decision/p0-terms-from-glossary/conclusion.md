---
id: https://agentic-knowledge-base.dev/id/chunk/9969c11c-7126-497c-b120-7c69760c16b8
type: decision
level: concrete
title_ko: 한글 용어는 용어집의 표준 용어만 쓰고 지식의 종류는 고유 용어로 부른다
title: Korean terms come only from the glossary, and kinds of knowledge are called by their own names
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/cd23fc9b-1ca6-41e7-b749-5dcb0991796b
composite: {id: https://agentic-knowledge-base.dev/id/composite/cd23fc9b-1ca6-41e7-b749-5dcb0991796b, title_ko: 산문 용어 — 용어집의 표준 용어, title: Prose terms — standard terms of the glossary}
---
**결론** — 산문의 한글 용어는 `docs/glossary.md`의 표준 용어만 쓴다(유저 결정 2026-09-10). 은유·조어를 새로 만들지 않는다. 용어집의 옛 표기 열이 그런 조어의 목록이다. 용어집에 없는 개념은 표준어를 찾아 용어집에 먼저 추가한다.

지식의 종류는 고유 용어로 부른다(유저 결정 2026-09-04). 고유 용어는 조건·개념·변수·후보·결정·가정·시그니처·함수·주석·관측이다. "결정 청크"가 아니라 "결정"이다. "청크"는 그것들이 따르는 구조 규칙을 말할 때만 쓴다. 온톨로지 클래스 이름(`agt:DecisionChunk` 등)과 그래프 라벨은 구조 타입의 식별자이므로 인용할 때 그대로 쓴다.

영문 식별자는 온톨로지의 것이고 이 결정의 대상이 아니다. 옛 표기의 잔존은 `consistency` ⑥이 보고하고, 위반으로 세는 것은 용어집 tier 1(기계 치환) 행뿐이다.
