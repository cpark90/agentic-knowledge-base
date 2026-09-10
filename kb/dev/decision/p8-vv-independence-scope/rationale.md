---
id: https://agentic-knowledge-base.dev/id/chunk/8e92a120-4898-48fa-921b-ad377220fbb8
type: decision
level: logical
title_ko: 권한과 의존 방향을 고정해야 독립이 실효를 갖는다
title: Independence takes effect only when permissions and dependency direction are fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e
---
**근거** (노트 8.5절) — 권한을 역할에 붙이고 스코프로 강제해야 독립이 실효를 갖는다. 규약으로만 두면 같은 에이전트가 두 KB를 함께 열고 실패하는 기준을 고치는 것이 가장 짧은 경로가 된다 (1.2절 방향 있는 실수).

- 의존 방향을 한쪽으로 고정하면 개발 KB의 빌드가 V&V KB의 상태에 영향받지 않는다. 검증이 깨져도 개발이 멈추지 않고, 반대로 V&V KB만 따로 빌드되는 일은 없다 — 검증할 대상이 없기 때문이다.
- **되먹임은 링크가 아니라 일반화으로 간다.** V&V의 결함이 개발 KB의 요구·결정을 바꾸는 것은 `prov:wasDerivedFrom`이 남는 승격이지, 개발 청크가 V&V 청크를 가리키는 링크가 아니다. 링크로 두면 방향 고정이 깨지고 개발 KB가 V&V KB에 의존하게 된다.
