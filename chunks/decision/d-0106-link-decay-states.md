---
id: https://agentic-knowledge-base.dev/id/chunk-d0106
type: decision
level: concrete
title_ko: 링크의 붕괴 — 상태 셋과 경계에서의 일괄 재판정
title: Link decay states and batched re-judgement at boundaries
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크는 가정(6.5절)과 같은 상태를 갖는다 — `valid`(양 끝이
마지막 확정 이후 바뀌지 않음) / `suspect`(양 끝 중 하나가 바뀜) /
`invalid`(재검토 결과 관계가 성립하지 않음). **변경 통지가 트리거**이며,
재판정은 즉시 하지 않고 **커밋·세션 종료 같은 경계에서 일괄로** 한다.
재판정은 **규칙부터 시도**하고, 규칙에 없는 변경만 8.4절 판정으로 간다.

**근거** (노트 8.6절)
- **링크는 만드는 것보다 유지하는 것이 어렵다.** 붕괴한 링크는 쓸모없는
  것이 아니라 **해롭다** — 오래된 링크는 시스템의 실제 구조를 오도한다.
- 링크 모델은 양 끝 산출물의 변경을 구독하고, 변경이 오면 `suspect`로
  바꾼다. 편집이 연속되는 동안 매번 판정하면 낭비다.
- "시그니처의 이름만 바뀌고 타입은 그대로" 같은 알려진 변경 패턴은
  규칙으로 자동 갱신한다 (규칙 목록은 8.11절).
- 여기서 6.5절 무효화와 만난다 — 가정 위반은 `assumes` 링크를 통해 항목을
  무효화하고, 산출물 변경은 그 항목의 다른 링크를 `suspect`로 만든다. 두
  메커니즘이 **같은 링크 모델 위에서** 동작한다.
- 전파가 성립하려면 셋이 필요하다 — 링크가 존재할 것, 보정이 plane 경계를
  넘을 것, 전파가 멈출 것(5.2절 단방향 규칙).
