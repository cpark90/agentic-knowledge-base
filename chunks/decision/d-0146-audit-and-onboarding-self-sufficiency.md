---
id: https://agentic-knowledge-base.dev/id/chunk-d0146
type: decision
level: concrete
title_ko: 감사와 온보딩은 체계의 출력만으로 성립한다
title: Audit and onboarding run on the system's output alone
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — audit 역할과 새로 들어오는 에이전트·사람은 **이 체계의 출력만으로
동작해야 한다.** 체계 밖 정보가 필요하면 그것은 체계의 누락이다.

**근거** (노트 10.4, 10.8절)
- 감사가 쓰는 것은 넷뿐이다 — 전 plane 읽기, 실행 기록, 링크 모델, 가정
  상태. 이 넷으로 부족한 감사 질문이 나오면 체계가 무언가를 기록하지 않은
  것이므로, 답을 밖에서 구하지 말고 기록을 늘린다.
- 온보딩 네 단계 — ① ODD를 읽는다(이 프로젝트가 무엇을 전제하는지)
  ② 자기 스코프의 라벨 목록을 받는다(무엇을 볼 수 있는지) ③ `decision`
  plane의 concrete 청크 라벨을 훑는다(무엇이 정해졌는지) ④ `suspect`·
  `invalidated` 목록을 본다(무엇이 흔들리는지).
- **이 네 단계에서 본문은 하나도 열지 않는다.** 라벨과 상태만으로 프로젝트의
  형태가 보여야 한다 — 라벨이 그 역할을 못 하면 4.13절 라벨 부패다.
