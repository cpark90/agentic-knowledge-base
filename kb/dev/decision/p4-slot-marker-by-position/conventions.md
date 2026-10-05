---
id: https://agentic-knowledge-base.dev/id/chunk/f049eeda-00c3-4a7f-8265-3806cbe00acd
type: decision
level: concrete
title_ko: 규범 문서 규약 — 굵은 표지는 그 줄의 필드 머리에 있을 때만 슬롯이고 짧은 한정어만 같은 표지로 본다
title: Normative-document conventions — A bold marker is a slot only at a field head of its line, and only a short qualifier keeps it the same marker
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e1fb54c7-56d8-4864-b56b-cbd7327217d1
---
**규약** — `p4-slot-marker-by-position`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **슬롯 표지는 자리로 판정한다**(2026-09-29). 굵은 표지(`**결론**`·`**요구**`·`**자극**` …)는 그 줄의 **필드 머리**에 있을 때만 슬롯이다 — 줄 시작, 목록 항목 표지(`- `) 바로 다음, 같은 줄에서 앞선 필드를 끝낸 ` · ` 바로 다음. 표 셀 뒤·산문 접속 뒤·문장 중간의 굵은 span은 강조이지 표지가 아니다. 표지 뒤의 한정어(`**대안 없음**`)는 12자 이하이고 마침표가 없을 때만 같은 표지다 — 길거나 마침표가 있으면 표지 낱말로 시작하는 별개의 문장이다. 일곱 틀 전부에 같은 규칙이다(`chunk2kg` 방출 = `decision-role`의 첫 산문 줄 판정과 같은 종류). 표지 낱말끼리 접두가 겹치면 `kb_lib`가 로드 시점에 죽는다.
