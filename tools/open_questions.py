#!/usr/bin/env python3
"""미결 집계 뷰 — 청크 본문의 선택 슬롯 `미확정:` 을 모아 open.md 를 생성한다 (p4-three-empty-values, p4-slot-answers-one-question).

미결을 문서가 아니라 항목 안에 두면 집계가 생성물이 되고, 답이 왔을 때 고칠 자리가 하나다. 이 뷰는 그 집계만
맡는다 — 미결의 상세(다섯 절)는 42줄 청크에 들어가지 않아 `docs/open-questions.md` 색인과 그 아래 문서로 남고,
뷰는 그것을 대체하지 않는다.

  입력  head 그래프(agt:bodySlot "미확정" 인 청크의 라벨·plane·level·상태·본문 위치)와 그 청크의 본문.
        슬롯 표지는 chunk2kg 가 본문에서 찾아 넣은 값이다 — 여기서 본문을 다시 훑지 않고 그래프가 대상을 고른다.
  계산  본문에서 `미확정: <질문 한 문장>. 상세는 `<문서>`다.` 줄을 뽑아 질문과 상세 문서 경로로 가른다.
        상세 경로가 없으면 `없음` 이다. 미결이 없어도 절을 낸다.
  판정  없음 — 뷰이고 게이트가 아니다. 미결의 해소는 답이 온 뒤 청크의 슬롯을 고치는 것이고 사람이 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음·본문 없음)
사용: open_questions.py --out open.md [--bodies <청크 .md …>] [--root .] <TTL…>   (bazel build //kg:open)
"""
import argparse
import re
import sys
from pathlib import Path

import rdflib
from rdflib import Graph, Namespace, RDF

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
SLOT = "미확정"  # 선택 슬롯의 표지 — 값 어휘의 정의처는 chunk2kg.BODY_SLOT_KEYWORDS 다
# `미확정: <질문>. 상세는 `<문서>`다.` — 상세 절은 선택이다. 질문만 적은 슬롯도 집계 대상이다
SLOT_LINE = re.compile(r"^" + SLOT + r":\s*(.+)$")
DETAIL = re.compile(r"상세는\s*`([^`]+)`\s*다\.?\s*$")
INDEX_DOC = "docs/open-questions.md"  # 손으로 관리하는 색인 — 이 뷰는 집계만 맡고 색인을 대체하지 않는다


# ── 본문의 미확정 슬롯을 모아 낸다 ────────────────────

def cell(s: str) -> str:
    """표 셀 — 줄바꿈과 파이프를 없앤다. 빈 값은 세 빈 값의 첫 값이다."""
    return " ".join(str(s).split()).replace("|", "\\|") or kb_lib.NONE_MARK


def question_of(body: str) -> tuple[str, str]:
    """본문 → (질문, 상세 문서 경로). 슬롯 줄이 없으면 ('', '')."""
    for line in body.split("\n"):
        m = SLOT_LINE.match(line.strip())
        if not m:
            continue
        text = m.group(1).strip()
        d = DETAIL.search(text)
        return (text[:d.start()].strip().rstrip(".").strip() if d else text), (d.group(1) if d else "")
    return "", ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bodies", nargs="*", default=[], help="청크 .md — 그래프의 assertionLocation 과 접미로 맞춘다")
    ap.add_argument("--root", default=".")
    ap.add_argument("files", nargs="+", help="그래프 TTL (head 포함)")
    a = ap.parse_args()
    root = Path(a.root)

    g = Graph()
    for f in a.files:
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

    rows, missing = [], []
    for c in sorted(set(g.subjects(AGT.bodySlot, rdflib.Literal(SLOT))), key=str):
        loc = str(next(g.objects(c, AGT.assertionLocation), ""))
        q, detail = question_of(body_of(loc))
        if not q:
            missing.append(loc)
            continue
        rows.append({
            "q": q, "detail": detail, "loc": loc,
            "ko": kb_lib.label_of(g, c, "ko"),
            "iri": kb_lib.compact_iri(str(c)),
            "plane": str(next(g.objects(c, RDF.type), "")).split("/")[-1].replace("Chunk", "").lower(),
            "level": str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1],
            "status": str(next(g.objects(c, AGT.status), "")),
        })
    rows.sort(key=lambda r: (r["loc"], r["q"]))

    head = kb_lib.gendoc_header(
        "open", "미결 집계", "tools/open_questions.py",
        f"head 그래프에서 선택 슬롯 `{SLOT}:` 을 가진 청크(`agt:bodySlot \"{SLOT}\"`)를 모아, 미결마다 질문 · 그것을 안은 청크(라벨·IRI) · "
        f"plane/level · 상세 문서를 낸다. **집계만 맡는다** — 미결의 상세 다섯 절은 42줄 청크에 들어가지 않아 "
        f"`{INDEX_DOC}` 색인과 그 아래 문서로 남고 이 뷰가 그것을 대체하지 않는다",
        "bazel build //kg:open", a.files, f"미결 {len(rows)}개 · 청크 {len({r['loc'] for r in rows})}개",
        kb_lib.gendoc_view_notice("미결을 안은 청크의 `미확정:` 슬롯"), input_kind="그래프 파일")

    lines = ["## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 미결 | {len(rows)} |",
             f"| 미결을 안은 청크 | {len({r['loc'] for r in rows})} |",
             f"| plane 분포 | " + (" · ".join(f"{p} {sum(1 for r in rows if r['plane'] == p)}"
                                              for p in sorted({r["plane"] for r in rows})) or kb_lib.NONE_MARK) + " |",
             f"| 상세 문서가 있는 미결 | {kb_lib.pct(sum(1 for r in rows if r['detail']), len(rows))} |",
             f"| 슬롯은 있으나 질문을 못 읽은 청크 | {len(missing)} |",
             "", "## 미결", "",
             "| 질문 | 청크 | plane/level | 상태 | 상세 |", "|---|---|---|---|---|"]
    for r in rows:
        # 링크가 아니라 코드 스팬이다 — 생성물은 bazel-bin/kg/ 에 놓이므로 소스 기준 상대경로가 성립하지 않는다 (STYLEGUIDE §9)
        detail = f"`{r['detail']}`" if r["detail"] else kb_lib.NONE_MARK
        lines.append(f"| {cell(r['q'])} | {cell(r['ko'])}<br>`{r['iri']}` | {cell(r['plane'])}/{cell(r['level'])} | "
                     f"{cell(r['status'])} | {detail} |")
    if not rows:
        lines.append("| " + " | ".join([kb_lib.NONE_MARK] * 5) + " |")

    lines += ["", "## 슬롯을 읽지 못한 청크", "",
              f"슬롯 표지는 있으나 `{SLOT}: <질문>` 줄을 본문에서 찾지 못한 청크다. 본문이 `--bodies` 에도 `--root` 아래에도 없거나 슬롯의 형태가 다르다.", ""]
    lines += [f"- `{loc}`" for loc in sorted(missing)] or [f"- {kb_lib.NONE_MARK}"]
    lines.append("")
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.files, input_kind="그래프 파일"), encoding="utf-8")
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
