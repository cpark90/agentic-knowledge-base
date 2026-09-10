---
id: https://agentic-knowledge-base.dev/id/chunk/729b826e-12fa-4ad9-ac52-a7f66b33203b
type: decision
level: logical
title_ko: 빈 칸의 두 뜻을 색이 갈라야 추적 누락이 읽힌다
title: Only color can split the two meanings of an empty cell, revealing missing traces
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/78873300-5f9a-4316-bc7c-9a384d60822b
---
**근거** (노트 13.6절, 9.12절 매트릭스)

- 빈 칸에는 **"금지"와 "누락" 두 뜻**이 있다. TIM이 허용하는데 링크가 하나도
  없는 칸이 추적 누락이므로, 색이 다르지 않으면 매트릭스를 읽을 수 없다.
- 셀의 **색 값이 suspect 비율**이다 — 어느 plane 쌍의 링크가 흔들리고 있는지
  한눈에 보인다. 개수가 아니라 비율인 이유는 plane 쌍마다 링크 수가 다르기
  때문이다.
- 셀에서 링크 목록으로 내려갈 때도 본문이 아니라 **라벨과 상태**를 보여준다
  (11.8절 온보딩과 같은 원칙).
- 필터가 level·상태·기간인 이유 — 이 셋이 매트릭스를 쪼개도 의미가 남는
  축이다. plane은 이미 행·열이다.
