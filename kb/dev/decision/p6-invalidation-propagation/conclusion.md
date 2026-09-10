---
id: https://agentic-knowledge-base.dev/id/chunk/651e2c44-9a19-4a3e-b04a-ed1226aeef23
type: decision
level: concrete
title_ko: 무효화 전파는 여덟 단계로 실행되고 단방향에서 멈춘다
title: Invalidation propagates in eight steps and stops at the one-way rule
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0088]
part_of: https://agentic-knowledge-base.dev/id/composite/01ce160f-72c9-4898-b0b1-fe6842b799e8
composite: {id: https://agentic-knowledge-base.dev/id/composite/01ce160f-72c9-4898-b0b1-fe6842b799e8, title_ko: 무효화 전파 절차, title: The invalidation propagation procedure}
---
**결론** — 6.5절 "자동으로 무효화 표시"의 절차는 여덟 단계다.

1. 가정 A가 거짓으로 판정됨
2. A를 `assumes` 하는 청크 집합 C₁을 질의
3. C₁의 각 청크를 `invalidated`로 표시
4. C₁을 부분으로 갖는 복합체를 `suspect`로 표시 (4.5절 집계)
5. C₁을 끝으로 하는 링크를 `suspect`로 표시 (9.6절)
6. 단방향 규칙(5.2절)에 따라 하위 plane으로 반복. **상위로는 가지 않음**
7. 영향 범위(청크 수, plane 분포)를 유저 채널로 통지
8. 무효화 이력을 관측 청크로 기록 — 일반화의 입력 (6.3절)
