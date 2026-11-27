---
id: https://agentic-knowledge-base.dev/id/chunk/8eb6cdbb-1b7f-4741-94dc-2c50c799253c
type: contract
level: logical
title_ko: 계산 규칙은 사람 정답 라벨 표본에서 기저율보다 낮은 Brier와 구간별 이항 신뢰구간 안의 빈도를 내고 일관성 게이트를 통과한다
title: A belief rule beats the base-rate Brier score on the human-labelled sample, keeps each bin within its binomial interval, and passes the consistency gate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5-5, at: 2026-11-27T15:33:25+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-11-27T11:49:43+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-27T12:32:26+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-27T14:10:40+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-27T15:38:18+09:00}]
---
**합격 기준** — 기준 종류는 **보정**이다. 표본 `S`의 항목 `i`에 계산 규칙 `R`이 낸 값을 `p_i`, 사람 정답 라벨을 `y_i ∈ {0, 1}`이라 한다. 아래 세 술어가 모두 참인 `R`만 합격이다.

**판정 술어**

- 표본. `S`는 질문지 Q-0047의 사람 정답 라벨 20건이고, 독립 사람 라벨(L01~L04)과 hci 권장 뒤 사람 확인 라벨(L05~L20)을 모두 넣는다(Q-0078의 Q178-b). `|S| ≥ 20`이고, `|S| < 20`이면 판정하지 않는다.
- 표본의 원본. 라벨과 지위의 원본은 관측 기록 `https://agentic-knowledge-base.dev/id/chunk/bbc63eed-be6f-4316-b0cb-5f1a46dadc5c`다.
- 독립 라벨의 병기. 측정 보고는 독립 사람 라벨 4건만으로 계산한 술어 1·2의 값을 함께 내고, 합격 판정은 `S` 전체의 값으로 한다.
- 술어 1(Brier). `B(R) = (1/|S|) Σ (p_i − y_i)²`이고 `ȳ = (1/|S|) Σ y_i`일 때 `B(R) < (1/|S|) Σ (ȳ − y_i)²`이다. 같으면 불합격이다.
- 술어 2(신뢰도). `|S| < 50`이면 구간은 `[0, 1/3)` · `[1/3, 2/3)` · `[2/3, 1]` 셋이다. 표본이 있는 구간 `k`마다 관측 빈도 `ō_k`가 그 구간 평균 예측값 `p̄_k`를 성공 확률로 하고 표본 수 `n_k`로 계산한 95% 이항 신뢰구간 안에 든다. 한 구간이라도 벗어나면 불합격이다.
- 술어 3(일관성). 게이트 `belief-consistency`가 둘을 판정하고 그 PASS가 술어 3이다. 상태 전이 규칙은 믿음 정도를 입력으로 읽지 않는다. 닫힌 계산 규칙이 없는 동안 병기 값은 선호의 동률 깨기에 쓰이지 않는다.
- 선택. 둘 이상의 규칙이 합격하면 `B(R)`가 가장 낮은 규칙이 고른 것이다.

**등급** — 합격한 규칙이 없다. 2026-11-27의 두 번째 측정(S3, 결과 기록 `https://agentic-knowledge-base.dev/id/chunk/ec0e87d8-4b32-4c1c-b01f-2001c801c0e4`)에서 A `kind-rank`와 B `beta-binomial`은 값이 있는 항목이 0건이라 표본 부족으로 판정하지 않았다. 결정 `p9-belief-by-calibrated-judge`가 정한 C `judge-mean`의 값은 보정한 값이고, 보정한 C(Platt, 하나씩 빼는 교차 검증)는 표본 20건에서 B(R) 0.186이 기저율 Brier 0.160보다 낮지 않아 술어 1이 거짓이고, 구간 [0, 1/3)의 관측 빈도 1/1이 허용 성공 수 0~0 밖이라 술어 2도 거짓이므로 불합격이다. 보정 전 C는 B(R) 0.166으로 참고로만 내고 판정에 쓰지 않는다. 술어 3의 게이트 `belief-consistency`는 저장소에 있고 술어 1·2는 `tools/belief_calibration.py`가 계산하며 생성물은 `//kg:belief_calibration`이다.

이 기준이 정제하는 검증 목표는 `https://agentic-knowledge-base.dev/id/chunk/209cb1b9-5182-4db1-886e-0e61dbd552df`다. 그 목표가 draft인 동안 `refines` 링크를 두지 않는다(`p4-chunk-state-machine`).

미확정: 다음 측정은 표본이 늘기를 기다린다. A·B는 표본 링크에 믿음 정도 값이 생겨야 판정할 수 있고, C는 라벨 0이 늘어야 하나씩 빼는 맞춤의 판별력과 첫 구간의 쏠림이 다시 재어진다. 보정은 사람 라벨 표본이 20건 이상이면 적용한다. 합격 규칙은 아직 없다.
