---
id: https://agentic-knowledge-base.dev/id/chunk/0d88fe7e-5085-4fbb-89c9-ba8627a97c56
type: decision
level: logical
title_ko: 시간 개체를 없앤 대가로 어휘 쪽에 자리를 만든다
title: Removing timeline entities requires giving time a place in the vocabulary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a65b4cb7-b236-46d5-ba86-c9c9c85ac000
---
**근거** (노트 0.5절, 0.4절)

- 시간열 개체를 두지 않기로 한 이상 시간 요구가 갈 곳이 없어진다. 그래서 ODD
  동적 갈래에 시간 제약을 하위 분류로 신설해 **어휘 쪽에 자리를 만든다.**
- 두 수준에 나눠 두는 것은 계층 원칙의 적용이다 — 요구는 functional 산문으로
  진술되고, 형식화는 logical에서 판정식을 갖는다. 한 수준에만 두면 요구가
  판정식 없이 남거나 형식화가 요구로 거슬러 오르지 못한다.
- 판정 등급이 A인 것은 실행 기록(`agt:Run`)이 append-only라 시각 순서가
  사후에 바뀌지 않기 때문이다.
