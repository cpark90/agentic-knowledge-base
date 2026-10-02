---
id: https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7
type: decision
level: concrete
title_ko: 지식 베이스는 에이전트의 컨텍스트에 실리는 세 층의 정돈된 위키이고 모든 것은 한 층의 항목이거나 그 투영이다
title: The knowledge base is a tidy three-layer wiki loaded into an agent's context, and everything is an item of one layer or its projection
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-01T15:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c4b958be-e5e4-43b6-b23f-989f628cb07f
composite: {id: https://agentic-knowledge-base.dev/id/composite/c4b958be-e5e4-43b6-b23f-989f628cb07f, title_ko: 하나의 서비스 — 세 층의 위키, title: One service — the three-layer wiki}
---
**결론** — 이 저장소가 만드는 서비스는 하나다(유저 정의 2026-10-01): **에이전트가 작업을 수행할 때 컨텍스트에 포함되는 구조화된 지식 자체와, 지식과 작업을 연결하는 방법론과, 작업을 수행하는 프로세스를 제공하는 정돈되고 기능화된 위키**다. 저장소의 모든 것은 세 층 중 하나의 **항목**이거나 그 **투영**이다 — 둘 다 아닌 것이 산발의 목록이다.

| 층 | 무엇 | 항목의 실물 |
|---|---|---|
| 지식 | 컨텍스트에 실리는 구조화된 지식 | 요구·결정·조건·가정·관측·V&V 항목 |
| 방법론 | 지식과 작업을 잇는 규칙·절차의 근거 | 규칙 결정, 프로파일, 추적·판정 규약 |
| 프로세스 | 작업을 수행하는 실행 표면 | 도구(코드 청크)·게이트·뷰·skill·절차 |

**층은 plane과 직교한다.** plane은 지식의 종류이자 판정 방식이고 층은 그 항목의 역할이다. 결정 하나가 지식 층(분야의 결정)일 수도 방법론 층(저작 규칙)일 수도 있다. 표시는 청크의 선택 키 `layer: knowledge | methodology | process`이며 기본값은 `knowledge`다 — 코드 청크는 등록부가 `process`를 주고, 게이트·skill·뷰는 프로세스 층의 실행 표면이라 접점은 **작업 집합 하나**다(skill = API·접점 셋은 철회). 규범 문서 넷(AGENTS·STYLEGUIDE·rules·method)은 방법론 층의 **투영**이고 원본은 청크다. 노트는 기획 원본으로 **동결**한다 — 정정은 유저 의도 대 노트의 어긋남이 확인된 자리에만 한다.

처리 방향은 제거가 아니라 **편입**이다. 어느 층에도 배정되지 않는 것은 지우지 않고 층의 형식으로 다시 쓴다.
