---
id: https://agentic-knowledge-base.dev/id/chunk/0ae3682d-1aea-48e1-9777-c8a6bcf34a65
type: decision
level: logical
title_ko: 전수조사를 질의 하나로 바꾸는 것이 갱신 단절의 해법이다
title: Replacing exhaustive survey with a single query solves the update break
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/db06ba12-f04a-45c7-b5e3-d26d97dc7e51
---
**근거** (노트 6.5절) — 갱신 단절의 해법이다. 조건을 명시하지 않으면 무엇이 낡았는지 알아내는 유일한 방법이 전수조사이고, 전수조사는 컨텍스트가 좁은 에이전트가 할 수 없는 일이다 (1.1절).

- 가정이 온톨로지 개념에 대한 명제이므로 `defect-rules`의 추론 규칙으로 판정할 수 있다. "`agt:ExternalClient` 개체가 `project-kg`에 존재하는가"는 질의 하나다. 판정 불가능한 가정도 기록하되 `unverified`로 둔다.
- 무효화 이력이 6.3절 일반화의 입력이 된다 — 어떤 가정이 자주 깨지는가는 그 자체로 일반화 대상이다. 삭제하면 이 입력이 사라진다.
- 가정을 청크 단위로 붙이면 입도 문제가 청크 분할 문제로 환원된다. 별도의 입도 규칙을 두지 않는다.
