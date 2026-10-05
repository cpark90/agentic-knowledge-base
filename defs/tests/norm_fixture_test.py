#!/usr/bin/env python3
"""규범 문서 생성기(tools/gen_norms.py)의 고정물 시험 — 양성 하나와 음성 여덟 (결정 p12-norm-documents-from-section-chunks).

고정물은 `defs/tests/norm/` 의 작은 가짜 트리 하나다 — 결정 둘(`fx-a` 의 규약 줄 열하나, `fx-b` 는 링크만)과 절 청크 열(머리 · depth 2 ·
depth 3 · 번호 없는 depth 2 · 묶음 둘 · 표 · 이어짐 둘 · 순서 목록)과 둘째 문서의 절 청크 둘(`fy/` — 머리 · 공유 절)과 커밋된
생성 결과 `FX.md`·`FY.md` 다. 문서 목록은 `norm/norm_docs.bzl` 이 준다(실제 목록 //defs:kb.bzl 의 NORM_DOCS 는 비어 있다).
  ok      트리의 `FX.md`·`FY.md` 가 재생성과 바이트로 같다 — PASS [norms-drift]. `FY.md` 는 `FX.md` 가 싣는 줄 `fx-a#4` 를
          다시 싣는다 — 서로 다른 문서가 같은 줄을 한 번씩 싣는 것은 허용된다(양성)
  orphan  규약 줄 하나를 더하고 어느 절도 싣지 않는다 — FAIL [gen-norms] 고아 줄
  double  같은 문서(fx)의 두 절이 같은 줄을 싣는다 — FAIL [gen-norms] 한 문서 안의 이중 소비
  weak    강도를 요구하는 문서에서 줄의 강도를 지운다 — FAIL [gen-norms] 강도 없음
  numbered depth 3 절에 `numbered: false` 를 단다 — FAIL [gen-norms] 번호는 depth 2 절에만 붙는다
  cells   표 절의 줄 하나에 칸을 하나 더한다 — FAIL [gen-norms] 칸 수가 표의 열 수와 다르다
  linkcol 표 절의 `link_column` 을 `columns` 의 마지막이 아닌 열로 바꾼다 — FAIL [gen-norms] 링크 열은 마지막 원소다
  tablestrength 표 절의 줄에 강도 `[지킴]` 을 단다 — FAIL [gen-norms] 표의 줄은 강도를 갖지 않는다
  firstcont 이어짐 절 청크(`continues: true`)를 문서의 첫 절로 옮긴다 — FAIL [gen-norms] 첫 절은 이어짐일 수 없다
  writer  카탈로그(kg/catalog-kg.ttl)로 writer 검사(validate.check_writer)를 돌린다 — `generated.by: orchestrator/…` 의 절 청크는
          통과하고 `developer/…` 의 절 청크는 거부된다 (절 청크는 orchestrator 저작, p12-norm-documents-from-section-chunks)
고정물에는 묶음 복합체 하나(three·four, p4-composite-as-part-of)가 있다 — 양성이 깊이 우선으로 펼친 절 순서와 바이트를 고정한다.
양성은 묶음의 꼴 넷도 바이트로 고정한다 — 링크 열이 있는 표(six), 링크 열이 없어 표 앞에 `원본:` 줄이 나오는 표를 가진 이어짐 절
(seven — 원본 줄은 행의 주 결정과 `+ slug2` 의 둘째 결정을 함께 싣는다), 항목마다 `1.` 인 순서 목록(eight), 목록 뒤의 이어짐
절(nine)이다. 이어짐 절은 제목이 없고 번호를 소비하지 않는다.
양성은 그 밖에 셋을 고정한다 — 번호 없는 절(five, `numbered: false`)이 번호를 받지도 소비하지도 않는 것, 링크 텍스트에 코드 스팬이
있는 링크(`[`x`](경로)`)는 출력 위치 기준으로 다시 계산되고 링크 밖 코드 스팬 안의 링크 꼴 예시는 그대로 옮겨지는 것, 줄을 넘는
코드 스팬 뒤의 링크도 다시 계산되는 것이다(one — 재기준화는 문단 단위다).
음성 시험은 고정물을 TEST_TMPDIR 에 복사해 한 곳만 바꾼다 — 고정물 자체는 언제나 양성이다.
사용: norm_fixture_test.py --case ok|orphan|double|weak|numbered|cells|linkcol|tablestrength|firstcont|writer
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

from tools import chunk2kg, gen_norms, kb_lib, validate

FIXTURE = Path("defs/tests/norm")
RESIDENCY = "defs/kb.bzl"
CONVENTIONS = "kb/dev/decision/fx-a/conventions.md"
SECTION_TWO = "kb/dev/norm/fx/two.md"
SECTION_FOUR = "kb/dev/norm/fx/four.md"
SECTION_SIX = "kb/dev/norm/fx/six.md"
HEAD = "kb/dev/norm/fx/head.md"
CATALOG = "kg/catalog-kg.ttl"


def mutate(root: Path, case: str) -> None:
    """음성 사례마다 한 곳을 바꾼다."""
    if case == "orphan":
        p = root / CONVENTIONS
        p.write_text(p.read_text(encoding="utf-8") + "규약: [지킴] 어느 문서도 싣지 않는 줄이다.\n", encoding="utf-8")
    elif case == "double":
        p = root / SECTION_TWO
        p.write_text(p.read_text(encoding="utf-8").replace("items: [fx-a#4 + fx-b]", "items: [fx-a#4 + fx-b, fx-a#1]"), encoding="utf-8")
    elif case == "weak":
        p = root / CONVENTIONS
        p.write_text(p.read_text(encoding="utf-8").replace("규약: [권장] ", "규약: "), encoding="utf-8")
    elif case == "numbered":
        p = root / SECTION_FOUR
        p.write_text(p.read_text(encoding="utf-8").replace("depth: 3\n", "depth: 3\nnumbered: false\n"), encoding="utf-8")
    elif case == "cells":
        replace_once(root / CONVENTIONS, "규약: 표의 첫 행 | 링크 열이 없다", "규약: 표의 첫 행 | 링크 열이 없다 | 넘치는 칸")
    elif case == "linkcol":
        replace_once(root / SECTION_SIX, "link_column: 결정\n", "link_column: 이름\n")
    elif case == "tablestrength":
        replace_once(root / CONVENTIONS, "규약: 행 하나 |", "규약: [지킴] 행 하나 |")
    elif case == "firstcont":
        p = root / HEAD
        text = p.read_text(encoding="utf-8").replace(", urn:fx:norm:seven", "")
        p.write_text(text.replace("[urn:fx:norm:head, urn:fx:norm:one", "[urn:fx:norm:head, urn:fx:norm:seven, urn:fx:norm:one"),
                     encoding="utf-8")


def replace_once(p: Path, old: str, new: str) -> None:
    """고정물 복사본의 한 곳을 바꾼다 — 바꿀 자리가 정확히 한 번 있어야 한다(고정물이 바뀌어 사례가 헛돌지 않게)."""
    text = p.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"FAIL [norms-fixture] {p}: 바꿀 자리 {old!r} 가 {text.count(old)}번 있다 — 정확히 한 번이어야 한다")
    p.write_text(text.replace(old, new), encoding="utf-8")


EXPECT = {  # 사례 → (종료 코드, 출력에 있어야 하는 문구)
    "ok": (0, "PASS [norms-drift] — 생성 문서 2개가 원본과 일치"),
    "orphan": (1, "고아 줄"),
    "double": (1, "가 문서 fx 안에서 2번 쓰였다(이중 소비)"),
    "weak": (1, "강도가 없다"),
    "numbered": (1, "numbered 는 depth 2 절에서만 쓴다"),
    "cells": (1, "의 칸 수 3 가 표의 열 수 2"),
    "linkcol": (1, "는 columns 의 마지막 원소"),
    "tablestrength": (1, "는 표 절의 행인데 줄에 강도 [지킴] 가 있다"),
    "firstcont": (1, "문서의 첫 절은 이어짐 절 청크"),
    "writer": (0, "PASS [writer] orchestrator 저작 절 청크 통과 · developer 저작 절 청크 거부"),
}


def run_writer() -> tuple[int, str]:
    """카탈로그 + 절 청크 둘(생성자만 다르다)의 그래프에 writer 검사를 돌린다. 기대는 orchestrator 통과 · developer 거부다."""
    from rdflib import Graph, Literal, URIRef
    from rdflib.namespace import RDF
    agt = kb_lib.AGT
    cls = URIRef(str(agt) + chunk2kg.PLANE_CLASS["norm"].split(":", 1)[1])
    lines = []
    results = {}
    for role in ("orchestrator", "developer"):
        g = Graph()
        g.parse(CATALOG, format="turtle")
        chunk = URIRef(f"urn:fx:norm:writer-{role}")
        g.add((chunk, RDF.type, cls))
        g.add((chunk, agt.generatedBy, Literal(f"{role}/claude-opus-5-5")))
        g.add((chunk, agt.assertionLocation, Literal(f"kb/dev/norm/fx/{role}.md")))
        errors = validate.check_writer(g)
        results[role] = errors
        lines += [f"{role}: {e}" for e in errors]
    ok = not results["orchestrator"] and len(results["developer"]) == 1
    lines.append(EXPECT["writer"][1] if ok else "FAIL [writer] 기대와 다르다")
    return (0 if ok else 1), "\n".join(lines)


def run(root: Path, check: bool) -> tuple[int, str]:
    argv = ["gen_norms.py", "--root", str(root), "--residency", RESIDENCY, "--norm-docs", str(root / "norm_docs.bzl")]
    old, sys.argv = sys.argv, argv + (["--check"] if check else [])
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            code = gen_norms.main()
    finally:
        sys.argv = old
    return code, buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", required=True, choices=sorted(EXPECT))
    a = ap.parse_args()
    want_code, want_text = EXPECT[a.case]
    if a.case == "ok":
        code, out = run(FIXTURE, check=True)
    elif a.case == "writer":
        code, out = run_writer()
    else:
        tmp = Path(tempfile.mkdtemp(dir=os.environ.get("TEST_TMPDIR")))
        root = tmp / "norm"
        shutil.copytree(FIXTURE, root)
        mutate(root, a.case)
        code, out = run(root, check=True)
    print(out)
    if code != want_code or want_text not in out:
        print(f"FAIL [norms-fixture:{a.case}] 종료 {code}(기대 {want_code}) · 문구 {want_text!r} 가 출력에 "
              f"{'있다' if want_text in out else '없다'}")
        return 1
    print(f"PASS [norms-fixture:{a.case}] 종료 {code} · {want_text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
