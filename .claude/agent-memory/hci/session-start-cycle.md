# hci 세션 시작 사이클 — 명령 순서

수치는 여기 적지 않는다. 기준선 수치는 낡는다. 정상 여부는 종료 코드와 생성물(`//kg:metrics`·`//kg:audit`)에서 읽는다.
게이트 목록의 원본은 `defs/kb.bzl` `GATES`이고 여기는 hci 의 실행 순서다.

| # | 명령 | 정상 |
|---|---|---|
| 1 | `git status -sb` · `git log --oneline -3` | 작업 트리에 **남의 변경**이 있을 수 있다(다른 세션이 같은 트리) — 있으면 커밋 전 `commit-lane-procedure.md` |
| 2 | `bazel test //...` | 종료 코드 0. FAIL 이면 지식 산출물을 고치는 것은 담당 역할 — hci 는 항목으로 보고 |
| 3 | `bazel test //harness:channel_lint_test --test_output=all` | `OK channel` · WAIT 는 대기 목록(정상) — 열린 질문지 = 유저 답 대기, `answered` 질문지 = 내 처리 대기, 수신함의 미완료 메시지 = 수신자 대기 |
| 4 | `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md` | 지표는 이 생성물에서 인용한다 |
| 5 | `bazel build //kg:audit` → `bazel-bin/kg/audit.md` | 검증 대응과 최근 실행은 이 생성물에서 인용한다 |
| 6 | `bazel build //kb:consistency` → ⑥ | tier 1 위반이 없다 |
| 7 | `./harness/scripts/inbox.sh hci` — 내 수신함. `question` 은 질문지로 옮기거나 근거와 함께 답하고, `result` 는 유저에게 보고한다 | 비어 있거나 처리할 메시지 목록 |
| 8 | `ls harness/user/` · `./harness/scripts/inbox.sh orchestrator` — 열린 질문지와 orchestrator 가 아직 끝내지 못한 지시 | 비어 있거나 대기 목록 |

## 알아 둘 것

- 역할 지침은 `harness/agents/` 의 `hci.md`·`orchestrator.md` 다 — vnv·developer 정의 파일은 없다(AGENTS 표가 원본).
- `.claude/agents/` 는 없다(2026-10-03 — hci 는 서브에이전트가 아니라 `harness/scripts/run-hci.sh` 로 띄운 세션이다).
- 채널 메시지는 git 밖이다. 새 클론에는 수신함이 비어 있다.
- 청크의 단위는 **토큰**이다 — 상한은 결정 `p1-chunk-unit-is-tokens`, 계수는 `bazel run //tools:tokens`. "42줄"은 2026-10-01 에 폐지됐다.
- 서비스 정의 — 결정 `p0-service-is-a-three-layer-wiki`(지식·방법론·프로세스).
- 판정자는 **세션 판정자**다(외부 서비스 없음, 유저 결정 2026-09-30). `jev` 는 방법론의 참고다.
- 2026-10-03: 채널이 `harness/` 의 두 채널로 바뀌었다. 옛 항목은 `harness/user/archive/legacy/`·`harness/channel/archive/legacy/` 로 옮겨졌고 게이트 대상이 아니다. 프로토콜 원본 `harness/README.md`.

## 되돌아오지 않은 것을 보는 법
`channel_lint` 의 WAIT 줄 + `./harness/scripts/inbox.sh orchestrator`(내가 보낸 `task` 가운데 `result` 가 아직 없는 것).

## git 인증
`git push` 는 저장된 자격이 만료돼 실패한다. `gh` 는 로그인돼 있으므로
`git -c credential.helper='!gh auth git-credential' push origin main` 으로 민다(설정을 바꾸지 않는다).
