#!/usr/bin/env bash
# requirements.in → requirements_lock.txt 재생성.
# pip의 install report로 전체 폐포와 해시를 얻는다 (pip-tools 불필요).
set -euo pipefail
cd "$(dirname "$0")"
report=$(mktemp)
trap 'rm -f "$report"' EXIT
python3 -m pip install --dry-run --quiet --ignore-installed \
    --report "$report" -r requirements.in
sdists=$(mktemp -d)
trap 'rm -rf "$report" "$sdists"' EXIT
python3 - "$report" "$sdists" > requirements_lock.txt <<'EOF'
import hashlib, json, subprocess, sys, pathlib
d = json.load(open(sys.argv[1])); sd = pathlib.Path(sys.argv[2])
print("# 전체 폐포(transitive closure) 고정 — tools/relock.sh가 생성. 손으로 고치지 않는다.")
print("# 순수 파이썬 휠(py3-none-any)은 해시 하나, 플랫폼 휠인 패키지는 호스트 휠 + sdist 두 해시 —")
print("# 다른 플랫폼에서는 rules_python이 sdist를 빌드한다 (2026-09-11, PyYAML 도입).")
for it in sorted(d["install"], key=lambda x: x["metadata"]["name"].lower()):
    n, v = it["metadata"]["name"], it["metadata"]["version"]
    url = it["download_info"]["url"]
    hashes = [it["download_info"]["archive_info"]["hashes"]["sha256"]]
    if not url.endswith("py3-none-any.whl"):
        subprocess.run([sys.executable, "-m", "pip", "download", "--quiet", "--no-deps", "--no-binary", ":all:",
                        "-d", str(sd), f"{n}=={v}"], check=True)
        for f in sd.glob(f"*{v}*.tar.gz"):
            hashes.append(hashlib.sha256(f.read_bytes()).hexdigest())
    print(f"{n}=={v} \\")
    print(" \\\n".join(f"    --hash=sha256:{h}" for h in hashes))
EOF
echo "wrote requirements_lock.txt"
