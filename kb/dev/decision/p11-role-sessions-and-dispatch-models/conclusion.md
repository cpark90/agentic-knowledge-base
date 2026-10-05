---
id: https://agentic-knowledge-base.dev/id/chunk/f217c4f5-761a-463a-b3a2-d58391383706
type: decision
level: concrete
title_ko: 세션 역할은 부팅 스크립트로 띄우고 스크립트 없는 세션은 orchestrator이며 dispatch는 opus 또는 sonnet으로 역할 표와 스코프를 브리핑한다
title: Session roles start from launch scripts, a session without one is the orchestrator, and dispatch runs on opus or sonnet with a briefing of the role table and scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/04ec773f-bf28-4ae8-a8d6-5fc4012dff58
composite: {id: https://agentic-knowledge-base.dev/id/composite/04ec773f-bf28-4ae8-a8d6-5fc4012dff58, title_ko: 역할 기동 — 세션과 dispatch, title: Starting roles — sessions and dispatch}
---
**결론** — 역할은 실행 모드에 따라 두 길로 기동한다. 실행 모드의 형식 원본은 `kg/catalog-kg.ttl`의 `agt:executionMode`다.

| 역할 | 실행 모드 | 기동 | 읽는 지침 |
|---|---|---|---|
| hci · orchestrator | 세션 유지 | `harness/scripts/run-hci.sh` · `harness/scripts/run-orchestrator.sh` | `harness/agents/<역할>.md` |
| developer · vnv | dispatch | orchestrator의 dispatch 호출 | 브리핑 |

- **스크립트 없이 띄운 세션은 orchestrator다.** 저장소의 진입 문서로 열린 기본 세션이 orchestrator의 자리다.
- **dispatch는 opus 또는 sonnet 모델로 한다**(유저 지시 2026-09-26·2026-10-03). 설계 판단·새 구조·상태 전파는 opus다. 규약이 정해진 기계적 반영과 전수 실측은 sonnet이다. 모델은 호출에 명시한다. 생략하면 dispatch 대상이 메인 세션의 모델을 물려받는다.
- **developer·vnv는 dispatch 때 역할 표와 스코프로 브리핑한다.** 브리핑은 그 역할의 책임·write plane·read plane과 스코프·앵커로 거른 작업 집합이다(`p11-execution-mode-and-workset`). dispatch 대상의 hand-back은 서로에게 전달되지 않는다. 한 역할의 판정값을 다른 역할에 넘길 때는 그 표를 브리핑 본문에 붙인다.

이 규약을 판정하는 게이트는 없다. 리뷰 규범이다.
