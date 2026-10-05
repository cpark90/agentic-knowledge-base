---
id: https://agentic-knowledge-base.dev/id/chunk/ef848ac6-9e48-4b13-8390-0640dbfd67c4
type: decision
level: logical
title_ko: 세션은 끝나면 사라지고 산출물은 남으므로 내용은 산출물에 두고 세션은 그 자리를 가리킨다
title: A session vanishes when it ends while artifacts remain, so content goes to artifacts and the session points at them
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/23cf6ac9-f4b7-498b-88dc-84e70d2d5f8c
---
**근거** — 요구 r-020은 세션이 끝나면 경험이 사라지는 구조에서 같은 실수가 반복된다고 적는다. 세션에 남긴 내용은 세션과 함께 사라진다. 산출물에 쓴 내용은 그래프에 들고 게이트를 거친다.

`p11-harness-two-channels`는 같은 원리를 채널에 적용한다. 메시지는 흐르고 지식 베이스는 남는다. 결론은 종류별 자리로 승격한다. 이 결정은 그 원리를 세션 보고와 채팅으로 넓힌다.

주석을 산출물과 다른 plane에 두는 것은 `p5-annotation-artifact-separation`이다. 주석이 산출물에 박히면 두 plane이 항상 함께 적재된다.

규약의 문장은 저장소 초기 구축(2026-09-01)의 `AGENTS.md` 소통 규칙부터 있었다. 채팅에 질문지 안내와 요지만 쓰는 문장도 같은 날 더해졌다(커밋 이력). orchestrator 지침 원칙 4는 `result`에 무엇을 어디에 썼는지만 요약한다고 적는다.

미확정: 임시 파일을 스크래치패드에 두는 규칙의 이유는 기록에서 확인하지 못했다.
