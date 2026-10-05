---
id: https://agentic-knowledge-base.dev/id/chunk/e0281397-3597-4650-be66-ea2613bded61
type: decision
level: logical
title_ko: 에이전트는 라벨 목록을 먼저 읽고 파일 하나를 열어 이해해야 하므로 뜻이 라벨과 정의에 있어야 한다
title: Agents read the label list first and must understand a file on opening it, so meaning has to live in labels and definitions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7e4beefd-65a6-45b8-9386-340c88a2a538
---
**근거** — `STYLEGUIDE.md` §0의 목표가 이유다. 다음 세션의 에이전트가 파일 하나를 열어 빠르게 이해하고 무엇을 재사용할지 알 수 있어야 한다.

에이전트는 라벨 목록을 먼저 받고 필요한 본문만 연다(`p4-label-is-the-interface`). 그러므로 항목의 뜻은 라벨과 정의에 있어야 조망 단계에서 보인다. 온톨로지 정의문은 이 규약을 따른다. 예를 들어 `agt:Chunk`의 정의문은 단위의 조건과 함께 그 조건을 판정하는 게이트와 리뷰 규범을 적는다.

미확정: 이 규약은 2026-09-01 초기 구축 때 `STYLEGUIDE.md`에 들어갔다. 유저 결정의 기록과, 정의의 내용을 존재 이유와 쓰임으로 정한 출처 문서는 확인하지 못했다.
