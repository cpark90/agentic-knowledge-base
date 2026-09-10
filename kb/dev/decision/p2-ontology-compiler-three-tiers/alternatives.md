---
id: https://agentic-knowledge-base.dev/id/chunk/c014f3ca-7476-48df-a5e3-dfbb5c6ce7ef
type: decision
level: logical
title_ko: 손으로 쓴 Turtle 직접 릴리스와 shape 일원화
title: Releasing hand-written Turtle; expressing every constraint as a shape
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/33d988f2-27b2-44d7-98f2-110215bfe237
---
**대안** — **손으로 쓴 Turtle을 그대로 기반으로 쓰는 안.** 배제 — 라벨 누락·순환 계층·잘못된 참조가 어휘에 그대로 남고, 그 어휘 위에 선 모든 판정이 오염된다.

**모든 제약을 SHACL shape으로만 쓰는 안.** 배제 — "이런 조합이 존재하면 실패" 형태는 shape으로 쓰기 어색하다. 그런 제약은 verify 질의로 쓴다. 둘은 대체재가 아니라 역할 분담이다.

**자체 검사 파이프라인을 만드는 안.** 배제 — 20년간 다듬어진 것을 다시 만들 이유가 없다 (0.0절).
