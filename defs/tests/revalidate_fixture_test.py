#!/usr/bin/env python3
"""재판정 대상(tools/revalidate.py)의 스냅숏 비교 고정물 시험 (유저 답 Q38-c).

고정물은 `defs/tests/revalidate/` 의 스냅숏 둘이다 — base 와 head 가 결정 결론 하나와 그것을 `refines` 하는 산출물 하나를 갖고,
head 의 결론만 본문 한 문장이 다르다(합성 변이). git 도 `bazel query` 도 부르지 않는다.
  dirs     양성 — `--base-dir`·`--head-dir`. 종료 1 · 링크 개체 행이 `suspect` · 바뀐 끝이 결정 결론인 것 1
  files    양성 — `--base-files`·`--head-files`. dirs 와 같은 판정이고 파일 목록이라 경로 변경을 보고하지 않는다
  same     음성 — base 와 base 를 비교한다. 종료 0 · 재판정 링크 개체 0
  partial  음성 — head 없이 base 만 준다. 입력 문제로 종료 2
사용: revalidate_fixture_test.py --case dirs|files|same|partial
"""
from __future__ import annotations

import argparse
import contextlib
import io
import sys
from pathlib import Path

from tools import revalidate

FIXTURE = Path("defs/tests/revalidate")
RESIDENCY = Path("defs/kb.bzl")
SUSPECT_ROW = "| 도착 | suspect |"


def run(argv: list[str]) -> tuple[int, str, str]:
    """revalidate.main 을 같은 프로세스에서 부른다 — (종료 코드, stdout, stderr)."""
    out, err, old = io.StringIO(), io.StringIO(), sys.argv
    sys.argv = ["revalidate.py", "--residency", str(RESIDENCY.resolve()), *argv]
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = revalidate.main()
    finally:
        sys.argv = old
    return code, out.getvalue(), err.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=("dirs", "files", "same", "partial"))
    a = ap.parse_args()
    base, head = FIXTURE / "base", FIXTURE / "head"
    argv = {"dirs": ["--base-dir", str(base), "--head-dir", str(head)],
            "files": ["--base-files", str(base / "conclusion.md"), str(base / "child.md"),
                      "--head-files", str(head / "conclusion.md"), str(head / "child.md")],
            "same": ["--base-dir", str(base), "--head-dir", str(base)],
            "partial": ["--base-dir", str(base)]}[a.case]
    code, out, err = run(argv)
    errs = []
    if a.case in ("dirs", "files"):
        if code != 1:
            errs.append(f"종료 코드 {code} ≠ 기대 1(재판정 대상 있음)")
        need = [SUSPECT_ROW, "재판정 링크 개체 1 (바뀐 끝이 결정 결론인 것 1)", "| `conclusion.md` | 본문 변경 |"]
        errs += [f"출력에 `{p}` 가 없다" for p in need if p not in out]
        if "bazel query 실패" in out or "타깃 라벨 사상" in out:
            errs.append("스냅숏 비교가 bazel 을 불렀다")
        if a.case == "files" and "경로 변경" in out:
            errs.append("파일 목록 비교가 경로 변경을 보고했다 — 파일 이름은 주소가 아니다")
    elif a.case == "same":
        if code != 0:
            errs.append(f"종료 코드 {code} ≠ 기대 0(재판정 대상 없음)")
        if "변경 청크 0 · 재판정 대상 0" not in out or "suspect |" in out.split("## 재판정 대상 링크 개체", 1)[-1]:
            errs.append("같은 스냅숏 비교가 재판정 대상이나 suspect 행을 냈다")
    else:
        if code != 2 or "CONFIG [revalidate]" not in err:
            errs.append(f"한쪽만 준 스냅숏이 입력 문제(종료 2, `CONFIG [revalidate]`)로 거부되지 않았다 — 종료 {code}")
    print(out, err)
    for e in errs:
        print(f"FAIL [{a.case}] {e}")
    print(f"{'PASS' if not errs else 'FAIL'} — revalidate 고정물 `{a.case}`")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
