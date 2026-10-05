#!/usr/bin/env python3
"""검증 라운드 기록의 고정물 시험 — `vv_run --round` · verify 질의 `round-stop-rule-violated` · `weave` audit 라운드 절 (유저 답 Q39-c),
그리고 `vv_run` 허용 목록의 `revalidate` 스냅숏 꼴 (유저 답 Q38-c).

  record     양성 — 임시 트리(판정 주석 다섯, 그중 판정 결과 하나 · 미래 시각 하나)에서 `--round complete` 가 round-<UTC>.md 하나를 쓴다. 라운드 1 · 신규 3 ·
             본문이 종료 사유 개체 하나를 인용한다. 둘째 기록은 라운드 2 · 신규 1 이다. 음성 — 같은 시각의 기록은 덮지 않고(종료 2),
             `--round` 와 `--record` 를 섞으면 종료 2 다
  classify   양성 — `python3 tools/revalidate.py --base-dir … --head-dir …` 는 실행 대상이다. 음성 — 기본 꼴(`--base HEAD`)과 head 없는
             꼴은 SKIP 이고 사유가 스냅숏 꼴을 안내한다
  violated   양성 — 신규 2 · 2 뒤에 셋째 라운드가 `완료` 로 닫힌 그래프에서 질의가 행 하나를 낸다
  kept       음성 — 같은 계열에 셋째가 `정지 규칙` 이거나, 계열이 3 · 1 로 줄었거나, 기록이 없으면 질의가 행을 내지 않는다
  weave      양성 — 라운드 기록이 있으면 audit 의 라운드 절이 기록으로 자르고 위반 1 을 적는다. 음성 — 기록이 없으면 날짜 대리 절 그대로다
사용: round_fixture_test.py --case record|classify|violated|kept|weave
"""
from __future__ import annotations

import argparse
import contextlib
import io
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

from tools import kb_lib, vv_run, weave
from tools.chunk2kg import apply_plane_level_state, load_plane_level_state

RESIDENCY = Path("defs/kb.bzl")
QUERY = Path("tools/verify-queries/round-stop-rule-violated.rq")
ONTOLOGY = Path("kb/ontology/related/state/round-end-reason-ontology.ttl")
AGT, PROV = kb_lib.AGT, Namespace("http://www.w3.org/ns/prov#")
COMMENT = """---
id: urn:fx:comment:{i}
type: annotation
level: concrete
title_ko: 고정물 주석 {i}
title: Fixture comment {i}
status: stable
generated: {{by: {by}, at: {at}}}
---
issue (non-blocking): 고정물 주석이다.
"""


def utc(text: str) -> datetime:
    return datetime.fromisoformat(text).replace(tzinfo=timezone.utc)


