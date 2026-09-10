---
id: https://agentic-knowledge-base.dev/id/chunk-d0063
type: decision
level: concrete
title_ko: 프로젝트는 ODD 작성으로 시작하고 5단계를 거친다
title: A project starts by authoring the ODD in five steps
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 새 프로젝트의 첫 산출물은 ODD다. 온톨로지는 프로젝트 간에
공유되므로 이미 있다. 작성은 식별 → 분류 → 정량화 → 제외 검토 → 검증
5단계이며, **5단계를 통과하기 전에는 스코프를 파생하지 않는다.**

**근거** (노트 3.7절, 3.8절)
- 빈 ODD로는 시작할 수 없다. restrictive 모드에서 빈 ODD는 아무것도 허용하지
  않으므로 스코프가 잘리지 않고, 가정이 참조할 속성이 없어 지식 항목을 만들
  수 없다. **ODD가 비어 있으면 체계 전체가 정지한다** — 전제를 적지 않고
  작업을 시작하는 것을 막는 의도된 동작이다.
- 5단계: (1) 프로젝트가 의존하는 조건을 정적/환경/동적 3갈래로 열거
  (2) 각 속성을 온톨로지 `related/condition` 개념에 대응, 없으면 온톨로지
  확장 (3) 값 또는 범위와 판정 방법 지정 (4) 검토했으나 밖에 두는 것을
  명시 제외에 기록 (5) 현재 실제 조건이 ODD 안에 있는지 3.5절로 대조.
- 첫 대조에서 이탈이 나오면 틀린 쪽은 현실이 아니라 ODD다.

**대안** (미확정) — 이전 프로젝트의 ODD를 복사해 시작하는 것을 기본 경로로
둘지 아직 확정하지 않았다. 상승(6.3절)으로 자란 온톨로지와 이전 ODD의
조합을 새 프로젝트의 출발점으로 삼는 안이 있다.
