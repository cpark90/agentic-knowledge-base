#!/usr/bin/env bash
# 다음 id 의 채널 메시지를 만든다. 본문은 stdin 이다.
#   send.sh <from> <to> <type> <subject...>
#   RE=<id>          이 메시지가 답하는 메시지 — answer·result 는 필수다
#   SOURCE=<Q-id>    근거가 된 질문지 (harness/user/ 또는 harness/user/archive/ 에 실재해야 한다)
# 예:
#   printf '%s\n' "Q12-a 로 정했다" | RE=0013 SOURCE=Q-0008 \
#     ./send.sh interpreter orchestrator answer "도구 태그는 등록하지 않는다"
# 역할은 interpreter | orchestrator 다. 옛 이름 hci 도 받되 interpreter 로 적는다 (hci 는 interpreter 의 하위 역할이다).
# 거부 규칙은 harness/README.md 의 type 표와 같다 — 어휘, 방향, re 의 실재와 대상 type, task 의 필수 절 여섯.
# 그다음 발신 전 검사를 건다 — 수신함 밖 임시 파일에 메시지를 써서 channel_lint 의 메시지 단위 검사(--message: 필드·어휘·방향·
# re 필수·필수 절·경어·식별자 옆 한글 이름)를 돌리고, FAIL 이면 보내지 않는다. 검사 도구가 돌지 못해도 보내지 않는다. 우회 스위치는 없다.
# 채널 전체를 보는 검사(짝·자리·id 유일)는 게이트 //harness:channel_lint_test 에 남는다.
# 검사를 모두 통과한 뒤에만 번호를 잡는다. 쓰기는 임시 파일에 쓴 뒤 rename 한다 — rename 이 완료 선언이다.
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 4 ] || die "사용법: send.sh <from> <to> <type> <subject...>  (본문은 stdin)"
FROM="$1"; TO="$2"; TYPE="$3"; shift 3
SUBJECT="$*"
RE="${RE:-}"
SOURCE="${SOURCE:-}"

FROM="$(canon_role "$FROM")" || exit 1
TO="$(canon_role "$TO")" || exit 1
[ "$FROM" != "$TO" ] || die "from 과 to 가 같다"
case "$TYPE" in task|question|answer|result|knowledge|status|ack) ;;
  *) die "type '$TYPE' 은 어휘 밖이다 (task|question|answer|result|knowledge|status|ack)";; esac
[ -n "${SUBJECT// /}" ] || die "subject 가 비었다"

# 방향 — task 는 interpreter 가 orchestrator 에, result·status 는 orchestrator 가 interpreter 에 보낸다.
case "$TYPE" in
  task)          [ "$FROM" = interpreter ] || die "task 는 interpreter → orchestrator 로만 보낸다" ;;
  result|status) [ "$FROM" = orchestrator ] || die "$TYPE 은 orchestrator → interpreter 로만 보낸다" ;;
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

CREATED="$(date --iso-8601=seconds 2>/dev/null || date +%Y-%m-%dT%H:%M:%S%z)"

# 메시지 전문을 stdout 에 낸다. 인수는 id 다 — 발신 전 검사는 번호를 잡기 전이라 자리표 0000 으로 쓴다.
render() {
  echo "---"
  echo "id: $1"
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
}

# 발신 전 검사 — 검사 바이너리 //harness:channel_send_check 는 bazel 의 밀폐 해석기와 이름 원천을 runfiles 에 싣는다.
# bazel 시험 안(runfiles 에 바이너리가 있다)에서는 그것을 바로 쓰고, 밖에서는 bazel build 로 최신으로 맞춘 뒤 bazel-bin 의
# 것을 쓴다. 인수 파일의 경로가 runfiles 의 _main 기준이라 그 디렉토리에서 돌린다.
CHECK_TMP="$(mktemp -d "${TMPDIR:-/tmp}/akb-send.XXXXXX")"
trap 'rm -rf "$CHECK_TMP"' EXIT
render 0000 > "$CHECK_TMP/0000.md"
RUNFILES="${RUNFILES_DIR:-${TEST_SRCDIR:-}}"
if [ -n "$RUNFILES" ] && [ -x "$RUNFILES/_main/harness/channel_send_check" ]; then
  CHECK_BIN="$RUNFILES/_main/harness/channel_send_check"
else
  WS="$(cd "$HARNESS_DIR/.." && pwd)"
  (cd "$WS" && bazel build --noshow_progress --ui_event_filters=-info,-stdout //harness:channel_send_check) \
    >"$CHECK_TMP/build.log" 2>&1 \
    || { tail -n 20 "$CHECK_TMP/build.log" >&2; die "발신 전 검사 도구를 빌드하지 못했다 — 보내지 않았다 (bazel build //harness:channel_send_check)"; }
  CHECK_BIN="$WS/bazel-bin/harness/channel_send_check"
  RUNFILES="$CHECK_BIN.runfiles"
fi
[ -x "$CHECK_BIN" ] && [ -d "$RUNFILES/_main" ] || die "발신 전 검사 도구가 없다 ($CHECK_BIN) — 보내지 않았다"
set +e
(cd "$RUNFILES/_main" && "$CHECK_BIN" @harness/channel_send_check.args --message "$CHECK_TMP/0000.md") >"$CHECK_TMP/check.out" 2>&1
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  sed "s#$CHECK_TMP/0000.md#(보낼 메시지)#g" "$CHECK_TMP/check.out" >&2
  if [ "$rc" -eq 1 ]; then die "발신 전 검사가 FAIL 이다 — 보내지 않았다 (번호를 잡지 않았다)"; fi
  die "발신 전 검사 도구가 판정하지 못했다 (종료 코드 $rc) — 보내지 않았다"
fi

DIR="$(inbox_dir "$TO")"
mkdir -p "$DIR"
ID="$(claim_seq)"
FILE="$DIR/$ID.md"
TMP="$DIR/.$ID.tmp"
render "$ID" > "$TMP"
mv "$TMP" "$FILE"

echo "보냈다 $ID -> $TO : [$TYPE] $SUBJECT"
echo "$FILE"
