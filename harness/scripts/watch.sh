#!/usr/bin/env bash
# 역할 수신함에 new 메시지가 생길 때까지 기다린 뒤 목록을 내고 0 으로 끝난다. 에이전트가 백그라운드로 돌려
# 메시지가 오면 다시 깨어나게 한다.
#   watch.sh <role> [poll_seconds] [max_seconds]
# max_seconds 가 0 이면 무기한 기다린다. inotifywait 가 있으면 쓰고 없으면 폴링한다.
# 역할마다 감시는 하나다. PID 파일(채널 디렉토리의 부모, 곧 harness/.watch-<role>.pid, role 은 정규 이름)에 자기 PID 를 쓰고, 정상 종료·시그널 때 자기 PID 일 때만 지운다.
# 종료 코드: 0 new 메시지를 냈다 / 1 사용 오류 / 2 시간 초과 / 3 같은 역할의 감시가 이미 돈다.
# 143 은 시그널로 끝났다는 뜻이다. 이 스크립트는 SIGINT·SIGTERM·SIGHUP 을 잡아 PID 파일을 치운 뒤 143(128 + SIGTERM 15)으로
# 끝나고, 도구가 백그라운드 작업을 거둘 때 보내는 SIGTERM 이 가장 흔한 원인이다. 잡을 수 없는 SIGKILL 이면 137 이 되고,
# 상위 래퍼(도구의 백그라운드 실행기·부팅 스크립트·tmux)가 자기 관례로 다른 신호 코드를 보고할 수도 있다. 이 코드들은
# 감시가 결과를 내지 못했다는 뜻일 뿐 수신함의 상태를 말하지 않으므로, 받은 쪽은 수신함을 한 번 직접 읽고 감시를 다시 건다.
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 1 ] || die "사용법: watch.sh <interpreter|orchestrator> [poll_seconds] [max_seconds]"
ROLE="$(canon_role "$1")" || exit 1  # 옛 이름 hci 는 interpreter 로 읽는다 — 같은 수신함과 같은 PID 파일을 쓴다
POLL="${2:-3}"
MAX="${3:-0}"
DIR="$(inbox_dir "$ROLE")"
mkdir -p "$DIR"

# 같은 역할의 감시가 살아 있는가. PID 가 살아 있고 그 명령줄이 이 역할의 watch.sh 일 때만 참이다.
PID_FILE="$(dirname "$CHANNEL_DIR")/.watch-$ROLE.pid"
is_watching() {
  local pid cmd
  pid="$(cat "$PID_FILE" 2>/dev/null || true)"
  [[ "$pid" =~ ^[0-9]+$ ]] || return 1
  [ "$pid" != "$$" ] || return 1
  kill -0 "$pid" 2>/dev/null || return 1
  cmd="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)"
  [[ "$cmd" == *"watch.sh $ROLE "* ]] && return 0
  [ "$ROLE" = interpreter ] && [[ "$cmd" == *"watch.sh hci "* ]]  # 옛 이름으로 건 감시도 같은 역할의 감시다
}
if is_watching; then
  echo "이미 감시 중: PID $(cat "$PID_FILE")"
  exit 3
fi
# 낡은 파일을 치우고 배타적으로 만든다. 동시에 시작한 쪽이 지면 이미 감시 중으로 본다.
rm -f "$PID_FILE"
if ! ( set -o noclobber; echo "$$" > "$PID_FILE" ) 2>/dev/null; then
  echo "이미 감시 중: PID $(cat "$PID_FILE" 2>/dev/null || echo '?')"
  exit 3
fi
cleanup() {
  [ "$(cat "$PID_FILE" 2>/dev/null || true)" = "$$" ] && rm -f "$PID_FILE"
  return 0
}
trap cleanup EXIT
trap 'exit 143' INT TERM HUP

has_new() {
  local f
  for f in "$DIR"/*.md; do
    [ -e "$f" ] || continue
    [ "$(field "$f" status)" = "new" ] && return 0
  done
  return 1
}

if has_new; then
  echo "$ROLE 수신함에 new 메시지가 이미 있다:"
  bash "$HARNESS_DIR/scripts/inbox.sh" "$ROLE"
  exit 0
fi

elapsed=0
while true; do
  if command -v inotifywait >/dev/null 2>&1; then
    inotifywait -q -t "$POLL" -e create -e moved_to -e modify "$DIR" >/dev/null 2>&1 || true
  else
    sleep "$POLL"
  fi
  if has_new; then
    echo "$ROLE 수신함에 new 메시지가 왔다:"
    bash "$HARNESS_DIR/scripts/inbox.sh" "$ROLE"
    exit 0
  fi
  elapsed=$((elapsed + POLL))
  if [ "$MAX" -gt 0 ] && [ "$elapsed" -ge "$MAX" ]; then
    echo "$ROLE 수신함에 ${MAX}초 동안 new 메시지가 없다 — 시간 초과"
    exit 2
  fi
done
