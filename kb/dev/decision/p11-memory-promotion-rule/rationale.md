---
id: https://agentic-knowledge-base.dev/id/chunk/1683e5a1-7b80-41ef-abfa-b4651b36edb3
type: decision
level: logical
title_ko: 읽는 시점이 저장 위치를 가르고 규칙이 없으면 memory가 예산을 잠식한다
title: Read timing decides the location; without a rule the memory plane eats the budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/46d1f19a-5541-4328-903d-caa729dcb9b4
---
**근거** (노트 11.4절)

- **읽는 시점이 두 저장 위치를 가르는 기준이다.** 첫 실행 시 한 번에 들어가야
  하는 것만 단기기억이고, 나머지는 필요할 때 라벨로 찾아 여는 장기기억이다.
- 무엇이 오래 남을 지식인지는 프로젝트마다 다르므로 규칙을 유저가 준다.
  규칙이 바뀌면 `memory` plane 비우기 정책이 바뀐다(10.1절 파급).
- 세션 유지 모드의 컨텍스트 누적을 비우는 것이 이 규칙이다(10.3절). 규칙이
  없으면 `memory`가 무한히 커져 컨텍스트 예산을 잠식하고, 첫 실행에 한 번에
  읽는다는 전제부터 무너진다.
