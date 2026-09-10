---
id: https://agentic-knowledge-base.dev/id/chunk/b009c97f-50bf-4084-9487-8430c00af7f1
type: decision
level: concrete
title_ko: 정체성은 IRI이고 상태 변화는 wasRevisionOf 연쇄다
title: Identity is the IRI; state change is a wasRevisionOf chain
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0051]
part_of: https://agentic-knowledge-base.dev/id/composite/215abd9c-4b8f-458e-aec7-6d09034dd8bd
composite: {id: https://agentic-knowledge-base.dev/id/composite/215abd9c-4b8f-458e-aec7-6d09034dd8bd, title_ko: 개체의 시간 정체성, title: Temporal identity of individuals}
---
**결론** — 지식 베이스는 현재 상태 하나이고, 개체는 개정을 거치며 지속한다. **개체의 시간 정체성을 온톨로지가 정의한다.**

개체는 시간을 관통하여 존재하고(endurant) 개정될 뿐이라는 관점을 채택한다. **정체성은 개체의 IRI이고, 상태의 변화는 PROV-O의 `prov:wasRevisionOf` 연쇄다.** 별도의 정체성 관계를 지어내지 않는다 (4.8절).
