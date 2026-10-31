---
id: https://agentic-knowledge-base.dev/id/chunk/209cb1b9-5182-4db1-886e-0e61dbd552df
type: requirement
level: functional
pattern: ubiquitous
title_ko: 병기되는 믿음 정도는 사람 정답 라벨에 대해 보정되어 있어야 한다
title: A degree of belief written alongside a link or candidate must be calibrated against human-labelled answers
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:09:57+09:00}
---
**검증 목표** — 계산 규칙이 낸 믿음 정도가 확률로 읽혀도 된다는 것이 보여져야 한다. 이 목표가 재는 것은 계산 규칙의 값과 사람이 판정한 참·거짓의 대응이고, 값을 가질 수 있는가는 재지 않는다.

- **이해관계자**: 유저 · 검증자 · **관심사**: 지식 베이스 자체의 확률화

**무엇을 관측하면 성립하는가**

- 사람 정답 라벨 표본의 각 항목에 계산 규칙의 값과 사람의 판정이 나란히 있고, 그 쌍에서 Brier 점수가 계산된다.
- 같은 표본에서 기저율 규칙의 Brier 점수가 함께 계산되어 두 값이 비교된다.
- 예측값 구간마다 관측 빈도와 그 구간의 표본 수가 신뢰도 그림으로 드러난다.
- 상태 전이 규칙이 믿음 정도를 읽지 않는다는 것과, 닫힌 계산 규칙이 없는 동안 병기 값이 동률 깨기에 쓰이지 않는다는 것이 게이트로 판정된다.

판정의 원본은 요구 `r-032-links-and-candidates-carry-degree-of-belief`(`https://agentic-knowledge-base.dev/id/chunk/a0037ff5-559b-4f3b-894d-2bdef12e206c`)와 설계 공간 `space/degree-of-belief-space.md`의 닫기 기준이다. 그 요구가 draft인 동안 `derivesFrom` 링크를 두지 않는다(`p4-chunk-state-machine`).

미확정: 사람 정답 라벨 표본(하한 20)은 질문지 Q-0047의 답을 기다린다. 표본이 서기 전에는 이 목표의 관측이 하나도 계산되지 않는다.
