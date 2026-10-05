# harness — hci · orchestrator 두 세션 프로토콜

이 디렉토리는 이 저장소에서 일하는 에이전트의 **운영 틀**이다. 독립된 Claude Code 세션 둘이
파일 채널로 협업한다. 작업 규칙(황금률·역할·권한·언어)은 [`../AGENTS.md`](../AGENTS.md)에서 읽고(생성 파일 — 원본은 결정의 규약 청크와 `kb/dev/norm/`의 절 청크),
이 문서는 **소통 프로토콜의 원본**이다. 프로토콜은 런타임·채널·메시지·질문지·스크립트를 다룬다.

하네스의 파일은 **그래프 밖**이다. 지식 산출물이 아니라 운영 기록이다. 소통이 낳은 결론은
여기에 남기지 않고 지식 베이스로 승격한다([지식 축적](#지식-축적)).

## 역할

| 에이전트 | 하는 일 | 유저와의 접점 |
|---|---|---|
| **hci** ([`agents/hci.md`](agents/hci.md)) | 유저와 대화해 의도·도메인 지식·결정을 끌어내고, 그것을 지시와 지식으로 정제해 orchestrator에 넘긴다. orchestrator의 질문과 결과를 유저에게 되돌린다. 조사와 git 관리를 맡는다 | **있다** — 유일한 창구 |
| **orchestrator** ([`agents/orchestrator.md`](agents/orchestrator.md)) | hci가 넘긴 지시를 계획하고 수행한다. 요구·결정을 저작하고 developer·vnv를 dispatch해 통합한다. 막히면 질문을, 끝나면 결과를 hci에 올린다 | **없다** — 채널로만 소통한다 |
| developer · vnv | orchestrator가 dispatch한다. 세션을 유지하지 않으므로 수신함이 없다. 결과와 질문은 hand-back으로 orchestrator에 돌아가고, 유저에게 물을 것은 orchestrator가 채널에 올린다 | 없다 |

두 세션은 **서로를 직접 호출하지 않는다.** 아래 채널 파일로만 소통한다. 역할별 write plane과
권한은 `AGENTS.md`의 역할 표와 `kg/catalog-kg.ttl`이 정한다.

## 런타임

터미널 둘에서 각각 독립 세션으로 띄운다.

```
터미널 A:  ./harness/scripts/run-hci.sh            # 유저가 여기서 대화한다
터미널 B:  ./harness/scripts/run-orchestrator.sh   # 작업을 수행한다
```

각 세션은 자기 지침(`agents/` 아래 파일)을 읽고 이 문서의 프로토콜대로 채널을 감시·소비·응답한다.

## 구조

```
harness/
├── README.md              # 이 문서 (프로토콜 원본)
├── agents/                # 역할 지침 — hci.md · orchestrator.md
├── channel/               # 에이전트 채널: hci ↔ orchestrator (런타임 산출물, git 밖)
│   ├── to_orchestrator/   #   hci → orchestrator (수신함: orchestrator)
│   ├── to_hci/            #   orchestrator → hci (수신함: hci)
│   └── archive/           #   처리가 끝난(done) 메시지 · legacy/ (옛 에이전트·인수인계 lane, git 추적)
├── user/                  # 유저 채널: 유저 ↔ hci 질문지 (git 추적)
│   ├── README.md          #   질문지 형식과 생애주기
│   ├── Q-<번호>.md        #   열린 질문지
│   └── archive/           #   닫힌 질문지 · legacy/ (옛 유저 lane·조사 lane)
└── scripts/               # 세션 부팅과 채널 조작
```

## 에이전트 채널 (`channel/`)

- **단일 작성자 규칙.** `to_orchestrator/`에는 hci만 쓰고 `to_hci/`에는 orchestrator만 쓴다.
  읽기와 상태 전이·보관은 **수신자**가 한다. 쓰기는 `scripts/send.sh`로만 한다.
- **메시지 id는 채널 전역에서 유일한 단조 증가 번호다**(`channel/.seq`). 방향이 달라도 번호가
  겹치지 않으므로 id만으로 대화 순서가 복원된다.
- **채널 메시지는 런타임 산출물이다.** git이 추적하지 않는다(`.gitignore`). 기록으로 남는 것은
  질문지(유저의 답)와 지식 베이스(승격된 결론)와 git 이력이다.

### 메시지 포맷

파일명은 `<id>.md`이고 id는 네 자리다(예: `0007.md`).

```markdown
---
id: 0007
from: hci              # hci | orchestrator
to: orchestrator       # orchestrator | hci
type: task             # task | question | answer | result | knowledge | status | ack
status: new            # new | read | in_progress | done | blocked
re: 0006               # (선택) 이 메시지가 답하는 메시지 id — answer·result 는 필수
source: Q-0003         # (선택) 근거가 된 질문지 id
subject: 한 줄 요약
created: 2026-10-03T14:03:00+09:00
---

본문은 마크다운이다. 지식은 이름이 아니라 IRI·조건 id·`파일:줄`로 가리킨다.
```

### type

| type | 방향 | 뜻 | 본문 |
|---|---|---|---|
| `task` | hci → orchestrator | 수행 지시. 그것만 읽고 작업할 수 있게 자족적으로 쓴다 | 필수 절 여섯: `## 배경` `## 목표` `## 완료조건` `## 제약` `## 파급효과` `## 확인 못 한 것` |
| `question` | 양방향 | 되묻기. 받는 쪽이 `answer`로 회신한다 | 유저 판단이 필요하면 **다섯 절**: 질문 / 이미 정해진 것 / 현재 상태 / 답이 가르는 것 / 선택지, 그리고 추천 |
| `answer` | 양방향 | `question`의 답. `re`가 원 질문을 가리킨다 | 유저의 답이면 원문과 질문 번호(`Q12-a`) |
| `result` | orchestrator → hci | 작업 결과. `re`가 원 `task`를 가리킨다 | 수행 요약 / 검증(`bazel test //...` 결과) / 변경 파일 / 남은 이슈 |
| `knowledge` | 주로 hci → orchestrator | 사실·제약·도메인 지식의 전달. orchestrator가 지식 베이스로 승격한다 | 사실과 출처(질문 번호·`파일:줄`) |
| `status` | orchestrator → hci | 진행 보고·문제·특이사항 | 자유 |
| `ack` | 양방향 | 수신 확인 (선택) | 자유 |

`task`의 `## 파급효과`에는 `bazel run //tools:impact -- <타깃>` 출력과 닿지 않는 것을 적는다.
`## 확인 못 한 것`에는 자료로 확인하지 못해 지시에 넣지 않은 것을 적는다. 없으면 "없음"이라 적는다.

### status 생애주기

작성자는 항상 `new`로 만든다. 이후 **수신자**가 `scripts/mark.sh`로 전이한다.

```
new → read → in_progress → done        (정상 처리 — archive/ 로 이동)
                        └→ blocked      (추가 정보 필요 — question 을 보내고 answer 를 기다린다)
```

- `done`인 메시지는 `archive/`로 옮긴다. `mark.sh`가 옮긴다.
- **완료는 상태 확인으로 판정한다.** `task`는 그것을 `re`로 가리키는 `result`가 있어야 `done`이
  되고, `question`은 `answer`가 있어야 `done`이 된다. 시간으로 완료를 가정하지 않는다.
- `blocked`는 수신함에 남는다. 상대에게 `question`을 보내고 `answer`가 오면 재개한다.

## 유저 채널 (`user/`)

유저에게 피드백·결정을 요청할 때는 **항상 파일 질문지**로 한다. hci가 `user/Q-<번호>.md`를 쓰고,
유저가 같은 파일의 `답:` 줄에 답을 적는다. 채팅으로 결정을 받지 않는다. 형식과 생애주기의 원본은
[`user/README.md`](user/README.md)다.

## 지식 축적

메시지는 흐르고 **지식 베이스는 남는다.** 한 프로젝트의 하네스가 `KNOWLEDGE.md` 한 파일에
누적하는 것 — 현황·목표·확정된 결정·발견된 제약·작업 결과·열린 질문 — 이 이 저장소의 지식
베이스가 담으려는 지식이다(유저 진술 2026-10-03). 이 하네스에는 그 파일이 없다. 그 자리는
지식 베이스 자신이다.

| `KNOWLEDGE.md`에 쌓이던 것 | 지식 베이스의 자리 | 쓰는 역할 |
|---|---|---|
| 목표 | 요구 (`requirement` plane) · 진입 문서 `INTENT.md` | orchestrator (stable 전이는 유저 승인) |
| 확정된 설계 결정 (질문지의 답) | 결정 (`decision` plane — 결론·근거·대안). 근거에 질문 번호를 적는다 | orchestrator |
| 발견된 제약 · 주의사항 | ODD 조건 (`kb/odd/project-odd.yml`) · 가정 (`kg/base-kg.ttl`) | developer |
| 프로젝트 현황 · 작업 결과 | 관측 (`memory` plane) · 구현 (`artifact` plane) · 판정 주석 (`annotation` plane) | orchestrator · developer · vnv |
| 열린 질문 | 선택 슬롯 `미확정:` · 설계 공간(`-space`)의 열린 후보 · 열린 질문지 | 그 항목의 write plane 역할 · hci |

hci는 지식 베이스에 쓰지 않는다. 유저에게 받은 결정과 사실을 메시지로 넘기고, orchestrator가
담당 write plane의 역할을 통해 지식으로 승격한다. 채널·질문지 경로는 소멸성이라 청크 본문의
인용원이 될 수 없다. 근거는 질문 번호(`Q12-a`)로 적는다.

## 쓰기 경계

| 행위자 | 작성·수정 | 조회 |
|---|---|---|
| **유저** | 전체. 질문지에서는 `답:` 줄과 `status: answered`(hci 세션에서 "답 적었어"라고 알리면 hci가 대신 적는다) | 전체 |
| **hci** | `harness/user/` 전체 · `harness/channel/to_orchestrator/`(`send.sh`) · 자기 수신함 `harness/channel/to_hci/`의 상태 전이(`mark.sh`) · 자기 역할 메모리 `.claude/agent-memory/hci/` | 저장소 전체 |
| **orchestrator** | `harness/channel/to_hci/`(`send.sh`) · 자기 수신함 `harness/channel/to_orchestrator/`의 상태 전이(`mark.sh`) · 자기 write plane | 저장소 전체 |
| developer · vnv | 채널과 질문지에 쓰지 않는다. 자기 write plane만 쓴다 | dispatch 때 받은 작업 집합 |

## 스크립트 (`scripts/`)

| 스크립트 | 용도 |
|---|---|
| `run-hci.sh` · `run-orchestrator.sh` | 역할 세션을 띄운다 |
| `send.sh <from> <to> <type> <subject>` | 다음 id의 메시지를 만든다. 본문은 stdin이다. `RE=<id>`로 답장을, `SOURCE=<질문지 id>`로 근거 질문지를 지정한다 |
| `inbox.sh <role>` | 그 역할 수신함의 미처리 메시지 목록 |
| `read-msg.sh <id>` | 메시지 하나를 출력한다 |
| `mark.sh <id> <status>` | 상태를 전이한다. `done`이면 `archive/`로 옮긴다 |
| `watch.sh <role>` | 그 역할 수신함에 `new` 메시지가 생길 때까지 기다린 뒤 목록을 내고 끝난다. 백그라운드로 돌린다 |
| `reset.sh` | 채널을 비운다 (archive 포함). 되돌릴 수 없다 |

### 수신 감시

`watch.sh`는 메시지 하나를 알리고 끝나는 일회성 감시다. 감시가 끊기는 원인은 셋이다.
- 메모리 압박 때 Claude Code가 유휴 세션의 백그라운드 셸을 회수한다.
- 외부 시그널로 끝난다(종료 144가 관측됐다).
- 처리 뒤 다시 걸지 않는다.

그래서 두 역할 세션은 다음을 지킨다.

- `run-hci.sh`·`run-orchestrator.sh`는 `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1` 환경으로 `claude`를 띄운다. 이 변수는 시작 환경에서만 효과가 있다. 그래서 세션을 이 스크립트로 다시 띄워야 적용된다. 범위는 그 세션의 백그라운드 셸 전부다.
- 메시지를 처리한 턴의 끝마다 감시가 살아 있는지 확인하고, 없으면 다시 건다.
- 감시가 0이 아닌 코드로 끝나면 수신함을 한 번 직접 읽은 뒤 다시 건다.
- 감시는 도구의 백그라운드 실행으로 하나만 띄운다. `watch.sh`는 같은 역할의 감시가 이미 살아 있으면 그 PID를 알리고 따로 끝난다. 종료 코드는 스크립트 머리 주석이 원본이다.
- 프로세스는 PID로만 멈춘다. 같은 머신에 다른 프로젝트의 같은 이름 감시가 있을 수 있다.

규칙의 원본은 결정 `p11-role-sessions-and-dispatch-models`의 규약 줄이다.

## 전형적 흐름

```
유저 ↔ hci      "게이트 id를 한 곳에서 정의하자."
hci             결정이 필요한 지점을 질문지 Q-0007 로 쓴다 → 유저가 답을 적고 answered 로 바꾼다
hci  → send.sh hci orchestrator task "게이트 id 단일 정의처"     SOURCE=Q-0007   (0012, new)
orch            watch.sh 가 0012 를 감지 → mark.sh 0012 in_progress → developer dispatch
orch → send.sh orchestrator hci question "도구 태그도 등록할 것인가"  RE=0012  (0013) → mark.sh 0012 blocked
hci             질문지 Q-0008 → 유저 답 → send.sh hci orchestrator answer …  RE=0013  (0014)
orch            재개 → bazel test //... PASS → send.sh orchestrator hci result …  RE=0012 → mark.sh 0012 done
hci             유저에게 결과를 요약해 보고한다 → Q-0007·Q-0008 을 closed 로 닫아 archive/ 로 옮긴다
```

## 게이트

`//harness:channel_lint_test`(게이트 id `channel`)가 이 프로토콜을 기계로 강제한다. 검사 목록의
원본은 `tools/channel_lint.py`의 docstring이다. 요지는 다음과 같다.

- 메시지: 필수 필드와 어휘, 단일 작성자(디렉토리와 `from`·`to`의 일치), type별 방향, `re`·`source`의
  실재, `task`의 필수 절, `done`과 `archive/`의 일치, 짝 없는 완료(`result` 없는 `task`, `answer` 없는 `question`).
- 질문지: 필수 필드와 `status` 어휘, `closed`와 `archive/`의 일치, 닫힌 질문지의 빈 `답:`.
- hci가 채널 밖에 반영했다는 서술이 질문지에 있으면 그 질문지를 `source`로 갖는 `task`의
  `result`가 있어야 한다. `//kg:gate_test`의 writer 검사가 청크 `generated.by`의 역할을 따로 대조한다.

## 옛 채널

2026-10-03 이전의 채널(`git:4c31fb2:docs/feedback/`의 네 lane)은 이 구조로 대체됐다. 기록은
지우지 않고 옮겼다. 유저 lane 항목과 조사 기록은 `harness/user/archive/legacy/`에, 에이전트 lane과
인수인계 lane의 항목은 `harness/channel/archive/legacy/`에 있다. 옛 형식 그대로이고 게이트 대상이
아니다. 읽는 법은 [`user/archive/legacy/README.md`](user/archive/legacy/README.md)에 있다.
