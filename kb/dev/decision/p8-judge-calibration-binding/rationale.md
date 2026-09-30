---
id: https://agentic-knowledge-base.dev/id/chunk/07a8e14d-7b0a-4fca-904c-835f31e37185
type: decision
level: logical
title_ko: 게이트 밖에 두면 밀폐성과 자동화를 함께 지키고 집단 캘리브레이션은 개별 보증이 아니다
title: Outside the gates keeps hermeticity and automation; population calibration is not a per-answer guarantee
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-29T01:20:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0524cc2d-1d9f-4d40-8a7a-502e6af0e4c5
---
**근거** — 판정자를 게이트 안에 넣으면 네트워크·자격·모델 버전이 `bazel test`의 입력이 되어 같은 리비전이 다른 판정을 낸다. 게이트 밖에 두고 로그만 검사하면 게이트는 밀폐된 채로 남고 판정은 자동으로 돈다. 두 성질을 동시에 지키는 배치는 이것뿐이다.

①의 근거는 모델 문서의 문장이다 — "캘리브레이션은 예측 집단에 걸쳐 측정되며 개별 답의 정확성을 보장하지 않는다." 옛 결정은 임계 셋으로 처리를 갈랐으나 임계의 뜻을 적지 않았다. 뜻이 없으면 0.9 위의 답을 자동 적용하는 것이 무엇을 받아들이는 일인지 말할 수 없다.

②의 근거는 산술이다. 구간이 셋인데 표본이 20이면 구간당 7건 안팎이라 정확도가 한 건에 15%씩 흔들린다. 라벨 대표성 실험(2026-09-11)이 60건이었고 캘리브레이션에서 "오답 0이라 판정 불가"로 끝났다 — 그 실험이 기준선이고, 구간당 표본이 그 공백을 메운다.

③은 모델의 상한이다. "같은 주장을 담은 블록은?"을 청크 780 후보로 물으면 넘는다. 옛 규약 "라벨 유사 상위 k개"가 실질적으로 지켰으나 규칙으로 적혀 있지 않았다.

④의 근거는 모델이 텍스트를 만들지 못한다는 명시된 한계다. 주석 형식(`p7-commentary-form`)의 `본문:` 슬롯이 문장 ≤4를 요구하므로 작성 주체가 비면 슬롯이 채워지지 않는다.

⑤는 옛 결정의 문장에 근거를 더한 것이다 — 보상 기반 캘리브레이션은 모델별로 학습되므로 모델이 바뀌면 같은 0.9가 다른 정확도를 뜻한다.
