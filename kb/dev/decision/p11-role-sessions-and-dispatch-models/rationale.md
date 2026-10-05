---
id: https://agentic-knowledge-base.dev/id/chunk/62f83e48-db35-45e6-a103-a9740ac5f2a5
type: decision
level: logical
title_ko: 역할이 실제로 하는 일은 하네스의 몫이므로 세션 역할은 지침 파일로 정하고 dispatch 모델은 유저 지시를 따른다
title: What a role actually does belongs to the harness, so session roles are set by instruction files and the dispatch model follows the user's instruction
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-strawberry-harness}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/04ec773f-bf28-4ae8-a8d6-5fc4012dff58
---
**근거** — 노트 11.2절은 카탈로그가 역할과 권한 요구까지만 규정한다고 적는다. 각 역할이 실제로 무엇을 하는지(프롬프트·절차)는 하네스의 몫이다. 지침 파일과 부팅 스크립트가 그 몫의 자리다. 2026-10-03 유저 지시로 하네스를 strawberry 프로젝트의 하네스를 참고해 정돈하면서 두 세션 역할에 지침 파일과 부팅 스크립트가 섰다(`p11-harness-two-channels`). 같은 날 hci의 서브에이전트 정의 파일이 삭제됐다. 카탈로그는 hci의 실행 모드를 세션 유지(`agt:sessionPersistent`)로 둔다.

orchestrator가 기본 세션인 것은 저장소 초기 구축(2026-09-01)의 역할 표부터다. 그 표는 orchestrator를 "메인"으로 적었다.

dispatch 모델은 유저 지시다. 2026-09-26에 처음 지시됐고 2026-10-03 하네스 정돈 중에 다시 지시됐다. 작업 종류에 따른 opus와 sonnet의 배분은 orchestrator 지침 원칙 5가 적는다.

브리핑을 작업 집합으로 한정하는 까닭은 요구 r-015다. 무엇을 보게 할지가 곧 무엇을 판단하게 할지다. 노트 11.3절은 dispatch의 깨끗한 컨텍스트가 누적 지식을 잃는 문제를 작업 집합 전달로 대응한다.

미확정: 유저가 dispatch 모델을 opus와 sonnet으로 정한 이유는 기록에서 확인하지 못했다. 2026-09-26 지시의 원문 위치도 확인하지 못했다. 스크립트 없는 세션을 orchestrator로 둔 판단이 2026-10-03 정돈에서 다시 검토됐는지도 확인하지 못했다.
