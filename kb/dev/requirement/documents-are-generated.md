---
id: https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b
type: requirement
level: functional
title_ko: 문서는 저장하지 않고 생성한다
title: Documents are generated, not stored
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
---
**요구** — 체계는 코드 파일·문서·보고서·라벨 목록을 청크의 뷰로 생성하고 별도 원본으로 저장하지 않아야 한다.

- **이해관계자**: 업체 · 사람 독자 · **관심사**: 갱신 단절 방지
- **출처**: 노트 4.6절 · 8.24절 · 부록 E.2 (요구 층 공백 — 재도출 감사 §3, 2026-09-10 보충)

저장된 문서는 청크와 별개의 원본이 되어 갱신 단절이 재발한다. 뷰는 리비전과 질의를 가지므로 재현된다.
