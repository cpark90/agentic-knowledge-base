---
id: https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320
type: decision
level: concrete
title_ko: 실행 모드는 입력이고 dispatch에는 스코프로 거른 작업 집합만 전달한다
title: Execution mode is an input, and dispatch carries only the scope-filtered workset
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0126]
part_of: https://agentic-knowledge-base.dev/id/composite/7e1f24c0-e217-46a1-8599-5fd5ac39e486
composite: {id: https://agentic-knowledge-base.dev/id/composite/7e1f24c0-e217-46a1-8599-5fd5ac39e486, title_ko: 실행 모드와 dispatch 재진입, title: Execution mode and dispatch re-entry}
---
**결론** — 실행 모드는 **세션 유지**와 **dispatch** 둘이며 유저가 입력으로
준다.

dispatch 대상에게는 전체 컨텍스트가 아니라 **그 역할의 스코프로 거른 작업
집합**(0.5절)만 전달한다. 스코프가 이미 무엇을 볼지 정해 두었으므로 요약의
범위를 따로 정하지 않는다.

세션 유지 모드의 컨텍스트 로트·오염 누적은 `memory` plane 승격 규칙으로
주기적으로 비운다.
