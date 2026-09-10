---
id: https://agentic-knowledge-base.dev/id/chunk/2f4dffbe-34da-4dc7-ad52-8e549088d23f
type: decision
level: concrete
title_ko: 시간열 개체를 두지 않는다
title: No timeline entities
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0012]
part_of: https://agentic-knowledge-base.dev/id/composite/52124ca7-97f8-4b5e-818f-1574ab131484
composite: {id: https://agentic-knowledge-base.dev/id/composite/52124ca7-97f8-4b5e-818f-1574ab131484, title_ko: 상태의 단위는 리비전과 작업 집합 둘뿐이다, title: Revision and workset are the only units of state}
---
**결론** — **시간열 개체를 두지 않는다.** 두 지식 베이스 모두 현재 상태
하나이고, 전개는 관측(append-only)과 `prov:wasRevisionOf`가 운반한다. 상태를
가리키는 단위는 둘이다.

- **리비전** — 전체 그래프의 정규화 직렬화 해시 (2.5절). 스냅샷의 식별자이며
  저장하지 않는다. 커밋이 곧 리비전이다
- **작업 집합**(`agt:Workset`) — 지식 베이스를 **스코프 × level 창**으로 거른
  청크 집합. 질의 결과이며 저장하지 않는다 (4.6절)

**작업 집합이 인지 측정(11.3절)과 dispatch 전달(10.3절)의 단위다.** 스코프가
plane과 조건을, level 창이 계층 높이를 거른다 — 구현 에이전트는 logical
이하만, 설계 에이전트는 abstract 이상만 본다.

과거 작업 집합이 필요하면 **그 리비전에 같은 질의를 다시 건다.**
