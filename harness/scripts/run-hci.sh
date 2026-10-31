#!/usr/bin/env bash
# 옛 이름의 기동 경로다. hci 는 interpreter 의 유저 대상 하위 역할이고 같은 세션이 맡으므로, run-interpreter.sh 를 그대로 부른다.
# 그래서 이 스크립트로 띄워도 같은 지침(agents/interpreter.md)의 같은 세션이 뜬다.
set -euo pipefail
exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/run-interpreter.sh" "$@"
