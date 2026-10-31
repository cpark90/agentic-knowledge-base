---
id: https://agentic-knowledge-base.dev/id/chunk/da2b13ef-9082-4917-bf7f-827578fc334f
type: decision
level: concrete
title_ko: 스키마가 폼을 구속하고 같은 게이트와 롤백이 잘못된 상태를 남기지 않는다
title: Schema-bound forms, the same gate and rollback leave no invalid state behind
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0163-authoring-ui-shares-the-gate.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:48:42+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:48:42+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/4f30d4af-1a70-4db1-9bf3-1b2fe3bd8b5b
---
**근거** — 출처는 harness-functional `docs/webui-design.md`의 §1과 §5, §6이다.

- 폼의 선택지가 스키마에서 나오면 사람은 새 클래스나 타입 없는 간선을 애초에 만들 수 없다. 그래서 drift를 규칙이 아니라 UI의 구조로 봉한다.
- 저장 파이프라인은 낙관적 쓰기와 원자 교체, 검증, **실패 시 롤백**의 차례로 흐른다. 잘못된 상태가 디스크에 남지 않고 실패 보고와 diff를 편집 화면에 그대로 돌려주므로, 고치는 자리와 판정하는 자리가 같다.
- 읽은 뒤 파일이 바뀌었으면 충돌로 거절한다. 사람과 에이전트가 같은 파일을 동시에 쓰는 것이 예외가 아니라 정상 상황이기 때문이다.
- 영속은 파일 전체의 재직렬화가 아니라 **그 노드 블록만 치환**한다. 배너와 주석, 서식이 살아남아야 사람이 diff로 리뷰할 수 있고, 그 diff가 곧 협업의 기판이다. 그래서 검증은 파싱된 그래프로 하고 영속은 텍스트로 하여 두 축을 분리한다.
- 인증 대신 로컬 신뢰를 전제하고 협업은 버전 관리의 리뷰로 옮긴다. 도구가 공유 서버가 되는 순간 그 서버가 두 번째 진실 공급원이 되기 때문이다.

이 저장소에서 편집기의 최소 요구(`p13-chunk-editor-requirements`)가 무엇을 저장 시점에 막을 것인가를 정한다면, 이 규칙은 그 검사가 에이전트의 게이트와 같은 것이어야 한다는 점을 정한다.
