#!/usr/bin/env python3
"""실행기 환경 격리 게이트 — 케이스의 명령이 실행기의 파이썬 문맥을 물려받지 않는지 `bazel test` 안에서 판정한다
(결정 p8-verifier-env-isolation, 주석 runner-env-leaks-into-case).

실행기를 어떻게 불렀는가가 케이스의 판정을 바꾸면 그 판정은 재현이 아니다. `bazel run //tools:vv_run` 의 스텁이
`PYTHONSAFEPATH=1` 을 두던 때 케이스가 부르는 검증기는 `import kb_lib` 에서 `ModuleNotFoundError` 로 죽었고
`python3 tools/vv_run.py` 는 같은 케이스를 통과시켰다. `vv_run.clean_env()` 가 그 문맥을 걷어낸다.

**이 게이트는 실행기 전체가 아니라 환경 격리만 판정한다.** 케이스가 `bazel test` 를 부르므로 실행기 전체는
테스트 타깃 안에서 돌릴 수 없다(중첩 실행). 그러나 `clean_env()` 와 `run_command()` 는 bazel 을 부르지 않는다 —
판정 대상을 격리의 동작으로 좁히면 중첩 없이 `bazel test //...` 안에 든다.

판정하는 것은 셋이다.
1. 걷어내는 변수 목록이 규약의 다섯과 정확히 같고, `clean_env()` 가 그 다섯을 **전부** 지운다.
   기대 목록은 이 파일이 자기 상수로 갖는다 — 대상 코드에서 읽으면 목록이 비어도 통과한다.
2. `PYTHONSAFEPATH=1` 을 둔 부모에서 `run_command` 로 읽기 전용 검증기를 실제 하위 프로세스로 띄워 종료 0 이다.
   격리가 없으면 `ModuleNotFoundError` 로 종료 1 이 난다.
3. 하위 프로세스의 작업 디렉토리가 실행기에 건넨 워크스페이스 루트다. 테스트 프로세스의 cwd 를 딴 곳으로 옮겨 놓고
   재므로 상속이 아니라 `cwd=root` 임이 드러난다. 실행기의 루트는 `BUILD_WORKSPACE_DIRECTORY` 다(vv_run.py main).

사용: bazel test //tools:vv_run_env_test
      python3 tools/vv_run_env_test.py [--probe chunk_lint]
종료: 위반 있음 1 (EXIT_FAIL) · 없음 0 (EXIT_OK)
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 종료 코드 규약의 단일 정의처
import vv_run  # noqa: E402 — 판정 대상. clean_env·run_command 는 bazel 을 부르지 않는다

GATE = "vv-run-env"
# 규약이 걷어내는 다섯. **이 목록은 이 파일이 자기 기대로 갖는다** — vv_run.BAZEL_PY_ENV 에서 읽으면 그 목록이
# 비거나 줄어도 이 검사가 통과해 아무것도 판정하지 않는다 (결정 p8-verifier-env-isolation 의 결론 문장이 원본이다)
EXPECTED_ENV = ("PYTHONSAFEPATH", "PYTHONPATH", "PYTHONHOME", "RUNFILES_DIR", "RUNFILES_MANIFEST_FILE")
SENTINEL = "VV_RUN_ENV_SENTINEL"  # 격리가 환경 전체를 비우지 않고 다섯만 걷어내는지 — PATH 가 사라지면 검증기가 돌지 않는다
CWD_PROBE = 'python3 -c "import os; print(os.getcwd())"'


# ── 환경 오염 주입과 세 검사 ────────────────────

def poison(names: tuple[str, ...]) -> None:
    """부모 환경에 실행기의 bazel 파이썬 문맥을 심는다 — 실제 `bazel run` 이 하위 프로세스에 넘기던 값이다."""
    for n in names:
        os.environ[n] = "1" if n == "PYTHONSAFEPATH" else "/nonexistent/vv-run-env"
    os.environ[SENTINEL] = "keep"


def check_strip() -> list[str]:
    """① 걷어내는 목록이 규약의 다섯과 같고 clean_env 가 그 다섯을 전부 지운다."""
    msgs, declared = [], tuple(vv_run.BAZEL_PY_ENV)
    missing = [n for n in EXPECTED_ENV if n not in declared]
    extra = [n for n in declared if n not in EXPECTED_ENV]
    if missing:
        msgs.append(f"FAIL [{GATE}] vv_run.BAZEL_PY_ENV: {', '.join(missing)} 이 없다 — "
                    "결정 p8-verifier-env-isolation 은 다섯을 전부 걷어낸다. 목록을 줄이려면 결정을 먼저 고친다")
    if extra:
        msgs.append(f"FAIL [{GATE}] vv_run.BAZEL_PY_ENV: {', '.join(extra)} 은 결정에 없다 — "
                    "걷어낼 변수를 늘리려면 결정 p8-verifier-env-isolation 과 이 검사의 기대를 같은 커밋에서 고친다")
    poison(EXPECTED_ENV)
    env = vv_run.clean_env()
    left = [n for n in EXPECTED_ENV if n in env]
    if left:
        msgs.append(f"FAIL [{GATE}] clean_env(): {', '.join(left)} 이 남았다 — "
                    "케이스의 명령이 실행기의 파이썬 문맥을 물려받는다")
    if env.get(SENTINEL) != "keep":
        msgs.append(f"FAIL [{GATE}] clean_env(): 다섯 밖의 변수 {SENTINEL} 까지 사라졌다 — "
                    "격리는 환경을 비우는 것이 아니라 다섯을 걷어내는 것이다")
    return msgs


def check_subprocess(root: Path, probe: str) -> list[str]:
    """② PYTHONSAFEPATH=1 을 둔 부모에서 실제 하위 프로세스를 띄워 검증기가 종료 0 을 낸다."""
    poison(EXPECTED_ENV)
    cmd = f"python3 tools/{probe}.py --help"
    r = vv_run.run_command(cmd, root)
    if r["rc"] != 0:
        return [f"FAIL [{GATE}] {cmd}: 종료 {r['rc']} — 부모의 파이썬 문맥이 하위 프로세스로 샌다. "
                f"격리가 없으면 검증기는 자극에 닿기 전에 죽는다:\n{r['tail']}"]
    return []


def check_cwd(root: Path) -> list[str]:
    """③ 하위 프로세스의 작업 디렉토리가 건넨 루트다 — 테스트 프로세스의 cwd 를 딴 곳에 두고 잰다."""
    here = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="vv-env-") as elsewhere:
        os.chdir(elsewhere)
        try:
            r = vv_run.run_command(CWD_PROBE, root)
        finally:
            os.chdir(here)
    got = Path(r["out"].strip()).resolve()
    if r["rc"] != 0 or got != root.resolve():
        return [f"FAIL [{GATE}] {CWD_PROBE}: 작업 디렉토리가 {got} 다 — 워크스페이스 루트 {root.resolve()} 여야 "
                "케이스가 적은 상대 경로가 자극에 닿는다"]
    return []


# ── 판정과 보고 ────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", default="chunk_lint", metavar="VERIFIER",
                    help="하위 프로세스로 띄울 읽기 전용 검증기 — tools/<이름>.py --help 를 부른다")
    a = ap.parse_args()
    root = Path.cwd()  # bazel test 는 runfiles 루트가, 손으로 돌리면 워크스페이스 루트가 cwd 다
    if a.probe not in vv_run.READ_ONLY_VERIFIERS:
        print(f"FAIL [{GATE}] --probe {a.probe}: 허용 목록(vv_run.READ_ONLY_VERIFIERS) 밖이다 — "
              "격리를 재는 자극은 읽기 전용 검증기여야 한다")
        return kb_lib.EXIT_CONFIG
    if not (root / "tools" / f"{a.probe}.py").is_file():
        print(f"FAIL [{GATE}] tools/{a.probe}.py: 없다 — 워크스페이스 루트(또는 runfiles 루트)에서 돌린다")
        return kb_lib.EXIT_CONFIG
    msgs = check_strip() + check_subprocess(root, a.probe) + check_cwd(root)
    for m in msgs:
        print(m)
    if msgs:
        return kb_lib.EXIT_FAIL
    print(f"OK [{GATE}] 걷어내는 변수 {len(EXPECTED_ENV)} · 검증기 {a.probe} 종료 0 · 작업 디렉토리 {root.resolve()}")
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
