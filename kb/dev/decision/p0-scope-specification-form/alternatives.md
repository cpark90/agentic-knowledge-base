---
id: https://agentic-knowledge-base.dev/id/chunk/40165645-9791-437b-a053-d89805f82bc4
type: decision
level: logical
title_ko: mode 생략과 프로세스 규칙을 문서로 두는 안의 기각
title: Rejecting an implicit mode and process rules kept as prose
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/780d333f-1d35-4e81-83cf-58355a1d3d41
---
**대안** — mode를 두지 않고 include/exclude 목록만 쓰는 안. 기각 — 목록에
없는 조건의 처리가 구현마다 달라지고, 같은 스코프 문서가 하네스에 따라 다른
권한을 뜻하게 된다.

**대안** — "구현 전 상세 설계" 같은 프로세스 규칙을 문서 규칙으로 두고 사람이
지키는 안. 기각 — 규칙 준수가 검토에 의존하면 1.1절의 이유로 규모에서 깨진다.

**미확정** — conditional의 판정식 언어는 0.4절이 고정하지 않는다. 예시는
결정의 level을 참조하는 형태를 보이지만, 참조 가능한 속성이 ODD 속성과 청크
메타 속성 중 어디까지인지는 열려 있다.
