---
id: https://agentic-knowledge-base.dev/id/chunk-d0087
type: decision
level: concrete
title_ko: 가정에는 판정 유형과 판정 식을 함께 적는다
title: Each assumption records its verification type and expression
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 가정 청크의 assertion에 **판정 유형과 판정 식을 함께 적는다.**
판정 식이 없는 가정은 `unverified`로만 존재한다 — 기록은 되지만 `valid`에
기여하지 못한다.

| 유형 | 형태 | 예 |
|---|---|---|
| 그래프 질의 | `project-kg`에 특정 개체·관계가 존재하는가 | "`agt:ExternalClient` 개체가 있다" |
| 파일 검사 | 특정 파일·값이 존재하는가 | "lockfile에 FastAPI ≥ 0.110" |
| 실행 검사 | 명령이 특정 결과를 내는가 | "헬스체크 200" |
| 외부 조회 | 외부 시스템 상태 | "device-harvest API가 v2" |
| 사람 확인 | 유저가 참이라고 답함 | "고객이 여전히 이 기능을 원한다" |

**근거** (노트 6.9절)
- "가정이 깨지면 무효 범위가 계산된다"(6.5절)는 **가정을 깨졌다고 판정할
  수단이 있을 때만** 성립한다. 판정 방법을 가정과 함께 저장하지 않으면
  무효화 절차의 1단계가 실행되지 않는다.
- 유형을 다섯으로 나누는 이유는 **비용과 자동화 수준이 다르기** 때문이다.
  그래프 질의는 상시 실행할 수 있지만 사람 확인은 그럴 수 없다.
- 유형은 3.9절 등급과 짝을 이룬다.
