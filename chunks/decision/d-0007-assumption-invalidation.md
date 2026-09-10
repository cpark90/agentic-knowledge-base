---
id: https://agentic-knowledge-base.dev/id/chunk-d0007
type: decision
level: concrete
title_ko: 가정 위반이 무효화의 트리거
title: Assumption violation triggers invalidation
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 각 지식 항목은 참이라고 전제한 조건(agt:Assumption) 위에 서
있고, 가정이 깨지면 그 가정에 의존하는 모든 항목이 자동으로 무효화
표시된다. 전수조사가 필요 없다 — 어떤 가정이 깨졌는지만 판정하면 무효
범위가 계산된다.

**근거** (노트 6.5절)
- 가정은 ODD 속성 위의 명제이므로 판정이 질의 하나로 환원된다. 판정
  불가능한 가정도 기록하되 unverified로 둔다.
- 무효화는 plane 단방향 규칙(5.2절)을 따라 전파되므로 파급이 유계다.
- 가정은 청크 단위로 붙는다 — 입도 문제가 청크 분할 문제로 환원된다.

**무효화는 삭제가 아니다.** 무효화 이력은 상승(6.3절)의 입력이다 — 어떤
가정이 자주 깨지는가는 그 자체로 일반화 대상이다.

**상태 기계** — valid(모든 가정 참) / invalidated(하나 이상 거짓, 읽을 때
경고) / unverified(판정 불가, 검사 대상). 설계 시점의 가정과 실행 시점의
실제 조건의 차이 감지가 전이 트리거다 (0.4절).
