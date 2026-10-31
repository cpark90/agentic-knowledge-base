---
id: https://agentic-knowledge-base.dev/id/chunk/b3586277-3689-4fe1-934d-ac6896a3c79d
type: decision
level: logical
title_ko: 갈림길 아홉에서 고르지 않은 선택지는 단일 작성자나 확정 권한, ODD를 바꾸거나 외부 지식을 막아 기각된다
title: The options not chosen at the nine forks are rejected because they break the single writer, change confirmation authority or the ODD, or block external knowledge
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:26:29+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9fef5341-55b1-4fda-8a93-e5ffdfbfcf83
---
**대안** — 갈림길 아홉(Q121~Q129)에서 유저가 고르지 않은 선택지를 기각한다.

| 갈림길 | 고르지 않은 선택지 | 기각 이유 |
|---|---|---|
| Q121 세션의 수 | 대상 종류마다 세션을 둔다. 유저용은 세션 유지, 나머지는 요청마다 dispatch한다 | 앞의 것은 동시 에이전트 합이 6이 되어 ODD 한도 5를 넓혀야 하고, 뒤의 것은 역할이 실행 모드로 갈려 dispatch의 주체를 새로 정해야 한다 |
| Q122 런타임 | 같은 기계의 Claude Code 세션만 가정한다. HTTP 서버를 둔다 | 앞의 것은 다른 프레임워크의 에이전트를 받지 못하고, 뒤의 것은 ODD 조건 `id:cond-network`를 넓히고 인증을 새로 정해야 한다 |
| Q123 한글 이름 | "외부 소통", "통역" | 유저는 해석기의 뜻을 살린 이름을 골랐고, "통역"은 비유여서 문장 규칙 9에 걸린다 |
| Q124 카탈로그 | 개명하고 숨은 라벨로 hci를 남긴다. 개명만 한다 | 앞의 것은 유저 전용 몫이 역할로 드러나지 않고, 뒤의 것은 `generated.by`가 hci인 단위 지식이 writer 검사에서 빠진다 |
| Q125 쓰기 상한 | 읽기만 허용한다. 외부 에이전트에 확정을 위임한다 | 앞의 것은 외부 지식을 받지 못하고, 뒤의 것은 외부 대상이 이 프로젝트의 확정 지식을 바꾼다 |
| Q126 외부 후보의 확정 | 항상 유저가 질문지로 확정한다 | 외부 제안이 많아지면 질문지가 늘어 유저의 부담이 커진다 |
| Q127 지식의 제공 | r-002의 넷만 준다. r-003을 개정해 저장까지 허용한다 | 앞의 것은 질의와 응답을 막고, 뒤의 것은 ODD가 다른 프로젝트가 지식을 저장하게 한다 |
| Q128 채널 | 수신함을 바깥까지 넓힌다. 저장소 요청을 함께 쓴다 | 앞의 것은 단일 작성자 규칙을 깨고, 뒤의 것은 제안 큐의 검사를 더하며 매개별 번역이 자리 잡기 전에는 쓸모가 작다 |
| Q129 메시지 종류 | `knowledge`에 증거 종류 줄을 붙인다 | 승격과 후보 등록이 한 종류여서 후보가 확정으로 승격될 위험이 생긴다 |
