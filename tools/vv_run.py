#!/usr/bin/env python3
"""V&V executor — 케이스의 실행 명령 중 허용 목록의 양성 명령을 실행하고 결과를 실행 기록으로 남긴다 (노트 8.20절 executor,
r-026 관측은 append-only 실행 기록, p0-run-as-observation `agt:Run`, p8-vv-plane-instances memory = 실행 기록, p8-reproducibility).

케이스(`kb/vv/case/*.md`)마다 본문의 `**실행 명령**` 줄(코드 스팬 하나가 명령이다)을 읽어 명령을 `;`·`&&` 로 나눈다. **허용 목록(`bazel test`·`bazel build`·`bazel query`·
`python3 tools/gen_build.py --check`)으로 시작하는 읽기 전용 검증기만 실행한다**. 그 밖(임시 파일 자극 · 그 밖의 `python3 …` · `bazel run …`)은
실행하지 않고 SKIP 으로 적는다. 임시 파일(`/tmp/vv-*`)을 요구하는 자극은 프로즈에 구조만 있어 자동 생성할 수 없다. **SKIP 은 PASS 가 아니다**
(docs/tools.md 실패 종류 3).
케이스 판정: 실행한 명령 전부 종료 0 → pass · 하나라도 비영 → fail · 실행한 명령 없음 → skip.
재현성 기록 (p8-reproducibility 초기 상태·환경): 리비전(`git rev-parse --short HEAD`, 워킹트리 변경 여부) · 시각(UTC) · bazel·python 버전 ·
명령마다 종료 코드·소요. 난수 seed 는 없다 — 명령은 결정적이다.

--record 는 실행 기록을 관측(memory plane, concrete, append-only)으로 kb/vv/run/run-<UTC>.md 에 쓴다 — generated.by 는 역할이 아닌
`process:vv_run` 이라 writer 검사 밖이다(카탈로그의 executor 하위 역할을 도구가 맡는 첫 형태). 이미 있는 파일은 덮지 않는다.
생성 뒤 python3 tools/gen_build.py --root . 로 BUILD 를 갱신하고 bazel test //... 를 돌린다.
케이스가 `bazel test` 를 부르므로 `bazel run` 안에서는 중첩 실행이 된다 — odd_check 의 language_policy 와 같은 형태다. 문제가 나면
`bazel run` 밖에서 python3 tools/vv_run.py 로 돌린다.

사용: bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--out report.md]
      python3 tools/vv_run.py [--record] [--case <슬러그>…]
종료: fail 있음 1 (EXIT_FAIL) · 전부 pass 0 (EXIT_OK) · pass 없이 skip 만 3 (EXIT_SKIP) · 입력 문제 2 (EXIT_CONFIG)
"""
from __future__ import annotations

import argparse
import os
import platform
import re
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 네임스페이스·종료 코드·실행 기록 규약의 단일 정의처
from chunk2kg import parse_chunk  # noqa: E402 — 케이스의 frontmatter(라벨)는 chunk2kg 의 파서로 읽는다

ID = kb_lib.ID
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
CASE_DIR = kb_lib.KB_VV + "/case"
RUN_DIR = kb_lib.VV_RUN_DIR
GENERATOR = kb_lib.RUN_GENERATOR
ODD_IRI = str(ID["odd-agentic-knowledge-base"])  # 관측의 출처 — ODD 개체 (assume_check 와 같은 sources)
ASSUMPTIONS = [str(ID["asm-bazel-toolchain"]), str(ID["asm-chunk-conventions"])]  # 실행은 bazel 툴체인과 청크 규약을 전제한다
MAX_BODY_LINES = 42
# 케이스 본문의 실행 명령 줄 — `**실행 명령**` 뒤 대시, 그 뒤 코드 스팬 하나. 스팬 안의 전부가 명령이다
COMMAND_LINE = re.compile(r"^\*\*실행 명령\*\*\s*—\s*`(.+)`\s*$")
SPLIT = re.compile(r"\s*(?:;|&&)\s*")  # 순차 연산자 — 각 조각을 따로 판정한다
# 실행하는 양성 명령의 허용 목록 — 전부 읽기 전용 검증기다. 그 밖(bazel run · 임시 파일 자극 · 다른 python3)은 SKIP
POSITIVE_PREFIXES = ("bazel test ", "bazel build ", "bazel query ", "python3 tools/gen_build.py --check")
EXECUTED = re.compile(r"Executed (\d+) out of (\d+) tests?")  # bazel test 요약 — 실행 수 / 전체 수. 나머지는 캐시 재사용 (재현성의 근거)


