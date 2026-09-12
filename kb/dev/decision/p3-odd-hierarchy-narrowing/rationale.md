---
id: https://agentic-knowledge-base.dev/id/chunk/4bbd27d5-552a-4342-b317-0a83485a4fe4
type: decision
level: logical
title_ko: 부분집합 관계가 유지되어야 상위의 경계가 의미를 갖는다
title: Only a maintained subset relation keeps the parent boundary meaningful
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/7699d0eb-b30b-4015-b02c-d7db24b8eed1
---
**근거** (노트 3.11절) — 하위가 상위를 넓힐 수 있으면 상위 ODD가 더 이상 전체의 경계가 아니게 되고, 3.3절 파생물 게이트가 어느 ODD를 기준으로 판정해야 하는지 모호해진다. 좁히기만 허용하면 부분집합 관계가 불변식으로 유지되어 기계 검사가 가능하다.

전파의 비대칭은 부분집합 관계의 직접적 귀결이다. 상위 조건이 무너지면 그것을 좁혀 쓴 하위 전부의 전제가 무너지지만, 하위 하나가 자기 범위에서 이탈한 것은 다른 하위와 무관하다. 대칭으로 전파하면 무효화 범위가 실제보다 넓어져 전수조사와 다를 바 없어진다.
