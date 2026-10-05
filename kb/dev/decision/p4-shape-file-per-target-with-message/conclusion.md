---
id: https://agentic-knowledge-base.dev/id/chunk/19cd7b08-583b-4c9b-9cfa-8c7ef6a78a8a
type: decision
level: concrete
title_ko: shape 파일은 검사 대상 하나를 담고 모든 property shape는 강제하는 규칙을 적은 sh:message를 단다
title: A shape file holds one inspection target, and every property shape carries an sh:message stating the rule it enforces
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/715a53ec-b1a3-4a8a-92ff-31bb1806ef9b
composite: {id: https://agentic-knowledge-base.dev/id/composite/715a53ec-b1a3-4a8a-92ff-31bb1806ef9b, title_ko: shape 파일과 위반 메시지, title: Shape files and violation messages}
---
**결론** — SHACL shape(`kb/ontology/shapes/`)는 다음 꼴로 쓴다.

- **파일 하나가 검사 대상 하나 또는 밀접한 쌍을 담는다.** 파일명은 `<대상>-shapes.ttl`이다.
- **모든 property shape에 `sh:message`를 단다.** 메시지에는 강제하는 규칙을 적는다. 시행 중인 메시지는 출처(노트 절 번호 또는 결정 슬러그)를 괄호로 붙인다.

게이트 `shacl`(`tools/validate.py`)은 위반 보고에 `sh:message`를 싣고 "sh:message 가 수정 방향이다"로 끝낸다. 파일명과 메시지의 유무를 판정하는 게이트는 없다. 리뷰 규범이다.
