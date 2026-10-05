---
id: https://agentic-knowledge-base.dev/id/chunk/b8d74a2d-f94b-4fe7-8b3b-13dca638d338
type: decision
level: concrete
title_ko: 케이스의 자극과 기대는 검증기가 읽는 형식으로 적는다
title: A case writes its stimulus and expectation in a form the verifier reads
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
generated: {by: orchestrator/claude-opus-5, at: 2026-10-05T12:48:53+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T12:49:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e2064625-339c-4cef-8f06-5e775874f177
composite: {id: https://agentic-knowledge-base.dev/id/composite/e2064625-339c-4cef-8f06-5e775874f177, title_ko: 기계가 읽는 케이스, title: A machine-readable case}
---
**결론** — 케이스의 `**자극**`과 `**기대**`는 산문 옆에 **`yaml` 펜스 하나**를 두어 검증기가 읽을 수 있게 한다. 산문은 사람을 위한 것이고 펜스는 기계를 위한 것이며 둘은 같은 사실을 말한다.

| 키 | 내용 | 검증기가 하는 일 |
|---|---|---|
| `files` | 경로마다 파일 내용 | 명령 앞에 쓰고 뒤에 지운다. 커밋하지 않는다 |
| `expect` | 명령 순서마다 `exit`와 `contains` | 종료 코드를 대조하고 `contains`의 문구를 출력에서 찾는다 |

판정은 둘 다 맞아야 `pass`다. 종료 코드만 보면 "실패했는가"는 알아도 **"무엇이 거부되는가"는 모른다.** 음성 자극의 값은 거부 사유가 기대한 그것이라는 데 있다.

`files`가 있는 케이스는 음성 명령이 더는 건너뛰어지지 않는다. 건너뛴 명령이 있으면 케이스는 `pass`가 아니라 `skip`이므로, 자극을 기계가 읽게 하는 것이 그 케이스를 판정 가능하게 만드는 길이다.

**점진 도입이다.** 펜스가 없는 기존 케이스는 지금처럼 양성 명령만 돌고 판정도 그대로다. 규약을 어기는 것이 아니라 아직 옮기지 않은 것이다. 옮긴 케이스부터 음성 절반을 얻는다.

임시 파일의 경로는 검증기가 정하고 케이스가 정하지 않는다. 케이스는 이름만 적고 명령에서 `{{이름}}`으로 가리킨다. 케이스가 절대 경로를 적으면 병렬 실행이 서로를 덮고, `contains`에 그 경로를 적으면 대조가 깨진다.

**자극이 케이스 본문의 상한(1,092토큰)을 넘으면 생성기 입력인 시나리오를 나눈다.** 케이스는 전부 생성되고 수기 케이스는 0이다(Q27-a). 따라서 나누는 자리는 케이스가 아니라 그 입력이다. 상한의 단위는 토큰이므로 자극을 한 줄 스칼라로 접어도 토큰 수는 줄지 않는다.
