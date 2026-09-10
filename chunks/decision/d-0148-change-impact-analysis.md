---
id: https://agentic-knowledge-base.dev/id/chunk-d0148
type: decision
level: concrete
title_ko: 변경 영향 분석 절차
title: Change impact analysis procedure
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — "X를 바꾸면 무엇이 영향받는가"를 8.7절 질의의 조합으로 계산하고,
**변경 전에** 그 결과를 보고 진행 여부를 정한다.

**근거** (노트 10.6절)

```
1. X의 IRI에서 satisfies / refines / constrains 역방향 질의
   → 직접 의존 집합
2. 직접 의존 집합의 assumes 가정 중 X에 관한 것 → 무효화 후보
3. 단방향 규칙으로 하위 plane까지 반복
4. 결과: 청크 수, plane 분포, suspect가 될 링크 수,
   유저 승인이 필요한 design 청크 수
```

- 새 질의를 만들지 않는다 — 이미 있는 역방향 질의와 단방향 규칙(5.2절)의
  조합이다.
- 결과가 네 수치로 나오므로 변경의 크기가 비교 가능해진다. **코드 변경이
  큰 방향까지 바꿀 수 있다는 관찰을 정량화한 것이다.**
- 유저 승인이 필요한 design 청크 수가 따로 나오는 이유 — 그 수가 0이 아니면
  변경이 자율 진행 범위를 벗어난다.
