#!/usr/bin/env bash
# requirements.in → requirements_lock.txt 재생성.
# pip의 install report로 전체 폐포와 해시를 얻는다 (pip-tools 불필요).
# 해석은 호스트 인터프리터가 아니라 **툴체인의 파이썬**(MODULE.bazel의 python.toolchain)으로 한다 —
# 호스트가 3.12여도 bazel이 받는 휠은 cp311이고, 그 둘이 갈리면 lock에 없는 휠을 pip가 거부하거나
# sdist 빌드로 떨어진다 (2026-10-01, tiktoken 도입에서 드러났다).
# 기존 pin은 보존한다: 현재 lock의 `name==version`을 제약으로 넣어 requirements.in이 직접 올리지 않은
# 패키지의 버전이 재생성만으로 움직이지 않게 한다 — lock은 가산적이다.
set -euo pipefail
cd "$(dirname "$0")"
py=$(grep -oE 'python_version = "[0-9]+\.[0-9]+"' ../MODULE.bazel | head -1 | grep -oE '[0-9]+\.[0-9]+')
report=$(mktemp)
constraints=$(mktemp)
sdists=$(mktemp -d)
target=$(mktemp -d)
trap 'rm -rf "$report" "$constraints" "$sdists" "$target"' EXIT
direct=$(grep -oE '^[A-Za-z0-9_.-]+' requirements.in | tr 'A-Z_' 'a-z-' | sort -u)
grep -oE '^[A-Za-z0-9_.-]+==[0-9][^ \\]*' requirements_lock.txt \
  | while IFS= read -r line; do
      name=$(printf '%s' "${line%%==*}" | tr 'A-Z_' 'a-z-')
      grep -qx "$name" <<<"$direct" || printf '%s\n' "$line"
    done > "$constraints"
python3 -m pip install --dry-run --quiet --ignore-installed \
    --python-version "$py" --only-binary=:all: --target "$target" \
    --report "$report" -r requirements.in -c "$constraints"
python3 - "$report" "$sdists" "$py" > requirements_lock.txt <<'EOF'
import hashlib, json, subprocess, sys, pathlib
d = json.load(open(sys.argv[1])); sd = pathlib.Path(sys.argv[2]); py = sys.argv[3]
print("# 전체 폐포(transitive closure) 고정 — tools/relock.sh가 생성. 손으로 고치지 않는다.")
print(f"# 순수 파이썬 휠(py3-none-any)은 해시 하나, 플랫폼 휠인 패키지는 cp{py.replace('.','')} 휠 + sdist 두 해시 —")
print("# 다른 플랫폼에서는 rules_python이 sdist를 빌드한다 (2026-09-11, PyYAML 도입).")
print("# 해석은 툴체인 파이썬 " + py + " 기준이다 (2026-10-01, tiktoken 도입).")
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
