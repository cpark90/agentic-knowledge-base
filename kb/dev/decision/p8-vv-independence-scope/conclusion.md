---
id: https://agentic-knowledge-base.dev/id/chunk/60271a33-e150-4e2d-a6ed-728ea04e7ce3
type: decision
level: concrete
title_ko: 개발 역할은 V&V KB를 읽기만 한다
title: Development roles may only read the V&V KB
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
part_of: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e
composite: {id: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e, title_ko: 독립성과 스코프, title: Independence and scope}
---
**결론** — 두 KB의 스코프 규칙.

- **설계·개발** — 개발 KB 읽기·쓰기 / V&V KB **읽기만**. 결함·커버리지·기준을 볼 수 있으나 고칠 수 없다
- **V&V** — 개발 KB 읽기만 / V&V KB 읽기·쓰기
- **감사** — 양쪽 읽기
- **orchestrator** — 개발 KB 읽기·쓰기(dispatch) / V&V KB 읽기

**기준을 고쳐야 할 때 개발 역할은 개발 KB의 요구를 고친다.** 요구가 바뀌면 V&V 역할이 검증 목표와 기준을 다시 파생한다. 기준을 직접 고치는 경로는 없다.

저장도 분리한다 — 별도 저장소 또는 별도 최상위 패키지. 링크가 V&V → 개발 방향으로만 저장되므로 **개발 KB는 V&V KB 없이 빌드되고, V&V KB는 개발 KB 없이 빌드되지 않는다.**
