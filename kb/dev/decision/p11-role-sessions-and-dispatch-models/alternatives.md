---
id: https://agentic-knowledge-base.dev/id/chunk/2fc02270-220d-4bdd-95c9-cf951a3ca314
type: decision
level: logical
title_ko: hci를 서브에이전트로 정의하는 안과 dispatch가 메인 세션 모델을 물려받는 안은 기각된다
title: Defining hci as a subagent and letting dispatch inherit the main session model are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/04ec773f-bf28-4ae8-a8d6-5fc4012dff58
---
**대안** — 둘을 기각한다. 둘 다 이 저장소에서 실제로 시행됐다가 바뀐 방식이다.

| 대안 | 기각 이유 |
|---|---|
| hci를 서브에이전트 정의 파일로 둔다(2026-10-03까지) | 카탈로그의 hci 실행 모드는 세션 유지다. 서브에이전트는 dispatch처럼 호출마다 새 컨텍스트로 돈다. 2026-10-03 정돈에서 정의 파일을 지우고 부팅 스크립트로 옮겼다 |
| dispatch 호출에 모델을 적지 않는다 | 대상이 메인 세션의 모델을 물려받는다. 유저 지시(2026-09-26·2026-10-03)가 opus와 sonnet만 허용한다 |
