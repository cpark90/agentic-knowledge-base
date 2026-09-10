---
id: https://agentic-knowledge-base.dev/id/chunk/e90f9795-75f1-4d53-9aa0-ee2397ad4e17
type: decision
level: logical
title_ko: 네 수치가 변경의 크기를 비교 가능하게 만들고 자율 진행 여부를 가른다
title: Four numbers make change size comparable and decide whether autonomy holds
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/6b8cc1c0-c8c4-4aa4-a9e5-b72e150d72ab
---
**근거** (노트 12.6절)

- 새 질의를 만들지 않는다. 이미 있는 **역방향 질의와 단방향 규칙(5.2절)의
  조합**이므로 영향 분석 전용 인덱스를 따로 유지할 필요가 없다.
- 결과가 네 수치로 나오므로 변경의 크기가 **비교 가능**해진다. 코드 변경이 큰
  방향까지 바꿀 수 있다는 관찰을 정량화한 것이다.
- 유저 승인이 필요한 design 청크 수가 따로 나오는 이유 — 그 수가 0이 아니면
  변경이 자율 진행 범위를 벗어난다. 실행 도중이 아니라 착수 전에 알아야 한다.
- 2단계가 가정을 따로 훑는 이유 — 무효화는 링크가 아니라 가정을 타고 번지며
  (6.5절), 그 경로는 refines 연쇄와 일치하지 않는다.
