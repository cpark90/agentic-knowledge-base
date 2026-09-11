#!/usr/bin/env python3
"""영향 분석 1단계 — 변경 전에 "X를 바꾸면 무엇이 영향받는가"를 Bazel 의존 그래프에서 계산한다 (노트 12.6절, method §12).

링크가 deps 이므로 `bazel query rdeps(//kb/..., X)` 가 직접·전이 의존 집합이다. 네 수치를 낸다 —
영향 항목 수 · plane 분포 · suspect 가 될 링크 수(직접 의존자 수) · 유저 승인이 필요한 결정 수.
의미 판정(가정·무효화 전파)은 그래프 질의의 몫이고 이것은 구조 근사다.
사용: bazel run //tools:impact -- //kb/dev/requirement:r-008-every-requirement-descends [--universe //kb/...]
"""
import argparse
import os
import subprocess
import sys
from collections import Counter


def q(expr: str, cwd: str) -> list[str]:
    r = subprocess.run(["bazel", "query", expr, "--noshow_progress", "--output=label"], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr); raise SystemExit(f"impact: bazel query 실패: {expr}")
    return [l for l in r.stdout.split("\n") if l.startswith("//")]


def plane_of(label: str) -> str:
    pkg = label.split(":")[0]
    return {"//kb/dev/requirement": "requirement", "//kb/dev/decision": "decision", "//chunks/decision": "decision(deprecated)"}.get(pkg, pkg.split("/")[-1] or "?")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--universe", default="//kb/... + //chunks/...")
    a = ap.parse_args()
    cwd = os.environ.get("BUILD_WORKSPACE_DIRECTORY", ".")
    is_item = lambda l: ":kg" not in l and not l.endswith(":bodies") and l != a.target
    direct = [l for l in q(f"rdeps({a.universe}, {a.target}, 1)", cwd) if is_item(l)]
    trans = [l for l in q(f"rdeps({a.universe}, {a.target})", cwd) if is_item(l)]
    planes = Counter(plane_of(l) for l in trans)
    decisions = [l for l in trans if plane_of(l).startswith("decision") and "deprecated" not in plane_of(l)]
    print(f"# impact — {a.target}\n")
    print(f"- 영향 항목(전이): **{len(trans)}** · 직접 의존자(= suspect 가 될 링크): **{len(direct)}**")
    print("- plane 분포: " + (" · ".join(f"{k} {v}" for k, v in planes.most_common()) or "없음"))
    print(f"- 유저 승인이 필요한 결정: **{len(decisions)}** (decision 은 유저 승인이 stable 전이 조건, 5.4절)")
    print(f"- 자율 진행 범위: {'안' if not decisions else '**밖** — 승인 필요 수가 0이 아니다'} (method §12)\n")
    for l in sorted(direct)[:40]:
        print(f"  - {l}")
    if len(direct) > 40:
        print(f"  … 외 {len(direct)-40}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
