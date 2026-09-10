---
id: https://agentic-knowledge-base.dev/id/chunk/74a70b7e-ba89-4379-ab74-fdb9cd51844f
type: decision
level: concrete
title_ko: 새 프로젝트는 ODD 작성으로 시작하고 5단계를 거친다
title: A project starts by writing its ODD, in five steps
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0063]
part_of: https://agentic-knowledge-base.dev/id/composite/dc652ea1-791f-4fc8-bdb6-8862023ca380
composite: {id: https://agentic-knowledge-base.dev/id/composite/dc652ea1-791f-4fc8-bdb6-8862023ca380, title_ko: ODD 우선 착수와 작성 절차, title: ODD-first project start and authoring procedure}
---
**결론** — **새 프로젝트는 ODD 작성으로 시작한다.** 온톨로지는 프로젝트 간에 공유되므로 이미 있고, **ODD가 그 프로젝트의 첫 산출물**이다.

빈 ODD로 시작할 수 없다. restrictive 모드에서 빈 ODD는 아무것도 허용하지 않으므로 스코프가 잘리지 않고, 가정이 참조할 속성이 없어 지식 항목을 만들 수 없다. **ODD가 비어 있으면 체계 전체가 정지한다 — 이것은 의도된 동작이다.**

작성 절차는 다섯 단계다.

1. **식별** — 프로젝트가 의존하는 조건을 정적/환경/동적 3갈래로 열거 → 속성 목록
2. **분류** — 각 속성을 `related/condition` 개념에 대응. 없으면 온톨로지 확장 → 개념 대응표
3. **정량화** — 각 속성에 값 또는 범위와 판정 방법 → 속성 청크
4. **제외 검토** — 검토했으나 밖에 두는 것을 명시 제외에 기록 → 제외 절
5. **검증** — 현재 실제 조건이 ODD 안에 있는지 3.5절로 대조. **첫 모니터링에서 이탈이면 ODD가 틀린 것**

**5단계를 통과하기 전에는 스코프를 파생하지 않는다.**
