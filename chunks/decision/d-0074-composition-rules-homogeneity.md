---
id: https://agentic-knowledge-base.dev/id/chunk-d0074
type: decision
level: concrete
title_ko: 구성 규칙 — 비순환·7±2·동질성·참조 재사용
title: Composition rules - acyclic, 7+-2, homogeneity, reference reuse
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 구성 규칙 넷을 shape으로 쓴다. 비순환은 `part-of`의 반대칭
공리로 추론되고, 직접 부분은 최대 9개(`agt:hasDirectPart` `sh:maxCount 9`),
모든 부분의 plane 클래스와 level이 전체와 같아야 하며(동질성), 참조
재사용은 별도 규칙 없이 그래프의 기본 동작이다.

**근거** (노트 4.5절)
- **동질성이 핵심이다.** `part-of`는 **같은 plane·level 안에서** 청크를
  묶는 유일한 수단이고, plane이나 level을 넘는 모든 관계는 Part VIII의
  링크다. 두 메커니즘이 겹치지 않으므로 어느 쪽을 쓸지 고민할 일이 없다.
- 7±2는 42줄과 **같은 뿌리**다 — 인지 한계. 조망 가능한 크기를 청크에서는
  줄 수로, 구성체에서는 직접 부분 수로 강제한다.
- **참조 재사용이 공짜다.** 모듈형 문서에서 "복사하지 말고 참조하라"는 별도
  원칙이 필요했지만, 그래프에서는 한 개체가 여러 전체의 부분인 것이
  기본이고 오히려 복사가 어렵다. 청크가 바뀌면 그것을 부분으로 갖는 모든
  구성체에 반영되는 것도 저장 구조의 귀결이지 규칙이 아니다.

**구성체의 상태는 부분에서 추론된다** — 부분 청크 하나가 `invalidated`이면
구성체는 `suspect`. `defect-rules`의 규칙 하나로 쓴다.
