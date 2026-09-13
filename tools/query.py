#!/usr/bin/env python3
"""일반 질의 도구 — 역량 질문(docs/competency-questions.md)을 SPARQL 로 노출한다 (로드맵 다음 산출 4, 노트 2.7절).

질의 하나 = 파일 하나 tools/cq-queries/CQ-NN.rq. 머리 주석 첫 줄이 질문 원문, 둘째 줄이 답의 형태(행 = 무엇)다.
그래프는 metrics 와 같은 union(head·참조·시드·카탈로그·복합체·ODD)에 온톨로지 모듈을 더해 rdflib 에 **한 번** 올린다.
캐시·직렬화는 두지 않는다 — 원본은 그래프 파일이고 결과는 저장하지 않는 질의 결과다 (competency-questions 4).
결과는 표이고 --labels 가 IRI 열을 rdfs:label@ko 로 바꾼다 — 라벨이 인터페이스다 (p4-label-is-the-interface,
p12-knowledge-retrieval-by-label: 결과는 라벨 목록).

사용:
  bazel run //tools:query -- CQ-07 [--limit N] [--labels] [--bind ?x=<IRI|id:슬러그|agt:용어|라벨>]
  bazel run //tools:query                       # 전체 CQ 의 행 수 요약표
  query.py --report cq.md --queries <dir|*.rq> --ttl <TTL...>    # 뷰 //kg:cq 의 생성기
종료 코드는 kb_lib 상수 — 질의 파일 없음·SPARQL 파싱 실패·그래프 파일 없음·--bind 해석 실패는 EXIT_CONFIG, 질의 0건은 EXIT_SKIP.
행 0 은 답이지 실패가 아니다 (게이트가 아니다).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from rdflib import Graph, Literal, URIRef, RDFS
from rdflib.plugins.sparql import prepareQuery

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT, ID = kb_lib.AGT, kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
DEFAULT_QUERY_DIR = "tools/cq-queries"
DEFAULT_LIMIT = 50      # 표 상한 — 컨텍스트 예산(anti-rot). 0 이면 전부
REPORT_TOP = 5          # 뷰 cq.md 의 CQ 별 상위 행 수
REPORT_CELL = 100       # 뷰의 셀 폭 상한 (문자) — CLI 는 자르지 않는다
CQ_ID = re.compile(r"^CQ-\d+$")


class CqQuery:
    def __init__(self, path: Path):
        self.path = path
        self.id = path.stem
        text = path.read_text(encoding="utf-8")
        heads = [ln[1:].strip() for ln in text.splitlines()[:2] if ln.startswith("#")]
        self.question = heads[0] if heads else path.stem
        self.form = heads[1] if len(heads) > 1 else ""
        self.text = text
        self.prepared = prepareQuery(text)  # 파싱 실패는 여기서 예외 — 호출자가 EXIT_CONFIG


def find_queries(paths: list[str], root: Path) -> list[Path]:
    """디렉토리 또는 .rq 파일 목록 → 정렬된 .rq 경로. 없는 경로는 ValueError."""
    out: list[Path] = []
    for p in paths:
        cand = Path(p) if Path(p).exists() else (kb_lib.resolve_path(p, root) or (root / p if (root / p).is_dir() else None))
        if cand is None:
            raise ValueError(f"{p}: 질의 파일·디렉토리가 없다")
        out += sorted(cand.glob("*.rq")) if cand.is_dir() else [cand]
    return out


def load_graph(ttls: list[str], root: Path) -> Graph:
    """TTL 을 하나의 Graph 로 (metrics.py 와 같은 방식). 빈 목록이면 UNION_GRAPH_PATHS + 온톨로지 glob. 없는 파일은 ValueError."""
    files: list[Path] = []
    if ttls:
        for t in ttls:
            f = kb_lib.resolve_path(t, root)
            if f is None:
                raise ValueError(f"{t}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
    else:
        for p in kb_lib.UNION_GRAPH_PATHS:
            f = kb_lib.resolve_path(p, root)
            if f is None:
                raise ValueError(f"{p}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
        for pat in kb_lib.UNION_GRAPH_GLOBS:
            found = kb_lib.resolve_glob(pat, root)
            if not found:
                raise ValueError(f"{pat}: 온톨로지 모듈이 없다")
            files += found
    g = Graph()
    for f in files:
        if f.suffix == ".ttl":
            g.parse(str(f), format="turtle")
    return g


def resolve_binding(g: Graph, spec: str):
    """--bind ?var=value → (var, term). value 는 IRI · id:슬러그 · agt:용어 · 정수 · 라벨(ko/en 정확 일치). 모호하거나 없으면 ValueError."""
    if "=" not in spec:
        raise ValueError(f"--bind {spec!r}: ?var=value 형식이어야 한다")
    var, value = spec.split("=", 1)
    var = var.lstrip("?").strip()
    value = value.strip()
    if not var or not value:
        raise ValueError(f"--bind {spec!r}: 변수와 값이 비어 있으면 안 된다")
    if value.startswith("http://") or value.startswith("https://"):
        return var, URIRef(value)
    if value.startswith("id:"):
        return var, ID[value[3:]]
    if value.startswith("agt:"):
        return var, AGT[value[4:]]
    if re.fullmatch(r"-?\d+", value):
        return var, Literal(int(value))
    hits = sorted({s for s, lab in g.subject_objects(RDFS.label) if str(lab) == value}, key=str)
    if len(hits) == 1:
        return var, hits[0]
    if not hits:
        raise ValueError(f"--bind {spec!r}: 라벨 {value!r} 인 개체가 없다 (IRI·id:·agt: 표기도 된다)")
    raise ValueError(f"--bind {spec!r}: 라벨 {value!r} 인 개체가 {len(hits)}개다 — IRI 로 지정한다: " + ", ".join(kb_lib.compact_iri(str(h)) for h in hits))


def run(g: Graph, q: CqQuery, bindings: dict) -> tuple[list[str], list[tuple]]:
    res = g.query(q.prepared, initBindings=bindings)
    cols = [str(v) for v in res.vars] if res.vars else []
    return cols, [tuple(row) for row in res]


def cell(g: Graph, term, labels: bool, width: int = 0) -> str:
    if term is None:
        s = ""
    elif isinstance(term, URIRef):
        s = kb_lib.label_of(g, term) if labels else kb_lib.compact_iri(str(term))
    elif isinstance(term, Literal):
        s = str(term)
    else:
        s = f"_:{term}"
    s = " ".join(s.split()).replace("|", "\\|")
    if width and len(s) > width:
        s = s[: width - 1] + "…"
    return s


def table(cols: list[str], rows: list[list[str]]) -> list[str]:
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return out


def render_query(g: Graph, q: CqQuery, bindings: dict, limit: int, labels: bool) -> list[str]:
    cols, rows = run(g, q, bindings)
    shown = rows if limit <= 0 else rows[:limit]
    out = [f"## {q.id} — {q.question}", f"행 = {q.form}" if q.form else "", ""]
    if cols:
        out += table(cols, [[cell(g, t, labels) for t in r] for r in shown])
    tail = f"행 {len(rows)}"
    if len(shown) < len(rows):
        tail += f" (표시 {len(shown)} — --limit 0 이 전부)"
    if bindings:
        tail += " · bind " + ", ".join(f"?{k}={kb_lib.compact_iri(str(v))}" for k, v in bindings.items())
    out += ["", tail]
    return [ln for ln in out if ln is not None]


def summary(g: Graph, queries: list[CqQuery], bindings: dict) -> tuple[list[str], list[tuple[CqQuery, list[str], list[tuple]]]]:
    results = []
    for q in queries:
        cols, rows = run(g, q, bindings)
        results.append((q, cols, rows))
    lines = table(["CQ", "질문", "행"], [[q.id, q.question.replace("|", "\\|"), str(len(rows))] for q, _, rows in results])
    return lines, results


def report(g: Graph, results: list[tuple[CqQuery, list[str], list[tuple]]], summary_lines: list[str]) -> str:
    o = ["# cq — 역량 질문 뷰 (생성 파일, tools/query.py)", "",
         f"질의 {len(results)} · 트리플 {len(g)} · 질문 원문은 tools/cq-queries/*.rq 머리 주석, 등재는 docs/competency-questions.md. "
         f"행 수는 답이지 판정이 아니다 (게이트가 아니다). CQ 별로 상위 {REPORT_TOP}행을 라벨로 보인다 — 전부는 `bazel run //tools:query -- <CQ> --labels --limit 0`", ""]
    o += summary_lines + [""]
    for q, cols, rows in results:
        o += [f"## {q.id} — {q.question}", "", f"- 행 = {q.form}" if q.form else "", f"- 행 수 **{len(rows)}**", ""]
        if cols and rows:
            o += table(cols, [[cell(g, t, True, REPORT_CELL) for t in r] for r in rows[:REPORT_TOP]])
            if len(rows) > REPORT_TOP:
                o.append(f"… 외 {len(rows) - REPORT_TOP}행")
        o.append("")
    return "\n".join(ln for ln in o if ln is not None) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cq", nargs="*", help="역량 질문 id (CQ-07 …). 없으면 전체 요약표")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help=f"표시 행 상한 (기본 {DEFAULT_LIMIT}, 0 = 전부)")
    ap.add_argument("--labels", action="store_true", help="IRI 열을 rdfs:label@ko 로 (라벨 목록)")
    ap.add_argument("--bind", action="append", default=[], metavar="?VAR=VALUE", help="질의 변수 바인딩 — IRI · id:슬러그 · agt:용어 · 정수 · 라벨")
    ap.add_argument("--queries", nargs="+", default=[DEFAULT_QUERY_DIR], metavar="PATH", help=f"질의 디렉토리 또는 .rq 파일들 (기본 {DEFAULT_QUERY_DIR})")
    ap.add_argument("--ttl", nargs="*", default=[], metavar="TTL", help="그래프 파일들 (기본: kb_lib.UNION_GRAPH_PATHS + 온톨로지 모듈)")
    ap.add_argument("--report", default="", metavar="OUT", help="뷰 cq.md 를 쓴다 (전체 CQ · 상위 행 라벨)")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))

    try:
        rq_files = find_queries(a.queries, root)
    except ValueError as e:
        print(f"CONFIG {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not rq_files:
        print("SKIP 질의 파일이 0건이다 — tools/cq-queries/*.rq", file=sys.stderr)
        return EXIT_SKIP
    queries: list[CqQuery] = []
    for f in rq_files:
        try:
            queries.append(CqQuery(f))
        except Exception as e:  # pyparsing.ParseException 등 — 질의 자체의 결함은 설정 문제다
            print(f"CONFIG {f.as_posix()}: SPARQL 파싱 실패 — {e}", file=sys.stderr)
            return EXIT_CONFIG
    by_id = {q.id: q for q in queries}
    for cq in a.cq:
        if cq not in by_id:
            print(f"CONFIG {cq}: 질의 파일이 없다 — 있는 것: {', '.join(sorted(by_id))}", file=sys.stderr)
            return EXIT_CONFIG

    try:
        g = load_graph(a.ttl, root)
    except ValueError as e:
        print(f"CONFIG {e}", file=sys.stderr)
        return EXIT_CONFIG
    bindings = {}
    try:
        for spec in a.bind:
            var, term = resolve_binding(g, spec)
            bindings[var] = term
    except ValueError as e:
        print(f"CONFIG {e}", file=sys.stderr)
        return EXIT_CONFIG

    try:
        if a.report:
            summary_lines, results = summary(g, queries, bindings)
            Path(a.report).write_text(report(g, results, summary_lines), encoding="utf-8")
            return EXIT_OK
        if a.cq:
            for cq in a.cq:
                print("\n".join(render_query(g, by_id[cq], bindings, a.limit, a.labels)))
                print()
            return EXIT_OK
        summary_lines, _ = summary(g, queries, bindings)
        print(f"# 역량 질문 요약 — 질의 {len(queries)} · 트리플 {len(g)}", "", sep="\n")
        print("\n".join(summary_lines))
        return EXIT_OK
    except Exception as e:  # 실행 중 실패(질의 결함·바인딩 타입) — 산출물이 아니라 질의를 고친다
        print(f"CONFIG 질의 실행 실패 — {e}", file=sys.stderr)
        return EXIT_CONFIG


if __name__ == "__main__":
    raise SystemExit(main())
