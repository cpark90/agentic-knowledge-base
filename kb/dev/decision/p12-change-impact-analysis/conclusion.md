---
id: https://agentic-knowledge-base.dev/id/chunk/05cabe0e-10b0-4e02-81b1-8f5154a94fcc
type: decision
level: concrete
title_ko: 변경 영향은 기존 질의의 조합으로 변경 전에 계산한다
title: Change impact is computed before the change by composing existing queries
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0148]
part_of: https://agentic-knowledge-base.dev/id/composite/6b8cc1c0-c8c4-4aa4-a9e5-b72e150d72ab
composite: {id: https://agentic-knowledge-base.dev/id/composite/6b8cc1c0-c8c4-4aa4-a9e5-b72e150d72ab, title_ko: 변경 영향 분석 절차, title: Change impact analysis procedure}
---
**결론** — "X를 바꾸면 무엇이 영향받는가"를 9.7절 질의의 조합으로 계산하고,
**변경 전에** 그 결과를 보고 진행 여부를 정한다.

```
1. X의 IRI에서 satisfies / refines / constrains 역방향 질의
   → 직접 의존 집합
2. 직접 의존 집합의 assumes 가정 중 X에 관한 것 → 무효화 후보
3. 단방향 규칙으로 하위 plane까지 반복
4. 결과: 청크 수, plane 분포, suspect가 될 링크 수,
   유저 승인이 필요한 design 청크 수
```
