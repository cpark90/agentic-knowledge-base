#!/usr/bin/env python3
"""인수 — 쓰기 권한이 있는 역할이 검토한 청크에 OKF verified 를 붙인다 (writer 검사의 해소 수단).

hci 가 만든 청크(generated.by: hci/…)는 그 plane 을 쓸 수 있는 역할(orchestrator 등)의 verified 가 있어야 게이트를
통과한다. 이 도구는 검토를 대신하지 않는다 — 검토한 역할이 자기 이름으로 돌린다.
`--at` 이 지금보다 뒤이면 `FAIL [endorse]` 로 거부한다 — 미래 시각의 도장은 검토보다 앞선 인수를 꾸밀 수 있고, 게이트는
시계에 의존할 수 없어(재현성) 이 판정은 쓰는 시점에만 할 수 있다.
사용: bazel run //tools:endorse -- --by orchestrator/claude-fable-5 --at 2026-09-11T10:00:00+09:00 <청크 파일...>
"""
import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib 다
    from tools import kb_lib
except ImportError:
    import kb_lib

TAG = kb_lib.ENDORSE_TAG  # 도구 태그 — 게이트가 아니다 (defs/kb.bzl 의 TOOL_TAGS)


def future_at(at: str) -> str:
    """`--at` 이 읽히지 않거나 지금보다 뒤이면 거부 사유를, 아니면 빈 문자열을 낸다. 시간대가 없으면 지역 시각으로 읽는다."""
    try:
        when = datetime.fromisoformat(at.strip().replace("Z", "+00:00"))
    except ValueError:
        return f"--at {at!r} 이 ISO 8601 이 아니다"
    when = when.astimezone() if when.tzinfo is None else when
    now = datetime.now(timezone.utc)
    if when > now:
        return f"--at {at} 이 지금({now.isoformat(timespec='seconds')})보다 뒤다 — 도장 시각은 `date -Iseconds` 실측값을 쓴다"
    return ""


# ── 검토한 청크에 verified 를 붙인다 ────────────────────

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", required=True, help="<역할>/<모델> — 카탈로그에 있는, 그 plane 을 쓰는 역할")
    ap.add_argument("--at", required=True, help="ISO 8601")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    reason = future_at(a.at)
    if reason:
        print(f"FAIL [{TAG}] {reason}", file=sys.stderr)
        return kb_lib.EXIT_FAIL
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
