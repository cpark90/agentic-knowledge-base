---
iri: https://agentic-knowledge-base.dev/id/chunk-d0126
plane: decision
level: concrete
label_ko: 실행 모드와 dispatch 재진입 요약
label_en: Execution mode and dispatch re-entry summary
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 실행 모드(세션 유지 / dispatch)를 입력으로 받고, dispatch
대상에게는 전체 컨텍스트가 아니라 **그 역할의 스코프로 거른 situation**
(0.5절)만 전달한다.

**근거** (노트 9.3절)
- **세션 유지**는 누적 지식을 보존하지만 컨텍스트 로트·오염이 누적된다 →
  `memory` plane 승격 규칙으로 주기적으로 비운다 (9.4절).
- **dispatch**는 깨끗한 컨텍스트를 얻지만 누적 지식이 소실된다 → 재진입
  요약이 필요하고, 그 요약은 온톨로지 어휘로 쓴 situation이다.
- 스코프가 이미 무엇을 볼지 정해 두었으므로 **요약의 범위를 따로 정할 필요가
  없다.** 재진입 요약을 매번 사람이 재단하면 그 재단이 인지 요인 결함의
  원인이 된다.
- 실행 모드가 바뀌면 하네스가 재구성되고 재진입 요약의 필요 여부가 바뀐다
  (9.1절 파급).
