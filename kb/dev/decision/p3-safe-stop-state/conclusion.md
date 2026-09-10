---
id: https://agentic-knowledge-base.dev/id/chunk/a24ec170-66e3-4ed4-aa09-3f70fb7f4d28
type: decision
level: concrete
title_ko: 이탈 시 남겨야 할 상태와 복귀 가능성
title: What must remain after an exit, and the ability to return
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/3b134d68-35ab-47bc-86cc-94f3eb12be93]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0065]
part_of: https://agentic-knowledge-base.dev/id/composite/a28b73f3-e4b9-41b0-840a-1febcceae940
composite: {id: https://agentic-knowledge-base.dev/id/composite/a28b73f3-e4b9-41b0-840a-1febcceae940, title_ko: 안전 정지 상태, title: The safe stop state}
---
**결론** — 3.5절 ODD 이탈 시 "작업 중단"이 무엇을 뜻하는지 정의한다. 이탈 감지 후 에이전트가 남겨야 할 상태다.

| 항목 | 상태 |
|---|---|
| 진행 중 편집 | 커밋하지 않음. 작업 디렉토리에 남기되 `suspect` 표시 |
| 후보 링크 | 확정하지 않음. 후보 그대로 |
| `memory` plane | 이탈 시점의 **작업 집합과 리비전**을 관측 청크로 기록 |
| 통지 | 이탈한 속성, 의존 항목 수, 위 상태의 위치를 유저 채널로 |

**안전 정지는 되돌릴 수 있어야 한다.** 이탈이 오판이었으면 정지 전 상태로 복귀한다.
