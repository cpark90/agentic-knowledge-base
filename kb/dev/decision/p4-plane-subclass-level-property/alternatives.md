---
id: https://agentic-knowledge-base.dev/id/chunk/f31af815-e869-42e8-9ef7-5a687d5ba87c
type: decision
level: logical
title_ko: level을 클래스로 두는 안은 계층 전이를 타입 변경으로 만든다
title: Modeling level as a class would turn ladder transitions into type changes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/db06bc97-7100-4ad3-bad0-83fb1c876e1c
---
**대안** — `[배제]` level도 plane처럼 클래스로 두는 안.

- 계층 전이가 개체의 타입 변경이 되어, 새 청크 + `refines`로 기록하는
  4.2절의 방식과 충돌한다. 전이의 흔적이 링크가 아니라 타입 이력에 남는다.
- plane 클래스와 교차하는 클래스가 따로 필요해진다.
- 배제 근거는 4.2절 "같은 청크가 level을 바꾸는 일은 없으므로 속성으로
  충분하다"이다.
