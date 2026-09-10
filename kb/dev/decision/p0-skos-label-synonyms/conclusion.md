---
id: https://agentic-knowledge-base.dev/id/chunk/f5d2aa76-09cd-4533-83cf-b4e0f738594b
type: decision
level: concrete
title_ko: prefLabel·altLabel·hiddenLabel
title: prefLabel, altLabel, hiddenLabel
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0033]
part_of: https://agentic-knowledge-base.dev/id/composite/8a718aed-4f88-4847-9d00-800c0f14a0e7
composite: {id: https://agentic-knowledge-base.dev/id/composite/8a718aed-4f88-4847-9d00-800c0f14a0e7, title_ko: 동의어는 없애지 않고 SKOS 라벨로 등록한다, title: Register synonyms as SKOS labels instead of removing them}
---
**결론** — 0.6절 "동의어 사용 금지"를 어휘 수준에서 강제하는 방법은 동의어를
없애는 것이 아니라 **등록**하는 것이다. SKOS 라벨 구분을 쓴다.

- `skos:prefLabel` — 유일한 공식 이름. 한/영 각 하나
- `skos:altLabel` — 허용되는 대체 표기. 검색에는 쓰이되 산문에는 쓰지 않음
- `skos:hiddenLabel` — 과거 표기, 오타 변형. 검색에만
