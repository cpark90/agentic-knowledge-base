---
id: https://agentic-knowledge-base.dev/id/chunk/ca6505e8-987f-4890-b38a-07f6ed5f8612
type: decision
level: concrete
title_ko: 세 갈래 아래에 ODC 유형과 에이전트 고유 유형을 배치한다
title: ODC types plus agent-specific types sit under the three factors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0141-odc-defect-subtypes.md, id: https://agentic-knowledge-base.dev/id/chunk-d0141, title_ko: "요인의 하위 분류 — ODC + 에이전트 고유 유형", title: "Defect subtypes: ODC plus agent-specific types"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:43+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0141]
part_of: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc
composite: {id: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc, title_ko: 요인의 하위 분류, title: Subtypes of the defect factors}
---
**결론** — 3갈래 아래에 소프트웨어 결함 분류의 표준(직교 결함 분류, ODC)을 배치한다. ODC의 여덟 결함 유형은 "고치려면 무엇을 바꿔야 하는가"로 정의되어 서로 배타적이다. 인지·상호작용 갈래에는 ODC에 없는 **에이전트 고유 유형**을 더한다.

- **인지 요인**(전부 고유) — 오독(입력이 있었으나 잘못 읽음) · 누락(필요한 입력이 작업 집합 밖 — 적용 범위 설계 문제) · 낡음(`suspect`·`invalidated`를 `valid`로 취급) · 오인(낯선 것을 아는 것으로 취급, 1.2절 학습자료 종속)
- **상호작용 요인** — 순서·동기화(ODC timing/serialization) · 인터페이스(모듈·에이전트 간 계약 불일치, ODC interface) · 관계(잘못된 링크·part-of, ODC relationship) · 채널(통신 규약 위반·메시지 오해, 고유)
- **실행 요인**(전부 ODC) — 기능 · 할당(초기화·값 할당) · 검사(조건·경계 검사 누락) · 알고리즘 · 빌드·패키지 · 문서(`annotation`·`decision`의 오류)

현상 `agt:elementWithoutVocabularyDropped`(P19, 소스 요소가 어휘에 슬롯이 없어 조용히 빠짐)의 관측 수단은 게이트 `element-drop`(`validate`, 실행 계층 verify, 노트 8.21절 G1, 2026-09-29)이고 vnv가 설계했다. 판정은 둘이다. 단위 지식 frontmatter의 최상위 키 가운데 `chunk2kg`가 소비하지 않는 키가 있으면 FAIL이고, 프로파일이 선언한 지식 종류 실체 클래스와 `chunk2kg.PROFILE_SUBSTANCE` 치역의 대칭차가 비지 않으면 FAIL이다. 실체 대칭차는 `--ontology`만으로 돌아 `//kb/ontology:gate_test`와 `//kg:gate_test` 안에 있고, 키 전수 대조는 `//kg:gate_test`가 `chunk_files`(`//kb/dev`·`//kb/vv`·`//space`)로 본문을 넘겨 돈다. 2026-10-01 측정은 옛 chunks 디렉토리를 지우기 전(지시 0192 이전)의 입력으로 했고 키 25 대 30의 차집합과 실체 7 대 7의 대칭차가 모두 공집합이었다. 해소는 developer가 어휘를 넓히는 것이다. 키는 `chunk2kg`가 읽게 하고 `kb_lib.CHUNK_OPTIONAL_KEYS`에 등재하며, 실체 클래스는 프로파일에 선언한다. 요소는 버리지 않는다(가정 `asm-missing-vocabulary-is-signal`).
