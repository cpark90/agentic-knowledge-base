---
id: https://agentic-knowledge-base.dev/id/chunk/8a3978c2-4013-4f06-9dc0-6e1417553e28
type: norm
level: logical
title_ko: docs/method.md 절 — 프로파일 구축 절차와 확장점 열거
title: docs/method.md section — profile construction procedure and enumeration of extension points
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/bdc0f6e2-e2e2-4438-a6bd-917dec16b120
composite: {id: https://agentic-knowledge-base.dev/id/composite/bdc0f6e2-e2e2-4438-a6bd-917dec16b120, title_ko: docs/method.md의 프로파일·ODD 절 묶음, title: docs/method.md profile and ODD section group, part_of: https://agentic-knowledge-base.dev/id/composite/c040ba95-dc6c-4c10-af69-8d0d4c0cf6ec, ordered: [https://agentic-knowledge-base.dev/id/chunk/8a3978c2-4013-4f06-9dc0-6e1417553e28, https://agentic-knowledge-base.dev/id/chunk/e7b0a393-e91c-4e8d-8b48-01dd3c917e3c, https://agentic-knowledge-base.dev/id/chunk/ad3aee4c-9375-4c30-ae86-3780178320b3, https://agentic-knowledge-base.dev/id/chunk/d2959966-0530-4409-9566-06cd2f732183, https://agentic-knowledge-base.dev/id/chunk/539016c1-28bb-47b2-b587-948dbf710bc6]}
heading: 프로파일 구축
depth: 2
form: ordered
items: [p2-skeleton-and-domain-profile#2]
---
프로파일은 코어를 특정 작업 종류에 맞게 채운 온톨로지 모듈이다(`p2-skeleton-and-domain-profile`). 코어 클래스의
하위 클래스·개체·프로파일 전용 속성·shape만 더하고 코어를 수정하지 않는다 — boundary 게이트가 재정의를 거부한다
([`id:chunk-d0057`](../../../../chunks/decision/d-0057-profile-extension-only-module.md)). 절차는 첫 프로파일(`development`,
2026-09-18)을 만들면서 뽑았다.
