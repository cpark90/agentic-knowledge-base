---
id: https://agentic-knowledge-base.dev/id/chunk/a1b7d36b-0909-463b-b4f9-2134a1681e80
type: decision
level: logical
title_ko: 유저가 서비스를 두 에이전트로 정했고 인터프리터라는 이름은 외부 요청을 해석해 지식 베이스의 동작으로 옮긴다는 뜻이다
title: The user set the service as two agents, and the name interpreter means translating external requests into actions on the knowledge base
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:26:29+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:26:29+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9fef5341-55b1-4fda-8a93-e5ffdfbfcf83
---
**근거** — 유저는 Q-0056의 추가답변으로 서비스 구조를 정했다(2026-10-24). 원문은 "knowledge base는 orchestrator agent와 interpreter agent로 서비스되며, orchestrator agent는 기존과 유사하게 knowledge base에 대한 작업을 총괄하는 역할임. interpreter agent는 현재 hci agent의 역할을 일반화해서 knowledge base 외부의 대상들(사용자, knowledge base를 이용하는 타 프로젝트의 agent들 등)과 knowledge base orchestrator agent 사이의 커뮤니케이션을 담당"이다.

유저는 한글 이름을 "인터프리터"로 정하면서 "interpreter는 프로그래밍 언어의 해석기에서 차용한 용어임. 그와 유사한 역할을 할 예정임."이라고 설명했다(Q123-b). 해석기가 원시 코드를 읽어 실행할 동작으로 옮기듯이, 인터프리터는 외부의 요청을 읽어 지식 베이스에 대한 조회나 지시로 옮긴다.

공통 몫과 유저 전용 몫은 task 0195에 대한 orchestrator의 기획안이 나눈 것이다. 기획안은 hci의 일을 상대의 형식과 무관하게 같은 절차로 끝나는가로 갈랐다. 그래서 대상이 바뀌어도 절차가 같은 다섯이 공통 몫이 됐고, 사람이 읽고 답하는 형식인 질문지와 유저의 요청에만 따르는 git 관리가 유저 전용 몫이 됐다.

채널은 기획안의 비교를 따른다. 바깥 구간에서 수신함을 외부까지 넓히면(1A) 수신함의 단일 작성자 규칙이 깨지고, 저장소 요청(1C)은 질의와 응답을 담지 못한다. 반면 매개별 번역(1B)은 질문지를 유저의 매개로 그대로 쓰고 읽기 요청을 결정론적 도구가 답하게 하므로 orchestrator의 부하가 늘지 않는다. 안쪽 구간은 세션이 하나이므로 `origin`만 더해도(2A) 단일 작성자가 남는다. 또한 stdio MCP는 ODD 조건 `id:cond-network`의 값 `initial_fetch_then_offline` 안에 머문다.

쓰기 상한을 후보 제안까지로 두면 확정 권한을 바꾸지 않고 외부 지식을 받는데, 이 높이는 참조 프로파일의 claim 역할과 같다(`p11-dev-profile-role-permissions`). 외부 후보는 증거 종류 `proposal`로 들어와 확정 근거가 되지 않는다(`p9-language-model-place`). 투영과 `odd_mismatch`는 r-003의 근거, 곧 ODD가 다르면 가정 판정이 성립하지 않는다는 사실을 응답에 실어 보낸다. 메시지 종류 `proposal`을 따로 두는 까닭은 `knowledge`가 유저가 확인한 사실을 담기 때문이며, 둘을 섞으면 후보가 확정으로 승격될 위험이 생긴다.

유저는 기획안의 권장과 다른 셋을 골랐다(Q123-b, Q124-b, Q126-b). 한글 이름은 서술어 "외부 소통" 대신 "인터프리터"이고, 카탈로그는 개명 대신 상위 역할과 하위 역할을 함께 두며, 외부 후보의 확정은 질문지 대신 위임 범위 안의 orchestrator 확정이다.

**개정** — 유저는 외부 대상을 셋으로, 매개를 둘로 줄였다(Q-0063#Q157). 빠진 대상(모델 학습·검사 파이프라인)과 매개 둘(내보내기 묶음, 모델 출력 검사)은 폐기된 요구 r-030·r-031을 전제로 했다(Q-0063#Q156).
