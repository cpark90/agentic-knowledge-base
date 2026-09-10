---
id: https://agentic-knowledge-base.dev/id/chunk/ca6505e8-987f-4890-b38a-07f6ed5f8612
type: decision
level: concrete
title_ko: 세 갈래 아래에 ODC 유형과 에이전트 고유 유형을 배치한다
title: ODC types plus agent-specific types sit under the three factors
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0141]
part_of: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc
composite: {id: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc, title_ko: 요인의 하위 분류, title: Subtypes of the defect factors}
---
**결론** — 3갈래 아래에 소프트웨어 결함 분류의 표준(직교 결함 분류, ODC)을 배치한다. ODC의 여덟 결함 유형은 "고치려면 무엇을 바꿔야 하는가"로 정의되어 서로 배타적이다. 인지·상호작용 갈래에는 ODC에 없는 **에이전트 고유 유형**을 더한다.

- **인지 요인**(전부 고유) — 오독(입력이 있었으나 잘못 읽음) · 누락(필요한 입력이 작업 집합 밖 — 스코프 설계 문제) · 낡음(`suspect`·`invalidated`를 `valid`로 취급) · 오인(낯선 것을 아는 것으로 취급, 1.2절 학습자료 종속)
- **상호작용 요인** — 순서·동기화(ODC timing/serialization) · 인터페이스(모듈·에이전트 간 계약 불일치, ODC interface) · 관계(잘못된 링크·part-of, ODC relationship) · 채널(통신 규약 위반·메시지 오해, 고유)
- **실행 요인**(전부 ODC) — 기능 · 배정(초기화·값 배정) · 검사(조건·경계 검사 누락) · 알고리즘 · 빌드·패키지 · 문서(`annotation`·`decision`의 오류)
