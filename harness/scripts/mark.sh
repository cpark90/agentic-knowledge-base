#!/usr/bin/env bash
# 메시지의 상태를 전이한다. 새 상태가 done 이면 archive/ 로 옮긴다. 전이는 수신자가 한다.
#   mark.sh <id> <status>    # status = read | in_progress | done | blocked
# 완료는 상태 확인으로 판정한다 — task 는 그것을 re 로 가리키는 result 가, question 은 answer 가
# 채널(수신함 둘 + archive) 어딘가에 있어야 done 이 된다. 없으면 거부한다.
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 2 ] || die "사용법: mark.sh <id> <read|in_progress|done|blocked>"
ID="$(norm_id "$1")"
NEW="$2"
case "$NEW" in read|in_progress|done|blocked) ;; *) die "status '$NEW' 는 어휘 밖이다 (read|in_progress|done|blocked)";; esac

FILE="$(find_msg "$ID")" || die "메시지 $ID 가 채널에 없다"

if [ "$NEW" = "done" ]; then
  TYPE="$(field "$FILE" type)"
  case "$TYPE" in
    task)     find_reply "$ID" result >/dev/null || die "task $ID 를 re 로 가리키는 result 가 없다 — result 를 먼저 보낸다" ;;
    question) find_reply "$ID" answer >/dev/null || die "question $ID 를 re 로 가리키는 answer 가 없다 — answer 를 먼저 받는다" ;;
  esac
fi

# frontmatter 의 첫 status: 줄을 고친다. 임시 파일에 쓴 뒤 rename 한다.
DEST="$FILE"
if [ "$NEW" = "done" ]; then
  mkdir -p "$CHANNEL_DIR/archive"
  DEST="$CHANNEL_DIR/archive/$ID.md"
fi
TMP="$(dirname "$DEST")/.$ID.tmp"
awk -v s="$NEW" '
  BEGIN{done=0}
  /^status:[[:space:]]/ && !done {print "status: " s; done=1; next}
  {print}
' "$FILE" > "$TMP"
mv "$TMP" "$DEST"
[ "$DEST" = "$FILE" ] || rm -f "$FILE"

if [ "$NEW" = "done" ]; then
  echo "$ID 를 done 으로 전이했다 -> archive"
else
  echo "$ID 를 $NEW 로 전이했다"
fi
