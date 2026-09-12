---
id: https://agentic-knowledge-base.dev/id/chunk/f960aebc-973d-432d-ad7a-1cdbc82f2b8f
type: decision
level: logical
title_ko: 산출물 안 링크 표기와 경로·줄 번호 앵커의 기각
title: Rejecting inline link notation and path-plus-line anchors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T19:40:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c1ce996d-dc84-45c5-b567-a9da42421774
---
**대안** — 링크를 산출물 안에 인라인으로 적는 안. 기각 — 산출물을 열어야 질의할 수 있고 형식마다 표기를 따로 정해야 하며, 링크 모델을 산출물과 독립적으로 교체할 수 없다 (10.5절).

**대안** — 경로 + 줄 번호 앵커. 기각 — 편집마다 깨진다. 청크 IRI를 앵커로 두면 드리프트가 청크 안에 갇힌다 (4.8절, 10.9절).
