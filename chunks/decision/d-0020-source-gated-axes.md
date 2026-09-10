---
id: https://agentic-knowledge-base.dev/id/chunk-d0020
type: decision
level: concrete
title_ko: 원천이 없는 것은 지어내지 않는다
title: Source-gated axes - never fabricate fixtures
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 실행 거동 축(실행 모드·테스트 시나리오·실패 정책)은 **원천이
뒷받침할 때만 필수**다(source-gated). 원천이 진짜로 그 축을 갖지 않으면
픽스처를 발명하는 대신 **명시적 수용 사유**를 기록하고 그 축을
생략한다 — 이것은 갭이 아니라 정당한 감사 결과다.

**근거** (harness-concrete RECIPE_STANDARD §2)
- 원천에 없던 시나리오나 정책을 지어내는 것은 정직한 과소 반영보다
  나쁘다 — 표현이 원천을 왜곡하기 시작하면 coverage-audit(source→표현
  충실도 감사, d-0015)의 방향 자체가 무의미해진다.
- 실측이 이를 뒷받침한다: 시나리오 축 커버리지가 의도적으로 전수 미만
  이며, 그 결손들은 전부 수용 사유가 기록된 결과다. 100%를 만들려면
  원천에 없던 픽스처를 지어내야 했다.
- 수용 사유의 전형: 구조적 수락(자동 게이트·계약이 출력을 판정)이
  행위적 수락(실행 시나리오)을 대체하는 경우.

**이 저장소와의 관계** — 후보를 좁히는 작업은 자유롭되 근거 없이 하나를
배정하는 것은 금지(노트 Part XIV "충실한 수행 vs 과도한 추측")와 같은
균형점이다. 판정 방법 없는 조건을 ODD에 두지 않는 규칙(0.4절)과도 같은
결의 정직성 원칙이다.
