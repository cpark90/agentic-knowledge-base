---
id: https://agentic-knowledge-base.dev/id/chunk/46616ef9-3a36-4fa1-87cc-f3e2a76000e5
type: decision
level: logical
title_ko: 파일 단위 링크는 무효화를 파일 전체로 번지게 한다
title: File-level links spread invalidation across whole files
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/e9f394a2-e59b-41ea-be88-d8ed2c5f9c60
---
**근거** (노트 9.1·9.7절) — 파일 단위 링크는 어느 부분이 어느 부분에 대응하는지 말하지 못하므로, 파일 한 곳이 바뀌면 6.5절 무효화가 파일 전체로 번진다. 청크·복합체를 양 끝으로 삼아야 무효화가 실제로 바뀐 지식에서 멈춘다.

**TIM은 한 번 정해지면 바꾸기 어렵다.** 링크 타입을 바꾸면 그 타입으로 이미 만든 링크 전부가 재검토 대상이 된다. 그래서 타입을 소수로 고정하고, 확장은 **타입 추가로만** 한다. TIM을 온톨로지 안에 두는 것은 이 비용을 품질 검사와 게이트가 대신 감시하게 하려는 것이다.
