---
id: https://agentic-knowledge-base.dev/id/chunk/822db955-483e-47ed-ad68-fec783bc825b
type: decision
level: concrete
title_ko: 커뮤니티 탐지는 복합체 후보를 제안할 뿐이고 채택은 사람이 한다
title: Community detection only proposes composite candidates; adoption is a human decision
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/165ef75a-d4f3-4de2-aba2-ea3a8efb787a
composite: {id: https://agentic-knowledge-base.dev/id/composite/165ef75a-d4f3-4de2-aba2-ea3a8efb787a, title_ko: 커뮤니티 탐지와 복합체 후보, title: Community detection and composite candidates}
---
**결론** — 링크·인용 구조에서 계산한 커뮤니티(LARGER의 Leiden 분할)는 "통합이 필요한 것"의
**후보 목록**으로만 쓴다. 결과는 저장하지 않는 뷰(생성물)이고, 채택된 후보만 사람이
`kg/composite-kg.ttl`에 복합체로 쓴다.

| 단계 | 내용 |
|---|---|
| 입력 | 살아 있는 청크와 `refines`·`cites`·`coUpdatesWith` 링크 (head 그래프) |
| 계산 | 커뮤니티 분할. 같은 plane·level 안의 군집만 복합체 후보, plane·level을 넘는 군집은 `relatedTo` 링크 후보 |
| 판정 | 복합체의 통합 기준 둘 — 함께 읽혀야 이해되는가, 순서가 뜻을 갖는가 — 을 사람이 후보마다 본다 |
| 기록 | 채택은 복합체 선언, 기각은 관측 한 줄. 후보 자체는 남기지 않는다 |

도구 자리는 뷰 도구 `project`(도입 8단계)이며, 후보가 뜻을 가지려면 링크 밀도가 먼저 올라야
한다 — 링크 개체가 구축 기록뿐인 지금은 계산해도 복합체 선언과 같은 군집만 나온다.
