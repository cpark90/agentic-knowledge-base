#!/usr/bin/env bash
# 채널을 비운다 (수신함 둘 + archive 직계 메시지 + 번호 카운터). 되돌릴 수 없다.
# 디렉토리 구조와 .gitkeep 은 남긴다. archive/legacy/(옛 채널의 기록, git 추적)는 건드리지 않는다.
# 유저 채널(질문지)은 비우지 않는다. FORCE=1 이 아니면 확인을 묻는다.
. "$(dirname "$0")/lib.sh"

if [ "${FORCE:-0}" != "1" ]; then
  read -r -p "채널의 모든 메시지를 지운다 (archive 직계 포함, legacy 제외). 계속하는가? [y/N] " a
  case "$a" in y|Y) ;; *) echo "취소했다"; exit 0;; esac
fi

for d in to_orchestrator to_hci archive; do
  [ -d "$CHANNEL_DIR/$d" ] || continue
  find "$CHANNEL_DIR/$d" -maxdepth 1 -type f -name '*.md' -delete
done
rm -f "$SEQ_FILE" "$LOCK_FILE"
echo "채널을 비웠다"
