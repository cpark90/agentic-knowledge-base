---
id: https://agentic-knowledge-base.dev/id/chunk/1f335a27-9cd0-47d1-9483-b9a787eaf07e
type: decision
level: concrete
title_ko: 판정자는 게이트 밖의 System One 모델이고 확신도는 집단 수준의 캘리브레이션이다
title: The judge is a System One model outside the gates, and confidence is population-level calibration
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}, {resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/11ae001e-2c30-4527-9c01-d19efb779bb1]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-29T01:20:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0524cc2d-1d9f-4d40-8a7a-502e6af0e4c5
composite: {id: https://agentic-knowledge-base.dev/id/composite/0524cc2d-1d9f-4d40-8a7a-502e6af0e4c5, title_ko: 판정자의 결합과 캘리브레이션, title: Binding and calibrating the judge}
---
**결론** — 판정자는 구조화 출력 전용 모델(System One)에 붙이되 **게이트 밖의 도구**다. `bazel test`는 판정을 부르지 않고 판정 로그의 존재와 형식만 검사한다. 질문의 형 셋·원자성·척도를 상황으로 적기·계산과 다단계 추론 배제는 옛 결정 그대로이고, 다음 다섯을 더해 옛 결정을 대체한다(유저 승인 2026-09-29).

| # | 규칙 |
|---|---|
| ① | 확신도는 **집단 수준의 캘리브레이션**이다. 0.9는 "이 답이 90% 맞다"가 아니라 "0.9 구간의 답 무리가 90% 정확하다"이며 개별 답을 보증하지 않는다 |
| ② | 임계별 정확도는 **구간마다 표본으로** 잰다. 20건은 전체의 하한이 아니라 **구간당 하한**이다 — 구간 셋이면 60건이 시작 규모다 |
| ③ | 선택(choice)의 닫힌 집합은 **255 이하**다. 넘으면 독립 점수(score) → 명시 선택의 2단계로 묻는다 |
| ④ | 판정자는 설명을 만들지 못한다. 판정 결과 주석의 `본문:`은 **사람 또는 System 2 에이전트**가 쓰거나 `해당 없음`이다 |
| ⑤ | 판정자 모델 식별자와 캘리브레이션 표본은 **함께 버전이 바뀐다**. 모델이 바뀌면 확률의 뜻이 바뀐다 |

처리 임계 셋(0.9 자동 적용 · 0.5 사람 확인 큐 · 그 아래 보류)은 유지하되 ②의 구간별 측정이 끝나기 전에는 자동 적용 구간이 없다 — 전부 사람 확인 큐다.

판정 로그의 필수 필드는 질문 id · 값 · 확신도 · 모델 식별자 · 입력 지문이다. 외부 서비스 도달·자격·모델 버전은 ODD 조건으로 올린다 — 게이트 밖 도구의 전제는 ODD가 판정한다.
