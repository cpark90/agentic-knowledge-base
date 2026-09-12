#!/usr/bin/env python3
"""두 파일이 바이트 동일한지 — 타깃별 병합 head 그래프와 union head 그래프의 대조 (bazel-dependency-review 5단계).

출력·종료: 다르면 `FAIL [kg-equivalence] <병합본>: …` + 첫 40줄 diff + EXIT_FAIL. 인자 부족·파일 없음은 EXIT_CONFIG.
사용: same_bytes.py <병합본> <union본>
"""
import sys
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)
TAG = "kg-equivalence"


def main() -> int:
    if len(sys.argv) != 3:
        print(f"FAIL [{TAG}] 인자는 <병합본> <union본> 둘이어야 한다: {sys.argv[1:]}")
        return EXIT_CONFIG
    merged_path, union_path = sys.argv[1:3]
    try:
        a, b = Path(merged_path).read_bytes(), Path(union_path).read_bytes()
    except OSError as e:
        print(f"FAIL [{TAG}] {getattr(e, 'filename', merged_path)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    if a == b:
        print(f"PASS [{TAG}] — 동일 {len(a)} bytes")
        return 0
    import difflib
    al, bl = a.decode("utf-8").splitlines(), b.decode("utf-8").splitlines()
    print(f"FAIL [{TAG}] {merged_path}: 병합 결과가 union {union_path} 과 다르다 — 조각 병합(kb_kg_merge)과 union(chunk2kg) 이 같은 바이트여야 한다")
    print("\n".join(list(difflib.unified_diff(bl, al, "union", "merge", lineterm="", n=1))[:40]))
    return EXIT_FAIL


if __name__ == "__main__":
    sys.exit(main())
