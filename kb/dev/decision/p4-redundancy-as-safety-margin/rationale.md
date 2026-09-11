---
id: https://agentic-knowledge-base.dev/id/chunk/d7b890a0-6d3d-4b8d-b19b-4cc1597283e0
type: decision
level: logical
title_ko: 자립성은 반복을 낳고, 반복의 비용은 예산이며, 드리프트는 링크 부재로 드러난다
title: Self-containment breeds repetition; its cost is budget; drift shows as a missing link
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-label-representativeness-protocol}]
generated: {by: claude/fable-5, at: 2026-09-11T03:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/6053b67e-afec-4a59-b710-31b6ab85b108
---
**근거** — 청크는 자립적이어야 한다(4.4절). 자립성은 곧 맥락의 반복을 요구한다 —
근거 청크가 결론의 맥락을 되풀이하지 않으면 홀로 읽히지 않는다. 그래서 본문 중복은
결함이 아니라 자립성의 **결과**이며, 에이전트가 좁게 보는 상황(1.1절)에서는 필요한
정보가 한 번 더 있는 것이 빠져 있는 것보다 안전하다 — 유저가 이를 안전율이라 불렀다.

병합 신호(`p4-chunk-split-and-merge`)는 "항상 함께 읽힘·자립성 위반"이지 "내용이
겹침"이 아니다. 즉 내용 중복을 금지한 결정은 없었고, 이 결정은 기존 결정을 뒤집지
않고 **경계표만 새로 긋는다**.

경계가 T-Box·요구·라벨 앞에서 멈추는 이유: 개념의 중복은 어휘 드리프트(0.0절)이고,
요구의 중복은 전방·후방 추적 커버리지의 분모를 가르며, 라벨의 중복은 인터페이스
충돌이다 — 셋은 안전율이 아니라 구조 훼손이다.

용인의 비용은 컨텍스트 예산(1.4절)이다. 중복이 같은 작업 집합 안에 있으면 같이
펼쳐져 예산을 두 번 먹는다 — 그래서 "어디서 겹치는가"가 용인 여부를 가른다.

`coUpdatesWith`를 조건으로 두는 이유: 이 링크가 있어야 한쪽의 변경이 다른 쪽을
`suspect`로 만들어 두 서술이 어긋나는 순간이 **기계적으로 드러난다**. 링크가 없는
중복은 어긋나도 아무도 모른다 — 그것이 드리프트의 정의다.
