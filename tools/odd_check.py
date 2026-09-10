#!/usr/bin/env python3
"""ODD 모니터링 — 실제 조건(COD)을 ODD 문서의 CHECKS 로 판정해 이탈을 보고한다 (노트 3.5절).

CHECKS.<속성>.cmd 가 있으면 실행한다 — 종료 0 = ODD 안, 1 = 이탈, 그 밖(없음·오류) = unverified.
이탈은 결함이 아니라 신호다: 기본 대응은 작업 중단 + 유저 에스컬레이션이며, 이탈 속성에 의존하는 항목이 무효화 대상이다.
사용: bazel run //tools:odd_check -- [--odd kb/odd/project-odd.yml] [--out report.md]
"""
import argparse
import os
import subprocess
from pathlib import Path

import yaml


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--odd", default="kb/odd/project-odd.yml")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    doc = yaml.safe_load((root / a.odd).read_text(encoding="utf-8"))
    checks, attrs = doc.get("CHECKS") or {}, doc.get("ATTRIBUTES") or {}
    rows, out_of, unverified = [], [], []
    for name, c in checks.items():
        cmd = c.get("cmd")
        if not cmd:
            state = "unverified"; unverified.append(name)
        else:
            r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True)
            state = "in" if r.returncode == 0 else "out" if r.returncode == 1 else "unverified"
            (out_of if state == "out" else unverified if state == "unverified" else []).append(name)
        rows.append(f"| {name} | {attrs.get(name, {}).get('title_ko', '')} | {c.get('grade')} | {state} |")
    verdict = "**ODD 이탈**" if out_of else ("모니터링 불완전 (unverified 있음)" if unverified else "정상 — 모든 속성이 ODD 안")
    rep = [f"# odd_check — {a.odd}", "", f"결과: {verdict}", "", "| 속성 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"] + rows
    if out_of: rep += ["", "이탈 속성: " + ", ".join(out_of) + " — 작업 중단 + 유저 에스컬레이션, 의존 항목 무효화 대상 (3.5절)"]
    if unverified: rep += ["", "판정 불가: " + ", ".join(unverified) + " — 판정 방법(cmd) 보완 대상"]
    text = "\n".join(rep) + "\n"
    print(text)
    if a.out: Path(a.out).write_text(text, encoding="utf-8")
    return 1 if out_of else 0


if __name__ == "__main__":
    raise SystemExit(main())
