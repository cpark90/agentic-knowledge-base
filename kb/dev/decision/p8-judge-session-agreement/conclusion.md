---
id: https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0
type: decision
level: concrete
title_ko: 판정자는 세션이고 임계는 확신도가 아니라 일치율이며 기계 환원이 먼저다
title: The judge is a session, the threshold is agreement rather than confidence, and mechanical reduction comes first
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-jev-system-one}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/1f335a27-9cd0-47d1-9483-b9a787eaf07e]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db
composite: {id: https://agentic-knowledge-base.dev/id/composite/abf9e76a-0b1d-42c4-b70c-f77c7902f8db, title_ko: 세션 판정자와 일치율, title: Session judges and agreement}
---
**결론** — 판정자는 외부 서비스가 아니라 **에이전트 세션**이다(유저 답 2026-09-30). 서비스 결합 결정을 대체한다.

| # | 규칙 |
|---|---|
| ① | **기계 환원이 먼저다.** 요약(핵심마다 지지 블록 참조)·채움은 게이트가 판정하고, 중복·자리는 후보 생성까지 기계가 한다. 판정자에게 남는 것은 **근거**와 **라벨 대표성** 둘이다 |
| ② | 판정자는 새 세션 둘 이상이다. 같은 입력 상태에 같은 질문을 주고 값과 확신도를 `--responses`로 받는다. 확신도는 **자기 보고**라 캘리브레이션을 재지 않는다 — "판정 불가"로 적는다 |
| ③ | **임계는 일치율이다** — 판정자 둘의 값 일치 + 미끼(`label_sample --decoys`) 검출. 단독 응답으로는 자동 적용이 없다 |
| ④ | 자동 적용은 3지표 가운데 **정확도·판별력이 재진 뒤**에만 켠다. 그 전에는 전부 사람 확인 큐다 |
| ⑤ | 질문의 형 셋(noul·choice·score, choice ≤ 255)·원자성·척도를 상황으로·주석 `본문:`은 판정자가 쓰지 않음 — 옛 결정 그대로다 |

판정 로그의 필수 필드는 질문 id · 값 · 확신도 · **판정자 식별자**(세션·모델) · 입력 지문 · 시각이고 열 `일치`가 붙는다. 외부 서비스의 ODD 조건과 가정은 뺀다.

**참고 출처의 자리** — 질문의 형 셋과 "확신도를 값으로 남긴다"는 TypeSafe System One(jev)의 **참고**에서 왔고 서비스 도입은 아니었다. 2026-09-26의 결정·도구·ODD는 참고를 도입으로 읽은 오독이었다 — 이 문장이 다음 세션의 같은 오독을 막는다.
