---
id: https://agentic-knowledge-base.dev/id/chunk/2b641fb6-fbd9-4d17-b4bc-e41479df2706
type: decision
level: logical
title_ko: 약한 판정은 형식 검사까지만 자동화하고 나머지를 유저 승인으로 메운다
title: Weak verification automates form only and fills the rest with user approval
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/e41d8f22-3084-4182-870e-8abbf9f95076
---
**근거** (노트 5.4절)

- 게이트가 사람의 검토를 대신하려면 **plane마다 무엇으로 판정하는지가 도구로
  지목되어** 있어야 한다. 지목되지 않은 plane의 청크는 `draft`를 벗어날 근거가
  없다.
- 자동화가 낮은 두 plane은 **자동 검사를 구조의 존재까지만** 밀고 나머지를 유저
  승인으로 메운다 — `decision`의 논증 구조 검사가 결론·근거·대안 세 청크의
  존재를 확인하는 것(4.7절)이 그 예다.
- 그래서 4.11절 상태 기계에서 `stable`로 올라가는 조건이 plane마다 다르다.
  `annotation`은 해소 상태만, `memory`는 판정 자체가 없다.
