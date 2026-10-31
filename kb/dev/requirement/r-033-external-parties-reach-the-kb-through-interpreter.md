---
id: https://agentic-knowledge-base.dev/id/chunk/e461c8ed-196f-4eac-9cff-4052d5833776
type: requirement
level: functional
pattern: ubiquitous
title_ko: 외부 대상은 인터프리터를 거쳐 지식 베이스와 소통한다
title: External parties shall reach the knowledge base through the interpreter
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-req-agent
---
**요구** — 체계는 지식 베이스 밖의 대상이 인터프리터를 거쳐서만 지식 베이스와 소통하게 하여야 한다. 밖의 대상은 유저와 지식 베이스를 쓰는 다른 프로젝트의 에이전트, 다음 프로젝트다(Q-0063#Q157).

- **이해관계자**: 업체 · **관심사**: 지식 베이스의 서비스 경계
- **출처**: 유저 지시 2026-10-24("knowledge base는 orchestrator agent와 interpreter agent로 서비스되며 … interpreter agent는 현재 hci agent의 역할을 일반화해서 knowledge base 외부의 대상들 … 과 knowledge base orchestrator agent 사이의 커뮤니케이션을 담당"), 유저 답 Q121~Q130(Q-0058)

인터프리터는 외부의 요청을 해석해 지식 베이스에 대한 동작으로 옮기고, 지식 베이스의 작업은 orchestrator가 총괄한다. 외부 대상이 쓸 수 있는 범위와 확정 권한의 자리는 결정이 정한다.
