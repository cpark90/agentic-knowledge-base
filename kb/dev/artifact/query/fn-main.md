---
id: https://agentic-knowledge-base.dev/id/chunk/5882ff10-a171-41fe-9c29-5556eeb9f75c
type: artifact
level: executable
title_ko: 함수 main (tools/query.py)
title: function main in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/4358cd56-6be2-4ce1-9f2f-9fb0ed47b5d3
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
        g = kb_lib.load_union(a.ttl, root)  # 로딩 로직의 단일 정의처 — weave·metrics 와 같은 union
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
            Path(a.report).write_text(report(g, results, summary_lines, [str(f) for f in rq_files] + list(a.ttl)), encoding="utf-8")
            return EXIT_OK
        if a.cq:
            for cq in a.cq:
                print("\n".join(render_query(g, by_id[cq], bindings, a.limit, a.labels)))
                print()
            return EXIT_OK
        summary_lines, _ = summary(g, queries, bindings)
        print("\n".join(kb_lib.gendoc_header(
            "cq-summary", "역량 질문 행 수 요약", "tools/query.py",
            f"등재된 역량 질문 {len(queries)}건을 전부 돌려 질문과 행 수만 — 한 질의의 답은 `bazel run //tools:query -- <CQ> --labels`",
            "bazel run //tools:query", [str(f) for f in rq_files] + list(a.ttl), f"트리플 {len(g)} · 질의 {len(queries)}",
            kb_lib.gendoc_view_notice("질의 파일 `tools/cq-queries/*.rq` 와 청크"))))
        print("\n".join(summary_lines))
        return EXIT_OK
    except Exception as e:  # 실행 중 실패(질의 결함·바인딩 타입) — 산출물이 아니라 질의를 고친다
        print(f"CONFIG 질의 실행 실패 — {e}", file=sys.stderr)
        return EXIT_CONFIG
```
<!-- 인용 끝 -->
