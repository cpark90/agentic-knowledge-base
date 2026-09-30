---
id: https://agentic-knowledge-base.dev/id/chunk/379c3aa1-5979-40ab-8d32-d7ccce656d5c
type: decision
level: logical
title_ko: 자유 서술 판정은 재현되지 않고 정확도를 잴 수 없다
title: A free-form verdict is not reproducible and its accuracy cannot be measured
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-30T14:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a5873a98-652e-4341-b229-b3ef6a05e702
---
**근거** — 요구 `verification-means-trust`는 검증 수단 자체의 신뢰도를 재라고 정한다. 자유 서술 판정은 그 측정을 불가능하게 한다. 같은 입력에 같은 답이 나오는지 비교할 값이 없고, 사람 라벨과 대조할 형식도 없기 때문이다. 답의 형을 닫으면 정확도·일치율·캘리브레이션이 전부 계산된다.

확신도 임계를 셋으로 두는 근거는 판정자의 오답 비용이 구간마다 다르다는 것이다. 확신이 높은 구간의 자동 적용은 사람의 시간을 아끼고, 중간 구간은 사람이 확인하며, 낮은 구간은 판정 자체를 보류한다. 임계 없이 자동 적용하면 판정자의 오답이 지식에 그대로 들어간다.

척도의 단계를 상황으로 적는 근거는 판정자와 사람이 같은 뜻으로 읽어야 한다는 것이다. "매우 그렇다"는 판정자마다 다른 지점에서 갈리지만 "입력에 같은 문장이 있다"는 확인할 수 있다. 이것은 ODD 조건의 판정 방법을 "정상이다"가 아니라 "명령 X가 Y를 반환한다"로 적게 한 규칙과 같은 사상이다.

20건 라벨링을 먼저 요구하는 근거는 실측이다. 라벨 대표성 실험(2026-09-11)이 층화 표본 60과 미끼 10으로 판정자 둘의 일치 69/70을 재고 유저가 10건을 재판정했다. 그 절차가 없었다면 라벨 적합 100%라는 수치를 믿을 근거가 없었다.

**참고 출처.** 질문의 형 셋과 확신도를 값으로 남기는 방식은 TypeSafe System One(jev)의 **참고**다 — 서비스 도입이 아니었다(유저 확인 2026-09-30). 2026-09-26의 결합 결정은 참고를 도입으로 읽은 것이며 대체됐다.
