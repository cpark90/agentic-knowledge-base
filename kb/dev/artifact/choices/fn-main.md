---
id: https://agentic-knowledge-base.dev/id/chunk/95b58056-4fdd-47fa-aeed-2c79bc73071a
type: artifact
level: executable
title_ko: 함수 main (tools/choices.py)
title: function main in tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6c9da832-fd4f-4fba-a0f6-33561303de46
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+", help="그래프 TTL — 설계 공간(*-space)과 head(-kg)")
    a = ap.parse_args()

    g = Graph()
    for f in a.files:
        try:
            g.parse(f, format="turtle")
        except Exception as e:  # noqa: BLE001 — rdflib 의 파싱 예외는 종류가 여럿이다
            print(f"CONFIG [{kb_lib.SPACE_GATE}] 그래프를 읽을 수 없다 — {f}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG

    spaces = []
    for s in sorted(g.subjects(RDF.type, AGT.Space), key=str):
        links = sorted(g.objects(s, AGT.hasCandidate), key=str)
        # 선호는 후보 사이의 부분순서다 — 링크 IRI 가 아니라 그 후보의 이름으로 읽힌다 (p4-label-is-the-interface)
        named = {l: (lambda t: name(g, t) if t is not None else kb_lib.NONE_MARK)(next(g.objects(l, AGT.linkTo), None))
                 for l in links}
        cands = []
        for link in links:
            state = one(g, link, AGT.linkState)
            cands.append({"mark": MARK.get(state, "[ ]"), "state": state, "to": named[link],
                          "when": one(g, link, AGT.when),
                          "minus": evidence(g, link, "-"), "plus": evidence(g, link, "+"),
                          "over": sorted(named.get(o, kb_lib.compact_iri(str(o))) for o in g.objects(link, AGT.preferredOver))})
        frm = next(g.objects(s, AGT.variableFrom), None)
        kind = next(g.objects(s, AGT.variableKind), None)
        spaces.append({
            "ko": kb_lib.label_of(g, s, "ko"),
            "loc": one(g, s, AGT.assertionLocation),
            "status": one(g, s, AGT.spaceStatus),
            "from": name(g, frm) if frm is not None else kb_lib.NONE_MARK,
            "kind": f"agt:{str(kind).rsplit('/', 1)[-1]}" if kind is not None else kb_lib.NONE_MARK,
            "constraints": sorted(str(c) for c in g.objects(s, AGT.compatibilityConstraint)),
            "candidates": sorted(cands, key=lambda c: (c["mark"], c["to"])),
        })
    spaces.sort(key=lambda s: (s["status"] != "open", s["loc"], s["ko"]))

    total = sum(len(s["candidates"]) for s in spaces)

    def count(state: str) -> int:
        return sum(1 for s in spaces for c in s["candidates"] if c["state"] == state)

    head = kb_lib.gendoc_header(
        "choices", "열린 설계 변수와 후보", "tools/choices.py",
        "설계 공간 그래프에서 공간(`agt:Space`)마다 변수(출발 항목 + 링크 타입)·상태·후보를 모아 체크박스로 낸다 — "
        "`[ ]` 는 열린 후보, `[-]` 는 배제된 후보와 그 근거, `[x]` 는 확정된 후보다. 고르는 일은 이 뷰에서 하지 않는다",
        "bazel build //space:choices", a.files,
        f"설계 공간 {len(spaces)}개 · 후보 {total}개",
        kb_lib.gendoc_view_notice("`space/` 의 `-space` 청크"), input_kind="그래프 파일")

    lines = ["## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 설계 공간 | {len(spaces)} |",
             f"| 열린 변수 | {kb_lib.pct(sum(1 for s in spaces if s['status'] == 'open'), len(spaces))} |",
             f"| 후보 | {total} |",
             f"| 열린 후보 `[ ]` | {kb_lib.pct(count(kb_lib.LINK_STATE_CANDIDATE), total)} |",
             f"| 배제된 후보 `[-]` | {kb_lib.pct(count(kb_lib.LINK_STATE_INVALID), total)} |",
             f"| 확정된 후보 `[x]` | {kb_lib.pct(count(kb_lib.LINK_STATE_CONFIRMED), total)} |",
             "", "## 변수", ""]
    if not spaces:
        lines += [f"설계 공간이 {kb_lib.NONE_MARK}. `space/` 에 `-space` 청크를 두면 여기 나온다.", ""]
    for s in spaces:
        lines += [f"### {s['ko']} {QUOTE}", "",
                  f"- 변수: {s['from']} 의 `{s['kind']}` · 상태 {s['status']} · `{s['loc']}` {QUOTE}", ""]
        for c in s["candidates"]:
            parts = [f"- {c['mark']} {c['to']}"]
            if c["state"] == kb_lib.LINK_STATE_INVALID:
                parts.append("배제: " + (" · ".join(c["minus"]) or kb_lib.NONE_MARK))
            elif c["plus"]:
                parts.append("근거: " + " · ".join(c["plus"]))
            if c["when"]:
                parts.append(f"조건: `{c['when']}`")
            if c["over"]:
                parts.append("선호: " + " · ".join(c["over"]) + " 보다 앞선다")
            lines.append(" — ".join(parts) + f" {QUOTE}")
        if not s["candidates"]:
            lines.append(f"- 후보가 {kb_lib.NONE_MARK}. 변수만 선언한 공간이다.")
        lines += ["", "- 양립 제약: " + (" · ".join(f"`{c}`" for c in s["constraints"]) or kb_lib.NONE_MARK), ""]
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.files, input_kind="그래프 파일"), encoding="utf-8")
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
