---
id: https://agentic-knowledge-base.dev/id/chunk/6d39d7fe-baea-46c6-bc60-61a1fae7a230
type: decision
level: concrete
title_ko: 두 형태가 다 정당하므로 전역 기본값 대신 단위마다 기록하고 결손은 스텁으로 보이게 한다
title: Both forms are legitimate, so the choice is recorded per unit instead of a global default, and gaps stay visible as stubs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0184-reference-reach-tradeoff.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:13:45+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:13:45+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/3343eae6-4b88-48c8-abfc-da8bb1af307a
---
**근거** — 출처는 harness-concrete `docs/recipes-design.md`의 "Reference reach" 절이다.

- 두 형태가 다 정당하다. 재현을 저장소 하나로 닫아야 하면 내부 참조를 쓰고, 라이선스나 규모, 소유권 때문에 원천을 복제하면 안 되면 외부 참조를 쓴다. 그래서 하나를 전역 기본값으로 강제하면 둘 가운데 한쪽 요구가 항상 위반된다.
- 따라서 선택은 단위마다 기록한다. 기록이 없으면 나중에 사본이 실수인지 의도인지 알 수 없고, 드리프트를 감수한 사본이 원천처럼 취급된다. 내부 참조를 쓴다는 것은 **드리프트 위험을 명시적으로 산 것**이다.
- 강등이 실패보다 나은 이유는 참조 하나가 닿지 않는다고 조립 전체가 멈추면, 원천에 부분적으로만 닿는 환경에서 명세를 아예 검증할 수 없기 때문이다. 스텁은 여기에 무엇이 와야 하는가를 남겨 결손을 **보이게** 하며, 이것은 조용히 비우는 것과 다르다.
