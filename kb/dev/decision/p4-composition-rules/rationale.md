---
id: https://agentic-knowledge-base.dev/id/chunk/c5d73d32-e369-47e5-916e-e735959ce112
type: decision
level: logical
title_ko: 두 메커니즘이 겹치지 않아야 하고 참조 재사용은 그래프에서 공짜다
title: The two mechanisms must not overlap, and reference reuse is free in a graph
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/27157a50-048e-4b31-835f-ce91abcb93a8
---
**근거** (노트 4.5절)

- **동질성**이 있어야 구성과 링크 두 메커니즘이 겹치지 않는다. 겹치면 같은
  관계를 두 곳에 쓸 수 있게 되고, 어느 쪽을 질의해야 하는지가 사라진다.
- **7±2와 42줄은 같은 뿌리다** — 인지 한계(4.1절). 부분이 아홉을 넘으면 전체를
  한 번에 조망할 수 없으므로 중간 복합체로 한 겹 더 나눈다.
- **참조 재사용이 공짜다.** 모듈형 문서에서 "복사하지 말고 참조하라"는 별도
  원칙이 필요했지만, 그래프에서는 한 개체가 여러 전체의 부분인 것이 기본
  동작이고 복사가 오히려 어렵다. 청크가 바뀌면 그것을 부분으로 갖는 모든
  복합체에 반영되는 것도 저장 구조의 귀결이지 규칙이 아니다.
- 복합체 상태를 부분에서 추론하면 복합체에 따로 상태를 적을 필요가 없다 —
  적으면 부분과 어긋날 수 있다.
