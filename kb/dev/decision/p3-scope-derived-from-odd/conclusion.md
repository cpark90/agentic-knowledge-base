---
id: https://agentic-knowledge-base.dev/id/chunk/d5fd57f5-a6d5-464f-af17-4f5bab994774
type: decision
level: concrete
title_ko: 하네스는 ODD에서 스코프를 잘라낸다
title: The harness cuts scope out of the ODD
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0060]
part_of: https://agentic-knowledge-base.dev/id/composite/494002b4-33ba-470c-93ee-cc0fe39be1c7
composite: {id: https://agentic-knowledge-base.dev/id/composite/494002b4-33ba-470c-93ee-cc0fe39be1c7, title_ko: 스코프의 파생, title: Deriving scope from the ODD}
---
**결론** — 하네스는 ODD에서 스코프를 잘라낸다. 스코프는 **어느 ODD에서 나왔는지를 `from`으로 밝히고**, restrictive 모드로 쓴다.

- `inherit` — ODD 속성을 가져온다 (`inherit static.*`, `inherit environment.database`)
- `include plane` — plane 권한을 준다 (`include plane source (write)`)
- `conditional` — 조건부 권한 (`if design-decision(target).level = concrete`)

**스코프에 ODD에 없는 속성을 새로 쓸 수 없다.**

에이전트의 작업 집합(0.5절)은 지식 베이스를 이 스코프로 거른 질의 결과다. 따라서 **에이전트가 볼 수 있는 조건은 ODD 속성 중 스코프가 inherit한 것뿐이고, 나머지는 그 에이전트에게 존재하지 않는다.**
