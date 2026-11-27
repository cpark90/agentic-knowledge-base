---
id: https://agentic-knowledge-base.dev/id/chunk/1adeb68f-a1ed-4eb3-bb03-6aaaa27cbc6e
type: decision
level: concrete
title_ko: 시나리오는 OpenSCENARIO 코어 구조에 프로파일의 도메인 모델을 얹고 기준은 별도 단위 지식이다
former_title_ko: ["시나리오는 OpenSCENARIO 코어 구조에 프로파일의 도메인 모델을 얹고 기준은 별도 청크다", "시나리오는 OpenSCENARIO 코어 구조에 프로파일의 도메인 모델을 얹고 기준은 별도 지식 항목이다"]
title: Scenarios use the OpenSCENARIO core structure with a profile-defined domain model; criteria are separate chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-01T04:38:26+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
composite: {id: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea, title_ko: 시나리오 = OpenSCENARIO DSL 구조, title: Scenario = OpenSCENARIO DSL structure}
part_of: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea
---
**결론** — 시나리오는 OpenSCENARIO DSL 구조에 자체 도메인 모델을 얹는다(노트 부록 E.5). 시나리오의 원본은 DSL `.osc` 파일이고, 그 내용은 언어 핵심과 프로파일의 도메인 모델이다. md 단위 지식은 그 `.osc`에서 추출한 생성물이다. 다만 이 저장소의 현행 시나리오 단위 지식 61개는 추출이 생기기 전의 손 저작으로 남는다. DSL 문법과 이 저장소의 표기가 부딪히면 DSL 문법을 지킨다(Q173-a).

코어 언어에서 쓰는 것은 `scenario`, parameter, actor, `do serial`/`do parallel`, `keep()`, `cover()`다. `keep(it in [a..b])`는 속성 제약이고, OpenODD 모듈을 `keep()`으로 내보내는 것이 "시나리오 변수는 ODD 속성"의 표준 구현이다. `cover(expr, event:, target:)`는 DSL 표준 뜻으로만 쓴다. 그 뜻은 스칼라 식의 값을 이벤트 시점에 표본화하는 커버리지 수집점이고, `target`은 목표 관측 횟수다. 표본 추출 규칙(등가분할, 경계값 등)은 `cover()`가 아니다. 합격 기준처럼 별도 단위 지식으로 두고, 커버리지 집계는 이 저장소의 자체 집계기가 한다. 지금 `tools/case_gen.py`가 읽는 펜스의 `cover` 키는 표본 추출 규칙 목록이며, 이 이름은 도구를 고칠 때 함께 바꾼다.

수준 배치는 수준마다 파일 하나다. 하위 수준 파일은 상위 수준 파일을 `import`해 구조체와 도메인 모델을 공유하고, 매개변수를 다시 선언해 `keep()`을 단다. 수준 사이의 정제는 단위 지식의 `refines`다. 도메인 모델(actor와 action)의 원본은 `.osc` 라이브러리와 Python 액션이고, 이 저장소의 대상은 에이전트·유저·서비스와 요청·편집·응답이다. **합격 기준은 시나리오 파일에 두지 않고 별도 기준으로 둔다.**

`.osc` 추출 모양과 OSC 파서 의존, `case_gen`의 `.osc` 읽기는 다음 프로젝트의 실물이 나온 뒤 따로 정한다(Q173-a). 그 전까지 이 저장소는 `.osc` 파일을 두지 않는다.
