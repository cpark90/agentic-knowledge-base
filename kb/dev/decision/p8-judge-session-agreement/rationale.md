---
id: https://agentic-knowledge-base.dev/id/chunk/487f2dda-e832-44f5-abbd-3b904b678c6f
type: decision
level: logical
title_ko: 자기 보고 확신도는 캘리브레이션이 없으므로 판정의 근거는 독립 판정자의 일치뿐이다
title: Self-reported confidence has no calibration, so the only ground for a verdict is agreement between independent judges
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db
---
**근거** — 세션 판정자의 확신도는 학습된 확률이 아니라 자기 보고다. 0.9라는 값이 "0.9 구간의 답 무리가 90% 맞다"를 뜻하려면 그 구간을 잰 표본이 있어야 하는데, 세션은 같은 입력에 같은 확률을 내지 않으므로 구간 자체가 서지 않는다. 2026-09-11 실험이 캘리브레이션에서 "판정 불가"로 끝난 것이 그 실측이다. 그래서 임계를 확신도에 두면 근거 없는 수치에 자동 적용을 건다.

독립 판정자 둘의 일치는 다르다. 같은 입력·같은 질문에 서로 모르는 두 세션이 같은 값을 내면 그것은 입력이 답을 결정한다는 증거이고, 미끼를 둘 다 잡으면 답이 입력을 읽은 결과라는 증거다. 69/70(2026-09-11)이 그 형태의 유일한 표본이며 일치율 임계의 출발점이다.

기계 환원이 먼저인 까닭은 판정자에게 보낼 것을 줄이는 것이 정확도를 올리는 가장 싼 길이기 때문이다. 요약의 지지 참조·채움 문구는 결정적으로 검사되고, 중복·자리는 후보를 기계가 내면 판정자는 확정만 한다. 남는 둘(근거·라벨 대표성)만이 입력을 읽고 판단해야 하는 질문이다.

외부 서비스를 빼는 까닭은 유저 지시다 — 방법론과 System One은 참고였다. 서비스를 붙이면 네트워크·자격·모델 버전이 운영 조건이 되고 그것을 위해 ODD 조건·가정·도구 갈래가 생겼다. 참고에서 가져올 것은 질문의 형과 값의 기록 방식이고, 그것은 남는다.
