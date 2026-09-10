---
id: https://agentic-knowledge-base.dev/id/chunk-d0130
type: decision
level: concrete
title_ko: 테스트·검증은 체계의 응용이다
title: Testing and verification are an application of the system
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 테스트·검증은 체계의 구성요소가 아니라 **응용**이다. 체계는
시험 대상·경계·결과 축적·실패 분류의 단위를 제공하고, 시험 절차 자체는
규정하지 않는다.

**근거** (노트 10.1절) — 검증이 필요로 하는 것과 체계가 주는 것의 대응.
- **무엇을 시험할지** → `agt:Scenario`의 concrete 개체. `verifies` 링크로
  대상과 연결된다.
- **시험 대상의 경계** → 대상 항목의 `agt:Assumption`과 프로젝트의 ODD.
  경계 밖의 실패는 결함이 아니라 ODD 이탈이다 (3.5절).
- **결과의 축적** → `agt:Run`. 실행 기록이 6.3절 상승의 입력이 된다.
- **실패 분류** → `defect` 어휘 + `defect-rules` 추론.
- 네 단위가 전부 체계에 이미 있으므로, 검증 기능은 별도 저장소를 만들지
  않고 체계의 출력만 소비한다 (Part X 원칙).
