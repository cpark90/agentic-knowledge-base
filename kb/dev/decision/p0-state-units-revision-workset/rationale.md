---
id: https://agentic-knowledge-base.dev/id/chunk/e94ebdc8-ac6e-4e75-bbed-ce17251f9f78
type: decision
level: logical
title_ko: 스냅샷을 열거하면 저장 비용과 진위 물음이 함께 늘어난다
title: Enumerating snapshots multiplies storage and raises the question of which one is true
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/52124ca7-97f8-4b5e-818f-1574ab131484
---
**근거** (노트 0.5절)

- 스냅샷을 개체로 열거하면 저장 비용이 상태 수만큼 늘고, 같은 사실이 상태마다
  중복되며, **"어느 스냅샷이 참인가"** 라는 물음이 생긴다. 개정 연쇄는 변한
  것만 기록한다.
- 작업 집합을 저장하지 않는 것도 같은 이유다. 저장하면 질의 조건이 바뀌었을 때
  옛 집합이 남아 무엇이 현재의 dispatch 입력인지 흐려진다.
- 두 필터가 분리되어 있어야 역할별 조망을 조합으로 만들 수 있다 — plane 권한은
  스코프가, 계층 높이는 level 창이 담당한다.
