# 수신 감시가 멈추는 원인과 해결 (2026-10-05 조사 · 같은 날 해결)

- **원인 셋.** 메모리 압박 회수(claude 세션 30개, RSS 합 6.2GiB/15GiB)·외부 시그널(종료 144, 주체 미확인)·일회성 감시를 처리 뒤 다시 걸지 않는 것.
- **해결(task 0089 → result 0090).** `run-hci.sh`·`run-orchestrator.sh`가 `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`로 띄운다(시작 환경에서만 효과).
  `watch.sh`는 PID 파일 `harness/channel/.watch-<역할>.pid`로 중복을 막는다. 종료 코드 0 new · 1 사용 오류 · 2 시간 초과 · 3 중복 · 143 시그널.
- **재무장 규칙**(원본 결정 `p11-role-sessions-and-dispatch-models` 규약 줄): 메시지를 처리한 턴 끝마다 감시 생존 확인·재기동, 0 아닌 종료 뒤 `inbox.sh hci` 직접 확인 후 재기동, 백그라운드 실행 하나만.
- 세션 시작 시 `echo $CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP`가 1인지 본다. 1이 아니면 유저에게 `run-hci.sh`로 다시 띄우라고 알린다.
- 종료 144가 회수 끄기 뒤에도 나오면 orchestrator에 다시 보고한다(0090 남은 이슈).

관련: [session-start-cycle](session-start-cycle.md)
