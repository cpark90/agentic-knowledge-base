---
iri: https://agentic-knowledge-base.dev/id/chunk-d0145
plane: decision
level: concrete
label_ko: 평가의 세 측정 단위
label_en: Three units of evaluation measurement
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 평가의 측정을 셋으로 둔다. **인지능력**(입력 정보 누락률),
**추적 커버리지**(링크 없는 항목 비율), **가정 건전성**(`invalidated`·
`unverified` 비율). 셋 다 체계가 이미 가진 구조에서 읽어내며, 별도 계측을
붙이지 않는다.

**근거** (노트 10.3절)
- **인지능력** — 입력은 `agt:Situation`이다. scene 대비 누락은 스코프 설계
  문제이고 situation 대비 누락은 에이전트 문제로 갈린다 (0.5절). 측정은
  10.1절 에이전트 검증 3단계(시뮬레이션 프로젝트)에서 기록된 situation을
  재생해 수행한다 — 재현 가능한 단계여야 재생이 성립한다.
- **추적 커버리지** — 8.7절 추적 매트릭스의 빈 칸이 그대로 분자다.
- **가정 건전성** — 6.5절 상태 집계.

**대안**
- metric 선택 자체가 설계 대상이다 (10.3절) — 위 셋은 체계가 이미 산출하는
  값이라는 이유로 고른 초기 집합이며 확정 목록이 아니다.
