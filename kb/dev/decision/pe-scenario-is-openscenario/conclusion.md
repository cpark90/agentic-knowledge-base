---
id: https://agentic-knowledge-base.dev/id/chunk/1adeb68f-a1ed-4eb3-bb03-6aaaa27cbc6e
type: decision
level: concrete
title_ko: 시나리오는 OpenSCENARIO 코어 구조에 프로파일의 도메인 모델을 얹고 기준은 별도 청크다
title: Scenarios use the OpenSCENARIO core structure with a profile-defined domain model; criteria are separate chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
composite: {id: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea, title_ko: 시나리오 = OpenSCENARIO DSL 구조, title: Scenario = OpenSCENARIO DSL structure}
part_of: https://agentic-knowledge-base.dev/id/composite/7fcedb3d-e6cb-4df2-81fc-0787c3934fea
---
**결론** — 시나리오 = OpenSCENARIO DSL 구조 + 자체 도메인 모델 (노트 부록 E.5). 코어 언어의 `scenario`·parameter·actor·`do serial/parallel`·`keep()`·`cover()`를 쓰고, 도메인 모델(actor·action)은 프로파일이 정의한다 — 에이전트·유저·서비스, 요청·편집·응답. 세 수준이 한 파일. OpenODD 모듈 → `keep()` 내보내기가 "시나리오 변수는 ODD 속성"의 표준 구현. **합격 기준은 시나리오 파일이 아니라 별도 기준 청크.** 도구 성숙도 때문에 시작은 동형 YAML, OSC 텍스트 변환기를 둔다. 이 저장소: 도입 순서 (d), 7단계 (유저 결정 Q6).

외부 조사로 채운 세부 (OpenSCENARIO DSL 2.x 언어 참조, 2026-09-11) — `keep(it in [a..b])`가 속성 제약, `do serial(duration: […]) / parallel`이 시간 구성, actor는 시나리오를 담는 구조체. **`cover(expr, event:, target:)`** 는 커버리지 수집점으로 스칼라 식의 값을 이벤트 시점에 표본화하고 `target`이 목표 관측 횟수다 — 8.23절 `cover()`가 커버리지 분모라는 용법과 일치한다.
