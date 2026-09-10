---
id: https://agentic-knowledge-base.dev/id/chunk-d0021
type: decision
level: concrete
title_ko: 도메인 중립 골격과 도메인 프로파일
title: Domain-neutral skeleton and domain profile
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 체계는 작업의 종류를 가리지 않는다. 대신 **도메인 중립 골격**과
**도메인 프로파일**로 나누고, 작업 종류마다 달라지는 것 — 판정 방식·판정
도구·조건 어휘 — 만 프로파일에 둔다. 설계 노트는 골격을 정의하고 소프트웨어
개발을 참조 프로파일로 쓴다.

**근거** (노트 산출물 정의, 2.11절)
- 대상은 에이전트가 무언가를 읽고 판단하고 만드는 모든 작업이다 —
  소프트웨어 개발, 문서 작성, 운영, 분석. 하나에만 맞춘 골격은 나머지에
  옮길 때 골격 자체를 다시 써야 한다.
- plane이 저장 위치나 파일 형식이 아니라 **판정 방식**으로 정의되기
  때문에(5.1절) 골격이 중립일 수 있다. 각 plane의 실체와 판정 도구는
  프로파일이 채운다.
- 골격에 특정 도메인의 도구 이름이 들어가는 순간 그 이름이 온톨로지 어휘가
  되고, 다른 도메인에서는 해석 불가능한 지어낸 용어가 된다(0.0절).
