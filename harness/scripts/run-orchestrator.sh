#!/usr/bin/env bash
# orchestrator 세션을 띄운다 (작업을 수행한다, 유저와 직접 대화하지 않는다). 모델은 ORCHESTRATOR_MODEL 로 정한다
# (비우면 claude 기본값).
set -euo pipefail
HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_DIR="$(cd "$HARNESS_DIR/.." && pwd)"
cd "$PROJECT_DIR"

command -v claude >/dev/null 2>&1 || { echo "claude CLI 가 PATH 에 없다" >&2; exit 1; }

# 메모리 압박 때 Claude Code 가 유휴 세션의 백그라운드 셸(수신 감시)을 회수하지 않게 한다. 이 세션의 백그라운드 셸 전부에 걸리고 전역 설정은 건드리지 않으며, 유저가 이미 정한 값은 존중한다.
export CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP="${CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP:-1}"

exec claude ${ORCHESTRATOR_MODEL:+--model "$ORCHESTRATOR_MODEL"} "너는 agentic-knowledge-base 하네스의 **orchestrator 에이전트**다. \
먼저 $HARNESS_DIR/agents/orchestrator.md 를 끝까지 읽고, $HARNESS_DIR/README.md 의 프로토콜과 \
$PROJECT_DIR/AGENTS.md 와 $PROJECT_DIR/STYLEGUIDE.md 를 숙지한 뒤 그 명세대로만 동작하라. \
너는 유저와 직접 대화하지 않는다 — 입출력은 채널 파일을 통한다. 시작 시 수신함($HARNESS_DIR/channel/to_orchestrator)을 \
확인하고, 미처리 메시지가 없으면 scripts/watch.sh orchestrator 를 백그라운드로 돌려 새 지시를 기다려라."
