---
id: https://agentic-knowledge-base.dev/id/chunk/d002fe54-d635-4383-a60e-0d168df9b7e9
type: decision
level: concrete
title_ko: 요인 추론과 귀속은 기호 도구 넷의 결과 위에서 하고 언어모델은 도구를 고르고 서술한다
title: Factor inference and attribution run on the results of four symbolic tools; the LM selects and narrates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
composite: {id: https://agentic-knowledge-base.dev/id/composite/9b5d96a6-065b-42d1-8a6b-49b8a56384ff, title_ko: 기호 진단 도구, title: Symbolic diagnosis tools}
part_of: https://agentic-knowledge-base.dev/id/composite/9b5d96a6-065b-42d1-8a6b-49b8a56384ff
---
**결론** — 사후분석 2단계 "요인 추론"과 8.4절 귀속 판단은 언어모델의 서술이 아니라 **기호 도구의 결과** 위에서 한다 (노트 12.12절).

| 도구 | 입력 → 산출 | 이 체계에서 |
|---|---|---|
| 불만족 핵 | 관측 + 기준·가정 집합 → 모순의 최소 부분집합 | 어느 가정·기준이 실제로 충돌하는가 — 무효화 범위의 하한 |
| 보간 | 관측 σ, 명세 φ (σ∧φ 불만족) → 공통 어휘로만 쓴 설명 I | 실패의 설명. 공통 어휘 = 온톨로지 |
| 최약 전제조건 | 전이·구현 + 지켜야 할 성질 → 가장 일반적인 조건 | 좁은 수정 대신 일반 제약. 6.11절 배제 반복의 공리화 |
| 명세 추론 | 실행 기록 → 성립하는 불변식·파라미터 값 | logical 범위 후보. `origin:observed` |

보간의 조건이 통제 어휘(0.0절)와 맞물린다 — 설명 I가 온톨로지 어휘로 안 써지면 두 쪽 어휘가 어긋난 것이고 그 자체가 온톨로지 확장 신호다. 도구 결과는 관측 청크로 기록되고 지침(8.4절)의 근거 절이 이를 참조한다. 언어모델은 도구를 고르고 결과를 서술하며 귀속을 제안한다 — 결과를 대신 만들지 않는다. 이 저장소: `diagnose` 도구(미구현, 도입 7단계).
