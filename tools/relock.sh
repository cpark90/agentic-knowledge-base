#!/usr/bin/env bash
# requirements.in → requirements_lock.txt 재생성.
# pip의 install report로 전체 폐포와 해시를 얻는다 (pip-tools 불필요).
set -euo pipefail
cd "$(dirname "$0")"
report=$(mktemp)
trap 'rm -f "$report"' EXIT
python3 -m pip install --dry-run --quiet --ignore-installed \
    --report "$report" -r requirements.in
python3 - "$report" > requirements_lock.txt <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
print("# 전체 폐포(transitive closure) 고정 — tools/relock.sh가 생성. 손으로 고치지 않는다.")
print("# 모든 패키지가 py3-none-any 순수 파이썬 휠이므로 플랫폼 독립이다.")
for it in sorted(d["install"], key=lambda x: x["metadata"]["name"].lower()):
    n, v = it["metadata"]["name"], it["metadata"]["version"]
    h = it["download_info"]["archive_info"]["hashes"]["sha256"]
    print(f"{n}=={v} \\\n    --hash=sha256:{h}")
EOF
echo "wrote requirements_lock.txt"