def classify(cmd: str) -> str | None:
    """명령 하나의 SKIP 사유 — 실행 대상(bazel test)이면 None."""
    if "/tmp/" in cmd:
        return "임시 파일 자극 — 프로즈에 구조만 있어 자동 생성 불가"
    if cmd.startswith(POSITIVE_PREFIXES):
        return None
    head = " ".join(cmd.split()[:2])
    return f"`{head}` — 실행 대상은 허용 목록의 읽기 전용 검증기뿐"


def load_cases(root: Path, only: list[str]) -> tuple[list[dict], list[str]]:
    """케이스 파일 → [{slug, path, label, iri, commands: [{cmd, skip}]}], 실행 명령 줄이 없는 케이스 목록."""
    files = sorted((root / CASE_DIR).glob("*.md"))
    if only:
        files = [f for f in files if f.stem in only]
    cases, missing = [], []
    for f in files:
        meta, _ = parse_chunk(str(f))
        body = kb_lib.chunk_body(f.read_text(encoding="utf-8"))
        line = next((m for ln in body.splitlines() if (m := COMMAND_LINE.match(ln.strip()))), None)
        if line is None:
            missing.append(f.stem)
            continue
        cmds = [c for c in SPLIT.split(line.group(1).strip()) if c]
        cases.append({"slug": f.stem, "path": f.as_posix(), "label": meta["title_ko"], "iri": meta["id"], "status": meta["status"],
                      "commands": [{"cmd": c, "skip": classify(c)} for c in cmds]})
    return cases, missing


def run_command(cmd: str, root: Path) -> dict:
    """셸로 실행 — 워크스페이스 루트에서. 종료 코드·소요·출력 꼬리를 남긴다."""
    t0 = time.monotonic()
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True)
    out = r.stdout + r.stderr
    tail = "\n".join(out.strip().splitlines()[-6:])
    m = EXECUTED.search(out)
    tests = (int(m.group(2)), int(m.group(1))) if m else None  # (전체, 실행) — 없으면 요약 줄이 없는 실패
    return {"rc": r.returncode, "secs": time.monotonic() - t0, "tail": tail, "tests": tests}


def tests_note(commands: list[dict]) -> str:
    """케이스의 실행 명령이 돌린 테스트 수와 캐시 재사용 수 — `테스트 3 · 캐시 3`. 요약 줄이 없으면 빈 문자열."""
    ran = [c for c in commands if c["skip"] is None and c.get("tests")]
    if not ran:
        return ""
    total = sum(c["tests"][0] for c in ran)
    executed = sum(c["tests"][1] for c in ran)
    return f"테스트 {total} · 캐시 {total - executed}"


def execute(cases: list[dict], root: Path) -> None:
    """케이스마다 실행 대상 명령을 순서대로 돌리고 판정을 붙인다 (제자리 갱신)."""
    for case in cases:
        for c in case["commands"]:
            if c["skip"] is None:
                c.update(run_command(c["cmd"], root))
        ran = [c for c in case["commands"] if c["skip"] is None]
        case["verdict"] = "skip" if not ran else "fail" if any(c["rc"] != 0 for c in ran) else "pass"
        case["secs"] = sum(c["secs"] for c in ran)


def revision(root: Path) -> tuple[str, bool]:
    """(짧은 리비전, 워킹트리에 추적 파일 변경이 있는가). git 밖이면 ('없음', False)."""
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=root, capture_output=True, text=True,
                                    check=True).stdout.strip())
        return rev, dirty
    except (OSError, subprocess.CalledProcessError):
        return "없음", False


