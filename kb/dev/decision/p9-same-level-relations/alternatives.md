---
id: https://agentic-knowledge-base.dev/id/chunk/5d6d052f-46c8-4939-8bcc-27c1ed88b928
type: decision
level: logical
title_ko: 구성 관계의 수기 지정은 후보가 하나일 때 유지되고 여럿이면 -space 변수로 간다
title: Hand-assigned composition is kept for a single candidate and moves to a -space variable for several
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-30T16:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-30T16:05:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/152194cd-d12e-4d2c-9626-ccb6119e1baf
---
**대안** — `part-of`·`depends-on`을 사람이 head에 직접 적는 안(현행 `part_of`). 유지·확장 — 후보가 하나뿐이면 지금처럼 head에 직접 적고, 후보가 여럿이면 `-space` 변수로 다룬다. 배제 근거 없이 하나를 할당하는 것은 금지된다 (노트 9.11절, 요구 24). 도입 5단계에서 전환.
