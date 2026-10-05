#!/usr/bin/env bash
# hci 세션을 띄운다 (유저와 대화하는 유일한 에이전트). 모델은 HCI_MODEL 로 바꾼다 (기본 opus).
set -euo pipefail
HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_DIR="$(cd "$HARNESS_DIR/.." && pwd)"
cd "$PROJECT_DIR"

command -v claude >/dev/null 2>&1 || { echo "claude CLI 가 PATH 에 없다" >&2; exit 1; }

# 메모리 압박 때 Claude Code 가 유휴 세션의 백그라운드 셸(수신 감시)을 회수하지 않게 한다. 이 세션의 백그라운드 셸 전부에 걸리고 전역 설정은 건드리지 않으며, 유저가 이미 정한 값은 존중한다.
export CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP="${CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP:-1}"

exec claude --model "${HCI_MODEL:-opus}" "너는 agentic-knowledge-base 하네스의 **hci 에이전트**다. \
먼저 $HARNESS_DIR/agents/hci.md 를 끝까지 읽고, $HARNESS_DIR/README.md 의 프로토콜과 \
$HARNESS_DIR/user/README.md 의 질문지 규약, $PROJECT_DIR/AGENTS.md 와 $PROJECT_DIR/STYLEGUIDE.md 를 숙지한 뒤 \
그 명세대로만 동작하라. 시작 시 수신함($HARNESS_DIR/channel/to_hci)과 열린 질문지($HARNESS_DIR/user)를 확인하고 \
유저에게 현재 상태를 알려라. 너는 유저와 직접 대화하는 유일한 에이전트이며 orchestrator 와는 채널 파일로만 소통한다."
