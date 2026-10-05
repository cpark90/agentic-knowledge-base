# AGENTS.md — 이 저장소의 에이전트 하네스 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 30개 · 절 9 · 규약 줄 38 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/AGENTS/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/AGENTS/` 의 절 청크와 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

## 목차

- [황금률](#황금률)
- [에이전트 역할](#에이전트-역할)
- [작업](#작업)
- [소통 규칙 (문서 우선)](#소통-규칙-문서-우선)
- [언어 정책](#언어-정책)
- [셀프체크](#셀프체크)
- [입력 파일](#입력-파일)

<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

이 저장소가 무엇을 만드는지는 [`README.md`](README.md)에, 목적은
[`docs/purpose.md`](docs/purpose.md)에 있다. 여기는 **에이전트가 이 저장소에서 일하는 규칙**을
정한다. 그 규칙은 역할·권한·소통·커밋을 다룬다. 지식을 어떻게 만드는지는
[`docs/method.md`](docs/method.md), 무엇이 유효한 구조인지는 [`docs/rules.md`](docs/rules.md),
저작 스타일은 [`STYLEGUIDE.md`](STYLEGUIDE.md)에 있다. 그 문서는 생성 파일이고 원본은 결정의 규약 청크와
`kb/dev/norm/STYLEGUIDE/`의 절 청크다([`p12-norm-documents-from-section-chunks`](kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md)).

## 황금률

1. **지식 파일을 고치면 `bazel test //...` 를 돌린다** ([`p6-self-check-before-completion`](kb/dev/decision/p6-self-check-before-completion/conclusion.md), [`p6-weakening-a-check-needs-user-approval`](kb/dev/decision/p6-weakening-a-check-needs-user-approval/conclusion.md)). 실패하면 고친 파일을 수정한다. shape·게이트 코드를 약화시키지 않는다.
1. **어휘 밖에서 쓰지 않는다** ([`p2-ontology-as-vocabulary`](kb/dev/decision/p2-ontology-as-vocabulary/conclusion.md), [`p2-ontology-file-is-a-chunk`](kb/dev/decision/p2-ontology-file-is-a-chunk/conclusion.md)). 데이터의 술어는 `agt:` 온톨로지 또는 등록된 표준 어휘여야 한다. 새 개념이 필요하면 온톨로지 모듈에 파일을 먼저 추가한다. 게이트가 한/영 라벨과 `skos:definition`을 강제한다([`docs/ontology.md`](docs/ontology.md)).
1. **ODD가 상위다** ([`p0-odd-scope-assumption`](kb/dev/decision/p0-odd-scope-assumption/conclusion.md), [`pe-odd-is-openodd`](kb/dev/decision/pe-odd-is-openodd/conclusion.md)). 스코프·가정은 `kb/odd/project-odd.yml`의 조건만 참조할 수 있다. 이 문서는 OpenODD이고 TTL은 생성물이다. 없는 조건이 필요하면 ODD를 먼저 확장한다. 판정 방법과 등급이 필수다.
1. **[지킴]** **한 청크는 한 파일, 한 파일은 한 주제다** ([`p4-one-file-one-topic`](kb/dev/decision/p4-one-file-one-topic/conclusion.md)). 지식·온톨로지·shape 전부가 대상이다. 라벨 하나로 요약되지 않으면 두 주제다. 그때는 분할한다.
   1. **[지킴]** **본문은 토큰 상한 이하다** — 저작 산문 1,092(42×26), 인용(`artifact`·`memory`) 2,856(42×68); 계수기는 고정된 `o200k_base`다(2026-10-01 — 그 전에는 42줄) ([`p1-chunk-unit-is-tokens`](kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md)). 단위는 컴포넌트별 절이 정의한다.
1. **[지킴]** **지식의 종류는 고유 용어로 부른다** ([`p0-terms-from-glossary`](kb/dev/decision/p0-terms-from-glossary/conclusion.md)). 고유 용어는 조건·개념·변수·후보·결정·가정·시그니처·함수·주석·관측이다. "결정 청크"가 아니라 "결정"이다. "청크"는 그 항목이 따르는 구조 규칙을 말할 때만 쓴다. 온톨로지 클래스 이름·그래프 라벨 인용은 예외다.
1. **생성 산출물을 손으로 고치지 않는다** ([`pe-kg-hand-and-generated-files`](kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md), [`pe-generated-outputs-stay-in-bazel-out`](kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md)). head 그래프(`//kg:chunks_kg`)는 frontmatter에서 생성된다. 고칠 것은 원본 파일이다.
1. **문서와 그래프는 일치해야 한다** ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md)). 아래 역할 표의 형식 원본은 `kg/catalog-kg.ttl`이다. 역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.
1. **유저와의 상세 소통은 hci만 한다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). orchestrator는 유저 판단이 필요하거나 문제·특이사항이 생기면 에이전트 채널에 `question` 등의 메시지를 보낸다. 유저에게 직접 묻지 않는다. hci는 유저의 결정을 유저 채널의 **파일 질문지**로 받는다. 프로토콜 원본은 [`harness/README.md`](harness/README.md)다.

## 에이전트 역할

형식 원본은 `kg/catalog-kg.ttl`(`id:h-akb`)이다. 역할 4개와 각각의 스코프(`id:scope-*`)가
거기 있다.

- 각 역할은 자기 write plane 밖을 수정하지 않는다 ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p0-odd-scope-assumption`](kb/dev/decision/p0-odd-scope-assumption/conclusion.md)).
- 설계·구현·운영 역할은 같은 write plane을 공유하지 않는다 ([`p11-dev-profile-role-permissions`](kb/dev/decision/p11-dev-profile-role-permissions/conclusion.md), [`p11-input-validation-shapes`](kb/dev/decision/p11-input-validation-shapes/conclusion.md)).
- 세션으로 도는 두 역할은 지침 파일을 갖고 스크립트로 띄운다(`harness/agents/hci.md`·`harness/agents/orchestrator.md`, `harness/scripts/run-hci.sh`·`harness/scripts/run-orchestrator.sh`) ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)).
- 스크립트 없이 띄운 세션은 orchestrator다 ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)).
- developer·vnv는 dispatch 시 역할 표와 스코프로 브리핑한다 ([`p11-execution-mode-and-workset`](kb/dev/decision/p11-execution-mode-and-workset/conclusion.md), [`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)).

원본: [`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md) · [`p12-norm-sections-written-by-orchestrator`](kb/dev/decision/p12-norm-sections-written-by-orchestrator/conclusion.md) · [`p8-vv-independence-scope`](kb/dev/decision/p8-vv-independence-scope/conclusion.md) · [`p8-vv-roles`](kb/dev/decision/p8-vv-roles/conclusion.md) · [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md).

| 역할 | 책임 | write | read | 구동 | git |
|---|---|---|---|---|---|
| **orchestrator** (=메인) | 계획·dispatch·통합. 요구(유저 관심사의 EARS 저작 — stable 전이는 유저 승인)·결정 저작. 직접 구현하지 않는다. 유저와 직접 대화하지 않고 채널로 hci와 소통한다 | `requirement` · `decision` · `memory`(세션·판정 관측, 2026-09-14) · `norm`(규범 문서의 절 청크, 2026-10-04, Q21-a) | 전 plane | 세션 유지 | ✗ |
| **developer** (dispatch) | 분배된 산출물(코드·설정·온톨로지 개념) 저작. 노트 10.2절 9역할 중 design(T-Box·ODD 편집)을 겸한다 — 유저 결정 C4 | `artifact` (+T-Box·ODD) | `contract`·`schema`·`decision`. **`kb/vv/`는 읽기 전용** | dispatch | ✗ |
| **vnv** (dispatch) | 판정 전용: `bazel test //...` PASS 확인 + 결과 주석. **V&V KB(`kb/vv/`)의 유일한 편집 주체** — `verifies`의 주어는 V&V 청크뿐. 노트 8.20절의 다섯 V&V 하위 역할(engineer·검증기 저자·executor·judge·audit)을 겸하되 다른 세션에서 한다 | `kb/vv/`의 전 plane(`agt:writesIn "kb/vv"`, 2026-09-19 — 판정 주석도 V&V KB 안의 annotation plane) | `requirement`·`artifact`·`decision` | dispatch | ✗ |
| **hci** (별도 세션) | **유저 소통 전담 — 유일한 유저 창구.** 유저의 의도·결정을 질문지(유저 채널)로 받아 지시·지식으로 정제해 orchestrator에 넘기고, 질문과 결과를 유저에게 되돌린다. **조사와 git 관리**(add/commit/push, 유저 요청 시)를 맡는다 — 옛 inspection 역할을 2026-09-13에 이관 | — (채널만) | `requirement`·전 plane + 저장소 전체 | 세션 유지 | ✓ |

- dispatch는 **opus 또는 sonnet 모델**로 한다(유저 지시 2026-09-26·2026-10-03) ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)). 설계 판단과 새 구조는 opus, 규약이 정해진 기계적 반영은 sonnet이다.
- dispatch 대상에게는 전체 컨텍스트가 아니라 **작업 집합**만 전달한다 ([`p11-execution-mode-and-workset`](kb/dev/decision/p11-execution-mode-and-workset/conclusion.md), [`p0-workset-anchor-neighbourhood`](kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)). 작업 집합은 스코프 × level 창으로 거른 청크 집합이다([`docs/method.md` §8](docs/method.md#8-조회)). 저장소를 통째로 컨텍스트에 싣지 않는다.
- **채널 쓰기 경계** ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 채널은 둘이다. 유저 채널은 hci가 질문지를 쓰고 유저가 답을 적는다. 에이전트 채널은 **단일 작성자**다. `to_orchestrator/`에는 hci만, `to_hci/`에는 orchestrator만 쓰고(`harness/scripts/send.sh`), 상태 전이와 보관은 수신자가 한다(`harness/scripts/mark.sh`). hci의 작성·수정 범위는 이 채널 몫과 자기 역할 메모리(`.claude/agent-memory/hci/`)뿐이고 조회 범위는 저장소 전체다. developer·vnv는 채널에 쓰지 않는다. 그들의 질문과 결과는 hand-back으로 orchestrator에 돌아가고 orchestrator가 채널에 올린다(2026-10-03).
- 역할별 `agt:maxConcurrent`의 합은 ODD 동적 요소(`id:cond-concurrent-agents`) 안이어야 한다 ([`p11-input-validation-shapes`](kb/dev/decision/p11-input-validation-shapes/conclusion.md)). 그 한도는 현재 5 이하다. 역할을 추가하면 ODD 한도도 함께 검토한다. **이 검사는 `//kg:gate_test`의 `catalog`가 한다**(2026-09-13) ([`docs/tools.md` §게이트 밖](docs/tools.md#게이트-밖--규약으로-남은-것)).
- 커밋 전 `bazel test //...` PASS를 확인한다 ([`p7-dev-roles-and-scopes`](kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). 커밋은 hci(유저 요청 시) 또는 유저가 한다.
- **[지킴]** 수신 감시(`harness/scripts/watch.sh <역할>`)는 도구의 백그라운드 실행으로 하나만 띄운다 ([`p11-role-sessions-and-dispatch-models`](kb/dev/decision/p11-role-sessions-and-dispatch-models/conclusion.md)). 메시지를 처리한 턴의 끝마다 감시가 살아 있는지 확인하고 없으면 다시 건다. 감시가 0이 아닌 코드로 끝나면 수신함을 한 번 직접 읽은 뒤 다시 건다. 역할 세션은 백그라운드 셸 회수를 끈 환경으로 띄운다(`harness/scripts/run-hci.sh`·`harness/scripts/run-orchestrator.sh`).

## 작업

지식을 만드는 절차는 전부 [`docs/method.md`](docs/method.md)에 있다. 그 절차는 프로파일
구축, ODD 작성, 청크 저작, 정제 전이, 후보 관리, 연결, 갱신, 조회, 뷰, 일반화, 검증, 영향
분석이다. 하네스 쪽에서 추가로 지켜야 할 것은 아래 둘뿐이다.

- **게이트 실패 대응** ([`p6-gate-catalogue`](kb/dev/decision/p6-gate-catalogue/conclusion.md), [`p6-weakening-a-check-needs-user-approval`](kb/dev/decision/p6-weakening-a-check-needs-user-approval/conclusion.md)). FAIL 메시지의 인용이 수정 방향이다. 게이트가 틀렸다고 판단되면 게이트를 고치지 말고 채널에 `question`을 보낸다. shape 약화는 유저 승인 사항이다.

**유저 피드백 처리.** 파이프라인 원본은 [`harness/README.md`](harness/README.md)다.

1. 유저가 hci 세션에서 말한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). 요청은 조사·구체화·제안이다. orchestrator의 `question`도 hci의 수신함으로 들어온다.
1. hci가 검토·구체화한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-hci-investigates-and-commits`](kb/dev/decision/p11-hci-investigates-and-commits/conclusion.md)). 조사는 직접 한다. 유저의 결정이 필요한 지점은 **질문지**(유저 채널의 `Q-<번호>.md`)로 묻는다.
1. 유저가 질문지에 답을 적고 `status: answered`로 태깅한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 이것이 반영 허가 신호다. 유저가 답을 적고 hci 세션에서 알리면 hci가 대신 태깅한다. hci는 그 답을 `task`·`answer`·`knowledge` 메시지로 정제해 orchestrator에 보낸다. hci는 수행하지 않는다. 이를 `//harness:channel_lint_test`·writer 검사가 강제한다.
1. orchestrator가 담당 write plane의 역할을 통해 반영한다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p6-self-check-before-completion`](kb/dev/decision/p6-self-check-before-completion/conclusion.md)). 반영 후 `bazel test //...` PASS를 확인하고 `result` 메시지로 무엇을 어디에 썼는지 돌려준다. 결론은 지식으로 남긴다.
1. hci가 유저에게 결과를 보고하고 질문지를 `closed`로 닫아 유저 채널의 `archive/`로 옮긴다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)).

## 소통 규칙 (문서 우선)

- **[지킴]** **유저에게 결정을 요청할 때는 항상 파일 질문지로 한다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md), [`p11-session-output-goes-to-artifacts`](kb/dev/decision/p11-session-output-goes-to-artifacts/conclusion.md)). 채팅에는 질문지를 만들었다는 안내와 요지만 쓴다. 유저가 채팅으로 먼저 답하면 hci가 그 답을 질문지에 원문으로 옮겨 적는다.
- 상태·결정·주석은 해당 산출물에 쓴다 ([`p11-session-output-goes-to-artifacts`](kb/dev/decision/p11-session-output-goes-to-artifacts/conclusion.md)). 결정은 `decision`에, 주석은 `annotation`에 쓴다. 세션에는 무엇을 어디에 썼는지 요점만 남긴다. 임시 파일은 스크래치패드에 둔다.
- 채널 파일은 그래프 밖이고 지식 파일의 게이트 입력 규약에서 제외되는 유일한 문서군이다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)). 어휘·shape 검사 대상이 아니고, 그 형식은 게이트 `channel`이 따로 강제한다.
- **메시지는 흐르고 지식 베이스는 남는다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 소통의 결론은 채널에 남기지 않고 온톨로지·ODD·청크의 지식으로 승격한다. 한 프로젝트의 에이전트들이 하네스의 `KNOWLEDGE.md`에 누적하는 것이 이 저장소에서는 지식 베이스에 남는다([`harness/README.md` §지식 축적](harness/README.md#지식-축적)).
- **[지킴]** 유저 판단을 요청하는 질문은 **다섯 가지**를 갖춘다(유저 지적 2026-09-02) ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 다섯 가지는 질문(왜 어려운가 포함) / 이미 정해진 것 / 현재 상태(실측) / 답이 가르는 것 / 선택지다. 한 줄 질문은 답을 받지 못한다. 선택지마다 비용을 적고 `**권장:**`으로 권장안을 붙인다.

## 언어 정책

- 산문은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase(`agt:Assumption`), 라벨은 한/영 1:1이다 ([`p0-notation-format`](kb/dev/decision/p0-notation-format/conclusion.md)).
- **지어낸 용어를 쓰지 않는다** ([`p0-no-invented-terms`](kb/dev/decision/p0-no-invented-terms/conclusion.md)). 확립된 표준어가 있으면 그것을 쓴다.
- **[지킴]** **산문은 학술 산문체의 단정 서술형이다**(유저 결정 2026-09-13) ([`p0-prose-assertive-register`](kb/dev/decision/p0-prose-assertive-register/conclusion.md)). 대상은 문서·청크 본문·채널 메시지·질문지·세션 보고·dispatch 브리핑 전부다. 문장은 평서형 종결 "…다"로 끝난다. 경어체("습니다·세요·해요"), 감탄, 구어("근데·그냥·좀"), 추측 표현("것 같다·듯하다·수도 있다")을 쓰지 않는다. 의문문은 질문을 다루는 절에만 둔다. 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다. 경어·감탄은 게이트 `prose`(`chunk_lint`·`doccheck`)가 거부한다. 추측·구어·대시 밀도는 `consistency` ⑦이 보고한다.

## 셀프체크

작업 완료 전 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화
python3 tools/gen_build.py --root .        # frontmatter 링크를 고쳤으면 BUILD 재생성 (//:build_drift_test)
python3 tools/gen_skills.py --root .       # 도구 docstring·kb_lib.SKILLS 를 고쳤으면 skill 재생성 (//:skills_drift_test)
bazel run //tools:extract -- <소스>       # 소스를 고쳤으면 코드 청크 재추출 (//:extract_drift_test)
```

<!-- 인용 끝 -->

## 입력 파일

원본 파일 30개다. 디렉토리로 묶었고 빠진 파일은 없다.

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

