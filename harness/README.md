# harness — interpreter · orchestrator 두 세션 프로토콜

이 디렉토리는 이 저장소에서 일하는 에이전트의 **운영 틀**이고, 이 문서는 그 **소통 프로토콜의 원본**이다.
운영 틀 안에서는 독립된 Claude Code 세션 둘이 파일 채널로 협업한다. 프로토콜은 런타임과 채널, 메시지,
질문지, 스크립트를 다룬다. 황금률과 역할, 권한, 언어 같은 작업 규칙은 [`../AGENTS.md`](../AGENTS.md)에서 읽는다.
`AGENTS.md`는 생성 파일이고, 원본은 결정의 규약 항목과 `kb/dev/norm/`의 절 항목이다.

하네스의 파일은 지식 산출물이 아니라 운영 기록이므로 **그래프 밖**이다. 그래서 소통이 낳은 결론은
여기에 남기지 않고 지식 베이스로 승격한다. 승격의 자리는 [지식 축적](#지식-축적) 절이 정한다.

## 역할

| 에이전트 | 하는 일 | 유저와의 접점 |
|---|---|---|
| **interpreter** ([`agents/interpreter.md`](agents/interpreter.md)) | 외부 대상의 요청을 해석해 지시와 지식으로 정제해 orchestrator에 넘기고, orchestrator의 질문과 결과를 대상에게 되돌린다. 조사를 직접 한다 | 유저와는 하위 역할 hci로 만난다 |
| **hci** ([`agents/hci.md`](agents/hci.md)), interpreter의 유저 대상 하위 역할 | 유저와 대화해 의도와 도메인 지식, 결정을 끌어내고, 그것을 지시와 지식으로 정제해 orchestrator에 넘긴다. orchestrator의 질문과 결과를 유저에게 되돌린다. 유저 전용 몫인 질문지와 git 관리를 맡는다 | **있다** — 유일한 창구 |
| **orchestrator** ([`agents/orchestrator.md`](agents/orchestrator.md)) | interpreter가 넘긴 지시를 계획하고 수행한다. 요구와 결정을 저작하고, developer와 vnv를 dispatch해 결과를 통합한다. 막히면 질문을, 끝나면 결과를 interpreter에 올린다 | **없다** — 채널로만 소통한다 |
| developer · vnv | orchestrator가 dispatch한다. 세션을 유지하지 않으므로 수신함이 없다. 결과와 질문은 hand-back으로 orchestrator에 돌아가고, 유저에게 물을 것은 orchestrator가 채널에 올린다 | 없다 |

**interpreter**는 hci를 일반화한 역할이고, 지식 베이스 밖의 대상과 orchestrator 사이의 소통을 맡는다. 외부 대상은 셋이다.
유저와 지식 베이스를 쓰는 다른 프로젝트의 에이전트, 다음 프로젝트가 그 셋이다. 모든 대상에 공통인
interpreter의 몫은 요청의 해석과 저장소 조회로 직접 답하기, 지시 작성, 되묻기 중계, 결과 검증이다. 반면 질문지와 git 관리는
유저 대상 하위 역할인 hci의 몫이다. interpreter는 세션 하나이고, hci 하위 역할도 그 세션이 맡는다. 그 세션은
`run-interpreter.sh`로 띄우고 세션이 `agents/interpreter.md`를 읽으며, 그 지침이 유저 대상 몫인 `agents/hci.md`를 포함한다.
옛 기동 경로 `run-hci.sh`는 `run-interpreter.sh`를 그대로 불러 같은 세션을 띄운다. 이 문서에서 hci는 interpreter 세션의 유저 대상
몫을 가리킨다(결정 [`p11-interpreter-generalizes-hci`](../kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md)).

두 세션은 **서로를 직접 호출하지 않고**, 아래 채널 파일로만 소통한다. 역할별 쓰기 지식 종류와
권한은 `AGENTS.md`의 역할 표와 `kg/catalog-kg.ttl`이 정한다.

## 런타임

터미널 둘에서 각각 독립 세션으로 띄운다.

```
터미널 A:  ./harness/scripts/run-interpreter.sh    # 유저가 여기서 대화한다 (옛 이름 run-hci.sh 도 같은 세션을 띄운다)
터미널 B:  ./harness/scripts/run-orchestrator.sh   # 작업을 수행한다
```

각 세션은 `agents/` 아래의 자기 지침 파일을 읽는다. 그리고 이 문서의 프로토콜대로 채널을 감시하고, 메시지를 소비하고, 응답한다.

## 구조

```
harness/
├── README.md              # 이 문서 (프로토콜 원본)
├── agents/                # 역할 지침 — interpreter.md (유저 대상 몫 hci.md 를 포함한다) · orchestrator.md
├── channel/               # 에이전트 채널: interpreter ↔ orchestrator (런타임 산출물, git 밖)
│   ├── to_orchestrator/   #   interpreter → orchestrator (수신함: orchestrator)
│   ├── to_interpreter/    #   orchestrator → interpreter (수신함: interpreter)
│   └── archive/           #   처리가 끝난(done) 메시지 · legacy/ (옛 에이전트·인수인계 lane, git 추적)
├── user/                  # 유저 채널: 유저 ↔ hci 질문지 (git 추적)
│   ├── README.md          #   질문지 형식과 생애주기
│   ├── Q-<번호>.md        #   열린 질문지
│   └── archive/           #   닫힌 질문지 · legacy/ (옛 유저 lane·조사 lane)
└── scripts/               # 세션 부팅과 채널 조작
```

## 에이전트 채널 (`channel/`)

- **단일 작성자 규칙이 적용된다.** `to_orchestrator/`에는 interpreter(하위 역할 hci 포함)만 쓰고 `to_interpreter/`에는
  orchestrator만 쓴다. 읽기와 상태 전이, 보관은 **수신자**가 한다. 쓰기는 `scripts/send.sh`로만 한다.
- **역할 어휘는 `interpreter`와 `orchestrator`다.** `hci`는 interpreter의 옛 이름으로 계속 유효하다. 스크립트는 역할 인자
  `hci`를 `interpreter`로 읽어 같은 수신함과 같은 감시 PID 파일을 쓰고, `send.sh`는 `hci`를 받아 `interpreter`로 적는다.
  옛 메시지의 `from: hci`·`to: hci`는 고치지 않으며, 게이트는 `hci`와 `interpreter`를 같은 작성자로 본다.
- **메시지 id는 채널 전역에서 유일한 단조 증가 번호다.** 번호는 `channel/.seq`가 센다. 방향이 달라도 번호가
  겹치지 않으므로 id만으로 대화 순서가 복원된다.
- **채널 메시지는 런타임 산출물이므로 git이 추적하지 않는다.** 제외는 `.gitignore`가 정한다. 기록으로 남는 것은
  유저의 답을 담은 질문지와 승격된 결론을 담은 지식 베이스, 그리고 git 이력이다.

### 메시지 포맷

파일명은 `<id>.md`이고 id는 네 자리다(예: `0007.md`).

```markdown
---
id: 0007
from: interpreter      # interpreter | orchestrator (옛 메시지의 hci 는 interpreter 와 같다)
to: orchestrator       # orchestrator | interpreter
type: task             # task | question | answer | result | knowledge | status | ack
status: new            # new | read | in_progress | done | blocked
re: 0006               # (선택) 이 메시지가 답하는 메시지 id — answer·result 는 필수
source: Q-0003         # (선택) 근거가 된 질문지 id
subject: 한 줄 요약
created: 2026-10-03T14:03:00+09:00
---

본문은 마크다운이다. 지식은 식별자(결정 slug, `agt:` 어휘, `id:` 개체, IRI, 조건 id, `파일:줄`)로 가리킨다. 결정과 어휘, 개체의 식별자를 적은 줄에는 그 한글 이름을 그대로 함께 적는다. 이 규약과 경어 금지는 `//harness:channel_lint_test`가 판정한다. 이름 검사는 시행 시각(`channel_lint.NAMES_SINCE`, 2026-10-24T08:20:24+09:00) 이후에 만든 메시지에 걸린다.
```

### type

| type | 방향 | 뜻 | 본문 |
|---|---|---|---|
| `task` | interpreter → orchestrator | 수행 지시다. 그것만 읽고 작업할 수 있게 자족적으로 쓴다 | 필수 절 여섯: `## 배경` `## 목표` `## 완료조건` `## 제약` `## 파급효과` `## 확인 못 한 것` |
| `question` | 양방향 | 되묻기다. 받는 쪽이 `answer`로 회신한다 | 유저 판단이 필요하면 **다섯 절**: 질문 / 이미 정해진 것 / 현재 상태 / 답이 가르는 것 / 선택지, 그리고 추천. 유저에게 묻는 것은 확정 권한과 방향, 비용이 큰 선택, 새 파일, 검사의 약화다(Q-0060#Q140) |
| `answer` | 양방향 | `question`의 답이다. `re`가 원 질문을 가리킨다 | 유저의 답이면 원문과 질문 번호(`Q12-a`) |
| `result` | orchestrator → interpreter | 작업 결과다. `re`가 원 `task`를 가리킨다 | 수행 요약 / 검증(`bazel test //...` 결과) / 변경 파일 / 남은 이슈 |
| `knowledge` | 주로 interpreter → orchestrator | 사실과 제약, 도메인 지식을 전달한다. orchestrator가 지식 베이스로 승격한다 | 사실과 출처(질문 번호·`파일:줄`) |
| `status` | orchestrator → interpreter | 진행 보고와 문제, 특이사항을 전한다 | 자유 |
| `ack` | 양방향 | 수신 확인 (선택) | 자유 |

`task`의 `## 파급효과`에는 `bazel run //tools:impact -- <타깃>` 출력과 닿지 않는 것을 적는다.
`## 확인 못 한 것`에는 자료로 확인하지 못해 지시에 넣지 않은 것을 적고, 그런 것이 없으면 "없음"이라 적는다.

### status 생애주기

작성자는 항상 `new`로 만든다. 이후 **수신자**가 `scripts/mark.sh`로 전이한다.

```
new → read → in_progress → done        (정상 처리 — archive/ 로 이동)
                        └→ blocked      (추가 정보 필요 — question 을 보내고 answer 를 기다린다)
```

- `done`인 메시지는 `mark.sh`가 `archive/`로 옮긴다.
- **완료는 상태 확인으로 판정한다.** `task`는 그것을 `re`로 가리키는 `result`가 있어야 `done`이
  되고, `question`은 `answer`가 있어야 `done`이 된다. 시간으로 완료를 가정하지 않는다.
- `blocked`는 수신함에 남는다. 상대에게 `question`을 보내고 `answer`가 오면 재개한다.

## 유저 채널 (`user/`)

유저에게 피드백이나 결정을 요청할 때는 **항상 파일 질문지**로 한다. hci가 `user/Q-<번호>.md`를 쓰고,
유저가 같은 파일의 `답:` 줄에 답을 적는다. 채팅으로는 결정을 받지 않는다. 질문지의 형식과 생애주기의 원본은
[`user/README.md`](user/README.md)다.

## 지식 축적

채널 메시지는 git에는 남지 않지만 **지식 베이스는 남는다.** 어떤 프로젝트의 하네스는 현황과 목표, 확정된 결정,
발견된 제약, 작업 결과, 열린 질문을 `KNOWLEDGE.md` 한 파일에 누적한다. 이 저장소의 지식 베이스가 담으려는 지식이
바로 그것이다(유저 진술 2026-10-03). 그래서 이 하네스에는 `KNOWLEDGE.md`가 없고, 그 자리를
지식 베이스 자신이 맡는다.

| `KNOWLEDGE.md`에 쌓이던 것 | 지식 베이스의 자리 | 쓰는 역할 |
|---|---|---|
| 목표 | 요구 (`requirement` 지식 종류) · 진입 문서 `INTENT.md` | orchestrator (stable 전이는 유저 승인) |
| 확정된 설계 결정 (질문지의 답) | 결정 (`decision` 지식 종류 — 결론, 근거, 대안). 근거에 질문 번호를 적는다 | orchestrator |
| 발견된 제약 · 주의사항 | ODD 조건 (`kb/odd/project-odd.yml`) · 가정 (`kg/base-kg.ttl`) | developer |
| 프로젝트 현황 · 작업 결과 | 관측 (`memory` 지식 종류) · 구현 (`artifact` 지식 종류) · 판정 주석 (`annotation` 지식 종류) | orchestrator · developer · vnv |
| 열린 질문 | 선택 슬롯 `미확정:` · 설계 공간(`-space`)의 열린 후보 · 열린 질문지 | 그 항목의 쓰기 지식 종류를 맡은 역할 · hci |

hci는 지식 베이스에 쓰지 않는다. hci는 유저에게 받은 결정과 사실을 메시지로 넘기고, orchestrator가
그 쓰기 지식 종류를 맡은 역할을 통해 지식으로 승격한다. 채널과 질문지의 경로는 소멸성이므로 단위 지식 본문의
인용원이 될 수 없다. 그래서 근거는 `Q12-a` 같은 질문 번호로 적는다.

## 쓰기 경계

| 행위자 | 작성·수정 | 조회 |
|---|---|---|
| **유저** | 전체를 쓴다. 질문지에서는 `답:` 줄과 `status: answered`(hci 세션에서 "답 적었어"라고 알리면 hci가 대신 적는다) | 전체 |
| **interpreter** | `harness/channel/to_orchestrator/`(`send.sh`) · 자기 수신함 `harness/channel/to_interpreter/`의 상태 전이(`mark.sh`) · 자기 역할 메모리 | 저장소 전체 |
| **hci** (interpreter의 하위 역할) | `harness/user/` 전체 · interpreter의 역할 메모리 `.claude/agent-memory/interpreter/` | 저장소 전체 |
| **orchestrator** | `harness/channel/to_interpreter/`(`send.sh`) · 자기 수신함 `harness/channel/to_orchestrator/`의 상태 전이(`mark.sh`) · 자기 쓰기 지식 종류 | 저장소 전체 |
| developer · vnv | 채널과 질문지에 쓰지 않는다. 자기 쓰기 지식 종류만 쓴다 | dispatch 때 받은 작업 집합 |

## 스크립트 (`scripts/`)

| 스크립트 | 용도 |
|---|---|
| `run-interpreter.sh` · `run-orchestrator.sh` | 역할 세션을 띄운다. `run-hci.sh`는 `run-interpreter.sh`를 부르는 옛 이름이다 |
| `send.sh <from> <to> <type> <subject>` | 다음 id의 메시지를 만든다. 본문은 stdin이다. `RE=<id>`로 답장을, `SOURCE=<질문지 id>`로 근거 질문지를 지정한다. 보내기 전에 메시지 하나를 `//harness:channel_send_check`(`channel_lint.py --message`)로 검사해 FAIL이면 수신함에 놓지 않고 번호도 잡지 않는다 |
| `inbox.sh <role>` | role은 `interpreter`나 `orchestrator`이고 `hci`는 `interpreter`로 읽는다. 그 역할 수신함의 미처리 메시지 목록을 낸다 |
| `read-msg.sh <id>` | 메시지 하나를 출력한다 |
| `mark.sh <id> <status>` | 상태를 전이한다. `done`이면 `archive/`로 옮긴다 |
| `watch.sh <role>` | 그 역할 수신함에 `new` 메시지가 생길 때까지 기다린 뒤 목록을 내고 끝난다. 백그라운드로 돌린다 |
| `reset.sh` | 채널을 비운다 (archive 포함). 되돌릴 수 없다 |

### 수신 감시

`watch.sh`는 메시지 하나를 알리고 끝나는 일회성 감시이고, 감시가 끊기는 원인은 셋이다.

- 메모리 압박 때 Claude Code가 유휴 세션의 백그라운드 셸을 회수한다.
- 외부 시그널로 끝난다. 종료 코드 144가 관측됐다.
- 세션이 메시지를 처리한 뒤 감시를 다시 걸지 않는다.

그래서 두 역할 세션은 다음을 지킨다.

- `run-interpreter.sh`(옛 이름 `run-hci.sh`)와 `run-orchestrator.sh`는 `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1` 환경으로 `claude`를 띄운다. 이 변수는 시작 환경에서만 효과가 있으므로, 세션을 이 스크립트로 다시 띄워야 적용된다. 적용 범위는 그 세션의 백그라운드 셸 전부다.
- 메시지를 처리한 턴의 끝마다 감시가 살아 있는지 확인하고, 없으면 다시 건다.
- 감시가 0이 아닌 코드로 끝나면 수신함을 한 번 직접 읽은 뒤 다시 건다.
- 감시는 도구의 백그라운드 실행으로 하나만 띄운다. 같은 역할의 감시가 이미 살아 있으면 `watch.sh`는 그 PID를 알리고 따로 끝난다. `watch.sh hci`와 `watch.sh interpreter`는 같은 역할의 감시다. 종료 코드의 원본은 스크립트 머리 주석이다.
- 같은 머신에 다른 프로젝트의 같은 이름 감시가 있을 수 있으므로, 프로세스는 PID로만 멈춘다.

규칙의 원본은 결정 `p11-role-sessions-and-dispatch-models`의 규약 줄이다.

## 전형적 흐름

```
유저 ↔ hci      "게이트 id를 한 곳에서 정의하자."
hci             결정이 필요한 지점을 질문지 Q-0007 로 쓴다 → 유저가 답을 적고 answered 로 바꾼다
intp → send.sh interpreter orchestrator task "게이트 id 단일 정의처"     SOURCE=Q-0007   (0012, new)
orch            watch.sh 가 0012 를 감지 → mark.sh 0012 in_progress → developer dispatch
orch → send.sh orchestrator interpreter question "도구 태그도 등록할 것인가"  RE=0012  (0013) → mark.sh 0012 blocked
hci             질문지 Q-0008 → 유저 답 → send.sh interpreter orchestrator answer …  RE=0013  (0014)
orch            재개 → bazel test //... PASS → send.sh orchestrator interpreter result …  RE=0012 → mark.sh 0012 done
hci             유저에게 결과를 요약해 보고한다 → Q-0007·Q-0008 을 closed 로 닫아 archive/ 로 옮긴다
```

## 게이트

게이트 `//harness:channel_lint_test`가 이 프로토콜을 기계로 강제하고, 그 게이트 id는 `channel`이다. 검사 목록의
원본은 `tools/channel_lint.py`의 docstring이고, 그 요지는 셋이다.

- 메시지 검사는 필수 필드와 어휘, 단일 작성자, type별 방향, `re`와 `source`의
  실재, `task`의 필수 절, `done`과 `archive/`의 일치, 짝 없는 완료를 본다. 단일 작성자는 디렉토리와 `from`·`to`가 일치하는지로 보고(옛 이름 `hci`는 `interpreter`로 읽는다),
  짝 없는 완료는 `result` 없는 `task`와 `answer` 없는 `question`이다.
- 질문지 검사는 필수 필드와 `status` 어휘, `closed`와 `archive/`의 일치, 닫힌 질문지의 빈 `답:`을 본다.
- hci가 채널 밖에 반영했다는 서술이 질문지에 있으면, 그 질문지를 `source`로 갖는 `task`의
  `result`가 있어야 한다. 이와 별도로 `//kg:gate_test`의 writer 검사가 단위 지식 `generated.by`의 역할을 대조한다.

## 옛 채널

2026-10-03 이전의 채널은 `git:4c31fb2:docs/feedback/`의 네 lane이었고, 이 구조로 대체됐다. 옛 기록은
지우지 않고 옮겼다. 유저 lane 항목과 조사 기록은 `harness/user/archive/legacy/`에 있고, 에이전트 lane과
인수인계 lane의 항목은 `harness/channel/archive/legacy/`에 있다. 옛 기록은 옛 형식 그대로이므로 게이트 대상이
아니다. 읽는 법은 [`user/archive/legacy/README.md`](user/archive/legacy/README.md)에 있다.
