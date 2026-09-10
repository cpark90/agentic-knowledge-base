---
id: https://agentic-knowledge-base.dev/id/chunk/2f009d87-1c7c-46f2-bbf0-1d37d7c793b0
type: decision
level: concrete
title_ko: plane 배정은 툴 표면을 바꿔야 효과가 난다
title: Plane assignment only works if the tool surface changes with it
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0081, https://agentic-knowledge-base.dev/id/chunk-d0082]
part_of: https://agentic-knowledge-base.dev/id/composite/3ebc2598-b846-412e-b76e-4ebb13ce90a4
composite: {id: https://agentic-knowledge-base.dev/id/composite/3ebc2598-b846-412e-b76e-4ebb13ce90a4, title_ko: plane 배정과 읽기 응답, title: Plane assignment and read response}
---
**결론** — 에이전트는 read scope와 write scope에 해당하는 plane만 배정받는다.
**툴 표면이 배정에 따라 달라져야 실제 효과가 난다.** 저장소만 나누고 읽기 툴이
전체를 반환하면 컨텍스트 분리는 달성되지 않는다.

읽기 응답은 **청크 라벨 목록**이 기본이다(4.4절). plane마다 라벨이 담는 것이
다르다.

| plane | 기본 읽기 응답 |
|---|---|
| `decision` | 결정 단위 요약 (ID + 결론 + 상태) |
| `annotation` | 미해소 스레드만 |
| `schema` | 변경된 필드 diff |
| `contract` | 시그니처 목록 |
| `artifact` | 심볼 목록, 요청 시 본문 |
