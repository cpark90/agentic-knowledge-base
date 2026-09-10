---
id: https://agentic-knowledge-base.dev/id/chunk/5fd867b9-6d4d-4a4a-ab2d-98691b2392c2
type: decision
level: logical
title_ko: 권한과 조건을 한 문서에서 잘라야 경계가 하나다
title: Cutting both rights and conditions from one document keeps one boundary
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/494002b4-33ba-470c-93ee-cc0fe39be1c7
---
**근거** (노트 3.4절) — 스코프가 ODD와 독립이면 하네스마다 경계를 따로 정의하게 되고(3.3절), 두 경계가 어긋날 때 어느 쪽이 참인지 판정할 수단이 없다. `from`으로 출처를 밝히고 `inherit`로만 속성을 얻으면 경계는 언제나 ODD 하나다.

조건 상속과 plane 권한을 한 문서에서 다루는 것이 중요하다 — 에이전트가 볼 수 있는 것은 "어떤 plane을" × "어떤 조건 아래" 둘의 교집합이기 때문이다.

작업 집합이 질의 결과라는 점이 이 규칙을 강제한다. 질의가 참조할 수 있는 속성이 ODD에 없으면 그 조건은 애초에 결과에 나타나지 않는다.
