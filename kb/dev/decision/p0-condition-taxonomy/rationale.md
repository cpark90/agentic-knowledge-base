---
id: https://agentic-knowledge-base.dev/id/chunk/46957827-a764-43a0-b254-06d90f7cd453
type: decision
level: logical
title_ko: 둘째 수준이 고정되어야 갈래별 커버리지를 셀 수 있다
title: A fixed second level is what makes per-branch coverage countable
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/7d50713a-5c4d-485d-8a46-a36172a1b114
---
**근거** (노트 0.4절, 3.9절)

- 둘째 수준을 고정하면 ODD 속성이 빠짐없이 분류되어 **갈래별 커버리지를
  셀 수 있다.** 셋째 수준까지 고정하면 프로젝트마다 맞지 않아 강제가 깨진다.
- 판정 등급을 하위 분류마다 붙이는 이유는 ODD 이탈 감지의 실효성이 등급의
  분포로 결정되기 때문이다. 대부분 A(기계 판정)지만 코딩 규약은 B(린터),
  아키텍처 스타일과 외부 행위자는 C다.
- **시간 제약이 동적 갈래에 새로 들어온 것은 0.5절이 시간열 개체를 없앤
  결과다.** 선행·배타·시한을 형식화할 자리가 ODD 어휘밖에 남지 않았고, 판정은
  실행 기록의 시각 순서로 하므로 등급 A다.
- 환경 조건의 "시간"(시간대·배포 창·마감)과 동적 요소의 "시간 제약"은 다른
  개념이다 — 전자는 밖에서 주어지는 조건, 후자는 작업 간 순서·배타 요구다.
