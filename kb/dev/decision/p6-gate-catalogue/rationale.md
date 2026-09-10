---
id: https://agentic-knowledge-base.dev/id/chunk/05b54661-5696-4596-8fa7-6fab11b57497
type: decision
level: logical
title_ko: 계층 배치가 컨텍스트 예산과 재검증 시점 입력의 근거다
title: Layer placement grounds the context budget and the re-judgement boundary input
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/33c8a1a1-fc90-4ce7-83a9-20c607a7c163
---
**근거** (노트 6.7절, 1.4절, 11.1절, 4.11절) — 즉시 계층이 느리면 편집이 막히고, 경계 계층이 즉시 돌면 낭비다. 그래서 청크 하나로 판정 가능한 것(shape)과 빌드 그래프로 판정 가능한 것(analysis)만 즉시이고, 그래프 전체가 필요한 것(verify)과 실행이 필요한 것(test)은 재검증 시점(11.1절 입력)로 모인다. 실패가 `draft`에 머물러 전파되지 않는 것은 4.11절("draft는 링크의 끝이 될 수 없다")의 귀결이며, 게이트가 하류를 오염시키지 않는 이유다. 한 표로 모으는 이유는 "이 규칙을 누가 판정하는가"가 비어 있는 게이트를 드러내기 위함이다.
