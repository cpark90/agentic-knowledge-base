---
id: https://agentic-knowledge-base.dev/id/chunk/b3c791cf-87e6-4f92-b1b3-058211f6d5e3
type: decision
level: logical
title_ko: 판정 방식으로 정의하면 plane이 도메인 중립이 되고 프로파일이 실체를 정한다
title: Defining planes by verification keeps them domain-neutral; profiles supply the specifics
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5b5edf6d-f638-4c16-bc32-f4d8e6ed9785
---
**근거** (노트 5.1절)

- plane을 판정 방식으로 정의하므로 **도메인 중립**이다. 도메인
  프로파일(2.11절)이 각 plane의 청크가 구체적으로 무엇인지, 판정 도구가
  무엇인지 정한다.
- 참조 프로파일(소프트웨어 개발) — `requirement`는 요구사항(EARS 권장)과
  이해관계자 승인, `decision`은 ADR과 논증 구조 검사 + 유저 승인, `schema`는
  프로토콜·메시지 스키마와 스키마 검사기, `contract`는 인터페이스 시그니처와
  타입 체커·컴파일러, `artifact`는 함수(42줄 = 함수 하나)와 컴파일·테스트·린터,
  `annotation`은 리뷰 코멘트와 해소 상태, `memory`는 세션 관측.
- 다른 도메인 — 문서 작성이면 `artifact`는 문단, `contract`는 문체·용어 규약,
  판정 도구는 린터와 편집자 승인. 운영이면 `artifact`는 실행된 절차,
  `contract`는 SLA, 판정 도구는 모니터링 지표.
- **청크 열이 곧 그 plane의 원자 단위다.** 각 도메인은 이미 안정적인 식별자를
  갖고 있고 청크 ID는 그것으로 해석된다. 파일 추상은 이를 "경로 + 줄 번호"로
  붕괴시킨다. 청크 ID가 2.6절 시간 정체성의 근거다.
