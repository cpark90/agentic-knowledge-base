---
id: https://agentic-knowledge-base.dev/id/chunk/baddb122-9292-430d-99f9-2388a5a7cc1e
type: decision
level: concrete
title_ko: 규범 문서 규약 — plane은 판정 방식으로 정의되고 코어는 일곱이다
title: Normative-document conventions — Planes are defined by verification mechanism; the skeleton has seven
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5b5edf6d-f638-4c16-bc32-f4d8e6ed9785
---
**규약** — `p5-plane-by-verification`의 결론을 규범 문서에 싣는 문장이다.

규약: `requirement` | 이해관계자 확인 (EARS 형식 + 유저 승인) | 매우 낮음 | 요구사항 문장
규약: `decision` | 논증의 타당성 (논박 가능, 기계 판정 불가 → 유저 승인) | 낮음 | 설계 결정·아키텍처 문서
규약: `schema` | 스키마·호환성 검사 | 낮음 | 데이터 프로토콜·스키마
규약: `contract` | 형식 검사 (결정론적) | 중간 | 인터페이스·타입 시그니처
규약: `artifact` | 실행·실측 | 빠름 | 소스코드
규약: `annotation` | 사회적 합의 (해소/승인) | 매우 높음 | 주석·리뷰 코멘트
규약: `memory` | 없음 (휘발성) | 매우 빠름 | 에이전트 작업 메모리
규약: **plane과 level을 정한다.** plane 할당 기준은 **판정 방식**이고, 저장 위치나 파일 형식이 아니다 ([rules §3](../../../../docs/rules.md#3-plane--판정-방식으로-나뉜-종류)).
