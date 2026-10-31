---
id: https://agentic-knowledge-base.dev/id/chunk/69ed3440-e06b-48e2-968f-ad4461332258
type: norm
level: logical
title_ko: docs/method.md 절 — 정제 전이는 새 단위 지식과 refines 링크다
title: docs/method.md section — a refinement transition is a new chunk plus refines
former_title_ko: ["docs/method.md 절 — 정제 전이는 새 지식 항목과 refines 링크다"]
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/005b8875-a251-4864-a47e-7f261fffe156
heading: 정제 전이
depth: 2
---
정제 수준은 `functional → abstract → logical → concrete → executable` 순이다. 각 정제는 **근거와
`refines` 링크를 남기고** 전이 게이트를 통과해야 한다. 전이 게이트는 어휘 검사를 통과하는지, 후보가 비어
있지 않은지, 배제 근거가 있는지, 판정 도구를 통과하는지를 본다. 게이트 없이 만든 하위 단위 지식은 고아율에
잡힌다 ([`p6-refinement-ladder`](../../decision/p6-refinement-ladder/conclusion.md)).

기존 단위 지식의 수준은 바꾸지 않는다. 전이는 기존 단위 지식의 수준을 갱신하는 것이 아니라 **새 단위 지식을
만들고 `refines`로 잇는 것**이다 (`p4-plane-subclass-level-property`). 단계를 건너뛰면 의도와 결과만 남고 그 사이가 빈다.
