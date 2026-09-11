---
id: https://agentic-knowledge-base.dev/id/chunk/23a48782-3383-4721-a184-8185f2a5a554
type: decision
level: concrete
title_ko: 결정은 abstract·logical·concrete 세 수준에 걸치고 수준마다 별개 청크다
title: A decision spans abstract, logical and concrete, one chunk per level
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/9acf3e73-f933-4260-9b42-432825013b6c, title_ko: 결정의 세 수준, title: A decision spans three levels}
part_of: https://agentic-knowledge-base.dev/id/composite/9acf3e73-f933-4260-9b42-432825013b6c
---
**결론** — **`decision`이 세 수준에 걸친다.** abstract에서 변수를 선언하고, logical에서 후보·제약·배제 근거를 갖고, concrete에서 확정 값을 갖는다. 한 결정은 수준마다 별개의 청크이고 `refines`로 이어진다. 결정이 "확정됐다"는 것은 concrete 청크가 생겼다는 뜻이다 (노트 7.2절).

이 저장소의 구현 (유저 결정 2026-09-10, Q1(a)) — 역할 세 청크(결론 concrete·근거 logical·대안 logical)를 기본으로 두고, abstract 변수 청크는 `-space`가 있는 결정에만 만든다. 후보가 하나뿐이어서 `-space`가 없는 결정은 abstract 청크 없이 logical·concrete만 갖는다.
