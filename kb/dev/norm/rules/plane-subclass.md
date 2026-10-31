---
id: https://agentic-knowledge-base.dev/id/chunk/7b24ba7c-57b9-4479-a39b-6d65d3169412
type: norm
level: logical
title_ko: docs/rules.md 절 지식 종류의 이어짐 — 지식 종류는 하위 클래스이고 추가 근거는 판정 방식이다
former_title_ko: ["docs/rules.md 절 plane의 이어짐 — 지식 종류는 하위 클래스이고 추가 근거는 판정 방식이다"]
title: docs/rules.md plane section continued — planes are subclasses and are added only for a new verification method
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/45b22017-61a8-4082-a99f-9e446ecd67ec
continues: true
---
`plane`으로 적는 지식 종류는 `agt:Chunk`의 **하위 클래스**이고, `level`로 적는 정제 수준은 **속성**인 `agt:hasLevel`이다. 이렇게
나눈 까닭은 지식 종류마다 다른 shape을 붙이기 위해서이고, 같은 항목이 수준을 바꾸는 일이 없기 때문이다. 수준의
전이는 새 단위 지식을 만들어 `refines`로 잇는 방식으로 한다 ([`p4-plane-subclass-level-property`](../../decision/p4-plane-subclass-level-property/conclusion.md)).

**지식 종류를 추가하는 유일한 근거는 판정 방식이 기존 어디와도 다를 때다.** 판정 방식이 같으면 하위 클래스로
둔다. 영향은 단방향이고 순서의 기준은 변화 속도이며, 그 순서는
`requirement → decision → contract/schema → artifact → annotation → memory`다. 무효화도 이 순서로만 전파되므로
파급이 유계가 된다 (노트 5.2절).
