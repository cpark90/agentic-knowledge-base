---
id: https://agentic-knowledge-base.dev/id/chunk/be3f2d14-0cf4-4295-a9d3-2e8d9e5e2d00
type: decision
level: logical
title_ko: 주는 넷과 받는 넷이 짝을 이루고 활용의 내부 절차는 체계 밖이다
title: The four given pair with the four returned; a use's internal procedure lies outside
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d8683edb-e683-4f3f-a6cc-fd448b724280
---
**근거** (노트 12.1절, Part XII 도입)

- 주는 것 넷이 받는 것 넷과 짝을 이룬다. 요구가 없으면 검증 목표가 없고, ODD가
  없으면 커버리지의 분모가 없으며, 가정이 없으면 검증 경계가 없다 — 개발 KB의
  공백이 그대로 V&V KB의 공백이 된다.
- 돌아오는 넷은 전부 개발 KB의 항목을 움직인다. 결함은 상승 후보를 낳고,
  검증 상태는 링크를 suspect로 내린다.
- 활용 기능의 내부 절차를 체계가 규정하지 않는 이유 — **의존 방향이
  반대다.** 입력이 바뀌면 체계가 재구성되고, 체계가 바뀌면 활용이 영향받는다.
  둘을 한 곳에 두면 변경 파급 계산이 뒤섞인다.
