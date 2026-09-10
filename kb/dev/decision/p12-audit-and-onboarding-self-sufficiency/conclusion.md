---
id: https://agentic-knowledge-base.dev/id/chunk/64cbbffa-54d9-4f66-a2a0-ea2a34dc8653
type: decision
level: concrete
title_ko: 감사와 온보딩은 체계의 출력만으로 성립한다
title: Audit and onboarding run on the system's output alone
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/ba638521-e9b0-4c38-b073-44230ac22785]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0146]
part_of: https://agentic-knowledge-base.dev/id/composite/7f9b04c1-54f8-415f-83a2-7c0de8016c6a
composite: {id: https://agentic-knowledge-base.dev/id/composite/7f9b04c1-54f8-415f-83a2-7c0de8016c6a, title_ko: 감사와 온보딩의 자족성, title: Self-sufficiency of audit and onboarding}
---
**결론** — audit 역할과 새로 들어오는 에이전트·사람은 **이 체계의 출력만으로
동작해야 한다.** 감사가 쓰는 것은 전 plane 읽기 · 실행 기록 · 링크 모델 ·
가정 상태 넷이고, 체계 밖 정보가 필요하면 그것은 **체계의 누락**이다.

온보딩은 네 단계다.

1. ODD를 읽는다 — 이 프로젝트가 무엇을 전제하는지
2. 자기 스코프의 라벨 목록을 받는다 — 무엇을 볼 수 있는지
3. `decision` plane의 concrete 청크 라벨을 훑는다 — 무엇이 정해졌는지
4. `suspect`·`invalidated` 목록을 본다 — 무엇이 흔들리는지

**본문은 이 네 단계에서 하나도 열지 않는다.**
