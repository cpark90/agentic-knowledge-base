---
id: https://agentic-knowledge-base.dev/id/chunk-d0184
type: decision
level: concrete
title_ko: 참조의 도달 범위는 단위별로 명시하는 트레이드오프다
title: Reference reach is a per-unit, explicitly recorded tradeoff
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 참조는 두 형태 중 하나이고, 단위마다 **어느 쪽을 왜 골랐는지
기록한다.** 내부(저장소 상대) 참조는 어디서나 해석되지만 그 자체가
사본이다. 외부 참조는 명세를 순수하게 유지하지만 원천에 닿는 곳에서만
해석된다. 해석되지 않는 참조는 **실패가 아니라 스텁으로 강등**한다.

**근거** (harness-concrete docs/recipes-design.md §"Reference reach")
- 둘 다 정당하다 — 재현을 저장소 하나로 닫아야 하면 내부 참조를, 원천을
  복제하면 안 되면(라이선스·규모·소유권) 외부 참조를 쓴다. 하나를 전역
  기본값으로 강제하면 둘 중 한쪽 요구가 항상 위반된다.
- 그래서 선택은 단위마다 기록한다. 기록이 없으면 나중에 사본이 실수인지
  의도인지 알 수 없고, 드리프트를 감수한 사본이 원천처럼 취급된다.
  내부 참조를 쓴다는 것은 **드리프트 위험을 명시적으로 산 것**이다.
- 강등이 실패보다 나은 이유 — 참조 하나가 닿지 않는다고 조립 전체가
  멈추면, 원천에 부분적으로만 닿는 환경에서는 명세를 아예 검증할 수 없다.
  스텁은 "여기에 무엇이 와야 하는가"를 남겨 결손을 **보이게** 한다.
  조용히 비우는 것과 다르다.
