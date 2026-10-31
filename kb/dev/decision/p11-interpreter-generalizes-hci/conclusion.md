---
id: https://agentic-knowledge-base.dev/id/chunk/fd376243-16f1-4f4c-a463-099b87637565
type: decision
level: concrete
title_ko: 인터프리터는 hci를 일반화해 외부 대상과 orchestrator 사이의 소통을 맡고 hci는 그 유저 대상 하위 역할이다
title: The interpreter generalizes hci to carry communication between external parties and the orchestrator, and hci is its user-facing sub-role
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/e461c8ed-196f-4eac-9cff-4052d5833776]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:17:21+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9fef5341-55b1-4fda-8a93-e5ffdfbfcf83
composite: {id: https://agentic-knowledge-base.dev/id/composite/9fef5341-55b1-4fda-8a93-e5ffdfbfcf83, title_ko: 인터프리터와 외부 대상, title: The interpreter and external parties}
---
**결론** — 지식 베이스는 orchestrator와 인터프리터(interpreter) 두 에이전트로 서비스된다(유저 지시 2026-10-24, 유저 답 Q121~Q130). orchestrator는 지식 베이스의 작업을 총괄하고, 인터프리터는 지식 베이스 밖의 대상과 orchestrator 사이의 소통을 맡는다.

| 몫 | 맡는 역할 | 일 |
|---|---|---|
| 공통 몫 | 인터프리터 | 요청의 해석과 저장소 조회로 직접 답하기, 지시 작성, 되묻기 중계, 결과 검증의 다섯이다 |
| 유저 전용 몫 | 하위 역할 hci | 질문지와 유저 요청 시의 git 관리의 둘이다 |

- **외부 대상은 셋이다.** 셋은 유저와 지식 베이스를 쓰는 다른 프로젝트의 에이전트, 다음 프로젝트(r-002)다(Q-0063#Q157).
- **인터프리터는 세션 하나다.** 대상은 메시지의 `origin` 필드로 가른다(Q121-a). 카탈로그에는 인터프리터를 상위 역할로, hci를 유저 대상 하위 역할로 함께 두고, hci 하위 역할은 같은 세션이 맡는다(Q124-b).
- **채널은 두 구간으로 나뉜다.** 외부 대상과 인터프리터 사이의 바깥 구간은 대상마다 맞는 매개로 번역하고(1B), 인터프리터와 orchestrator 사이의 안쪽 구간은 지금의 에이전트 채널에 `origin` 필드를 더해 쓴다(2A, Q128-a). 매개는 질의와 응답, 후보 제안의 둘이다.
- **타 프로젝트의 에이전트는 MCP 클라이언트로 가정한다.** 그래서 인터프리터 쪽에 표준 입출력(stdio) MCP 서버를 두고, 이 서버는 네트워크를 쓰지 않으므로 ODD를 바꾸지 않는다(Q122-b).
- **외부 대상의 쓰기는 후보 제안까지다**(Q125-b). 외부에서 온 후보는 유저가 미리 정한 범위 안에서 orchestrator가 확정하고 그 결과를 유저에게 보고하며, 인터프리터는 확정하지 않는다(Q126-b).
- **타 프로젝트의 에이전트에는 지식을 투영으로 준다**(Q127-a). 응답에는 이 프로젝트의 ODD 조건을 붙이고, 요청자의 ODD 값이 다르면 `odd_mismatch`를 표시한다.
- **에이전트 채널의 메시지 종류에 `proposal`을 더한다**(Q129-a). 이 종류는 외부 후보를 orchestrator에 넘기며, 유저가 확인한 사실을 담는 `knowledge`와 갈린다.

매개의 형식과 MCP 서버의 세부, 위임 범위, r-003의 재서술, 메시지 종류 `proposal`의 도입은 뒤 단계의 결정이 정한다. 첫 단계는 역할과 문서만 넓히므로 hci 세션과 스크립트, 채널 디렉토리는 그대로 남는다(Q130-a).
