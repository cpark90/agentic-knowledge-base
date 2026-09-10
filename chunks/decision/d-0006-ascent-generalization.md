---
id: https://agentic-knowledge-base.dev/id/chunk-d0006
type: decision
level: concrete
title_ko: 상승 — 관측을 어휘로 일반화
title: Ascent - generalizing observation into vocabulary
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 하강만 있는 체계는 지식이 축적되지 않는다. 관측에서 어휘로
올라가는 상승 전이를 체계의 동작으로 둔다.

| 전이 | 동작 | 산출 |
|---|---|---|
| executable → concrete | 관측 기록 | run-kg의 agt:Run |
| concrete → logical | 반복 패턴에서 도메인 추출 | -space 도메인 갱신 |
| logical → abstract | 도메인을 관통하는 변수 식별 | -space 변수 선언 갱신 |
| abstract → functional | 변수를 설명하는 개념 식별 | **온톨로지 갱신** |

**근거** (노트 6.3절) — 마지막 전이가 특별하다. 상승이 온톨로지까지 닿으면
어휘 자체가 자라고, 다음 프로젝트는 자란 어휘로 시작한다. 이것이 재사용
가치의 실체다. 메모리 승격(9.4절)은 상승의 최소 단위다.

**대안** — 상승 자동화는 기각(`[안]`). 후보를 제시하고 확인을 받으며,
온톨로지 갱신은 위생 검사(2.5절)를 통과해야 한다. 상승 트리거는 미해결.
