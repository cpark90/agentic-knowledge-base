#!/usr/bin/env python3
"""두 파일이 바이트 동일한지 — 타깃별 병합 head 그래프와 union head 그래프의 대조 (bazel-dependency-review 5단계)."""
import sys
from pathlib import Path

a, b = (Path(p).read_bytes() for p in sys.argv[1:3])
if a == b:
    print(f"OK 동일 {len(a)} bytes")
    sys.exit(0)
import difflib
al, bl = a.decode("utf-8").splitlines(), b.decode("utf-8").splitlines()
print("FAIL [kg-equivalence] 병합 결과가 union 과 다르다:")
print("\n".join(list(difflib.unified_diff(bl, al, "union", "merge", lineterm="", n=1))[:40]))
sys.exit(1)
