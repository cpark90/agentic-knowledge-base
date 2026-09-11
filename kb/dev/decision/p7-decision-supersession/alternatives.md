---
id: https://agentic-knowledge-base.dev/id/chunk/46606cc7-09b7-4086-b999-1663bd806be5
type: decision
level: logical
title_ko: 제자리 수정과 삭제의 기각
title: Rejecting in-place edits and deletion
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c34b1d2f-86fb-4cd1-b532-edf65e7230c7
---
**대안** — 옛 결정을 제자리에서 고쳐 쓰는 안. 기각 — 결론이 바뀐 것은 새 결정이며, 제자리 수정은 `wasRevisionOf`(같은 결정의 개정)와 구분되지 않는다 (노트 7.6절 스키마의 호환 규칙과 같은 논리).

**대안** — 옛 결정을 삭제하는 안. 기각 — `satisfies` 링크가 댕글링이 되고 근거가 사라진다 (노트 7.4절).
