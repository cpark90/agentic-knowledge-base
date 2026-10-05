#!/usr/bin/env bash
# 하네스 채널의 공용 도구다. 각 스크립트가 source 한다: . "$(dirname "$0")/lib.sh"
# 프로토콜 원본은 harness/README.md 다. 역할은 hci | orchestrator 둘뿐이다.
set -euo pipefail

# 하네스 루트(scripts/ 의 부모)를 정한다. 채널·유저 디렉토리는 환경 변수로 바꿀 수 있다 — 테스트가 임시 디렉토리로 돌린다.
HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHANNEL_DIR="${AKB_CHANNEL_DIR:-$HARNESS_DIR/channel}"
USER_DIR="${AKB_USER_DIR:-$HARNESS_DIR/user}"
SEQ_FILE="$CHANNEL_DIR/.seq"
LOCK_FILE="$CHANNEL_DIR/.seq.lock"

die() { echo "오류: $*" >&2; exit 1; }

# 역할 이름을 그 역할의 수신함 디렉토리로 바꾼다.
inbox_dir() {
  case "$1" in
    orchestrator) echo "$CHANNEL_DIR/to_orchestrator" ;;
    hci)          echo "$CHANNEL_DIR/to_hci" ;;
    *) die "역할 '$1' 은 어휘 밖이다 (hci | orchestrator)" ;;
  esac
}

# 메시지 id 를 네 자리로 맞춘다. 숫자가 아니면 그대로 둔다.
norm_id() {
  if [[ "$1" =~ ^[0-9]+$ ]]; then printf '%04d\n' "$((10#$1))"; else echo "$1"; fi
}

# 채널 전역의 다음 메시지 id 를 원자적으로 잡는다 (네 자리). 두 세션이 같은 번호를 잡지 않게 잠근다.
claim_seq() {
  mkdir -p "$CHANNEL_DIR"
  (
    exec 9>"$LOCK_FILE"
    if command -v flock >/dev/null 2>&1; then flock 9; fi
    local n=0
    [ -f "$SEQ_FILE" ] && n=$(cat "$SEQ_FILE")
    n=$((10#$n + 1))
    echo "$n" > "$SEQ_FILE"
    printf '%04d\n' "$n"
  )
}

# 메시지 id 의 파일을 수신함 둘과 archive 에서 찾는다. 경로를 내거나 비영 종료한다.
find_msg() {
  local id="$1" f
  for f in "$CHANNEL_DIR"/to_orchestrator/"$id".md \
           "$CHANNEL_DIR"/to_hci/"$id".md \
           "$CHANNEL_DIR"/archive/"$id".md; do
    [ -f "$f" ] && { echo "$f"; return 0; }
  done
  return 1
}

# 파일 frontmatter 의 필드 값 하나를 읽는다 (첫 출현, `#` 뒤 주석 제거).
field() {
  local file="$1" key="$2"
  sed -n "s/^${key}:[[:space:]]*//p" "$file" | head -n1 | sed 's/[[:space:]]\{1,\}#.*$//; s/[[:space:]]*$//'
}

# 채널 어딘가에 <id> 를 re 로 가리키는 <type> 메시지가 있는가. 있으면 그 경로를 내고 0, 없으면 1.
find_reply() {
  local id="$1" type="$2" f
  for f in "$CHANNEL_DIR"/to_orchestrator/*.md "$CHANNEL_DIR"/to_hci/*.md "$CHANNEL_DIR"/archive/*.md; do
    [ -e "$f" ] || continue
    if [ "$(field "$f" re)" = "$id" ] && [ "$(field "$f" type)" = "$type" ]; then
      echo "$f"; return 0
    fi
  done
  return 1
}
