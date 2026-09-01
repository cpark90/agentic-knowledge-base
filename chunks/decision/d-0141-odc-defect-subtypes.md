---
iri: https://agentic-knowledge-base.dev/id/chunk-d0141
plane: decision
level: concrete
label_ko: 요인의 하위 분류 — ODC + 에이전트 고유 유형
label_en: Defect subtypes: ODC plus agent-specific types
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 3갈래 아래에 소프트웨어 결함 분류의 표준인 **직교 결함 분류
(ODC)** 를 배치하고, 인지·상호작용 갈래에는 ODC에 없는 **에이전트 고유
유형**을 더한다.

**근거** (노트 10.1절)
- ODC의 여덟 결함 유형은 "고치려면 무엇을 바꿔야 하는가"로 정의되어 서로
  배타적이다. 지어낸 분류 대신 표준어를 쓰는 원칙(0.0절)과도 맞는다.
- **인지 요인**(전부 고유) — 오독(입력이 있었으나 잘못 읽음), 누락(필요한
  입력이 situation 밖 — 스코프 설계 문제), 낡음(입력이 `suspect`·
  `invalidated`인데 `valid`로 취급), 오인(낯선 것을 아는 것으로 취급,
  1.2절 학습자료 종속).
- **상호작용 요인** — 순서·동기화(ODC timing/serialization), 인터페이스
  (모듈·에이전트 간 계약 불일치, ODC interface), 관계(개체 간 관계 오류 —
  잘못된 링크, 잘못된 part-of, ODC relationship), 채널(통신 규약 위반,
  메시지 오해 — 고유).
- **실행 요인**(전부 ODC) — 기능(function), 배정(초기화·값 배정,
  assignment), 검사(조건·경계 검사 누락, checking), 알고리즘(논리 오류),
  빌드·패키지(구성·병합·배포), 문서(`annotation`·`decision`의 오류).
