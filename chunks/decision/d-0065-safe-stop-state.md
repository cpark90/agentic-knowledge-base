---
id: https://agentic-knowledge-base.dev/id/chunk-d0065
type: decision
level: concrete
title_ko: ODD 이탈 시 남겨야 할 안전 정지 상태
title: The safe-stop state required on ODD exit
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 3.5절의 "작업 중단"이 뜻하는 상태를 정의한다. 이탈을 감지한
에이전트는 진행 중 편집을 커밋하지 않고 작업 디렉토리에 `suspect` 표시로
남기고, 후보 링크를 확정하지 않은 채 후보로 두며, 이탈 시점의 situation을
`memory` plane에 관측 청크로 기록하고, 이탈한 속성·의존 항목 수·남긴 상태의
위치를 유저 채널로 통지한다.

**근거** (노트 3.10절)
- "작업 중단"의 내용을 정하지 않으면 이탈 대응이 에이전트마다 달라지고,
  중단 후 무엇이 남았는지 아무도 모른다.
- 커밋하지 않되 버리지도 않는다 — **안전 정지는 되돌릴 수 있어야 하기**
  때문이다. 이탈이 오판이었으면 정지 전 상태로 복귀한다.
- 통지에 의존 항목 수가 들어가야 유저가 이탈의 파급 규모를 보고 판단할 수
  있다.
