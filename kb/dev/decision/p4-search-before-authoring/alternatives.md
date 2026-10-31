---
id: https://agentic-knowledge-base.dev/id/chunk/562c9027-07e2-4343-af2c-79c956652a22
type: decision
level: concrete
title_ko: 같은 뜻의 노드를 더 만드는 안과 한 노드에 두 가지를 담는 안은 택하지 않는다
title: Adding a same-meaning node and keeping two things in one node are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0187-authoring-discipline-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:40:17+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:40:17+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/54ecc54e-24cd-420e-b5c9-4405958c87ec
---
**대안** — 원천(harness-functional `ONTOLOGYSTYLE.md`)이 대비한 안 둘을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 같은 뜻의 노드를 하나 더 만든다 | 근사 동의어 클래스는 저장소가 막는 drift이고, 동의어는 새 노드가 아니라 한 노드의 `skos:altLabel`로 붙인다(ONTOLOGYSTYLE §1b) |
| 한 노드에 두 가지를 담아 둔다 | 단일 책임 위반의 신호로 다룬다. 그래서 서술 상한을 넘는 노드는 분해하거나 대안 서술을 별도 노드로 분리한다(§1c) |
