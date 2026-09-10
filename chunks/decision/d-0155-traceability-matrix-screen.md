---
id: https://agentic-knowledge-base.dev/id/chunk-d0155
type: decision
level: concrete
title_ko: 추적 매트릭스 화면의 상호작용
title: Interaction of the traceability matrix screen
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 추적 매트릭스 화면의 행·열은 plane이고, 셀 클릭은 그 셀의 링크
목록(라벨 + 상태)을 연다. `suspect` 셀과 "TIM 허용 & 0" 칸은 색으로
구분하며, 필터는 level·상태·기간이다.

**근거** (노트 11.6절, 8.12절 매트릭스)
- 셀의 **색 값이 suspect 비율**이다 — 어느 plane 쌍의 링크가 흔들리고
  있는지가 한눈에 보인다.
- **"TIM 허용 & 0"** 은 TIM이 허용하는 링크 타입인데 실제 링크가 하나도
  없는 칸이다. 별도 색으로 구분해 추적 누락을 드러낸다 — 빈 칸에는 "금지"와
  "누락" 두 뜻이 있으므로 색이 다르지 않으면 읽을 수 없다.
- 셀에서 링크 목록으로 내려갈 때도 본문이 아니라 **라벨과 상태**를 보여준다
  (10.8절 온보딩과 같은 원칙).

**대안**
- 의도 모호성 시각화(모호한 단어를 후보 링크 수에 비례해 다른 색으로 표현,
  11.1절) — **미확정**.
