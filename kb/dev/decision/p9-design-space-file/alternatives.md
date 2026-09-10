---
id: https://agentic-knowledge-base.dev/id/chunk/f9294170-85e0-42b1-9898-575df58d3b4c
type: decision
level: logical
title_ko: 후보를 head·deps에 두는 안의 기각
title: Rejecting candidates in head or deps
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T19:40:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/77fa385a-9aa6-406f-b72f-bb966f6c42f8
---
**대안** — 후보 링크를 확정 링크와 같은 자리(청크 head, Bazel deps)에 두는 안. 기각 — 후보는 절대 deps가 되지 않는다. 확정되는 순간 생성기가 `-space`에서 head로 옮기고 그것이 한 줄 diff로 리뷰된다 (9.4절, 9.10절).
