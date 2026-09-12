---
id: https://agentic-knowledge-base.dev/id/chunk-d0177
type: decision
level: concrete
title_ko: 설정 어휘는 닫힌 집합이고 미인식 값은 기본값으로 떨어지지 않고 실패한다
title: Configuration vocabulary is a closed set; unknown values fail instead of defaulting
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 선택 정책처럼 거동을 바꾸는 설정 어휘는 **닫힌 집합**으로
정의하고, 집합 밖의 값은 조용히 기본값으로 떨어뜨리지 않고 **즉시
실패**시킨다. 실패는 대상·잘못된 값·허용 집합을 함께 말한다. 조건에 맞는
후보가 하나도 없는 고정(pin)도 같은 실패다.

**근거** (harness-concrete docs/odr-bind-lock.md §"The policy set is CLOSED")
- 조용한 대체는 **"고정했다고 믿는 명세"** 를 만든다. 오타 하나가 지정한
  전략 대신 기본 전략을 실행시키고, 산출물은 정상으로 보인다. 명세와
  실제 거동의 차이가 어느 게이트에도 걸리지 않고 자란다.
- 실패 시점은 **산출 이전**이다. 설정 해석 단계에서 거부하면 파일이 하나도
  쓰이지 않고, 잘못된 설정이 반쪽 산출을 남기지 않는다.
- 체계가 답을 모르는 상황에서 그럴듯한 답을 지어내지 않는다는 점에서,
  모순을 자동으로 풀지 않고 사람에게 넘기는 규칙(d-0103)과 같은 결이다.

**대안**
- 열린 어휘 + 미인식 값 무시 — 기각. 확장성을 얻는 대신 오설정과 미지원
  전략을 구별할 수 없게 되고, 둘 다 기본값으로 수렴한다.
