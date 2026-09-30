---
id: https://agentic-knowledge-base.dev/id/chunk/923991f6-9383-4218-bd4f-257b0d11f12c
type: decision
level: logical
title_ko: 판정을 전부 사람에게 두는 안·로컬 모델 확률·형식만 남기고 미루는 안은 기각된다
title: All-human judgement, local-model probabilities, and keeping only the form are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db
---
**대안** — 셋을 기각한다(유저 답 2026-09-30, 선택지 1).

| 대안 | 기각 이유 |
|---|---|
| 판정을 전부 사람에게 둔다 | 요구 `verification-means-trust`(검증 수단의 신뢰도를 잰다)가 측정 대상을 잃는다. 도구·어휘 제거가 크고 남는 둘도 리뷰 규범으로 흩어진다 |
| 로컬 모델의 토큰 확률로 캘리브레이션을 세운다 | 외부 서비스는 아니나 추론 스택이 ODD에 들어온다(의존·하드웨어). 밀폐성·재현성을 다시 설계해야 한다 — 새 무거운 의존이다 |
| 형식만 남기고 판정 주체는 미룬다 | 정리만 남고 3지표가 비어 있다. 일치율 임계와 세션 절차가 지금 설 수 있으므로 미룰 이유가 없다 |

옛 결정(서비스 결합)의 규칙 ①~⑤ 가운데 남는 것은 choice ≤ 255·주석 `본문:`의 작성 주체·질문의 형이고, 집단 캘리브레이션·구간당 표본·모델 버전 결합은 서비스와 함께 빠진다.
