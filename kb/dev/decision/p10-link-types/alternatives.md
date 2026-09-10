---
id: https://agentic-knowledge-base.dev/id/chunk/a5c3ab0b-1684-4db5-8c75-e8162ca52250
type: decision
level: logical
title_ko: 미채택 확장 후보와 양방향 저장
title: Rejected extensions and bidirectional storage
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/42c1ecbe-34fd-4c59-9038-51db6144ad29
---
**대안** — 검토했으나 배제한 것들.

- `elaborates` (같은 level 안의 상세화) — **미채택.** 같은 level의 상세화는 복합체 `part-of`로 표현된다.
- `justifies` (근거 청크가 결론 청크를 정당화) — **미채택.** `decision` 복합체 안의 역할 태그(결론·근거·대안)로 표현된다.
- `tests` (테스트 코드가 대상을 검사) — **미채택.** `verifies`의 출발점을 테스트 청크로 확장하면 충분하다.
- **양방향 저장** — **미채택.** 역방향을 함께 저장하면 두 벌을 동기화해야 하는 부담만 생긴다. 역방향은 질의의 몫이다.
