---
id: https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c
type: decision
level: concrete
title_ko: 작업 집합은 스코프 × 수준 창 × 앵커 이웃이다
title: A working set is scope × level window × anchor neighbourhood
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-11T02:20:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a]
composite: {id: https://agentic-knowledge-base.dev/id/composite/0e7f41dc-e010-4c71-809f-51535f17e6ce, title_ko: 작업 집합의 정의 — 앵커 이웃, title: Working set definition — anchor neighbourhood}
part_of: https://agentic-knowledge-base.dev/id/composite/0e7f41dc-e010-4c71-809f-51535f17e6ce
---
**결론** — 작업 집합(`agt:Workset`)은 지식 베이스를 **스코프 × 수준 창 × 앵커 이웃**으로 거른 청크 집합이다 (노트 0.5절, 2026-09-11 유저 결정). 스코프가 plane과 조건을, 수준 창이 계층 높이를 거르고, **앵커 이웃이 양을 거른다.** 앵커(`agt:anchor`)는 지금 작업이 가리키는 청크 IRI이고, 이웃은 링크(`refines`·`hasDirectPart`·`cites`·`satisfies`·`supersedes`)로 k홉(기본 1) 안의 청크다.

- 라벨 목록은 이웃만 보이고 나머지는 접는다 — "N more (expand?)" (5.6절)
- 예산은 이웃의 본문을 우선순위로 펼치는 데 쓴다 — 앵커 > 같은 복합체 부분 > `refines` 양방향 > 나머지
- 앵커 없는 요청에는 접힌 라벨 목록만 준다. dispatch(11.3절)는 스코프와 앵커로 거른 작업 집합을 넘긴다
- 도입 2단계 통과 조건은 "역할·작업(앵커)별 작업 집합 ≤ 예산"이다 (14.1절 정정본)

도구: `tools/workset.py` (`bazel build //kg:workset_<role>`, 인자 `--anchor`·`--hops`·`--levels`·`--budget`). 지표: `metrics`의 "역할별 앵커 작업 집합의 예산 내 비율".
