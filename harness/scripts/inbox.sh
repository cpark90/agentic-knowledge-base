#!/usr/bin/env bash
# 역할 수신함의 미처리(done 이 아닌) 메시지를 id 순으로 보인다.
#   inbox.sh <role>        # role = hci | orchestrator
# 종료 코드는 메시지가 있든 없든 0 이다. 비어 있으면 그렇다고 적는다.
. "$(dirname "$0")/lib.sh"

[ "$#" -ge 1 ] || die "사용법: inbox.sh <hci|orchestrator>"
DIR="$(inbox_dir "$1")"
mkdir -p "$DIR"

found=0
for f in "$DIR"/*.md; do
  [ -e "$f" ] || continue
  st="$(field "$f" status)"
  [ "$st" = "done" ] && continue
  found=1
  printf '%-6s %-13s %-10s %-12s %s\n' \
    "$(field "$f" id)" "$(field "$f" from)" "$(field "$f" type)" "$st" "$(field "$f" subject)"
done
if [ "$found" = 0 ]; then
  echo "(수신함이 비었다: $1)"
fi
exit 0
