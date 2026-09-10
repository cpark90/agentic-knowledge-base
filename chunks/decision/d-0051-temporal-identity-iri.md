---
id: https://agentic-knowledge-base.dev/id/chunk-d0051
type: decision
level: concrete
title_ko: 개체의 시간 정체성은 IRI이고 상태 변화는 wasRevisionOf다
title: Temporal identity is the IRI; state change is wasRevisionOf
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — scene은 스냅샷이고 개체는 여러 scene을 관통하여 존재한다
(endurant). 정체성은 개체의 IRI이고, 상태의 변화는 PROV-O
`prov:wasRevisionOf` 연쇄로 적는다. 별도의 정체성 관계를 지어내지 않는다.

**근거** (노트 2.6절)
- 같은 결정, 같은 시그니처, 같은 모듈이 시간이 지나며 변한다. 변한 뒤에도
  "같은 것"으로 추적되어야 5.4절 무효화 전파와 Part VIII 링크가 성립한다.
- 시간 정체성을 명시하지 않으면 매 scene마다 새 개체가 생겨 링크가 전부
  끊어진다. 그래서 정체성은 온톨로지가 정의해야 할 사항이다.
- 표준 관계로 충분하므로 고유 관계를 만들지 않는다 (4.8절, 0.0절).
