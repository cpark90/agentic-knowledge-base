#!/usr/bin/env python3
"""케이스 생성기(tools/case_gen.py)의 고정물 시험 — 양성 둘과 음성 넷 (결정 p8-case-generation, 유저 답 Q27-a).

고정물은 `defs/tests/case_gen/` 의 작은 가짜 V&V 트리 하나다 — logical 시나리오 자극 청크 하나(`fx-cap-stimulus.md`, 변수 셋 ·
다섯 규칙 · seed 11) · 관측 재현의 근거인 실행 기록 하나 · ODD 문서 하나 · 커밋된 생성 케이스 열셋(`kb/vv/case/`)이다.
  ok          트리의 케이스가 재생성과 바이트로 같고 전부 생성기의 것이다 — PASS [case-drift]. 두 번 생성한 결과가 같고(결정론),
              생성 케이스가 chunk2kg 의 frontmatter 규칙을 지킨다
  derives     `case` 템플릿에 선택 키 `derivesFrom` 을 더해 생성한다 — 생성 케이스 전부의 `derivesFrom` 이 [시나리오, 더한 IRI] 이고
              `restored` 가 없으며, 그 출력을 --cases 로 준 --check 가 PASS [case-drift] 다
  unsampled   `cover` 에 근거 규칙(`rule`) 없는 항목을 더한다 — FAIL [case-gen] 표본 근거 없는 케이스
  handvalues  입력 펜스에 값을 손으로 적은 `cases` 목록을 더한다 — FAIL [case-gen] 표본 근거 없는 케이스
  drift       커밋된 생성 케이스 하나의 기대 문장을 바꾼다 — FAIL [case-drift]
  handwritten 생성기 밖의 케이스(generated.by 가 역할) 하나를 더하고 --all-generated 로 본다 — FAIL [case-drift] 수기 케이스
음성 시험은 고정물을 TEST_TMPDIR 에 복사해 한 곳만 바꾼다 — 고정물 자체는 언제나 양성이다.
사용: case_gen_fixture_test.py --case ok|derives|unsampled|handvalues|drift|handwritten
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

from tools import case_gen
from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk

FIXTURE = Path("defs/tests/case_gen")
RESIDENCY = "defs/kb.bzl"
SCENARIO = "kb/vv/scenario/fx-cap-stimulus.md"
CASE = "kb/vv/case/fx-cap-boundary-5.md"
HAND = "kb/vv/case/fx-hand.md"
UNSAMPLED = case_gen.UNSAMPLED
SCENARIO_IRI = "https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c001"
DERIVES = "https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c004"
VERIFIES_LINE = "  verifies: [https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-00000000c003]\n"
EXPECT = {
    "ok": (0, ["PASS [case-drift]", "생성 케이스 13개", "생성기 밖의 케이스 0"]),
    "derives": (0, ["PASS [case-drift]", "생성 케이스 13개"]),
    "unsampled": (1, ["FAIL [case-gen]", "근거 규칙이 없다", UNSAMPLED]),
    "handvalues": (1, ["FAIL [case-gen]", "`cases`", UNSAMPLED]),
    "drift": (1, ["FAIL [case-drift]", "fx-cap-boundary-5.md", "생성 결과와 어긋난다"]),
    "handwritten": (1, ["FAIL [case-drift]", "fx-hand.md", "생성기 밖의 케이스"]),
}


def mutate(root: Path, case: str) -> None:
    """음성 사례마다 한 곳을 바꾼다."""
    if case == "derives":
        p = root / SCENARIO
        text = p.read_text(encoding="utf-8")
        assert VERIFIES_LINE in text, "고정물 시나리오의 verifies 줄이 바뀌었다"
        p.write_text(text.replace(VERIFIES_LINE, VERIFIES_LINE + f"  derivesFrom: [{DERIVES}]\n"), encoding="utf-8")
    elif case == "unsampled":
        p = root / SCENARIO
        p.write_text(p.read_text(encoding="utf-8").replace("seed: 11\n", "  - {vars: [kind]}\nseed: 11\n"), encoding="utf-8")
    elif case == "handvalues":
        p = root / SCENARIO
        p.write_text(p.read_text(encoding="utf-8").replace("seed: 11\n", "seed: 11\ncases: [{tokens: 5, kind: plain, flag: \"on\"}]\n"),
                     encoding="utf-8")
    elif case == "drift":
        p = root / CASE
        p.write_text(p.read_text(encoding="utf-8").replace("게이트는 통과한다.", "게이트도 거부한다."), encoding="utf-8")
    elif case == "handwritten":
        text = (root / CASE).read_text(encoding="utf-8").replace("by: process:case_gen", "by: vnv/claude-opus-5-5")
        (root / HAND).write_text(text, encoding="utf-8")


def run(argv: list[str]) -> tuple[int, str]:
    """case_gen.main 을 같은 프로세스에서 부른다 — 출력과 종료 코드."""
    buf = io.StringIO()
    old = sys.argv
    sys.argv = ["case_gen.py", *argv]
    try:
        with contextlib.redirect_stdout(buf):
            code = case_gen.main()
    finally:
        sys.argv = old
    return code, buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=sorted(EXPECT))
    a = ap.parse_args()
    tmp = Path(tempfile.mkdtemp(dir=os.environ.get("TEST_TMPDIR")))
    root = tmp / "fx"
    shutil.copytree(FIXTURE, root)
    mutate(root, a.case)
    check = ["--check", "--root", str(root), "--residency", RESIDENCY, "--scenario", SCENARIO]
    errs = []
    if a.case == "derives":
        d = tmp / "derives"
        c, o = run(["--root", str(root), "--residency", RESIDENCY, "--scenario", SCENARIO, "--out", str(d)])
        if c != 0:
            errs.append(f"derivesFrom 을 가진 템플릿의 생성이 종료 {c} 다 — {o.strip()}")
        apply_plane_level_state(*load_plane_level_state(Path(RESIDENCY)))
        made = sorted(d.glob("*.md"))
        if not made:
            errs.append("생성 케이스가 없다")
        for f in made:
            meta, _ = parse_chunk(str(f))
            if meta.get("derivesFrom") != [SCENARIO_IRI, DERIVES]:
                errs.append(f"{f.name}: derivesFrom 이 {meta.get('derivesFrom')} 다 — [시나리오, 템플릿의 IRI] 가 아니다")
            if "restored" in meta:
                errs.append(f"{f.name}: 생성 케이스에 restored 가 있다 — 생성기의 링크는 구축이다")
        check += ["--cases", str(d)]
    code, out = run(check + (["--all-generated"] if a.case in ("ok", "handwritten") else []))
    want_code, phrases = EXPECT[a.case]
    errs += [f"종료 코드 {code} ≠ 기대 {want_code}"] if code != want_code else []
    errs += [f"출력에 `{p}` 가 없다" for p in phrases if p not in out]
    if a.case == "ok":
        outs = []
        for i in range(2):
            d = tmp / f"out{i}"
            c, o = run(["--root", str(root), "--residency", RESIDENCY, "--scenario", SCENARIO, "--out", str(d)])
            if c != 0:
                errs.append(f"생성 {i + 1}회째가 종료 {c} 다 — {o.strip()}")
            outs.append({p.name: p.read_bytes() for p in sorted(d.glob("*.md"))})
        if outs[0] != outs[1]:
            errs.append("같은 입력의 두 생성이 바이트로 다르다 — 생성은 결정론적이어야 한다 (규칙·seed 가 provenance 다)")
        apply_plane_level_state(*load_plane_level_state(Path(RESIDENCY)))
        for name in sorted(outs[0]):
            try:
                meta, _ = parse_chunk(str(tmp / "out0" / name))
            except ValueError as e:
                errs.append(f"{name}: chunk2kg 가 거부한다 — {e}")
                continue
            if (meta["type"], meta["level"], meta["generated"]["by"]) != ("schema", "concrete", case_gen.ACTOR):
                errs.append(f"{name}: type·level·generated.by 가 schema·concrete·{case_gen.ACTOR} 가 아니다")
    print(out)
    for e in errs:
        print(f"FAIL [{a.case}] {e}")
    print(f"{'PASS' if not errs else 'FAIL'} — case_gen 고정물 `{a.case}`")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
