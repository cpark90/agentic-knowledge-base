---
id: https://agentic-knowledge-base.dev/id/chunk/11ae001e-2c30-4527-9c01-d19efb779bb1
type: decision
level: concrete
title_ko: 판정자의 질문은 예아니오·선택·척도 셋뿐이고 확신도 임계가 처리를 가른다
title: A judge asks only yes/no, choice, or scale, and the confidence threshold routes the result
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a5873a98-652e-4341-b229-b3ef6a05e702
composite: {id: https://agentic-knowledge-base.dev/id/composite/a5873a98-652e-4341-b229-b3ef6a05e702, title_ko: 판정자 질문의 형식, title: The form of a judge question}
---
**결론** — 판정자는 고정된 입력에 대해 원자 질문에 값과 확신도로 답한다. 자유 서술을 하지 않는다.

- **질문의 형**은 셋뿐이다. 예/아니오, 닫힌 집합에서의 선택, 척도다. 자유 서술 리뷰는 판정이 아니다.
- **원자성** — 질문 하나가 판단 하나다. 복합 질문은 나눠 같은 입력에 병렬로 묻는다.
- **척도의 단계**는 정도가 아니라 상황으로 적는다. "입력에 같은 문장이 있다"가 "매우 그렇다"보다 판정 가능하다.
- **출력**은 값과 확신도다. 기록 자리는 `annotation` plane이다.
- **확신도 임계** 셋이 처리를 가른다.

| 확신도 | 처리 |
|---|---|
| 0.9 이상 | 자동 적용 |
| 0.5 이상 0.9 미만 | 사람 확인 큐 |
| 0.5 미만 | 판정 보류, 사람에게 |

- **도입 절차** — 자동화 전에 판정 로그를 남기고 20건 이상을 사람이 라벨링해 임계별 정확도를 잰다. 게이트 차단은 그 뒤다. 라벨 대표성 실험(2026-09-11, 층화 60·미끼 10)이 이 절차를 이미 썼다.
- **한계** — 계산·날짜·다단계 추론을 판정자에게 맡기지 않는다. 그 검사는 lint와 분석 시점의 것이다.

질문·척도·임계는 프로파일 shape에 저장하고 판정자 모델 식별자와 함께 버전을 맞춘다.
