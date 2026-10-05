# hci 세션 시작 사이클 — 명령 / 정상 (기준선 2026-10-02, base 61a8259)

정상 칸이 수치라 초록이 반증 가능하다. 기준선이 바뀌면 이 표를 고친다 — 게이트 목록·비-초록 기준선의 **원본은
`docs/tools.md` §게이트를 추가할 때**이고 여기는 hci 의 실행 순서다.

| # | 명령 | 정상 |
|---|---|---|
| 1 | `git status -sb` · `git log --oneline -3` | 작업 트리에 **남의 변경**이 있을 수 있다(다른 세션이 같은 트리) — 있으면 커밋 전 `commit-lane-procedure.md` |
| 2 | `bazel test //...` | **18/18 PASS** (코어 게이트 8 · 드리프트 2(BUILD·skills) · 채널 · doccheck · consistency_build · 음성 시험 5). FAIL 이면 지식 산출물을 고치는 것은 담당 역할 — hci 는 항목으로 보고 |
| 3 | `bazel test //harness:channel_lint_test --test_output=all` | `OK channel` · WAIT 는 대기 목록(정상) — 열린 질문지 = 유저 답 대기, `answered` 질문지 = 내 처리 대기, 수신함의 미완료 메시지 = 수신자 대기 |
| 4 | `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md` | 청크 813(살아 684 — 개발 634 · V&V 50) · 링크 개체 607, 증거 100% · 고아 0% · 복원 5.0% · **연결 성분 4**(관측 3건이 링크가 없어 각각 성분 — 유저 판단 대기) |
| 5 | `bazel build //kg:audit` → `bazel-bin/kg/audit.md` | 검증 대응물 있는 요구 18/33 · 기준 없는 verifies 0 · 최근 실행 pass 16·fail 0 |
| 6 | `bazel build //kb:consistency` → ⑥ | tier 1 위반 0(면제 1건) · 근사 중복 후보 1(실행 기록 둘, 형식이 같아 구조적) |
| 7 | `./harness/scripts/inbox.sh hci` — 내 수신함. `question` 은 질문지로 옮기거나 근거와 함께 답하고, `result` 는 유저에게 보고한다 | 비어 있거나 처리할 메시지 목록 |
| 8 | `ls harness/user/` · `./harness/scripts/inbox.sh orchestrator` — 열린 질문지와 orchestrator 가 아직 끝내지 못한 지시 | 기준선 2026-10-03: 질문지 `Q-0001`(척도 stable, 답 대기) · `Q-0002`(판정지 10건, 답 대기) · orchestrator 수신함 `task` 둘(통일 기획 진행 중 · 재판정 대기) |

## 없는 것 — 없는 것이 정상이다 (다음 세션이 고치러 오지 않게)

- `artifact`·`annotation` plane 0, `contract`·`schema` 는 V&V 사슬로만 16·16 — 사례 프로젝트 관통 전까지 그대로.
- V&V: 시나리오 0 · 검증기 청크 0 · 판정 주석 0 · `defect` 모듈 없음 · V&V 프로파일 없음(위험 분석 G1~G6 은 유저 입력 대기).
- `when` 실물 0 · `suspect` 실물 0 · selector 어휘 없음 — 링크 견고성 C·D·E 가 유저 판단 대기라 그렇다.
- 역할 지침은 `harness/agents/` 의 `hci.md`·`orchestrator.md` 둘뿐 — vnv·developer 정의 파일 없음(AGENTS 표가 원본).
- `.claude/agents/` 는 없다(2026-10-03 — hci 는 서브에이전트가 아니라 `harness/scripts/run-hci.sh` 로 띄운 세션이다).
- 채널 메시지는 git 밖이다. 새 클론에는 수신함이 비어 있다.

## 되돌아오지 않은 것을 보는 법
`channel_lint` 의 WAIT 줄 + `./harness/scripts/inbox.sh orchestrator`(내가 보낸 `task` 가운데 `result` 가 아직 없는 것).

## git 인증
`git push` 는 저장된 자격이 만료돼 실패한다. `gh` 는 로그인돼 있으므로
`git -c credential.helper='!gh auth git-credential' push origin main` 으로 민다(설정을 바꾸지 않는다).

## 기준선 갱신 2026-10-02 — 위 표의 수치는 낡았다. 생성물을 본다

- `bazel test //...` **75/75 PASS**(게이트 id 49 + 도구 태그 9, 원본 `defs/kb.bzl` `GATES`). 표의 18 은 2026-09-19 값이다.
- 청크의 단위는 **토큰**이다 — 저작 산문 1,092 · 인용 2,856(`bazel run //tools:tokens`). "42줄"은 2026-10-01 에 폐지됐다.
- 살아 있는 청크 약 1,480 · `artifact` 630 · 연결 성분 1 · 고아 0% · CQ19 64.5% · CQ20 100%. 수치는 적지 말고 `//kg:metrics`·`//kg:audit` 에서 인용한다.
- 서비스 정의 — 결정 `p0-service-is-a-three-layer-wiki`(지식·방법론·프로세스). 통일 기획 지시(orchestrator 수신함 `task` 0001)가 열려 있다.
- 판정자는 **세션 판정자**다(외부 서비스 없음, 유저 결정 2026-09-30). `jev` 는 방법론의 참고다.
- 2026-10-03: 채널이 `harness/` 의 두 채널로 바뀌었다. 옛 항목 100여 개는 `harness/user/archive/legacy/`·`harness/channel/archive/legacy/` 로 옮겨졌고 게이트 대상이 아니다. 프로토콜 원본 `harness/README.md`.
