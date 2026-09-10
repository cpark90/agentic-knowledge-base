---
id: https://agentic-knowledge-base.dev/id/chunk/57a89ef5-58bd-4c89-bf2a-07b4fa800153
type: decision
level: logical
title_ko: 사람 검토가 성립하지 않으므로 구조로 통제한다
title: Human review cannot scale, so control by structure
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/cca68a89-e572-4104-ba7e-cddd3c67c7bb
---
**근거** (노트 1.1·1.6절) — 에이전트는 200줄 밖을 못 보는 부분관측 행위자이므로,
무엇을 보게 할지가 곧 무엇을 판단하게 할지다. 이 체계는 그것을 우연에 맡기지
않고 스코프로 명세하고 하네스로 강제한다.

사람 쪽에도 한계가 있다 — 에이전트 산출물을 사람이 한 줄씩 따라 읽는 것은
불가능하다. 매 시점 산출물이 바뀌고 상세가 바뀌면 큰 방향도 바뀐다. 사람의
검토로 품질을 지키는 방식은 처음부터 성립하지 않으므로 지식 접근을 **구조로**
통제해야 한다.

이 대응이 있어야 "이 에이전트가 왜 그 판단을 했는가"를 관측(작업 집합)과
신념(memory)으로 재구성할 수 있다 — 11.3절 인지능력 측정의 근거다.
