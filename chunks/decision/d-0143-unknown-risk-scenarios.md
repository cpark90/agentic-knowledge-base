---
id: https://agentic-knowledge-base.dev/id/chunk-d0143
type: decision
level: concrete
title_ko: 알려지지 않은 위험 시나리오의 두 원인
title: Two sources of unknown risk scenarios
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 알려지지 않은 위험 시나리오는 둘 중 하나에서 온다. **알려지지
않은 요인**(`defect` 어휘에 없는 요인)과 **알려진 요인의 알려지지 않은
조합**(조합이 시나리오 도메인에 없음). 대응이 다르므로 구분한다.

**근거** (노트 10.1절)
- 첫째는 **어휘 문제**다 → 6.3절 상승으로 실행 기록에서 새 요인을 추출해
  `defect` 어휘에 추가한다.
- 둘째는 **커버리지 문제**다 → 조합 테스팅으로 시나리오 도메인을 체계적으로
  탐색한다.
- 구분이 실용적인 이유 — 어휘를 늘려야 할 때 조합만 늘리면 같은 사각지대가
  남고, 조합을 늘려야 할 때 어휘를 늘리면 분류만 비대해진다.
- 인시던트 사후분석(10.12절)이 이 구분을 그대로 절차로 쓴다 — 요인이
  어휘에 없으면 어휘 확장 후보, 있으나 조합이 없으면 새 시나리오 후보.
