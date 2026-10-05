---
id: https://agentic-knowledge-base.dev/id/chunk/a3fa6128-2744-4caf-8d3b-53788183350f
type: decision
level: concrete
title_ko: 규범 문서 규약 — 개발 KB의 쓰기 권한은 네 역할에 나뉘고 developer는 확정된 것만 본다
title: Normative-document conventions — Write access to the development KB is split across four roles; developers see only what is fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4
---
**규약** — `p7-dev-roles-and-scopes`의 결론을 규범 문서에 싣는 문장이다.

규약: 역할 | design(요구·결정·계약·스키마·ODD) / developer(`artifact`) / orchestrator(dispatch 결정) / V&V(`annotation`만)
규약: **문서와 그래프는 일치해야 한다.** 아래 역할 표의 형식 원본은 `kg/catalog-kg.ttl`이다. 역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.
규약: 각 역할은 자기 write plane 밖을 수정하지 않는다.
규약: **orchestrator** (=메인) | 계획·dispatch·통합. 요구(유저 관심사의 EARS 저작 — stable 전이는 유저 승인)·결정 저작. 직접 구현하지 않는다. 유저와 직접 대화하지 않고 채널로 hci와 소통한다 | `requirement` · `decision` · `memory`(세션·판정 관측, 2026-09-14) · `norm`(규범 문서의 절 청크, 2026-10-04, Q21-a) | 전 plane | 세션 유지 | ✗
규약: **developer** (dispatch) | 분배된 산출물(코드·설정·온톨로지 개념) 저작. 노트 10.2절 9역할 중 design(T-Box·ODD 편집)을 겸한다 — 유저 결정 C4 | `artifact` (+T-Box·ODD) | `contract`·`schema`·`decision`. **`kb/vv/`는 읽기 전용** | dispatch | ✗
규약: **vnv** (dispatch) | 판정 전용: `bazel test //...` PASS 확인 + 결과 주석. **V&V KB(`kb/vv/`)의 유일한 편집 주체** — `verifies`의 주어는 V&V 청크뿐. 노트 8.20절의 다섯 V&V 하위 역할(engineer·검증기 저자·executor·judge·audit)을 겸하되 다른 세션에서 한다 | `kb/vv/`의 전 plane(`agt:writesIn "kb/vv"`, 2026-09-19 — 판정 주석도 V&V KB 안의 annotation plane) | `requirement`·`artifact`·`decision` | dispatch | ✗
규약: **hci** (별도 세션) | **유저 소통 전담 — 유일한 유저 창구.** 유저의 의도·결정을 질문지(유저 채널)로 받아 지시·지식으로 정제해 orchestrator에 넘기고, 질문과 결과를 유저에게 되돌린다. **조사와 git 관리**(add/commit/push, 유저 요청 시)를 맡는다 — 옛 inspection 역할을 2026-09-13에 이관 | — (채널만) | `requirement`·전 plane + 저장소 전체 | 세션 유지 | ✓
규약: **채널 쓰기 경계.** 채널은 둘이다. 유저 채널은 hci가 질문지를 쓰고 유저가 답을 적는다. 에이전트 채널은 **단일 작성자**다. `to_orchestrator/`에는 hci만, `to_hci/`에는 orchestrator만 쓰고(`harness/scripts/send.sh`), 상태 전이와 보관은 수신자가 한다(`harness/scripts/mark.sh`). hci의 작성·수정 범위는 이 채널 몫과 자기 역할 메모리(`.claude/agent-memory/hci/`)뿐이고 조회 범위는 저장소 전체다. developer·vnv는 채널에 쓰지 않는다. 그들의 질문과 결과는 hand-back으로 orchestrator에 돌아가고 orchestrator가 채널에 올린다(2026-10-03).
규약: 커밋 전 `bazel test //...` PASS를 확인한다. 커밋은 hci(유저 요청 시) 또는 유저가 한다.
