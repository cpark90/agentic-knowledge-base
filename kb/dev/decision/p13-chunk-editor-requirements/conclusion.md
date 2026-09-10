---
id: https://agentic-knowledge-base.dev/id/chunk/c5890ddf-86b5-443e-9dff-544ae13e8ab3
type: decision
level: concrete
title_ko: 청크 편집기는 체계의 규칙을 저장 시점에 강제한다
title: The chunk editor enforces the system's rules at save time
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0154]
part_of: https://agentic-knowledge-base.dev/id/composite/922f75fe-58e0-4964-b79b-b9897ac35ce5
composite: {id: https://agentic-knowledge-base.dev/id/composite/922f75fe-58e0-4964-b79b-b9897ac35ce5, title_ko: 청크 편집기의 최소 요구, title: Minimum requirements for the chunk editor}
---
**결론** — 청크를 만드는 도구가 만족해야 할 최소 요구를 다섯으로 고정한다.
전부 체계의 규칙을 **저장 시점에** 강제하기 위한 것이다.

| 요구 | 이유 |
|---|---|
| 42줄 초과 시 즉시 경고, 저장 시 분할 제안 | shape 위반을 저장 전에 |
| 라벨 없이 저장 불가 | 라벨링 원칙 |
| plane·level 선택 필수 | head 그래프 |
| 참조한 청크를 provenance에 자동 기록 | 구축 (9.3절) |
| 본문 편집과 링크 편집을 다른 화면에 | 청크는 자기 링크를 모른다 (4.3절) |
