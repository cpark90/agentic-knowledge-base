---
id: https://agentic-knowledge-base.dev/id/chunk/db98947b-84c6-4e0f-9131-10a175665abc
type: decision
level: concrete
title_ko: 굵은 표지는 그 줄의 필드 머리에 있을 때만 슬롯이고 짧은 한정어만 같은 표지로 본다
title: A bold marker is a slot only at a field head of its line, and only a short qualifier keeps it the same marker
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:32:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e1fb54c7-56d8-4864-b56b-cbd7327217d1
composite: {id: https://agentic-knowledge-base.dev/id/composite/e1fb54c7-56d8-4864-b56b-cbd7327217d1, title_ko: 슬롯 표지 — 자리 판정, title: Slot markers — judged by position}
---
**결론** — 슬롯 표지는 자리로 판정한다(2026-09-29). 굵은 표지(`**결론**`·`**요구**`·`**자극**` 등)는 그 줄의 **필드 머리**에 있을 때만 슬롯이다. 필드 머리는 셋이다.

- 줄 시작
- 목록 항목 표지(`- `) 바로 다음
- 같은 줄에서 앞선 필드를 끝낸 ` · ` 바로 다음

표 셀 뒤·산문 접속 뒤·문장 중간의 굵은 span은 강조이지 표지가 아니다. 표지 뒤의 한정어(`**대안 없음**`)는 길이 12자 이하이고 마침표가 없으며, 꼴이 괄호(`(미확정)`), 대시(` — 미확정`), 낱말 ` 없음` 셋 중 하나일 때만 같은 표지다(지시 0234, 2026-10-24). `**자극 열**`처럼 그 밖의 꼴은 표지가 아니다. 길거나 마침표가 있으면 표지 낱말로 시작하는 별개의 문장이다. 일곱 틀 전부에 같은 규칙이다.

표지 낱말의 단일 정의 위치는 `chunk2kg`의 `BODY_SLOT_MARKERS` 하나다. 표지 판정 함수는 `chunk2kg.body_slot_mark` 하나이고, 방출과 게이트 `decision-role`, `consistency`가 모두 이 함수를 쓴다(지시 0240, 2026-10-24). 표지 낱말끼리 접두가 겹치면 `kb_lib`가 로드 시점에 죽는다.

**본문 슬롯 검사** — 틀이 요구하는 슬롯 표지가 빠지면 `*-body-shapes.ttl` 넷(2026-09-22)이 거부하고 게이트 id는 `shacl`(body-slot)이다. `chunk2kg`가 본문에서 표지를 찾아 `agt:bodySlot`으로 내고 shape가 판정하며, 슬롯마다 등록 질문이 `sh:description`에 있다. V&V 시나리오의 `**자극**`·`**요인**`·`**배제 자극**`은 새 틀이 아니라 결정 틀의 세 슬롯에 사상된 표지다(2026-09-29). 한정어 길이 상한의 단일 정의 위치는 `BODY_SLOT_QUALIFIER_MAX`이고 접두 겹침 검사는 `kb_lib.validate_body_slot_markers`다. 위반은 지식 종류의 write 역할이 빠진 슬롯을 채워 해소한다.
