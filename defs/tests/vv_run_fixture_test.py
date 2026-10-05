#!/usr/bin/env python3
"""V&V 실행기(tools/vv_run.py)의 고정물 시험 — 검증기 청크의 실행 명령을 케이스와 같은 규칙으로 실행하는 양성 (유저 답 Q29-a).

고정물은 `defs/tests/vv_run/` 의 작은 가짜 V&V 트리 하나다 — 케이스 하나(`fx-case`) · 실행 명령을 가진 검증기 하나(`fx-verifier`) ·
실행 명령 줄이 없는 검증기 하나(`fx-idle`). 명령은 읽기 전용 검증기의 도움말(`python3 tools/chunk2kg.py --help`)이라 bazel 을
중첩하지 않는다. 시험은 고정물을 TEST_TMPDIR 에 복사하고 `tools/` 를 runfiles 의 도구 디렉토리로 잇는다 — 실행의 cwd 가 트리
루트이므로 케이스·검증기가 적은 상대 경로가 그 자리에서 풀린다.
  all       선택 없이 돈다 — 종료 0. 보고에 검증기 절이 있고 `fx-verifier` 가 pass, `fx-idle` 은 실행 대상 밖으로 센다.
            실행 기록(`--record`, 임시 트리 안)에 검증기 표가 케이스 표와 따로 있고 run_evidence 의 표 읽기는 케이스 행만 읽는다
  case      `--case fx-case` 만 — 보고·기록에 검증기 절·표가 없다(케이스만의 꼴 그대로)
  verifier  `--verifier fx-verifier` 만 — 케이스 0 · 검증기 pass 로 종료 0
사용: vv_run_fixture_test.py --case all|case|verifier
"""
from __future__ import annotations

import argparse
import contextlib
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

from tools import kb_lib, run_evidence, vv_run

FIXTURE = Path("defs/tests/vv_run")
RESIDENCY = Path("defs/kb.bzl")
VERIFIER_HEAD = "## 검증기 —"


def run(root: Path, argv: list[str]) -> tuple[int, str]:
    """vv_run.main 을 같은 프로세스에서 부른다 — 출력과 종료 코드. 루트는 BUILD_WORKSPACE_DIRECTORY 로 준다(bazel run 과 같은 자리)."""
    vocab = root / "vocab.stub"  # 도움말 명령은 토큰을 세지 않는다 — 실행기의 어휘 해소(파일 존재)만 지나게 한다
    vocab.write_text("", encoding="utf-8")
    buf, old_argv, old_root = io.StringIO(), sys.argv, os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    sys.argv = ["vv_run.py", "--vocab", str(vocab), "--residency", str(RESIDENCY.resolve()), *argv]
    os.environ["BUILD_WORKSPACE_DIRECTORY"] = str(root)
    try:
        with contextlib.redirect_stdout(buf):
            code = vv_run.main()
    finally:
        sys.argv = old_argv
        if old_root is None:
            os.environ.pop("BUILD_WORKSPACE_DIRECTORY", None)
        else:
            os.environ["BUILD_WORKSPACE_DIRECTORY"] = old_root
    return code, buf.getvalue()


def record_of(root: Path) -> str:
    """임시 트리에 쓰인 실행 기록 하나의 본문."""
    runs = sorted((root / vv_run.RUN_DIR).glob("run-*.md"))
    return kb_lib.chunk_body(runs[-1].read_text(encoding="utf-8")) if runs else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=("all", "case", "verifier"))
    a = ap.parse_args()
    tmp = Path(tempfile.mkdtemp(dir=os.environ.get("TEST_TMPDIR")))
    root = tmp / "fx"
    shutil.copytree(FIXTURE, root)
    (root / "tools").symlink_to(Path("tools").resolve(), target_is_directory=True)
    argv = {"all": [], "case": ["--case", "fx-case"], "verifier": ["--verifier", "fx-verifier"]}[a.case]
    code, out = run(root, argv + ["--record"])
    body = record_of(root)
    errs = [f"종료 코드 {code} ≠ 기대 0"] if code != kb_lib.EXIT_OK else []
    if not body:
        errs.append("실행 기록이 임시 트리에 없다")
    verifier_row = "| `fx-verifier` | 1 실행 · 0 건너뜀 | pass |"
    if a.case in ("all", "verifier"):
        need = [VERIFIER_HEAD, "| `fx-verifier` |", "**pass**", "검증기 1 (pass 1 · fail 0 · skip 0)"]
        errs += [f"보고에 `{p}` 가 없다" for p in need if p not in out]
        if kb_lib.RUN_VERIFIER_TABLE_HEADER not in body or verifier_row not in body:
            errs.append(f"실행 기록에 검증기 표(`{kb_lib.RUN_VERIFIER_TABLE_HEADER}`)와 `fx-verifier` pass 행이 없다")
        read = [slug for slug, _, _ in run_evidence.run_rows(body)]
        if "fx-verifier" in read:
            errs.append("run_evidence 가 검증기 행을 케이스 행으로 읽는다 — 검증기는 verifies 가 없어 증거 쌍이 서지 않는다")
    if a.case == "all":
        if "실행 명령 줄이 없는 검증기 1건: `fx-idle`" not in out:
            errs.append("보고가 실행 명령 줄이 없는 검증기 `fx-idle` 을 실행 대상 밖으로 세지 않는다")
        if "실행 명령 줄이 없는 케이스" in out:
            errs.append("실행 명령 줄이 없는 검증기를 케이스의 결함으로 센다")
        if [slug for slug, _, _ in run_evidence.run_rows(body)] != ["fx-case"]:
            errs.append("run_evidence 의 케이스 표 읽기가 케이스 행 `fx-case` 하나를 내지 않는다")
    if a.case == "case":
        if VERIFIER_HEAD in out or vv_run.VERIFIER_DIR in out:
            errs.append("`--case` 만 준 실행의 보고에 검증기가 섞였다 — 케이스만의 꼴이어야 한다")
        if kb_lib.RUN_VERIFIER_TABLE_HEADER in body:
            errs.append("`--case` 만 준 실행의 기록에 검증기 표가 있다")
        if "| `fx-case` | 1 실행 · 0 건너뜀 | pass |" not in body:
            errs.append("실행 기록에 `fx-case` pass 행이 없다")
    if a.case == "verifier" and "케이스 0 (pass 0 · fail 0 · skip 0)" not in out:
        errs.append("`--verifier` 만 준 실행이 케이스를 실었다")
    print(out)
    for e in errs:
        print(f"FAIL [{a.case}] {e}")
    print(f"{'PASS' if not errs else 'FAIL'} — vv_run 고정물 `{a.case}`")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
