# AGENTS.md — 이 저장소의 에이전트 하네스 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 31개 · 절 9 · 규약 줄 44 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/AGENTS/` 의 절 항목을 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/AGENTS/` 의 절 항목과 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 해시값은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

## 목차

- [황금률](#황금률)
- [에이전트 역할](#에이전트-역할)
- [작업](#작업)
- [소통 규칙 (문서 우선)](#소통-규칙-문서-우선)
- [언어 정책](#언어-정책)
- [셀프체크](#셀프체크)
- [입력 파일](#입력-파일)

<!-- 인용 시작: 단위 지식에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

이 저장소가 무엇을 만드는지는 [`README.md`](README.md)에, 목적은
[`docs/purpose.md`](docs/purpose.md)에 있다. 이 문서는 **에이전트가 이 저장소에서 일하는 규칙**을
정하고, 그 규칙은 역할과 권한, 소통, 커밋을 다룬다. 지식을 어떻게 만드는지는
[`docs/method.md`](docs/method.md), 무엇이 유효한 구조인지는 [`docs/rules.md`](docs/rules.md),
저작 스타일은 [`STYLEGUIDE.md`](STYLEGUIDE.md)에 있다. STYLEGUIDE.md는 생성 파일이고, 원본은 결정의 규약 항목과
`kb/dev/norm/STYLEGUIDE/`의 절 항목이다([`p12-norm-documents-from-section-chunks`](kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md)).

## 황금률

1. **지식 파일을 고치면 `bazel test //...` 를 돌린다** ([`p6-self-check-before-completion`](kb/dev/decision/p6-self-check-before-completion/conclusion.md), [`p6-weakening-a-check-needs-user-approval`](kb/dev/decision/p6-weakening-a-check-needs-user-approval/conclusion.md)). 실패하면 shape와 게이트 코드를 약화하지 않고 고친 파일을 수정한다.
1. **어휘 밖에서 쓰지 않는다** ([`p2-ontology-as-vocabulary`](kb/dev/decision/p2-ontology-as-vocabulary/conclusion.md), [`p2-ontology-file-is-a-chunk`](kb/dev/decision/p2-ontology-file-is-a-chunk/conclusion.md)). 데이터의 술어는 `agt:` 온톨로지 또는 등록된 표준 어휘여야 하므로, 새 개념이 필요하면 온톨로지 모듈에 파일을 먼저 추가한다. 게이트가 한/영 라벨과 `skos:definition`을 강제한다([`docs/ontology.md`](docs/ontology.md)).
1. **ODD가 상위다** ([`p0-odd-scope-assumption`](kb/dev/decision/p0-odd-scope-assumption/conclusion.md), [`pe-odd-is-openodd`](kb/dev/decision/pe-odd-is-openodd/conclusion.md)). 적용 범위와 가정은 `kb/odd/project-odd.yml`의 조건만 참조할 수 있다. 이 파일은 OpenODD 형식이고 TTL은 생성물이다. 없는 조건이 필요하면 ODD를 먼저 확장하며, 확장한 조건에는 판정 방법과 등급이 반드시 있어야 한다.
1. **[지킴]** **한 단위 지식은 한 파일이고, 한 파일은 한 주제다** ([`p4-one-file-one-topic`](kb/dev/decision/p4-one-file-one-topic/conclusion.md)). 지식과 온톨로지, shape 전부가 대상이다. 라벨 하나로 요약되지 않으면 두 주제이므로 분할한다.
   1. **[지킴]** **본문은 토큰 상한 이하다** ([`p1-chunk-unit-is-tokens`](kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md)). 상한은 저작 산문이 42의 26배인 1,092, `artifact`와 `memory`의 인용이 42의 68배인 2,856이고, 계수기는 고정된 `o200k_base`다(2026-10-01, 그 전에는 42줄). 단위는 컴포넌트별 절이 정의한다.
1. **[지킴]** **지식의 종류는 고유 용어로 부른다** ([`p0-terms-from-glossary`](kb/dev/decision/p0-terms-from-glossary/conclusion.md)). 고유 용어는 조건과 개념, 변수, 후보, 결정, 가정, 시그니처, 함수, 주석, 관측이다. "결정 단위 지식"이 아니라 "결정"이라 부르고, "단위 지식"은 그 항목이 따르는 구조 규칙을 말할 때만 쓴다. 온톨로지 클래스 이름과 그래프 라벨의 인용은 예외다.
1. **생성 산출물을 손으로 고치지 않는다** ([`pe-kg-hand-and-generated-files`](kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md), [`pe-generated-outputs-stay-in-bazel-out`](kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md)). head 그래프인 `//kg:chunks_kg`는 frontmatter에서 생성되므로 고칠 것은 원본 파일이다.
1. **문서와 그래프는 일치해야 한다** ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md)). 아래 역할 표의 형식 원본이 `kg/catalog-kg.ttl`이므로 역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.
1. **유저와의 상세 소통은 hci만 한다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). orchestrator는 유저 판단이 필요하거나 문제·특이사항이 생기면 직접 묻지 않고 에이전트 채널에 `question` 등을 보낸다. hci는 유저 결정을 유저 채널의 **파일 질문지**로 받는다. 프로토콜 원본은 [`harness/README.md`](harness/README.md)다.

## 에이전트 역할

에이전트 역할의 형식 원본은 `id:h-akb`를 담은 `kg/catalog-kg.ttl`이고, 그 파일에 역할 다섯과 각 역할의
적용 범위인 `id:scope-*`가 있다.

- 각 역할은 자기 쓰기 지식 종류 밖을 수정하지 않는다 ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p0-odd-scope-assumption`](kb/dev/decision/p0-odd-scope-assumption/conclusion.md)).
- 설계와 구현, 운영 역할은 같은 지식 종류의 쓰기 권한(write)을 공유하지 않는다 ([`p11-dev-profile-role-permissions`](kb/dev/decision/p11-dev-profile-role-permissions/conclusion.md), [`p11-input-validation-shapes`](kb/dev/decision/p11-input-validation-shapes/conclusion.md)).
- **지식 베이스 밖의 대상은 interpreter를 거쳐 지식 베이스와 소통한다** ([`p11-interpreter-generalizes-hci`](kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md)). interpreter는 세션 하나로 외부 대상 셋을 맡고 대상은 메시지의 `origin`으로 가르며, 유저 대상 몫은 하위 역할 hci가 같은 세션에서 맡는다.
- 세션으로 도는 두 역할은 지침 파일을 갖고 스크립트로 띄운다(`harness/agents/interpreter.md`·`harness/agents/orchestrator.md`, `harness/scripts/run-interpreter.sh`·`harness/scripts/run-orchestrator.sh`) ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)).
- 스크립트 없이 띄운 세션은 orchestrator다 ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)).
- developer·vnv는 dispatch 시 역할 표와 적용 범위로 브리핑한다 ([`p11-execution-mode-and-workset`](kb/dev/decision/p11-execution-mode-and-workset/conclusion.md), [`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)).

원본: [`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md) · [`p12-norm-sections-written-by-orchestrator`](kb/dev/decision/p12-norm-sections-written-by-orchestrator/conclusion.md) · [`p8-vv-independence-scope`](kb/dev/decision/p8-vv-independence-scope/conclusion.md) · [`p8-vv-roles`](kb/dev/decision/p8-vv-roles/conclusion.md) · [`p11-interpreter-generalizes-hci`](kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md) · [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md).

| 역할 | 책임 | write | read | 구동 | git |
|---|---|---|---|---|---|
| **orchestrator** (메인) | 계획, dispatch, 통합과 요구·결정 저작을 맡고, 요구는 유저 관심사의 EARS 저작이며 `stable` 전이는 유저가 승인한다. 구현하지 않고 유저와 직접 대화하지 않으며 채널로 interpreter와 소통한다 | `requirement`, `decision`, 세션·판정 관측인 `memory`, 규범 문서의 절인 `norm`(memory는 2026-09-14, norm은 2026-10-04와 Q21-a) | 전 지식 종류 | 세션 유지 | ✗ |
| **developer** (dispatch) | 분배된 산출물인 코드와 설정, 온톨로지 개념을 저작하고, 노트 11.2절 9역할 중 T-Box·ODD 편집인 design을 겸한다(유저 결정 C4) | `artifact`, 개발 KB의 시그니처인 `contract`와 T-Box·ODD(Q79-a) | `contract`·`schema`·`decision`. **`kb/vv/`는 읽기 전용** | dispatch | ✗ |
| **vnv** (dispatch) | `bazel test //...` PASS 확인과 결과 주석만 맡는다. **V&V KB인 `kb/vv/`의 유일한 편집 주체**여서 `verifies`의 주어는 V&V 단위 지식뿐이다. 노트 8.20절의 V&V 하위 역할 다섯을 다른 세션에서 겸한다 | `kb/vv/`의 전 지식 종류(`agt:writesIn "kb/vv"`, 판정 주석도 V&V KB의 `annotation`, 2026-09-19) | `requirement`·`artifact`·`decision` | dispatch | ✗ |
| **interpreter** (별도 세션) | **외부 대상과 orchestrator 사이 소통의 창구다.** 외부 대상 셋(Q-0063#Q157)을 세션 하나로 맡고, 공통 몫은 요청의 해석과 저장소 조회로 직접 답하기, 지시 작성, 되묻기 중계, 결과 검증이다 | — (에이전트 채널 발신) | 전 지식 종류·저장소 전체 | 세션 유지 | 하위 역할 hci가 한다 |
| **hci** (interpreter의 하위 역할) | **interpreter의 유저 대상 하위 역할이고 유저 소통의 유일한 창구다.** 유저의 의도와 결정을 질문지로 받아 정제해 orchestrator에 넘기고 질문과 결과를 유저에게 되돌린다. 유저 전용 몫인 질문지와, 유저 요청 시 add/commit/push를 하는 **git 관리**를 맡는다 | — (유저 채널과 자기 역할 메모리) | `requirement`·전 지식 종류·저장소 전체 | interpreter 세션 | ✓ |

- dispatch는 **opus 또는 sonnet 모델**로 하며, 설계 판단과 새 구조는 opus가, 규약이 정해진 기계적 반영은 sonnet이 맡는다(유저 지시 2026-09-26·2026-10-03) ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)).
- dispatch 대상에게는 전체 컨텍스트가 아니라 **작업 집합**만 전달한다 ([`p11-execution-mode-and-workset`](kb/dev/decision/p11-execution-mode-and-workset/conclusion.md), [`p0-workset-anchor-neighbourhood`](kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)). 작업 집합은 적용 범위와 정제 수준 창으로 거른 지식 집합이다([`docs/method.md` §8](docs/method.md#8-조회)). 그래서 저장소를 통째로 컨텍스트에 싣지 않는다.
- **채널 쓰기 경계** — 채널은 둘이다 ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 유저 채널에는 hci가 질문지를 쓰고 유저가 답을 적으며, 에이전트 채널은 **단일 작성자**다. `to_orchestrator/`에는 interpreter(하위 역할 hci 포함)만, `to_interpreter/`에는 orchestrator만 `harness/scripts/send.sh`로 쓰고, 상태 전이와 보관은 수신자가 `harness/scripts/mark.sh`로 한다. interpreter 세션은 이 채널 몫과 유저 채널, 자기 역할 메모리만 쓰고 저장소 전체를 조회한다. developer·vnv는 채널에 쓰지 않고, 그 질문과 결과는 hand-back으로 orchestrator가 받아 채널에 올린다.
- **[지킴]** **외부 대상의 쓰기는 후보 제안까지다** ([`p11-interpreter-generalizes-hci`](kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md)). 외부 대상은 저장소 파일을 쓰지 않고, interpreter가 그 쓰기 요청을 후보 제안으로 정제해 orchestrator에 넘긴다.
- 외부에서 온 후보는 유저가 미리 정한 범위 안에서 orchestrator가 확정하고 결과를 유저에게 보고한다 ([`p11-interpreter-generalizes-hci`](kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md)). interpreter는 확정하지 않으며, 위임 범위는 뒤 단계의 결정이 정한다.
- 역할별 `agt:maxConcurrent`의 합은 ODD 동적 요소 `id:cond-concurrent-agents` 안이어야 하고, 그 한도는 현재 5 이하다 ([`p11-input-validation-shapes`](kb/dev/decision/p11-input-validation-shapes/conclusion.md)). 따라서 역할을 추가하면 ODD 한도도 함께 검토한다. **이 검사는 `//kg:gate_test`의 `catalog`가 한다**(2026-09-13, [`docs/tools.md` §게이트 밖](docs/tools.md#게이트-밖--규약으로-남은-것)).
- 커밋 전 `bazel test //...` PASS를 확인한다 ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). 커밋은 유저가 하거나, 유저가 요청하면 hci가 한다.
- **[지킴]** `harness/scripts/watch.sh <역할>`로 하는 수신 감시는 도구의 백그라운드 실행으로 하나만 띄운다 ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)). 메시지를 처리한 턴의 끝마다 감시가 살아 있는지 확인해 없으면 다시 걸고, 감시가 0이 아닌 코드로 끝나면 수신함을 한 번 직접 읽은 뒤 다시 건다. 역할 세션은 백그라운드 셸 회수를 끈 환경으로 띄운다(`harness/scripts/run-interpreter.sh`·`harness/scripts/run-orchestrator.sh`).

## 작업

지식을 만드는 절차는 프로파일 구축, ODD 작성, 단위 지식 저작, 정제 전이, 후보 관리, 연결, 갱신, 조회, 뷰,
일반화, 검증, 영향 분석이고, 전부 [`docs/method.md`](docs/method.md)에 있다. 하네스 쪽에서 추가로
지킬 것은 아래 둘뿐이다.

- **게이트 실패 대응** — FAIL 메시지의 인용이 수정 방향이다 ([`p6-gate-catalogue`](kb/dev/decision/p6-gate-catalogue/conclusion.md), [`p6-weakening-a-check-needs-user-approval`](kb/dev/decision/p6-weakening-a-check-needs-user-approval/conclusion.md)). 게이트가 틀렸다고 판단되면 게이트를 고치지 않고 채널에 `question`을 보낸다. shape 약화는 유저 승인 사항이다.

**유저 피드백 처리** — 파이프라인 원본은 [`harness/README.md`](harness/README.md)다.

1. 유저가 hci 세션에서 조사나 구체화, 제안을 요청한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). orchestrator의 `question`도 interpreter 수신함으로 들어온다.
1. hci가 검토·구체화하고 조사도 직접 한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). 유저 결정이 필요한 지점은 유저 채널의 **질문지** `Q-<번호>.md`로 묻는다.
1. 유저가 질문지에 답을 적고 `status: answered`로 태깅하면 반영이 허가된다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). hci 세션에서 답을 알리면 hci가 대신 태깅한다. hci는 그 답을 `task`·`answer`·`knowledge` 메시지로 정제해 orchestrator에 보낼 뿐 수행하지 않으며, `//harness:channel_lint_test`와 writer 검사가 이를 강제한다.
1. orchestrator가 담당 쓰기 지식 종류의 역할로 반영하고, `bazel test //...` 통과를 확인한 뒤 무엇을 어디에 썼는지 `result` 메시지로 돌려준다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p6-self-check-before-completion`](kb/dev/decision/p6-self-check-before-completion/conclusion.md)). 결론은 지식으로 남긴다.
1. hci가 유저에게 결과를 보고하고 질문지를 `closed`로 닫아 유저 채널의 `archive/`로 옮긴다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)).

## 소통 규칙 (문서 우선)

- **[지킴]** **유저에게 결정은 항상 파일 질문지로 요청한다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-session-output-goes-to-artifacts`](kb/dev/decision/p11-session-output-goes-to-artifacts/conclusion.md)). 채팅에는 질문지를 만들었다는 안내와 요지만 쓰고, 유저가 채팅으로 먼저 답하면 hci가 그 답을 질문지에 원문으로 옮겨 적는다.
- 상태와 결정, 주석은 해당 산출물에 써서 결정은 `decision`에, 주석은 `annotation`에 둔다 ([`p11-session-output-goes-to-artifacts`](kb/dev/decision/p11-session-output-goes-to-artifacts/conclusion.md)). 세션에는 무엇을 어디에 썼는지 요점만 남기고, 임시 파일은 스크래치패드에 둔다.
- 채널 파일은 그래프 밖이고 지식 파일의 게이트 입력 규약에서 제외되는 유일한 문서군이다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)). 어휘·shape 검사 대상이 아니고, 그 형식은 게이트 `channel`이 따로 강제한다.
- **메시지는 흐르고 지식 베이스는 남는다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 소통의 결론은 채널이 아니라 온톨로지와 ODD, 지식으로 승격한다. 하네스의 `KNOWLEDGE.md`에 쌓일 지식을 이 저장소는 지식 베이스에 남긴다([`harness/README.md` §지식 축적](harness/README.md#지식-축적)).
- **[지킴]** 유저 판단을 요청하는 질문은 **다섯 가지**를 갖춘다 ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 다섯 가지는 왜 어려운가를 포함한 질문과 이미 정해진 것, 측정치인 현재 상태, 답이 가르는 것, 선택지다. 한 줄 질문은 답을 받지 못한다. 선택지마다 비용을 적고 `**권장:**`으로 권장안을 붙인다(유저 지적 2026-09-02).
- **[지킴]** 유저에게 묻는 것은 확정 권한과 방향, 비용이 큰 선택, 새 파일, 검사의 약화로 좁히고, 구현 선택은 orchestrator가 정해 `result`에 적는다 ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 선택지마다 끝에 "권한·방향: 바꾼다" 또는 "권한·방향: 그대로"를 적는다(Q-0060#Q140).
- **[지킴]** 새 파일 질문의 예외는 판정 기록 하나다 ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 링크 후보 뷰에 새로 든 판정 없는 후보는 묻지 않고 판정해 판정 로그와 결과 주석을 기록한다. 한 번에 새 기록이 50개를 넘으면 판정 전에 묻고, 기록 수와 판정 결과는 매번 `result`로 알린다(Q-0074#Q170).

## 언어 정책

- 산문은 한글, 식별자는 영어 소문자 케밥, 개념은 `agt:Assumption` 같은 PascalCase이고, 라벨은 한/영 1:1이다 ([`p0-notation-format`](kb/dev/decision/p0-notation-format/conclusion.md)).
- **지어낸 용어를 쓰지 않는다** ([`p0-no-invented-terms`](kb/dev/decision/p0-no-invented-terms/conclusion.md)). 확립된 표준어가 있으면 그 표준어를 쓴다.
- **[지킴]** **산문은 학술 산문체의 단정 서술형이다**(유저 결정 2026-09-13) ([`p0-prose-assertive-register`](kb/dev/decision/p0-prose-assertive-register/conclusion.md)). 대상은 문서와 단위 지식의 본문, 채널 메시지, 질문지, 세션 보고, dispatch 브리핑 전부다. 문장은 평서형 종결 "…다"로 끝난다. 경어체와 감탄, 구어, 추측 표현을 쓰지 않는다. 경어체는 "습니다·세요·해요", 구어는 "근데·그냥·좀", 추측 표현은 "것 같다·듯하다·수도 있다" 같은 말이다. 의문문은 질문을 다루는 절에만 둔다. 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다. 경어와 감탄은 게이트 `prose`가 거부하며, 그 판정은 `chunk_lint`와 `doccheck`가 함께 쓴다. 추측과 구어, 대시 밀도는 `consistency` ⑦이 보고한다.

## 셀프체크

작업을 마치기 전에 아래 명령을 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화
python3 tools/gen_build.py --root .        # frontmatter 링크를 고쳤으면 BUILD 재생성 (//:build_drift_test)
python3 tools/gen_skills.py --root .       # 도구 docstring·kb_lib.SKILLS 를 고쳤으면 skill 재생성 (//:skills_drift_test)
bazel run //tools:extract -- <소스>       # 소스를 고쳤으면 코드 청크 재추출 (//:extract_drift_test)
```

<!-- 인용 끝 -->

## 입력 파일

원본 파일 31개다. 디렉토리로 묶었고 빠진 파일은 없다.

- `kb/dev/decision/p0-no-invented-terms/` — `conventions.md`
- `kb/dev/decision/p0-notation-format/` — `conventions.md`
- `kb/dev/decision/p0-odd-scope-assumption/` — `conventions.md`
- `kb/dev/decision/p0-prose-assertive-register/` — `conventions.md`
- `kb/dev/decision/p0-terms-from-glossary/` — `conventions.md`
- `kb/dev/decision/p1-chunk-unit-is-tokens/` — `conventions.md`
- `kb/dev/decision/p11-dev-profile-role-permissions/` — `conventions.md`
- `kb/dev/decision/p11-execution-mode-and-workset/` — `conventions.md`
- `kb/dev/decision/p11-harness-two-channels/` — `conventions.md`
- `kb/dev/decision/p11-input-validation-shapes/` — `conventions.md`
- `kb/dev/decision/p11-interpreter-generalizes-hci/` — `conventions.md`
- `kb/dev/decision/p11-role-sessions-and-dispatch-models/` — `conventions.md`
- `kb/dev/decision/p11-session-output-goes-to-artifacts/` — `conventions.md`
- `kb/dev/decision/p11-user-question-has-five-parts/` — `conventions.md`
- `kb/dev/decision/p2-ontology-as-vocabulary/` — `conventions.md`
- `kb/dev/decision/p4-one-file-one-topic/` — `conventions.md`
- `kb/dev/decision/p6-gate-catalogue/` — `conventions.md`
- `kb/dev/decision/p6-self-check-before-completion/` — `conventions.md`
- `kb/dev/decision/p7-dev-roles-and-scopes/` — `conventions.md`
- `kb/dev/decision/pe-kg-hand-and-generated-files/` — `conventions.md`
- `kb/dev/decision/pe-knowledge-files-are-gate-inputs/` — `conventions.md`
- `kb/dev/norm/AGENTS/` — `communication.md` · `golden.md` · `head.md` · `language.md` · `roles-dispatch.md` · `roles-table.md` · `roles.md` · `self-check.md` · `work-feedback.md` · `work.md`

