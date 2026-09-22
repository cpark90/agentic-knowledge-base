#!/usr/bin/env python3
"""설계 공간의 체크박스 뷰 — 열린 설계 변수와 그 후보를 choices.md 로 생성한다 (결정 p9-candidate-storage 13.5절).

후보는 `-space` 청크에 살고 사람에게는 체크박스로 보인다 — `[ ]` 는 열린 후보, `[-]` 는 배제된 후보와 그 근거,
`[x]` 는 확정된 후보다. `[x]` 하나만 남으면 그 변수는 resolved 다. 무엇을 아직 고르지 않았는지 한 화면에서 읽는
것이 이 뷰의 목적이고, 고르는 일은 여기서 하지 않는다 — 확정은 `-space` 청크의 `state` 를 고치고 생성기가 후보를
head 로 옮기는 것이며 그것이 한 줄 diff 로 리뷰된다.

  입력  설계 공간 그래프(`*-space.ttl`, tools/space2kg.py 의 생성물)와 head 그래프(후보·출발 항목의 라벨).
  계산  공간마다 변수(출발 항목 + 링크 타입) · 상태 · 후보의 체크 표시 · 배제 근거 · 양립 제약 · 선호를 낸다.
        체크 표시는 링크 상태에서 온다 — candidate 는 `[ ]`, invalid 는 `[-]`, confirmed 는 `[x]` 다.
  판정  없음 — 뷰이고 게이트가 아니다. 판정은 `//kg:gate_test` 의 `check_space`(게이트 id `space`)가 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음)
사용: choices.py --out choices.md <TTL…>   (bazel build //space:choices)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import Graph, RDF

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = kb_lib.AGT
QUOTE = kb_lib.GENDOC_QUOTE_LINE  # 라벨은 그래프에서 그대로 가져온 값이다 — 생성기가 고쳐 쓰지 않는다
# 링크 상태 → 체크 표시 (p9-candidate-storage 13.5절). 상태의 정의처는 kb_lib.SPACE_STATE_LINK 다
MARK = {kb_lib.LINK_STATE_CANDIDATE: "[ ]", kb_lib.LINK_STATE_INVALID: "[-]", kb_lib.LINK_STATE_CONFIRMED: "[x]"}


def one(g: Graph, s, p) -> str:
    return str(next(g.objects(s, p), ""))


def name(g: Graph, node) -> str:
    """항목의 사람 이름 — 한글 라벨과 축약 IRI. 라벨이 인터페이스다 (p4-label-is-the-interface)."""
    return f"{kb_lib.label_of(g, node, 'ko')} `{kb_lib.compact_iri(str(node))}`"


def evidence(g: Graph, link, polarity: str) -> list[str]:
    """링크의 증거 기록 중 극성이 맞는 것 — "<종류 라벨> `<참조>`" 목록."""
    out = []
    for e in sorted(g.objects(link, AGT.hasEvidence), key=str):
        if str(next(g.objects(e, AGT.polarity), "")) != polarity:
            continue
        kind = next(g.objects(e, AGT.evidenceKind), None)
        ref = next(g.objects(e, AGT.evidenceRef), None)
        label = kb_lib.label_of(g, kind, "ko") if kind is not None else kb_lib.NONE_MARK
        out.append(f"{label} `{kb_lib.compact_iri(str(ref))}`" if ref is not None else label)
    return sorted(out)


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


if __name__ == "__main__":
    sys.exit(main())
