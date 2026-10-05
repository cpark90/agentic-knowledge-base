---
id: https://agentic-knowledge-base.dev/id/chunk/63cd97c9-d7f5-4771-af07-1bc63e42ceff
type: decision
level: logical
title_ko: ODD 크기는 수치 상한 없이 참조율과 기각률로 조정한다
title: ODD size is tuned by reference rate and rejection rate, without a numeric cap
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-05T23:21:44+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e14838e7-3b70-4325-84b9-d5b69377bc39
composite: {id: https://agentic-knowledge-base.dev/id/composite/e14838e7-3b70-4325-84b9-d5b69377bc39, title_ko: ODD 크기의 두 지표 조정, title: Tuning ODD size by two indicators}
---
**결론** — ODD의 크기에 수치 상한을 두지 않고 두 지표로 조정한다. 두 지표는 참조율과 기각률이다. 참조율은 조건 중 가정·스코프가 실제 참조하는 비율이며 낮으면 과대다. 기각률은 "ODD에 없는 조건" 게이트의 거부 횟수이며 높으면 과소다. ODD의 변경 절차를 이 둘에 연동한다.
