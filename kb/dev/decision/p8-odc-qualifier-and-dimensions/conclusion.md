---
id: https://agentic-knowledge-base.dev/id/chunk/c52bc5b2-cd33-4676-843e-c0b0986b5237
type: decision
level: concrete
title_ko: 결함에 한정자와 세 차원을 붙이고 분포로 진단한다
title: Tag defects with a qualifier and three dimensions; the distribution is the diagnosis
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0142]
part_of: https://agentic-knowledge-base.dev/id/composite/a70f283f-26aa-465e-9162-51aadc42ec13
composite: {id: https://agentic-knowledge-base.dev/id/composite/a70f283f-26aa-465e-9162-51aadc42ec13, title_ko: 결함의 한정자와 차원, title: Defect qualifier and dimensions}
---
**결론** — ODC의 **한정자(qualifier)** 를 쓴다 — 각 결함은 `missing`(있어야 할 것이 없음) 또는 `incorrect`(있으나 틀림)다. 인지 요인의 "누락"과 실행 요인의 `missing`은 다르다 — 전자는 **입력의 부재**, 후자는 **산출물의 부재**다.

ODC의 다른 차원도 결함 청크의 속성으로 둔다.

- **트리거**(무엇이 드러냈는가) — 검사 게이트 / 테스트 / 리뷰 / 실행 시 / ODD 이탈 대조. 검사 체계의 효과 측정
- **영향**(무엇이 손상됐는가) — 기능 / 성능 / 추적성 / 가정 건전성 / 커버리지. 우선순위 결정
- **발견 단계**(사다리 어느 단계에서) — functional ~ executable. 하강 단절 지점 측정

**유형 분포가 진단이다.** 이 추론 규칙을 `defect-rules`에 둔다.
