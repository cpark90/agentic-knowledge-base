---
id: https://agentic-knowledge-base.dev/id/chunk-d0163
type: decision
level: concrete
title_ko: 저작 UI는 SSOT를 우회하지 않는다
title: The authoring UI never forks the source of truth
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 사람용 편집 도구는 상태를 자기 저장소로 fork하지 않는다. 에이전트가
읽고 쓰는 **같은 파일**을 단일 진실 공급원으로 쓰고, 저장은 에이전트가 통과하는
것과 **같은 검증 게이트**를 타며, 편집 폼은 스키마로 구속한다.

**근거** (harness-functional docs/webui-design.md §1·§5·§6)
- 폼의 선택지가 스키마에서 나오면 사람은 새 클래스나 타입 없는 간선을 애초에
  만들 수 없다 — drift를 규칙이 아니라 UI의 구조로 봉한다.
- 저장 파이프라인은 낙관적 쓰기 → 원자 교체 → 검증 → **실패 시 롤백**이다.
  잘못된 상태가 디스크에 남지 않고, 실패 리포트와 diff를 편집 화면에 그대로
  돌려주므로 고치는 자리와 판정하는 자리가 같다.
- 읽기 이후 파일이 바뀌었으면 충돌로 거절한다 — 사람과 에이전트가 같은 파일을
  동시에 쓰는 것이 예외가 아니라 정상 상황이기 때문이다.
- 영속은 파일 전체 재직렬화가 아니라 **그 노드 블록만 치환**한다. 배너·주석·
  서식이 살아남아야 사람이 diff로 리뷰할 수 있고, 그 diff가 곧 협업 기판이다.
  검증은 파싱된 그래프로, 영속은 텍스트로 — 두 축을 분리한다.
- 인증 대신 로컬 신뢰를 전제하고 협업은 버전 관리의 리뷰로 옮긴다. 도구가
  공유 서버가 되는 순간 그 서버가 두 번째 진실 공급원이 된다.

**이 저장소와의 관계** — 편집기의 최소 요구(d-0154)가 "무엇을 저장 시점에
막을 것인가"라면, 이 규칙은 "그 검사가 에이전트의 게이트와 같은 것이어야
한다"를 정한다.
