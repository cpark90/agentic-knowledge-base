---
id: https://agentic-knowledge-base.dev/id/chunk-d0097
type: decision
level: concrete
title_ko: 링크의 가능성은 확률이 아니라 가능 집합
title: Link possibility as feasible set, not probability
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크의 가능성은 **가능 / 불가능**의 가능 집합(제약 만족)
수준으로만 표현한다. 등급([0,1] 확률·가능성 측도)은 쓰지 않는다.
선호(연성 제약)는 유저가 후보 사이에 순서를 표현하고 싶을 때만 얹는다.

**근거** (노트 7.2절)
- 확률의 근거가 될 빈도 데이터가 없다. "이 링크가 60% 성립한다"는 말할
  수 없고, "이 링크는 성립 가능하다 / 불가능하다"는 말할 수 있다.
- 가능성은 제약 검사로 판정되며 **결정론적**이다 — 기계 검사로 충분하다.
- 선호는 수치 없이 후보 간 **부분순서**만 두는 확장이다 (7.9절).

**대안**
- 등급(가능성 측도 / 확률) — 미채택. 캘리브레이션 문제가 그대로 돌아온다.