def check_record(errs: list) -> None:
    root = Path(tempfile.mkdtemp(dir=os.environ.get("TEST_TMPDIR")))
    (root / vv_run.CASE_DIR).mkdir(parents=True)
    verdict = root / vv_run.VERDICT_DIR
    verdict.mkdir(parents=True)
    for i, (by, at) in enumerate([("vnv/fx", "2026-10-01T00:00:00Z"), ("vnv/fx", "2026-10-02T00:00:00+09:00"),
                                  ("vnv/fx", "2026-10-03T00:00:00Z"), (kb_lib.JUDGE_GENERATOR, "2026-10-03T01:00:00Z"),
                                  ("vnv/fx", "2098-01-01T00:00:00Z")]):  # 마지막은 첫 기록 뒤 — 둘째 라운드의 신규 하나다
        (verdict / f"c{i}.md").write_text(COMMENT.format(i=i, by=by, at=at), encoding="utf-8")
    out, old_argv, old_root = io.StringIO(), sys.argv, os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    os.environ["BUILD_WORKSPACE_DIRECTORY"] = str(root)
    try:
        with contextlib.redirect_stdout(out):
            sys.argv = ["vv_run.py", "--residency", str(RESIDENCY.resolve()), "--round", "complete"]
            code = vv_run.main()
            sys.argv = ["vv_run.py", "--residency", str(RESIDENCY.resolve()), "--round", "budget", "--record"]
            mixed = vv_run.main()
    finally:
        sys.argv = old_argv
        if old_root is None:
            os.environ.pop("BUILD_WORKSPACE_DIRECTORY", None)
        else:
            os.environ["BUILD_WORKSPACE_DIRECTORY"] = old_root
    records = sorted((root / vv_run.RUN_DIR).glob(f"{vv_run.ROUND_PREFIX}*.md"))
    if code != kb_lib.EXIT_OK or len(records) != 1:
        errs.append(f"`--round complete` 가 기록 하나를 쓰지 않았다 — 종료 {code} · 기록 {len(records)}")
        return
    text = records[0].read_text(encoding="utf-8")
    need = ["title_ko: 검증 라운드 1 종료", "신규 결함 3", "`agt:roundEndedByCompletion`", "generated: {by: process:vv_run",
            "| 1 | 없음 |"]
    errs += [f"라운드 기록에 `{p}` 가 없다" for p in need if p not in text]
    if sum(text.count(f"`{c}`") for c, _k, _e in vv_run.ROUND_REASONS.values()) != 1:
        errs.append("라운드 기록이 종료 사유 개체를 정확히 하나 인용하지 않는다")
    if list((root / vv_run.RUN_DIR).glob("run-*.md")):
        errs.append("`--round` 가 케이스를 돌려 실행 기록을 남겼다")
    if mixed != kb_lib.EXIT_CONFIG:
        errs.append(f"`--round` 와 `--record` 를 섞은 호출이 거부되지 않았다 — 종료 {mixed}")
    with contextlib.redirect_stdout(io.StringIO()):
        later = vv_run.record_round(root, "stop-rule", datetime(2099, 1, 1, tzinfo=timezone.utc))
        again = vv_run.record_round(root, "stop-rule", datetime(2099, 1, 1, tzinfo=timezone.utc))
    second = (root / vv_run.RUN_DIR / f"{vv_run.ROUND_PREFIX}20990101T000000Z.md")
    body = second.read_text(encoding="utf-8") if second.exists() else ""
    if later != kb_lib.EXIT_OK or "검증 라운드 2 종료" not in body or "신규 결함 1 " not in body:
        errs.append("둘째 라운드 기록이 라운드 2 · 신규 1(첫 기록 뒤의 주석 하나)을 적지 않았다")
    if again != kb_lib.EXIT_CONFIG:
        errs.append("같은 시각의 라운드 기록을 덮었다 — append-only 다")


def check_classify(errs: list) -> None:
    spec = {"files": {"b": "x"}, "expect": [{"exit": 1}]}
    ok = "python3 tools/revalidate.py --base-dir {{b}} --head-dir {{b}}"
    if vv_run.classify(ok, spec) is not None:
        errs.append(f"스냅숏 꼴이 실행 대상이 아니다 — {vv_run.classify(ok, spec)}")
    for bad in ("python3 tools/revalidate.py --base HEAD", "python3 tools/revalidate.py --base-dir {{b}}"):
        why = vv_run.classify(bad, spec)
        if not why or "스냅숏 꼴" not in why:
            errs.append(f"`{bad}` 가 SKIP 되지 않았다 — 사유 {why!r}")


def graph(rounds: list, comments: list) -> Graph:
    """라운드 기록 (시각, 종료 사유 지역명) 과 주석 (시각, 생성자) 의 최소 그래프 — chunk2kg·extract_refs 가 내는 술어만 쓴다."""
    g = Graph()
    g.parse(str(ONTOLOGY), format="turtle")
    for i, (at, reason) in enumerate(rounds):
        r = URIRef(f"urn:fx:round:{i}")
        g += [(r, RDF.type, AGT.MemoryChunk), (r, AGT.generatedBy, Literal(kb_lib.RUN_GENERATOR)), (r, AGT.usesConcept, AGT[reason]),
              (r, PROV.generatedAtTime, Literal(at, datatype=XSD.dateTime)), (r, AGT.tokenCount, Literal(1)),
              (r, AGT.status, Literal("stable")), (r, AGT.assertionLocation, Literal(f"kb/vv/run/round-{i}.md"))]
    for i, (at, by) in enumerate(comments):
        c = URIRef(f"urn:fx:comment:{i}")
        g += [(c, RDF.type, AGT.AnnotationChunk), (c, AGT.generatedBy, Literal(by)), (c, AGT.status, Literal("stable")),
              (c, PROV.generatedAtTime, Literal(at, datatype=XSD.dateTime)), (c, AGT.tokenCount, Literal(1)),
              (c, AGT.assertionLocation, Literal(f"kb/vv/verdict/c{i}.md"))]
    return g


