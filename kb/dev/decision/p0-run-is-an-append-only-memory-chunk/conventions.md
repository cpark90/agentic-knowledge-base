---
id: https://agentic-knowledge-base.dev/id/chunk/5cc5f2fb-9e1c-4866-8f9c-1d231b567546
type: decision
level: concrete
title_ko: 규범 문서 규약 — 관측된 실행은 kb/vv/run/의 append-only memory 청크인 agt:Run이고 대응 절차는 agt:Runbook으로 가른다
title: Normative-document conventions — Observed runs are agt:Run stored as append-only memory chunks under kb/vv/run/, and response procedures are agt:Runbook
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c
---
**규약** — `p0-run-is-an-append-only-memory-chunk`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `memory`는 관측된 실행 기록 `agt:Run`이다. 자극·환경·결과를 담는다. concrete 전용이고 `kb/vv/run/`의 청크 파일 하나가 기록 하나다. 대응 절차는 `agt:Runbook`으로 가른다. 기록은 append-only다(`r-026`). **커밋된 기록은 표기가 바뀌어도 소급하지 않는다.** 표기 변경은 앞으로의 기록부터 적용한다.
