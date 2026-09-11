---
id: https://agentic-knowledge-base.dev/id/chunk/a8129aa8-f771-496f-8a3c-6f3f0b2a0ebd
type: decision
level: logical
title_ko: 자극과 판정을 한 청크에 두면 기준 변경이 케이스 변경으로 보인다
title: Fusing stimulus and judgement makes a loosened criterion look like a changed case
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/14433614-5dd7-4df3-b32c-2422a25daef3
---
**근거** (노트 8.11절) — 자극(케이스)과 판정(기준)을 한 청크에 두면 **기준 변경이 케이스 변경으로 보인다.** 무엇이 느슨해졌는지가 이력에서 드러나지 않으므로 기준을 별도 청크로 두고 링크 속성으로 묶는다.

- 기준이 개발 KB의 abstract → logical 게이트를 성립시킨다 — 범위를 검사할 판정식이 V&V KB에 없으면 개발 계층이 다음 높이로 내려가지 못한다 (r-023).
- "검증했다"는 주장에 "무엇으로"가 없으면 검증이 아니다 (r-024). 판정식이 없는 기준은 아직 형식화만 된 상태이므로 level 표기도 abstract로 강등한다 — 6.8절 전이 게이트와 같은 처리다.
- 에이전트 대상 기준 둘(산출물 품질·인지)이 같은 목록에 있는 이유는 판정 방식이 같기 때문이다 (7.8절).
