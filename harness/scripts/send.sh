#!/usr/bin/env bash
# 다음 id 의 채널 메시지를 만든다. 본문은 stdin 이다.
#   send.sh <from> <to> <type> <subject...>
#   RE=<id>          이 메시지가 답하는 메시지 — answer·result 는 필수다
#   SOURCE=<Q-id>    근거가 된 질문지 (harness/user/ 또는 harness/user/archive/ 에 실재해야 한다)
# 예:
#   printf '%s\n' "Q12-a 로 정했다" | RE=0013 SOURCE=Q-0008 \
#     ./send.sh hci orchestrator answer "도구 태그는 등록하지 않는다"
# 거부 규칙은 harness/README.md 의 type 표와 같다 — 어휘, 방향, re 의 실재와 대상 type, task 의 필수 절 여섯.
# 검사를 모두 통과한 뒤에만 번호를 잡는다. 쓰기는 임시 파일에 쓴 뒤 rename 한다 — rename 이 완료 선언이다.
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 4 ] || die "사용법: send.sh <from> <to> <type> <subject...>  (본문은 stdin)"
FROM="$1"; TO="$2"; TYPE="$3"; shift 3
SUBJECT="$*"
RE="${RE:-}"
SOURCE="${SOURCE:-}"

case "$FROM" in hci|orchestrator) ;; *) die "from '$FROM' 은 어휘 밖이다 (hci | orchestrator)";; esac
case "$TO"   in hci|orchestrator) ;; *) die "to '$TO' 은 어휘 밖이다 (hci | orchestrator)";; esac
[ "$FROM" != "$TO" ] || die "from 과 to 가 같다"
case "$TYPE" in task|question|answer|result|knowledge|status|ack) ;;
  *) die "type '$TYPE' 은 어휘 밖이다 (task|question|answer|result|knowledge|status|ack)";; esac
[ -n "${SUBJECT// /}" ] || die "subject 가 비었다"

# 방향 — task 는 hci 가 orchestrator 에, result·status 는 orchestrator 가 hci 에 보낸다.
case "$TYPE" in
  task)          [ "$FROM" = hci ] || die "task 는 hci → orchestrator 로만 보낸다" ;;
  result|status) [ "$FROM" = orchestrator ] || die "$TYPE 은 orchestrator → hci 로만 보낸다" ;;
esac

# re — answer 는 question 에, result 는 task 에 답한다. 다른 type 의 re 도 실재해야 한다.
if [ -n "$RE" ]; then
  RE="$(norm_id "$RE")"
  RE_FILE="$(find_msg "$RE")" || die "re $RE 메시지가 채널에 없다"
  RE_TYPE="$(field "$RE_FILE" type)"
  case "$TYPE" in
    answer) [ "$RE_TYPE" = question ] || die "answer 의 re 는 question 이어야 한다 ($RE 는 $RE_TYPE)" ;;
    result) [ "$RE_TYPE" = task ] || die "result 의 re 는 task 여야 한다 ($RE 는 $RE_TYPE)" ;;
  esac
else
  case "$TYPE" in answer|result) die "$TYPE 은 RE=<id> 가 필수다";; esac
fi

# source — 실재하는 질문지여야 한다.
if [ -n "$SOURCE" ]; then
  [ -f "$USER_DIR/$SOURCE.md" ] || [ -f "$USER_DIR/archive/$SOURCE.md" ] \
    || die "source $SOURCE 질문지가 없다 ($USER_DIR/$SOURCE.md · $USER_DIR/archive/$SOURCE.md)"
fi

BODY="$(cat)"
[ -n "$BODY" ] || BODY="(본문 없음)"

# task 의 필수 절 여섯 — 그것만 읽고 작업할 수 있어야 한다.
if [ "$TYPE" = task ]; then
  missing=""
  for h in "## 배경" "## 목표" "## 완료조건" "## 제약" "## 파급효과" "## 확인 못 한 것"; do
    printf '%s\n' "$BODY" | grep -qE "^${h}([[:space:]]|\$)" || missing="$missing · $h"
  done
  [ -z "$missing" ] || die "task 본문에 필수 절이 없다 —${missing# ·}"
fi

DIR="$(inbox_dir "$TO")"
mkdir -p "$DIR"
ID="$(claim_seq)"
FILE="$DIR/$ID.md"
TMP="$DIR/.$ID.tmp"
CREATED="$(date --iso-8601=seconds 2>/dev/null || date +%Y-%m-%dT%H:%M:%S%z)"

{
  echo "---"
  echo "id: $ID"
  echo "from: $FROM"
  echo "to: $TO"
  echo "type: $TYPE"
  echo "status: new"
  [ -n "$RE" ] && echo "re: $RE"
  [ -n "$SOURCE" ] && echo "source: $SOURCE"
  echo "subject: $SUBJECT"
  echo "created: $CREATED"
  echo "---"
  echo
  printf '%s\n' "$BODY"
} > "$TMP"
mv "$TMP" "$FILE"

echo "보냈다 $ID -> $TO : [$TYPE] $SUBJECT"
echo "$FILE"
