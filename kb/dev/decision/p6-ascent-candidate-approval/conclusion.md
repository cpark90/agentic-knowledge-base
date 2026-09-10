---
id: https://agentic-knowledge-base.dev/id/chunk/b136d285-c4ba-461b-99cf-bda07c2243d8
type: decision
level: concrete
title_ko: 일반화는 자동화하지 않고 실행 가능 피드백이 붙은 관측을 먼저 올린다
title: Ascent is never automated and prefers observations with executable feedback
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0089]
part_of: https://agentic-knowledge-base.dev/id/composite/b3bb3bde-43af-4fad-8e67-3a52dd7a2fa9
composite: {id: https://agentic-knowledge-base.dev/id/composite/b3bb3bde-43af-4fad-8e67-3a52dd7a2fa9, title_ko: 일반화 후보의 선별과 승인, title: Selecting and approving ascent candidates}
---
**결론** — 일반화는 **자동화하지 않는다.** 후보를 제시하고 유저 확인을 받으며, 온톨로지 갱신은 2.5절 용어 제안 워크플로(template 행 → 3계층 검사 → 유저 승인 → 확장 모듈 병합)를 따른다.

후보의 우선순위는 **실행 가능 피드백**이다. 판정 도구의 결과(테스트·검사)가 붙은 관측 청크가 산문 관찰보다 먼저 승격된다. 피드백 자체의 신뢰성이 낮으면(7.13절 시뮬레이션 신뢰도) 일반화가 오염되므로, **신뢰도가 검증되지 않은 환경의 관측은 승격을 보류한다.**
