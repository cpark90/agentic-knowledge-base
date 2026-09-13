#!/usr/bin/env python3
"""ODD 모니터링 — 실제 조건(COD)을 ODD 문서의 CHECKS 로 판정해 이탈을 보고한다 (노트 3.5절).

CHECKS.<속성>.cmd 가 있으면 실행한다 — 종료 0 = ODD 안, 1 = 이탈, 그 밖(없음·오류) = unverified.
이탈은 결함이 아니라 신호다: 기본 대응은 작업 중단 + 유저 에스컬레이션이며, 이탈 속성에 의존하는 항목이 무효화 대상이다.
판정 함수(load_odd·judge_condition·judge_all)는 assume_check 가 재사용한다 — 가정의 판정식은 참조 조건 판정의 연언이다.
사용: bazel run //tools:odd_check -- [--odd kb/odd/project-odd.yml] [--out report.md]
"""
import argparse
import os
import subprocess
from pathlib import Path

import yaml

STATES = ("in", "out", "unverified")
ID_BASE = "https://agentic-knowledge-base.dev/id/"


def load_odd(path: Path) -> dict:
    """OpenODD 문서 하나를 읽는다. CHECKS·ATTRIBUTES 가 없으면 빈 맵으로 본다."""
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def condition_iri(attr: dict) -> str:
    """ATTRIBUTES.<속성>.iri 의 `id:cond-…` 를 전체 IRI 로 편다 (odd2kg 와 같은 접두사)."""
    iri = str(attr.get("iri", ""))
    return ID_BASE + iri[3:] if iri.startswith("id:") else iri


def judge_condition(check: dict, root: Path) -> str:
    """조건 하나의 판정 — cmd 종료 0 = in, 1 = out, 그 밖(없음·오류) = unverified."""
    cmd = check.get("cmd")
    if not cmd:
        return "unverified"
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True)
    return "in" if r.returncode == 0 else "out" if r.returncode == 1 else "unverified"


def judge_all(doc: dict, root: Path, forced: dict | None = None) -> list[dict]:
    """CHECKS 의 모든 속성을 판정한다 → [{name, iri, title_ko, grade, cmd, state}] (문서 순).

    forced 는 {속성명: 상태} — 그 속성은 cmd 를 돌리지 않고 주어진 상태로 둔다 (assume_check --break 의 인위 파괴).
    """
    checks, attrs = doc.get("CHECKS") or {}, doc.get("ATTRIBUTES") or {}
    forced = forced or {}
    rows = []
    for name, c in checks.items():
        c = c or {}
        attr = attrs.get(name) or {}
        state = forced[name] if name in forced else judge_condition(c, root)
        rows.append({"name": name, "iri": condition_iri(attr), "title_ko": attr.get("title_ko", ""),
                     "grade": str(c.get("grade", "")), "cmd": bool(c.get("cmd")), "state": state})
    return rows


def render(odd_label: str, rows: list[dict]) -> tuple[str, list[str]]:
    """odd_check 보고 본문과 이탈 속성 목록."""
    out_of = [r["name"] for r in rows if r["state"] == "out"]
    unverified = [r["name"] for r in rows if r["state"] == "unverified"]
    verdict = "**ODD 이탈**" if out_of else ("모니터링 불완전 (unverified 있음)" if unverified else "정상 — 모든 속성이 ODD 안")
    rep = [f"# odd_check — {odd_label}", "", f"결과: {verdict}", "", "| 속성 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"]
    rep += [f"| {r['name']} | {r['title_ko']} | {r['grade']} | {r['state']} |" for r in rows]
    if out_of:
        rep += ["", "이탈 속성: " + ", ".join(out_of) + " — 작업 중단 + 유저 에스컬레이션, 의존 항목 무효화 대상 (3.5절)"]
    if unverified:
        rep += ["", "판정 불가: " + ", ".join(unverified) + " — 판정 방법(cmd) 보완 대상"]
    return "\n".join(rep) + "\n", out_of


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--odd", default="kb/odd/project-odd.yml")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    rows = judge_all(load_odd(root / a.odd), root)
    text, out_of = render(a.odd, rows)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if out_of else 0


if __name__ == "__main__":
    raise SystemExit(main())
