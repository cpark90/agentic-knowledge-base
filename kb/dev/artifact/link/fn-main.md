---
id: https://agentic-knowledge-base.dev/id/chunk/6c4416f9-52c1-404c-8a6d-1c07e65cc077
type: artifact
level: executable
title_ko: 함수 main (tools/link.py)
title: function main in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--k", type=int, default=7, help="앵커(주어)당 후보 상한 (로드맵 입력표 k ≤ 7)")
    ap.add_argument("--min-shared", type=int, default=3, help="개념 공유 후보의 agt:usesConcept 교집합 하한")
    ap.add_argument("--root", default=".")
    ap.add_argument("files", nargs="*", help="그래프 파일들 (없으면 kb_lib.UNION_GRAPH_PATHS + 온톨로지 모듈)")
    a = ap.parse_args()
    if a.k < 1 or a.min_shared < 1:
        print(f"CONFIG [{TAG}] --k 와 --min-shared 는 1 이상이다 — 실제 k={a.k} min-shared={a.min_shared}", file=sys.stderr)
        return EXIT_CONFIG
    try:
        g = kb_lib.load_union(a.files, Path(a.root))
    except (ValueError, OSError, SyntaxError) as e:
        print(f"CONFIG [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    u = Units(g)

    # 이미 frontmatter 링크(직접 술어 LINK_KEYS + relatedTo 족)가 있는 쌍 — 단위 기준, 방향 무관
    linked = set()
    for key in LINK_KEYS + RELATED_KEYS:
        for s, o in g.subject_objects(AGT[key]):
            us, uo = u.unit_of.get(s), u.unit_of.get(o)
            if us is not None and uo is not None and us != uo:
                linked.add(frozenset((us, uo)))

    evidence, prefer, dropped, hint = gather(u, a.min_shared)
    by_anchor: dict = defaultdict(list)
    for key in sorted(evidence, key=lambda k: tuple(sorted(map(str, k)))):
        if key in linked:
            dropped[R_LINKED] += 1
            continue
        r = resolve(u, key, prefer, hint)
        if isinstance(r, str):
            dropped[r] += 1
            continue
        anchor, kind, target = r
        evs = sorted(evidence[key])
        by_anchor[anchor].append({"kind": kind, "target": target, "evs": evs, "rank": evs[0][0], "shared": max(e[3] for e in evs)})
    candidates = []
    for anchor in sorted(by_anchor, key=lambda x: (u.ko(x), str(x))):
        rows = sorted(by_anchor[anchor], key=lambda c: (c["rank"], -c["shared"], u.ko(c["target"]), str(c["target"])))
        dropped[R_CAP] += max(0, len(rows) - a.k)
        for c in rows[:a.k]:
            c["anchor"] = anchor
            candidates.append(c)

    kinds = Counter(e[1] for c in candidates for e in c["evs"])
    primary = Counter(c["evs"][0][1] for c in candidates)
    link_kinds = Counter(c["kind"] for c in candidates)
    ttl = [f for f in (a.files or list(kb_lib.UNION_GRAPH_PATHS)) if f.endswith(".ttl")]
    live_units = [x for x in u.members if u.alive(x)]
    head = kb_lib.gendoc_header(
        "link-candidates", "복원 후보 생성기 뷰", "tools/link.py",
        f"살아 있는 단위(결정 복합체는 결론이 앵커) 쌍 중 frontmatter 링크(`{'`·`'.join(LINK_KEYS)}` + relatedTo 족)가 없는 쌍에 대해 "
        f"(a) `agt:cites` → constructionRecord · (b) 같은 V&V 청크의 `agt:verifies` → testCoverage · (c) `agt:usesConcept` 교집합 ≥ {a.min_shared} → proposal · "
        f"(d) 조각 F 가 `prov:specializationOf` O 이면 O 를 가리키던 확정 링크 X→O 마다 X→F → constructionRecord(값 \"승계: O\"). "
        f"종류는 `kb_lib.TIM_CELLS` 허용 칸(인용 방향 → 역방향 → 칸이 없으면 `agt:overlapsWith`), 제약은 `defs/kb.bzl` `_check_links` 와 같다. 앵커당 k ≤ {a.k}",
        "bazel build //kg:link_candidates", ttl, f"트리플 {len(g)} ({kb_lib.gendoc_union(ttl)}) — 체계 밖 정보 0",
        kb_lib.gendoc_view_notice("앵커 청크의 frontmatter (`p10-candidate-and-confirmed-link` · `p10-restored-link-marking`)"),
        input_kind="그래프 파일",
        extra=[f"- 살아 있는 청크 {len(u.live)} · 단위 {len(live_units)} · 증거가 있는 쌍 {len(evidence)}",
               "- 판정은 사람이 후보마다 하고 확정은 앵커 청크의 frontmatter 에 적는다"])
    o = ["## 요약", "", "| 항목 | 값 |", "|---|---|",
         f"| 후보 수 | {len(candidates)} |",
         "| 근거 종류 분포 (첫 근거 기준) | " + (" · ".join(f"{k} {v}" for k, v in sorted(primary.items(), key=lambda kv: EVIDENCE_RANK[kv[0]])) or kb_lib.NONE_MARK) + " |",
         "| 근거 종류 분포 (모든 근거) | " + (" · ".join(f"{k} {v}" for k, v in sorted(kinds.items(), key=lambda kv: EVIDENCE_RANK[kv[0]])) or kb_lib.NONE_MARK) + " |",
         "| 링크 종류 분포 | " + (" · ".join(f"`{k}` {v}" for k, v in sorted(link_kinds.items())) or kb_lib.NONE_MARK) + " |",
         f"| 앵커 수 | {len(by_anchor)} |",
         f"| 탈락 수 | {sum(dropped.values())} — " + (" · ".join(f"{k} {v}" for k, v in sorted(dropped.items(), key=lambda kv: (-kv[1], kv[0]))) or kb_lib.NONE_MARK) + " |", "",
         "## 후보", "",
         "| # | 앵커 (ko) | 앵커 파일 | 링크 종류 | 대상 (ko) | 대상 IRI | 근거 종류 | 근거 값 (인용 식별자 / 케이스 슬러그 / 공유 개념 수 / 승계: 원본) | 판정 (채택 / 기각) |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(candidates, 1):
        o.append(f"| {i} | {cell(u.ko(c['anchor']))} | `{u.loc.get(c['anchor'], '')}` | `{c['kind']}` | {cell(u.ko(c['target']))} | `{kb_lib.compact_iri(str(c['target']))}` | "
                 + " · ".join(e[1] for e in c["evs"]) + " | " + " · ".join(cell(e[2]) for e in c["evs"]) + f" | {kb_lib.NONE_MARK} |")
    if not candidates:
        o.append("| " + " | ".join([kb_lib.NONE_MARK] * 2 + [f"후보 {kb_lib.NONE_MARK}"] + [kb_lib.NONE_MARK] * 6) + " |")
    o += ["", "## 확정 절차", "",
          f"1. 후보를 채택하면 앵커 청크의 frontmatter 에 링크 키와 복원 표시를 적는다 — `<링크 종류>: [<대상 IRI>]` 와 `{RESTORED_KEY}: [<대상 IRI>]`. "
          "대상 IRI 는 표의 `id:` 를 `https://agentic-knowledge-base.dev/id/` 로 푼 전체 IRI 다. 결정 복합체의 앵커는 결론 청크다. "
          f"`{RESTORED_KEY}` 의 IRI 가 같은 청크의 링크 대상에 없으면 `chunk2kg` 가 `FAIL [{kb_lib.RESTORED_GATE}]` 로 거부한다 (p10-restored-link-marking).",
          "2. 효과 — 그 링크 개체(`agt:Link`)에 후보의 출처 증거 `agt:proposal` 이 확정 기록 `agt:constructionRecord`(사람이 frontmatter 에 적은 행위)와 "
          "함께 붙고, `bazel build //kg:metrics`·`//kg:audit` 의 복원 비율에 복원으로 센다. `linkState` 는 `confirmed` 다 — frontmatter 에 적힌 것은 확정이다.",
          f"3. `{RELATED}` 후보도 다른 후보와 같이 적는다 — `{RELATED}: [<대상 IRI>]` 와 `{RESTORED_KEY}: [<대상 IRI>]` 다. 그 잎은 링크 키(LINK_KEYS)라 "
          "링크 개체와 복원 표시를 받고 복원 비율에 든다. 함께 갱신할 의무까지 판정했으면 `coUpdatesWith` 로 올려 적는다 — 그 키는 직접 트리플뿐이라 복원 표시를 "
          "받지 않는다. `verifies` 후보의 앵커는 V&V 청크이므로 vnv 가 적는다 (`kb/vv/` 는 vnv 의 write plane).",
          "4. `python3 tools/gen_build.py --root . && bazel test //...` — `refines`·`serves`·`supersedes`·`verifies` 는 Bazel deps 라 "
          "BUILD 를 재생성한다. 나머지 링크 키(`overlapsWith` 를 포함해)는 deps 가 아니라 그래프 트리플뿐이므로 BUILD 가 바뀌지 않는다.",
          "5. 기각은 관측 한 줄(memory plane)로 남긴다. 후보는 저장하지 않으므로 다음 생성에서 다시 나온다.", ""]
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, ttl, input_kind="그래프 파일"), encoding="utf-8")
    return EXIT_OK
```
<!-- 인용 끝 -->
