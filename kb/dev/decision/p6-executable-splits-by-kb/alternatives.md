---
id: https://agentic-knowledge-base.dev/id/chunk/7af94d35-2d65-4ff4-9ecd-f46ebd60d5a7
type: decision
level: logical
title_ko: 역할 태그만으로 구현·검증을 구분하는 안의 대체
title: Superseding tag-only separation of implementation and verification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-12T00:50:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/8e8697a1-16b9-4c24-a377-340db2b6000b
---
**대안** — 구현과 검증기를 같은 KB에 두고 역할 태그로만 구분하는 안(v2). 대체 — v3부터 KB가 다르다: 구현은 개발 KB, 검증기는 V&V KB이며 `verifies`의 주어는 V&V KB 청크뿐이다. 같은 저장소에 둘 때는 태그로 구분하되 스코프는 분리한다 (6.1절).
