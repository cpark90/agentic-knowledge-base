---
id: https://agentic-knowledge-base.dev/id/chunk/3d66b1bc-0e65-4e62-9654-fc0ddb6b7d20
type: decision
level: concrete
title_ko: ODD는 영역 개념이 아니라 프로젝트당 하나의 문서다
title: The ODD is one versioned document per project, not a region concept
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0058-odd-is-a-document.md, id: https://agentic-knowledge-base.dev/id/chunk-d0058, title_ko: "ODD는 영역 개념이 아니라 프로젝트당 하나의 문서다", title: "The ODD is a document, one per project - not a permission region"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0058]
part_of: https://agentic-knowledge-base.dev/id/composite/71a6fe17-3337-48af-b27d-271bb17a0ab4
composite: {id: https://agentic-knowledge-base.dev/id/composite/71a6fe17-3337-48af-b27d-271bb17a0ab4, title_ko: ODD는 문서다, title: The ODD is a document}
---
**결론** — ODD는 **이 프로젝트의 지식과 작업이 설계된 운영 조건의 명세**다. 적용 범위처럼 권한을 나누는 영역 개념이 아니라, **실제로 작성되고 버전 관리되고 참조되는 문서**다.

ODD가 답하는 질문은 하나다 — **"이 프로젝트의 산출물은 어떤 조건에서 동작하도록 설계되었는가."**

- 적용 범위 — 누가 무엇을 볼 수 있는가
- 가정 — 이 항목 하나가 무엇을 전제하는가
- **ODD — 전체가 무엇을 전제하는가**

**프로젝트당 하나다.** 하위 시스템이 별도 ODD를 가지면 상위 ODD의 부분집합이어야 한다 (3.11절).
