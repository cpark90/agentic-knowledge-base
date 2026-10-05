---
id: https://agentic-knowledge-base.dev/id/chunk/9be2f024-78e1-424a-926b-c50d75da9888
type: artifact
level: executable
title_ko: 함수 main (tools/open_questions.py)
title: function main in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813, https://agentic-knowledge-base.dev/id/chunk/1d3aee1d-549c-4ef9-be65-508014ca8f93, https://agentic-knowledge-base.dev/id/chunk/1f886c5e-4c41-43ff-9555-867c1f4f13d4, https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/2aa8020a-1553-48b5-8a54-b93aab820bbe, https://agentic-knowledge-base.dev/id/chunk/524a116b-45f4-4802-ba70-3d9426371ad6, https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--spaces", nargs="*", default=[], help="설계 공간 그래프(//space:design_space)")
    ap.add_argument("--bodies", nargs="*", default=[], help="청크 .md — 그래프의 assertionLocation 과 접미로 맞춘다")
    ap.add_argument("--root", default=".")
    ap.add_argument("files", nargs="+", help="그래프 TTL (head 포함)")
    a = ap.parse_args()
    root = Path(a.root)

    g = Graph()
    for f in list(a.files) + list(a.spaces):
        try:
            g.parse(f, format="turtle")
        except Exception as e:  # noqa: BLE001 — rdflib 의 파싱 예외는 종류가 여럿이다
            print(f"CONFIG [open] 그래프를 읽을 수 없다 — {f}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
    by_suffix = {str(p): p for p in (Path(b) for b in a.bodies)}

    def body_of(loc: str) -> str:
        for s, p in by_suffix.items():
            if s.endswith(loc):
                return kb_lib.chunk_body(p.read_text(encoding="utf-8"))
        f = root / loc
        return kb_lib.chunk_body(f.read_text(encoding="utf-8")) if f.is_file() else ""

    spaces = space_rows(g)
    by_iri = {s["iri"]: s for s in spaces}
    rows, missing, unresolved = [], [], []
    for c in sorted(set(g.subjects(AGT.bodySlot, rdflib.Literal(SLOT))), key=str):
        loc = str(next(g.objects(c, AGT.assertionLocation), ""))
        q, details = question_of(body_of(loc))
        if not q:
            missing.append(loc)
            continue
        r = {"q": q, "loc": loc, "ko": kb_lib.label_of(g, c, "ko"), "iri": kb_lib.compact_iri(str(c)),
             "plane": kb_lib.plane_of_node(g, c),
             "level": str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1],
             "status": str(next(g.objects(c, AGT.status), "")),
             "docs": [d for d in details if "://" not in d]}
        hit = [by_iri[d] for d in details if d in by_iri]
        for s in hit:
            s["slots"].append(r)
        unresolved += [(loc, d) for d in details if "://" in d and d not in by_iri]
        if not hit:
            rows.append(r)
    rows.sort(key=lambda r: (r["loc"], r["q"]))
    n_open = sum(1 for s in spaces if s["status"] == "open")
    n_slots = sum(len(s["slots"]) for s in spaces)

    head = kb_lib.gendoc_header(
        "open", "미결 집계", "tools/open_questions.py",
        f"설계 공간 그래프의 `agt:Space` 마다 제목 · status · 변수(`agt:variableFrom` · `agt:variableKind`) · 후보 링크의 상태별 수 · "
        f"그 공간을 상세로 가리키는 선택 슬롯 `{SLOT}:` 의 청크를 내고, head 그래프에서 공간을 가리키지 않는 슬롯"
        f"(`agt:bodySlot \"{SLOT}\"`)을 질문 · 청크(라벨·IRI) · plane/level · 상세 문서로 낸다. 미결 목록의 유일한 자리다",
        "bazel build //kg:open", list(a.files) + list(a.spaces),
        f"공간 {len(spaces)}개(open {n_open}) · 슬롯 미결 {len(rows)}개",
        kb_lib.gendoc_view_notice("설계 공간 청크(`space/*-space.md`)와 미결을 안은 청크의 `미확정:` 슬롯"),
        input_kind="그래프 파일")

    lines = ["## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 설계 공간 | {len(spaces)} |",
             f"| 열린 공간(status open) | {n_open} |",
             f"| 공간을 가리키는 슬롯 | {n_slots} |",
             f"| 공간을 가리키지 않는 슬롯 미결 | {len(rows)} |",
             f"| 슬롯 미결을 안은 청크 | {len({r['loc'] for r in rows})} |",
             f"| 슬롯 미결의 plane 분포 | " + (" · ".join(f"{p} {sum(1 for r in rows if r['plane'] == p)}"
                                                    for p in sorted({r["plane"] for r in rows})) or kb_lib.NONE_MARK) + " |",
             f"| 상세 문서가 있는 슬롯 미결 | {kb_lib.pct(sum(1 for r in rows if r['docs']), len(rows))} |",
             f"| 해석하지 못한 상세 IRI | {len(unresolved)} |",
             f"| 슬롯은 있으나 질문을 못 읽은 청크 | {len(missing)} |",
             "", "## 설계 공간", "",
             "공간 하나가 미결 하나다. 후보 열은 `state` 별 수이고 순서는 open · eliminated · confirmed 다. "
             "open 공간을 먼저, 같은 status 안에서는 파일 순으로 낸다.", "",
             "| 공간 | status | 변수 (from · kind) | 후보 open/eliminated/confirmed | 가리키는 슬롯 |", "|---|---|---|---|---|"]
    for s in spaces:
        # 링크가 아니라 코드 스팬이다 — 생성물은 bazel-bin/kg/ 에 놓이므로 소스 기준 상대경로가 성립하지 않는다 (STYLEGUIDE §9)
        slots = "<br>".join(f"{cell(r['ko'])} `{r['iri']}`" for r in s["slots"]) or kb_lib.NONE_MARK
        frm = f"{cell(s['from_ko'])}<br>`{s['from_iri']}` · {cell(s['kind'])}" if s["from_iri"] else kb_lib.NONE_MARK
        c = s["counts"]
        lines.append(f"| {cell(s['ko'])}<br>`{s['loc']}` | {cell(s['status'])} | {frm} | "
                     f"{'/'.join(str(c[k]) for k in kb_lib.SPACE_STATES)} | {slots} |")
    if not spaces:
        lines.append("| " + " | ".join([kb_lib.NONE_MARK] * 5) + " |")

    lines += ["", "## 슬롯 미결", "",
              "공간을 가리키지 않는 `미확정:` 슬롯이다. 질문 한 줄이 미결의 전부이거나 상세가 문서 경로다.", "",
              "| 질문 | 청크 | plane/level | 상태 | 상세 |", "|---|---|---|---|---|"]
    for r in rows:
        detail = "<br>".join(f"`{d}`" for d in r["docs"]) or kb_lib.NONE_MARK
        lines.append(f"| {cell(r['q'])} | {cell(r['ko'])}<br>`{r['iri']}` | {cell(r['plane'])}/{cell(r['level'])} | "
                     f"{cell(r['status'])} | {detail} |")
    if not rows:
        lines.append("| " + " | ".join([kb_lib.NONE_MARK] * 5) + " |")

    lines += ["", "## 해석하지 못한 상세", "",
              "슬롯의 상세 값이 IRI 인데 설계 공간 그래프에 그 공간이 없다. 공간이 지워졌거나 IRI 가 틀렸다.", ""]
    lines += [f"- `{loc}` → `{d}`" for loc, d in sorted(unresolved)] or [f"- {kb_lib.NONE_MARK}"]
    lines += ["", "## 슬롯을 읽지 못한 청크", "",
              f"슬롯 표지는 있으나 `{SLOT}: <질문>` 줄을 본문에서 찾지 못한 청크다. 본문이 `--bodies` 에도 `--root` 아래에도 없거나 슬롯의 형태가 다르다.", ""]
    lines += [f"- `{loc}`" for loc in sorted(missing)] or [f"- {kb_lib.NONE_MARK}"]
    lines.append("")
    inputs = list(a.files) + list(a.spaces)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, inputs, input_kind="그래프 파일"), encoding="utf-8")
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