def environment(root: Path) -> str:
    """환경 한 줄 — bazel·python 버전과 OS. p8-reproducibility 의 환경 구성."""
    try:
        bazel = subprocess.run(["bazel", "--version"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        bazel = "bazel 없음"
    return f"{bazel} · python {platform.python_version()} · {platform.system().lower()}"


def counts(cases: list[dict]) -> dict:
    return {v: sum(1 for c in cases if c["verdict"] == v) for v in kb_lib.RUN_VERDICTS}


def observation(now: datetime, cases: list[dict], rev: str, dirty: bool, env: str) -> str:
    """실행 기록 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory). frontmatter 는 assume_check 의 관측과 같은 형식이다."""
    stamp = now.strftime("%Y-%m-%dT%H:%MZ")
    n = counts(cases)
    ko = f"V&V 실행 {stamp}: pass {n['pass']} · fail {n['fail']} · skip {n['skip']}"
    en = f"V&V run {stamp}: {n['pass']} pass, {n['fail']} fail, {n['skip']} skip"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {now.isoformat(timespec='seconds')}}}", "---"]
    n_ran = sum(1 for c in cases for x in c["commands"] if x["skip"] is None)
    n_skipped = sum(1 for c in cases for x in c["commands"] if x["skip"] is not None)
    body = [f"**관측** — {now.isoformat(timespec='seconds')} 에 `vv_run` 이 케이스 {len(cases)}건의 실행 명령 {n_ran + n_skipped}건 중 "
            f"허용 목록의 양성 명령 {n_ran}건을 실행했다. 리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else '없음'}) · {env} · seed 없음.", "",
            kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        skipped = len(c["commands"]) - ran
        note = tests_note(c["commands"])
        body.append(f"| `{c['slug']}` | {ran} 실행 · {skipped} 건너뜀{' (' + note + ')' if note else ''} | {c['verdict']} | {c['secs']:.1f}s |")
    skips = [(c["slug"], x) for c in cases for x in c["commands"] if x["skip"] is not None]
    if skips:
        body += ["", "| 케이스 | 건너뛴 명령 | 사유 |", "|---|---|---|"]
        rows = [f"| `{slug}` | `{x['cmd'][:60]}{'…' if len(x['cmd']) > 60 else ''}` | {x['skip']} |" for slug, x in skips]
        budget = MAX_BODY_LINES - len(body) - 3  # 남는 줄 — 요약 2줄과 여유
        if len(rows) > budget:
            rows = rows[:max(budget - 1, 0)] + [f"| … | 외 {len(rows) - max(budget - 1, 0)}건 | 보고(`vv_run` 출력)에 전부 있다 |"]
        body += rows
    body += ["", f"판정 요약 — pass {n['pass']} · fail {n['fail']} · skip {n['skip']}. SKIP 은 PASS 가 아니다. "
             f"판정은 실행한 명령의 종료 코드로만 했고 기대 문구는 대조하지 않았다."]
    return "\n".join(head + body) + "\n"


def report(now: datetime, cases: list[dict], missing: list[str], rev: str, dirty: bool, env: str) -> str:
    n = counts(cases)
    verdict = ("**fail 있음**" if n["fail"] else "pass 없음 — 전부 skip" if not n["pass"] else "pass" + (" (skip 있음)" if n["skip"] else ""))
    rep = kb_lib.gendoc_header(
        "vv_run", "V&V 케이스 실행 판정", "tools/vv_run.py",
        "V&V 케이스 청크(`kb/vv/case/`)의 실행 명령 중 허용 목록의 양성 명령만 실제로 돌려 케이스마다 pass·fail·skip 을 — "
        "SKIP 은 PASS 가 아니다 (8.20절)",
        "bazel run //tools:vv_run", [c["path"] for c in cases],
        f"케이스 {len(cases)} (pass {n['pass']} · fail {n['fail']} · skip {n['skip']})",
        kb_lib.gendoc_view_notice("V&V 케이스 청크의 본문"), input_kind="케이스 파일",
        extra=[f"- 결과: {verdict}",
               f"- 초기 상태: 리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else kb_lib.NONE_MARK}) · {env}"])
    body = ["## 케이스 — 실행 대상은 허용 목록의 양성 명령뿐. SKIP 은 PASS 가 아니다", "",
            "| 케이스 | 라벨 | 명령 | 결과 | 소요 |", "|---|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        body.append(f"| `{c['slug']}` | {c['label']} | {ran} 실행 · {len(c['commands']) - ran} 건너뜀 | **{c['verdict']}** | {c['secs']:.1f}s |")
    body += ["", "## 명령", "", "| 케이스 | 명령 | 종료 | 소요 | 비고 |", "|---|---|---|---|---|"]
    for c in cases:
        for x in c["commands"]:
            if x["skip"] is None:
                t = x.get("tests")
                note = (f"테스트 {t[0]} · 실행 {t[1]} · 캐시 {t[0] - t[1]}" if t else "요약 줄 없음" if x["cmd"].startswith("bazel test ") else "") + ("" if x["rc"] == 0 else " · 실패")
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | {x['rc']} | {x['secs']:.1f}s | {note} |")
            else:
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | SKIP | — | {x['skip']} |")
    failed = [(c["slug"], x) for c in cases for x in c["commands"] if x["skip"] is None and x["rc"] != 0]
    if failed:
        body += ["", "## 실패한 명령의 출력 꼬리", ""]
        for slug, x in failed:
            body += [f"### `{slug}` — `{x['cmd']}` (종료 {x['rc']})", "", "```", x["tail"], "```", ""]
    if missing:
        body += ["", f"실행 명령 줄이 없는 케이스 {len(missing)}건: " + ", ".join(f"`{m}`" for m in missing) + " — 케이스 본문에 `**실행 명령**` 줄(대시 뒤 코드 스팬 하나)이 있어야 한다"]
    return kb_lib.gendoc_assemble(rep, body, [c["path"] for c in cases], input_kind="케이스 파일")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", action="append", default=[], metavar="SLUG", help="이 케이스(파일 stem)만 — 반복 가능")
    ap.add_argument("--record", action="store_true", help=f"결과를 실행 기록으로 {RUN_DIR}/run-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    if not (root / CASE_DIR).is_dir():
        print(f"FAIL [vv_run] {CASE_DIR}: 케이스 디렉토리가 없다 — 워크스페이스 루트에서 돌린다")
        return EXIT_CONFIG
    try:
        cases, missing = load_cases(root, a.case)
    except ValueError as e:  # parse_chunk 의 frontmatter 규칙 — 케이스가 청크가 아니면 실행할 수 없다
        print(f"FAIL [vv_run] {e}")
        return EXIT_CONFIG
    unknown = sorted(set(a.case) - {c["slug"] for c in cases} - set(missing))
    if unknown:
        print(f"FAIL [vv_run] --case 대상이 {CASE_DIR} 에 없다: {', '.join(unknown)}")
        return EXIT_CONFIG
    if not cases:
        print(f"SKIP [vv_run] {CASE_DIR}: 실행할 케이스가 없다")
        return EXIT_SKIP

    now = datetime.now(timezone.utc).replace(microsecond=0)
    rev, dirty = revision(root)
    env = environment(root)
    execute(cases, root)
    text = report(now, cases, missing, rev, dirty, env)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")

    if a.record:
        run_dir = root / RUN_DIR
        run_dir.mkdir(parents=True, exist_ok=True)
        target = run_dir / f"run-{now.strftime('%Y%m%dT%H%M%SZ')}.md"
        if target.exists():
            print(f"FAIL [vv_run] {target.relative_to(root)}: 이미 있다 — 실행 기록은 append-only 다 (r-026)")
            return EXIT_CONFIG
        target.write_text(observation(now, cases, rev, dirty, env), encoding="utf-8")
        print(f"실행 기록: {target.relative_to(root)} — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    n = counts(cases)
    return EXIT_FAIL if n["fail"] else EXIT_OK if n["pass"] else EXIT_SKIP


if __name__ == "__main__":
    raise SystemExit(main())