# 계열 2 · 2 — 라운드 1 은 처음부터 10-02 까지(주석 둘), 라운드 2 는 10-04 까지(주석 둘, 판정 결과 하나는 빠진다)
FLAT = [("2026-10-01T00:00:00Z", "fx"), ("2026-10-02T00:00:00Z", "fx"), ("2026-10-03T00:00:00Z", "fx"),
        ("2026-10-04T00:00:00+00:00", "fx"), ("2026-10-03T12:00:00Z", kb_lib.JUDGE_GENERATOR)]
BOUNDS = ["2026-10-02T00:00:00Z", "2026-10-04T00:00:00Z", "2026-10-06T00:00:00Z"]


def violations(g: Graph) -> list:
    return list(g.query(QUERY.read_text(encoding="utf-8")))


def check_violated(errs: list) -> None:
    rows = violations(graph(list(zip(BOUNDS, ["roundEndedByCompletion", "roundEndedByCompletion", "roundEndedByCompletion"])), FLAT))
    if len(rows) != 1 or str(rows[0][0]) != "urn:fx:round:2":
        errs.append(f"신규 2 · 2 뒤에 `완료` 로 닫힌 셋째 라운드를 질의가 잡지 않았다 — 행 {[tuple(map(str, r)) for r in rows]}")


def check_kept(errs: list) -> None:
    stop = violations(graph(list(zip(BOUNDS, ["roundEndedByCompletion", "roundEndedByCompletion", "roundEndedByStopRule"])), FLAT))
    falling = FLAT[:3] + [FLAT[4]]  # 계열 2 · 1 — 줄었으므로 셋째 라운드를 열어도 된다
    fell = violations(graph(list(zip(BOUNDS, ["roundEndedByCompletion"] * 3)), falling))
    empty = violations(graph([], FLAT))
    for name, rows in (("셋째가 정지 규칙", stop), ("계열이 줄었다", fell), ("기록 없음", empty)):
        if rows:
            errs.append(f"{name} — 질의가 행 {len(rows)} 을 냈다(기대 0)")


def check_weave(errs: list) -> None:
    apply_plane_level_state(*load_plane_level_state(str(RESIDENCY)))
    for rounds, need, forbid in (
            (list(zip(BOUNDS, ["roundEndedByCompletion"] * 3)),
             ["| 라운드 | 기록 | 구간 끝 | 신규 주석 |", "| 1 | `round-0.md` | 2026-10-02T00:00:00Z | 2 |", "신규 계열 2 · 2 · 0",
              "정지 규칙 위반 1", "**정지 규칙 위반**"], "| 라운드(날짜) |"),
            ([], ["| 라운드(날짜) | 신규 주석 | 직전 라운드 대비 |", "| 2026-10-01 | 1 |"], "| 라운드 | 기록 |")):
        m = weave.Model(graph(rounds, FLAT))
        by_gen = lambda c: str(next(m.g.objects(c, AGT.generatedBy), ""))  # noqa: E731 — render_audit 과 같은 정의
        text = "\n".join(weave._audit_comments(m, m.g, {c for c in m.chunks if m.live(c)}, kb_lib.pct, by_gen))
        errs += [f"audit 라운드 절에 `{p}` 가 없다 (기록 {len(rounds)})" for p in need if p not in text]
        if forbid in text:
            errs.append(f"audit 라운드 절에 `{forbid}` 가 섞였다 (기록 {len(rounds)})")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=("record", "classify", "violated", "kept", "weave"))
    a = ap.parse_args()
    errs: list = []
    {"record": check_record, "classify": check_classify, "violated": check_violated, "kept": check_kept, "weave": check_weave}[a.case](errs)
    for e in errs:
        print(f"FAIL [{a.case}] {e}")
    print(f"{'PASS' if not errs else 'FAIL'} — 라운드 고정물 `{a.case}`")
    return 0 if not errs else 1


if __name__ == "__main__":
    raise SystemExit(main())
