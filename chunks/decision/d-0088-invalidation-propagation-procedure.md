---
id: https://agentic-knowledge-base.dev/id/chunk-d0088
type: decision
level: concrete
title_ko: 무효화 전파의 여덟 단계 절차
title: The eight-step invalidation propagation procedure
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — "가정이 깨지면 자동으로 무효화 표시된다"(6.5절)를 다음 절차로
실행한다.

```
1. 가정 A가 거짓으로 판정됨
2. A를 assumes 하는 청크 집합 C₁을 질의
3. C₁의 각 청크를 invalidated로 표시
4. C₁을 부분으로 갖는 구성체를 suspect로 표시
5. C₁을 끝으로 하는 링크를 suspect로 표시
6. 단방향 규칙에 따라 하위 plane으로 반복. 상위로는 가지 않음
7. 영향 범위(청크 수, plane 분포)를 유저 채널로 통지
8. 무효화 이력을 관측 청크로 기록 — 상승의 입력
```

**근거** (노트 6.10절)
- **6단계의 정지 조건이 중요하다.** 단방향 규칙(5.2절)이 없으면 전파가
  순환한다 — 하위 plane이 상위를 무효화하고 그것이 다시 하위로 내려온다.
  전파가 유계인 것은 plane 순서 덕분이지 절차 덕분이 아니다.
- 청크(3단계)·구성체(4단계)·링크(5단계)가 각각 다른 상태를 받는다.
  구성체와 링크는 `invalidated`가 아니라 `suspect`다 — 부분이 깨졌다고
  전체가 거짓인 것은 아니고 재검토 대상일 뿐이기 때문이다.
- 7단계가 절차의 일부인 이유는 무효화가 조용히 일어나면 유저가 깨진 지식
  위에서 계속 작업하기 때문이다.
