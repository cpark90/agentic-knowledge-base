---
id: https://agentic-knowledge-base.dev/id/chunk/1346522d-0e9b-4a3d-9390-082cf9aa47f3
type: decision
level: concrete
title_ko: 검증 대상은 제품과 에이전트 둘이다
title: There are two verification targets - the product and the agent
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0131]
part_of: https://agentic-knowledge-base.dev/id/composite/e11ea926-9802-41f2-92a9-62dccfa80b4d
composite: {id: https://agentic-knowledge-base.dev/id/composite/e11ea926-9802-41f2-92a9-62dccfa80b4d, title_ko: 검증의 두 대상, title: The two targets of verification}
---
**결론** — 이 프로젝트에는 검증 대상이 둘이며, **둘을 섞으면 "무엇이 틀렸는가"가 흐려진다.**

- **제품** — 에이전트가 만든 소프트웨어. 자극은 concrete 케이스(입력 데이터·외부 서비스 응답·사용자 행동), 판정은 logical 기준 대비 동작
- **에이전트** — 소프트웨어를 만드는 에이전트 자체. 자극은 작업 집합과 유저 피드백, 판정은 산출물 품질과 인지능력(11.3절)

두 대상의 검증 청크는 별개이며 `verifies` 링크의 **도착점이 다르다** — 제품 검증은 `decision`·`contract`의 logical 기준을, 에이전트 검증은 하네스·스코프 개체를 검증한다.
