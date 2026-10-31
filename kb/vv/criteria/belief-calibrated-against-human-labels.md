---
id: https://agentic-knowledge-base.dev/id/chunk/8eb6cdbb-1b7f-4741-94dc-2c50c799253c
type: contract
level: logical
title_ko: 계산 규칙은 사람 정답 라벨 표본에서 기저율보다 낮은 Brier와 구간별 이항 신뢰구간 안의 빈도를 내고 일관성 게이트를 통과한다
title: A belief rule beats the base-rate Brier score on the human-labelled sample, keeps each bin within its binomial interval, and passes the consistency gate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5-5, at: 2026-10-25T16:39:00+09:00}
---
**합격 기준** — 기준 종류는 **보정**이다. 표본 `S`의 항목 `i`에 계산 규칙 `R`이 낸 값을 `p_i`, 사람 정답 라벨을 `y_i ∈ {0, 1}`이라 한다. 아래 세 술어가 모두 참인 `R`만 합격이다.

**판정 술어**

- 표본. `S`는 질문지 Q-0047의 사람 정답 라벨이고 `|S| ≥ 20`이다. `|S| < 20`이면 판정하지 않는다.
- 술어 1(Brier). `B(R) = (1/|S|) Σ (p_i − y_i)²`이고 `ȳ = (1/|S|) Σ y_i`일 때 `B(R) < (1/|S|) Σ (ȳ − y_i)²`이다. 같으면 불합격이다.
- 술어 2(신뢰도). `|S| < 50`이면 구간은 `[0, 1/3)` · `[1/3, 2/3)` · `[2/3, 1]` 셋이다. 표본이 있는 구간 `k`마다 관측 빈도 `ō_k`가 그 구간 평균 예측값 `p̄_k`를 성공 확률로 하고 표본 수 `n_k`로 계산한 95% 이항 신뢰구간 안에 든다. 한 구간이라도 벗어나면 불합격이다.
- 술어 3(일관성). 게이트 `belief-consistency`가 둘을 판정하고 그 PASS가 술어 3이다. 상태 전이 규칙은 믿음 정도를 입력으로 읽지 않는다. 닫힌 계산 규칙이 없는 동안 병기 값은 선호의 동률 깨기에 쓰이지 않는다.
- 선택. 둘 이상의 규칙이 합격하면 `B(R)`가 가장 낮은 규칙이 고른 것이다.

**등급** — 판정하지 않는다. 술어 3의 게이트 `belief-consistency`는 저장소에 있지만 사람 라벨 표본(Q-0047)이 아직 없어 술어 1·2를 계산할 수 없으므로 어떤 규칙도 합격하지 않는다.

이 기준이 정제하는 검증 목표는 `https://agentic-knowledge-base.dev/id/chunk/209cb1b9-5182-4db1-886e-0e61dbd552df`다. 그 목표가 draft인 동안 `refines` 링크를 두지 않는다(`p4-chunk-state-machine`).

미확정: 술어 1·2를 계산하는 도구가 없다. 표본은 Q-0047의 답을 기다린다.
