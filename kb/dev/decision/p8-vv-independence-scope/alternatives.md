---
id: https://agentic-knowledge-base.dev/id/chunk/0f6b9efd-3473-4c5a-bcfb-3727c6ad394d
type: decision
level: logical
title_ko: 기준 직접 수정 경로의 기각과 저장 분리 형태
title: Rejecting direct criterion edits; the storage-separation choice
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T19:40:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e
---
**대안** — 개발 역할이 합격 기준을 직접 고치는 경로를 두는 안. 기각 — 기준을 고쳐야 하면 개발 KB의 요구를 고치고 V&V 역할이 다시 파생한다 (8.5절).

**대안** — 별도 저장소 vs 별도 최상위 패키지. 둘 다 허용되며 이 저장소는 별도 패키지(`kb/dev`·`kb/vv`)를 택했다 — 게이트 하나로 두 KB를 검사한다 (8.5절, 유저 결정 2026-09-10).
