---
id: https://agentic-knowledge-base.dev/id/chunk/de40fe40-2780-464f-9e9c-d8e7c105bfe5
type: norm
level: logical
title_ko: STYLEGUIDE.md 절 — 강인성 세 축과 게이트 대응
title: STYLEGUIDE.md section — The three robustness axes and their gates
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/500a7843-2b7b-4f08-a0fb-be32c100dba3
heading: 강인성 세 축과 게이트 대응
depth: 3
---
| 축 | 위협 | 방어 | 게이트 |
|---|---|---|---|
| anti-drift | 어휘가 조용히 갈라짐 | `agt:` 어휘 통제, 표준어 우선 | `validate.py` vocab·labels·boundary |
| anti-rot | 컨텍스트가 무한히 커짐 | 토큰 상한(1,092), 라벨 목록 우선 읽기 | `chunk_lint.py`, SHACL `tokenCount` |
| anti-orphan | 쓰이지 않는 지식이 쌓임 | 복합체·링크 연결, 고아율 관측 | (없음 — [`docs/tools.md`](../../../../docs/tools.md) §게이트 밖) |
