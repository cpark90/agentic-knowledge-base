---
id: https://agentic-knowledge-base.dev/id/chunk/43ccbea0-23c0-49be-913c-960a7dcbbf8c
type: decision
level: concrete
title_ko: 스키마는 결정에서 파생되어 계약을 제약하고 변경은 호환성 검사를 거친다
title: Schemas derive from decisions, constrain contracts, and changes pass a compatibility check
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
composite: {id: https://agentic-knowledge-base.dev/id/composite/d7435609-eefb-48a3-bab6-2cab0f56476e, title_ko: 스키마의 파생과 변경, title: Schema derivation and change}
part_of: https://agentic-knowledge-base.dev/id/composite/d7435609-eefb-48a3-bab6-2cab0f56476e
---
**결론** — `schema`는 독립적으로 생기지 않는다. `decision`에서 `derives-from`으로 파생되고, `contract`를 `constrains`한다. 스키마의 logical(필드 범위·호환 제약)은 JSON Schema 자체이고, concrete는 예시 인스턴스다.

스키마 변경은 호환성 검사를 거친다. 하위 호환이면 `prov:wasRevisionOf`, 아니면 새 IRI + `supersedes`. 후자는 `constrains` 링크 전부를 `suspect`로 만든다 (노트 7.6절).
