---
id: https://agentic-knowledge-base.dev/id/chunk/c5bb1922-eb82-4b96-a49c-a46e41c239e4
type: decision
level: concrete
title_ko: 링크 타입은 수직 하나와 수평 열둘로 고정한다
title: One vertical link type and twelve horizontal ones
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/57a2dca5-8628-4255-a964-9928d2fd14a4, https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0010]
part_of: https://agentic-knowledge-base.dev/id/composite/42c1ecbe-34fd-4c59-9038-51db6144ad29
composite: {id: https://agentic-knowledge-base.dev/id/composite/42c1ecbe-34fd-4c59-9038-51db6144ad29, title_ko: 링크 타입은 수직 하나와 수평 열둘로 고정한다, title: One vertical link type and twelve horizontal ones}
---
**결론** — 링크 타입은 확립된 의미를 가진 것만 쓰고, **수직**(계층을 따라)과 **수평**(plane을 가로질러)으로 나눈다.

**수직** — `refines` (level n+1 → level n). 6.2절 정제의 모든 전이가 이 링크를 남기며, **계층은 링크로 구현된다.** concrete에서 `refines`를 거슬러 functional까지 닿지 않으면 단계 건너뛰기다.

**수평** — `satisfies`(`contract`·`artifact`→`decision`, n:1), `constrains`(`schema`→`contract`, n:m), `derives-from`(`schema`·`decision`→`decision`, n:1), `verifies`(V&V KB 청크 → 같은 level의 개발 KB 청크, n:m, **KB 간 유일한 링크**), `supersedes`(1:1), `targets`(`annotation`→임의, n:1), `assumes`(임의→`agt:Assumption`, n:m), `prov:wasRevisionOf`(1:1, 외부 어휘).

**확장 채택 4종** — `allocates`(`decision`→복합체, 1:n), `depends-on`(임의→임의, n:m, `constrains`·`generates`의 상위), `generates`(`schema`→`artifact`, 1:n), `conflicts-with`(임의→임의, n:m, 대칭).

특수한 셋 — `refines`만 계층을 따라, `assumes`만 plane을 가로질러 무효화를 전파, `prov:wasRevisionOf`만 시간을 가로질러 잇는다.

**한 방향만 저장한다.** `satisfies`를 저장하면 "무엇이 이 결정을 충족하는가"는 질의로 얻는다.
