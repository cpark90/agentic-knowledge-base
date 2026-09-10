---
id: https://agentic-knowledge-base.dev/id/chunk-d0053
type: decision
level: concrete
title_ko: 관계도 표준을 쓰고 고유 관계는 subPropertyOf로 매단다
title: Reuse standard relations; hang custom ones under subPropertyOf
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 관계도 지어내지 않는다. 상위 온톨로지 계열의 표준 관계
온톨로지(RO)를 비롯한 표준에 있는 것을 우선 쓰고, 표준에 없는 고유 관계만
정의하되 반드시 `rdfs:subPropertyOf`로 표준 관계 아래에 둔다.

**근거** (노트 2.8절)
- 표준으로 충분한 것들: 부분-전체 `bfo:part_of`, 출처
  `prov:wasDerivedFrom`, 역할·기능 실현 `ro:realizes`, 참여
  `ro:participates_in`, 선행 `ro:precedes`(scene 순서에서 co:index와 택일).
- 표준에 없어 고유하게 두는 것은 충족·검증·정련 셋뿐이다 —
  `agt:satisfies`(`ro:realizes`의 특수화)·`agt:verifies`·`agt:refines`.
- 고유 관계를 표준 관계 아래에 두면 표준 관계로 질의할 때 고유 관계도 함께
  걸린다. 외부 온톨로지·도구와의 질의 호환이 유지된다.
