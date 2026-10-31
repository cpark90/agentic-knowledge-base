---
id: https://agentic-knowledge-base.dev/id/chunk/dcf96f18-9ab2-42b2-bc6f-9bd02fcf2837
type: decision
level: concrete
title_ko: 산출물 리뷰는 본문보다 맥락을 먼저 보여준다
title: Artifact review shows context before the body
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0150-artifact-review-support.md, id: https://agentic-knowledge-base.dev/id/chunk-d0150, title_ko: "산출물 리뷰는 본문보다 먼저 맥락을 보여준다", title: "Artifact review shows context before the body"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:14:02+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0150]
part_of: https://agentic-knowledge-base.dev/id/composite/ea213fc4-d774-409a-91e6-3afd40a1b6f3
composite: {id: https://agentic-knowledge-base.dev/id/composite/ea213fc4-d774-409a-91e6-3afd40a1b6f3, title_ko: 산출물 리뷰 지원 화면, title: What artifact review displays}
---
**결론** — 변경된 산출물의 리뷰어에게 산출물 본문을 읽기 전에
**"무엇을 위한 변경이고 무엇이 흔들리는가"** 를 먼저 보여준다.

| 표시 | 출처 |
|---|---|
| 이 단위 지식이 충족하는 결정 | `satisfies` → 결정 라벨 |
| 그 결정의 가정과 현재 상태 | `assumes` + 상태 |
| 이 변경으로 `suspect`가 될 링크 | 9.6절 재검증 예측 |
| 이 단위 지식의 기준을 검증하는 검증 단위 지식 | `verifies` 역방향 |
| 토큰 상한 초과 여부, 라벨 변경 여부 | shape |

코드 리뷰가 대표적이나 문서·절차 리뷰도 같다.
