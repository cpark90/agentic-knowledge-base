#!/usr/bin/env python3
"""인수 — 쓰기 권한이 있는 역할이 검토한 청크에 OKF verified 를 붙인다 (writer 검사의 해소 수단).

hci 가 만든 청크(generated.by: hci/…)는 그 plane 을 쓸 수 있는 역할(orchestrator 등)의 verified 가 있어야 게이트를
통과한다. 이 도구는 검토를 대신하지 않는다 — 검토한 역할이 자기 이름으로 돌린다.
사용: bazel run //tools:endorse -- --by orchestrator/claude-fable-5 --at 2026-09-11T10:00:00+09:00 <청크 파일...>
"""
import argparse
import os
import re
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", required=True, help="<역할>/<모델> — 카탈로그에 있는, 그 plane 을 쓰는 역할")
    ap.add_argument("--at", required=True, help="ISO 8601")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    for f in a.files:
        p = root / f
        t = p.read_text(encoding="utf-8")
        entry = f"{{by: {a.by}, at: {a.at}}}"
        m = re.search(r"^verified: \[(.*)\]$", t, re.M)
        if m:
            if a.by in m.group(1):
                continue
            t = t.replace(m.group(0), f"verified: [{m.group(1)}, {entry}]")
        else:
            t = re.sub(r"^(generated: .*)$", r"\1\nverified: [" + entry + "]", t, count=1, flags=re.M)
        p.write_text(t, encoding="utf-8")
        print(f"{f}: verified by {a.by}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
