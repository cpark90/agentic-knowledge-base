---
id: https://agentic-knowledge-base.dev/id/chunk/f28a27f4-a539-4913-b1cd-fc8fc346eff3
type: decision
level: concrete
title_ko: 링크 가능성을 제약 만족 문제로 사상한다
title: Map link possibility onto a constraint satisfaction problem
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0098]
part_of: https://agentic-knowledge-base.dev/id/composite/aa7d5c28-822d-4904-9e3f-13920eb41256
composite: {id: https://agentic-knowledge-base.dev/id/composite/aa7d5c28-822d-4904-9e3f-13920eb41256, title_ko: 링크 가능성을 제약 만족 문제로 사상한다, title: Map link possibility onto a constraint satisfaction problem}
---
**결론** — 링크의 가능성을 **제약 만족 문제(CSP)** 로 다룬다. 변수와 도메인이 값이 아니라 **링크**로 정의된다.

- **변수** — 링크가 필요한 지식 항목 (출발점)
- **도메인** — 그 항목에서 갈 수 있는 **후보 링크의 도착점 집합**
- **제약** — 링크 간 **양립 조건.** "A→X가 성립하면 B→Y는 불가"
- **제약 전파** — 한 링크의 확정이 다른 항목의 후보 집합을 줄이는 과정
- **해** — 모든 변수의 링크가 하나씩 확정된 상태

이 사상 위에서 확정은 제약 전파의 결과로만 일어난다.
