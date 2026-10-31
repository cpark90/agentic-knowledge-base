---
id: https://agentic-knowledge-base.dev/id/chunk/a3fa6128-2744-4caf-8d3b-53788183350f
type: decision
level: concrete
title_ko: 규범 문서 규약 — 개발 KB의 쓰기 권한은 네 역할에 나뉘고 developer는 확정된 것만 본다
title: Normative-document conventions — Write access to the development KB is split across four roles; developers see only what is fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T17:44:41+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4
---
**규약** — `p7-dev-roles-and-scopes`의 결론을 규범 문서에 싣는 문장이다.

규약: 역할 | design은 요구, 결정, 계약, 스키마, ODD / developer는 `artifact`와 개발 KB의 `contract` / orchestrator는 dispatch 결정 / V&V는 `annotation`만
규약: **문서와 그래프는 일치해야 한다.** 아래 역할 표의 형식 원본이 `kg/catalog-kg.ttl`이므로 역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.
규약: 각 역할은 자기 쓰기 지식 종류 밖을 수정하지 않는다.
규약: **orchestrator** (메인) | 계획, dispatch, 통합과 요구·결정 저작을 맡고, 요구는 유저 관심사의 EARS 저작이며 `stable` 전이는 유저가 승인한다. 구현하지 않고 유저와 직접 대화하지 않으며 채널로 interpreter와 소통한다 | `requirement`, `decision`, 세션·판정 관측인 `memory`, 규범 문서의 절인 `norm`(memory는 2026-09-14, norm은 2026-10-04와 Q21-a) | 전 지식 종류 | 세션 유지 | ✗
규약: **developer** (dispatch) | 분배된 산출물인 코드와 설정, 온톨로지 개념을 저작하고, 노트 11.2절 9역할 중 T-Box·ODD 편집인 design을 겸한다(유저 결정 C4) | `artifact`, 개발 KB의 시그니처인 `contract`와 T-Box·ODD(Q79-a) | `contract`·`schema`·`decision`. **`kb/vv/`는 읽기 전용** | dispatch | ✗
규약: **vnv** (dispatch) | `bazel test //...` PASS 확인과 결과 주석만 맡는다. **V&V KB인 `kb/vv/`의 유일한 편집 주체**여서 `verifies`의 주어는 V&V 단위 지식뿐이다. 노트 8.20절의 V&V 하위 역할 다섯을 다른 세션에서 겸한다 | `kb/vv/`의 전 지식 종류(`agt:writesIn "kb/vv"`, 판정 주석도 V&V KB의 `annotation`, 2026-09-19) | `requirement`·`artifact`·`decision` | dispatch | ✗
규약: **hci** (interpreter의 하위 역할) | **interpreter의 유저 대상 하위 역할이고 유저 소통의 유일한 창구다.** 유저의 의도와 결정을 질문지로 받아 정제해 orchestrator에 넘기고 질문과 결과를 유저에게 되돌린다. 유저 전용 몫인 질문지와, 유저 요청 시 add/commit/push를 하는 **git 관리**를 맡는다 | — (유저 채널과 자기 역할 메모리) | `requirement`·전 지식 종류·저장소 전체 | interpreter 세션 | ✓
규약: **채널 쓰기 경계** — 채널은 둘이다. 유저 채널에는 hci가 질문지를 쓰고 유저가 답을 적으며, 에이전트 채널은 **단일 작성자**다. `to_orchestrator/`에는 interpreter(하위 역할 hci 포함)만, `to_interpreter/`에는 orchestrator만 `harness/scripts/send.sh`로 쓰고, 상태 전이와 보관은 수신자가 `harness/scripts/mark.sh`로 한다. interpreter 세션은 이 채널 몫과 유저 채널, 자기 역할 메모리만 쓰고 저장소 전체를 조회한다. developer·vnv는 채널에 쓰지 않고, 그 질문과 결과는 hand-back으로 orchestrator가 받아 채널에 올린다.
규약: 커밋 전 `bazel test //...` PASS를 확인한다. 커밋은 유저가 하거나, 유저가 요청하면 hci가 한다.
규약: **interpreter** (별도 세션) | **외부 대상과 orchestrator 사이 소통의 창구다.** 외부 대상 셋(Q-0063#Q157)을 세션 하나로 맡고, 공통 몫은 요청의 해석과 저장소 조회로 직접 답하기, 지시 작성, 되묻기 중계, 결과 검증이다 | — (에이전트 채널 발신) | 전 지식 종류·저장소 전체 | 세션 유지 | 하위 역할 hci가 한다
