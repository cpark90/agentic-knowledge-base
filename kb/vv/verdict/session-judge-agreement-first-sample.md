---
id: https://agentic-knowledge-base.dev/id/chunk/9fd4ae9c-85a9-4b4e-91f7-8104bdbe7ce2
type: annotation
level: concrete
title_ko: 세션 판정자 둘의 라벨 대표성 일치는 70건 중 67이고 미끼에 적합을 준 판정자는 없다
title: Two session judges agree on 67 of 70 label representativeness items and neither grades a decoy as fitting
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
generated: {by: vnv/claude-opus-5, at: 2026-09-30T03:30:00+09:00}
---
thought (non-blocking): 일치율 임계의 첫 표본이 섰다 — 서로 모르는 세션 판정자 둘이 같은 입력에 67/70 을 같은 값으로 냈다.

대상: https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0

본문: 2026-09-30 실험은 seed 20260930 으로 층화 표본 60건(요구 10 · 결론 20 · 근거 15 · 대안 15)과 미끼 10건을 뽑아 세션 판정자 둘(`judge-a/claude-sonnet-5` · `judge-b/claude-sonnet-5`)에게 라벨만 보이고 예측을 받은 뒤 본문을 공개해 질문 `agt:labelRepresentsBody` 를 물었다. 값 일치는 전체 67/70 = 95.7% 이고 실표본 58/60 = 96.7% · 미끼 9/10 으로 갈리며, 불일치 셋은 결론 하나(#12)·대안 하나(#62)·미끼 하나(#58)다. 미끼를 척도의 최저 상황(값 0)으로 잡은 비율은 판정자 a 가 9/10 · b 가 8/10 이고 값 2 를 준 미끼는 양쪽 모두 0건이라, 판별력을 "적합에서 갈라내는가"로 재면 10/10 이다. 캘리브레이션은 자기 보고라 판정 불가이고 사람 재판정은 이번 회차에 없다.

해소: 열림 — 표본 둘(2026-09-11 의 69/70 과 이번 67/70)로는 일치율 임계의 수치가 정해지지 않고, 사람 재판정과 정확도 축은 유저 확인에 남는다.
