---
id: https://agentic-knowledge-base.dev/id/chunk-d0084
type: decision
level: concrete
title_ko: 모든 plane이 다섯 level을 갖는다 — plane × level 격자
title: Every plane has all five levels - the plane x level grid
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 사다리는 `decision`만의 장치가 아니라 일반 메커니즘이므로
**모든 plane이 다섯 단계를 갖는다.** plane과 level은 서로 직교하는 두 축이고
청크는 그 격자의 한 칸에 놓인다.

**근거** (노트 6.4절)
- 각 plane에서 다섯 단계가 답하는 질문은 같은 모양이다. `schema`면
  "어떤 데이터가 오가는가 → 메시지·필드 변수 → 스키마 후보 + 호환 제약 →
  확정 스키마 개체 → 직렬화 코드", `artifact`면 "이 모듈이 하는 일 → 구조
  변수 → 알고리즘·구조 선택지 → 확정 구조 개체 → 코드"다.
- `memory`만 예외다 — 관측은 `concrete`의 실행 기록 단편으로만 존재하고
  추상 단계를 갖지 않는다.
- **`contract`와 `artifact`의 logical이 이 격자의 시험대다.** 현재 관행에서
  이 칸은 비어 있다 — 시그니처와 구현은 후보 공간을 남기지 않고 곧바로
  확정된다. 그 칸을 채울 수 있는지가 사다리가 일반 메커니즘이라는 주장의
  검증이다.

**대안 (미확정)** — `contract`·`artifact`의 logical이 `decision`의 logical을
투영한 것에 불과한지, 독립적 내용을 갖는지는 미해결이다. `requirement`
plane을 두면 functional 단계가 `decision`에서 옮겨가므로 격자 재검토 대상.
