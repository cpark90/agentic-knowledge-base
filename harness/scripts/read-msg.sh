#!/usr/bin/env bash
# 메시지 하나를 출력한다.
#   read-msg.sh <id>
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 1 ] || die "사용법: read-msg.sh <id>"
ID="$(norm_id "$1")"
FILE="$(find_msg "$ID")" || die "메시지 $ID 가 채널에 없다"
echo "# $FILE"
cat "$FILE"
