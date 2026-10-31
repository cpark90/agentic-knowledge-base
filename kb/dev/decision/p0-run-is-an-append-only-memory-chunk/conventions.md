---
id: https://agentic-knowledge-base.dev/id/chunk/5cc5f2fb-9e1c-4866-8f9c-1d231b567546
type: decision
level: concrete
title_ko: 규범 문서 규약 — 관측된 실행은 kb/vv/run/의 append-only memory 단위 지식인 agt:Run이고 대응 절차는 agt:Runbook으로 가른다
title: Normative-document conventions — Observed runs are agt:Run stored as append-only memory chunks under kb/vv/run/, and response procedures are agt:Runbook
former_title_ko: ["규범 문서 규약 — 관측된 실행은 kb/vv/run/의 append-only memory 지식 항목인 agt:Run이고 대응 절차는 agt:Runbook으로 가른다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:47:22+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T12:41:08+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c
---
**규약** — `p0-run-is-an-append-only-memory-chunk`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `memory`는 관측된 실행 기록 `agt:Run`이며 자극과 환경, 결과를 담는다. `memory`는 구체 수준 전용이고, `kb/vv/run/`의 단위 지식 파일 하나가 기록 하나다. 대응 절차는 `agt:Runbook`으로 가른다. 기록은 append-only다(`r-026`). 그래서 **커밋된 기록은 표기가 바뀌어도 소급하지 않고**, 표기 변경은 앞으로의 기록부터 적용한다.

규약: [지킴] 기록의 표 머리가 바뀌면 게이트는 기록 시각(frontmatter `generated.at`)으로 머리를 가린다. 전환 시각 이전 기록은 옛 머리만, 이후 기록은 새 머리만 받고, 시각을 읽지 못한 기록에는 새 머리를 요구한다. 전환 시각의 단일 정의 위치는 `tools/kb_lib.py`의 `RECORD_HEADER_SINCE`다. 판정 로그의 `입력 해시값` 열과 실행 기록의 `테스트 케이스` 열이 2026-10-25에 이 규칙으로 바뀌었다(Q-0065#Q161).
