#!/usr/bin/env python3
"""정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 청크 파일에서 보고한다 (p4-redundancy-as-safety-margin).

게이트가 아니라 **보고**다: 병합·묶기·유지의 판정은 사람 또는 승인된 판정자가 하고(9.8절), 이 도구는
후보를 추린다. 재검증 시점(커밋)마다 생성하고 저장하지 않는다 (4.6절 뷰 원칙).

  ① 정확 중복 — 본문 sha256 앞 12자(contentHash)가 같은 살아 있는 청크 쌍
  ② 라벨 중복 — title_ko 또는 title 이 같은 청크 (용인 불가: 라벨은 인터페이스)
  ③ 근사 중복 후보 — 본문 문자 5-gram 집합의 Jaccard ≥ θ (기본 0.5). 유사도는 후보 추림에만 쓴다
  ④ 묶임 여부 — ①·③ 쌍이 coUpdatesWith 로 묶여 있는가. 안 묶인 중복이 드리프트 후보다
  ⑤ 결론 라벨 형식 — 결정의 결론(conclusion.md 또는 단일 파일 결정)의 title_ko 가 문장형(…다)으로 끝나는가.
     근거·대안 라벨은 명사구가 관례라 보지 않는다 (label-representativeness-protocol (c) ④: "결정 라벨은 결론 문장형")
  ⑥ 용어 — docs/glossary.md 의 "옛 표기"가 살아 있는 청크 본문에 남아 있는가

사용: consistency.py --out consistency.md [--theta 0.5] [--glossary docs/glossary.md] <청크 .md …>
"""
import argparse
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import parse_chunk  # noqa: E402

LIVE = {"draft", "stable", "suspect"}


def body_of(path: str) -> str:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = lines[1:].index("---") + 1
    return "\n".join(l for l in lines[end + 1:]).strip()


def shingles(text: str, n: int = 5) -> set:
    s = re.sub(r"\s+", " ", text)
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}


def old_terms(glossary: str) -> list:
    """glossary 표의 셋째 열(옛 표기)에서 용어를 뽑는다 — '·'로 나뉜 항목 각각."""
    rows = []
    for line in Path(glossary).read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].startswith("---") or cells[0] == "표준 용어 (ko)":
            continue
        rows.append(cells)
    standard = {s.strip() for r in rows for s in re.split(r"\s*·\s*", r[0])}
    out = []
    for r in rows:
        for t in re.split(r"\s*·\s*", r[2]):
            t = t.strip()
            # 표준 용어이기도 한 옛 표기(예: "검증")는 잔존으로 세지 않는다
            if t and t != "—" and len(t) >= 2 and t not in standard:
                out.append((t, r[0]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--theta", type=float, default=0.5)
    ap.add_argument("--glossary", default="")
    ap.add_argument("chunks", nargs="+")
    a = ap.parse_args()

    items = []
    for p in a.chunks:
        if not p.endswith(".md"):
            continue
        meta, n = parse_chunk(p)
        if meta.get("status") not in LIVE:
            continue
        items.append({"path": p, "id": meta["id"], "type": meta["type"], "level": meta["level"],
                      "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
                      "hash": meta["_content_hash"], "body": body_of(p), "lines": n,
                      "co": set(meta.get("coUpdatesWith", []) or [])})
    by_id = {it["id"]: it for it in items}

    def linked(x, y):
        return y["id"] in x["co"] or x["id"] in y["co"]

    # ① 정확 중복
    by_hash = defaultdict(list)
    for it in items:
        by_hash[it["hash"]].append(it)
    exact = [grp for grp in by_hash.values() if len(grp) > 1]

    # ② 라벨 중복
    by_label = defaultdict(list)
    for it in items:
        for key in ("title_ko", "title"):
            if it[key]:
                by_label[(key, it[key])].append(it)
    label_dups = [(k, grp) for k, grp in by_label.items() if len(grp) > 1]

    # ③ 근사 중복 후보 (정확 중복 제외)
    sh = {it["id"]: shingles(it["body"]) for it in items}
    near = []
    for x, y in combinations(items, 2):
        if x["hash"] == y["hash"]:
            continue
        sx, sy = sh[x["id"]], sh[y["id"]]
        if not sx or not sy:
            continue
        j = len(sx & sy) / len(sx | sy)
        if j >= a.theta:
            near.append((j, x, y))
    near.sort(key=lambda t: -t[0])

    # ⑤ 결론 라벨 형식 — 결정의 결론만 문장형. 판정은 경로 basename: conclusion.md 이거나
    #    근거·대안(rationale.md·alternatives.md)이 아닌 단일 파일 결정(chunks/decision/d-*.md)
    def is_conclusion(it):
        return it["type"] == "decision" and Path(it["path"]).name not in ("rationale.md", "alternatives.md")

    bad_form = [it for it in items if is_conclusion(it) and not re.search(r"(다|음|함|없음|있음)$", it["title_ko"])]

    # ⑥ 용어
    term_hits = []
    if a.glossary:
        for old, std in old_terms(a.glossary):
            for it in items:
                if old in it["body"] or old in it["title_ko"]:
                    term_hits.append((old, std, it))

    def ref(it):
        return f"`{it['path']}` — {it['title_ko']}"

    total_pairs = len(exact) and sum(len(g) * (len(g) - 1) // 2 for g in exact)
    unlinked_exact = [g for g in exact if not all(linked(x, y) for x, y in combinations(g, 2))]
    unlinked_near = [(j, x, y) for j, x, y in near if not linked(x, y)]

    lines = ["# consistency — 정합성 보고 (생성물, 저장하지 않는다)", "",
             f"살아 있는 청크 {len(items)} · θ = {a.theta}", "",
             "## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 정확 중복 묶음 | {len(exact)} (쌍 {total_pairs}) — coUpdatesWith 미묶음 {len(unlinked_exact)} |",
             f"| 라벨 중복 | {len(label_dups)} (용인 불가) |",
             f"| 근사 중복 후보 (Jaccard ≥ θ) | {len(near)} — 미묶음 {len(unlinked_near)} |",
             f"| 결론 라벨 형식 위반 | {len(bad_form)} |",
             f"| 용어집 옛 표기 잔존 | {len(term_hits)} |",
             f"| **중복률** (정확·근사 관련 청크 / 전체) | {len({i['id'] for g in exact for i in g} | {i['id'] for _, x, y in near for i in (x, y)})}/{len(items)} |",
             ""]
    lines += ["## ① 정확 중복 (contentHash 동일)", ""]
    for g in exact:
        tag = "묶임" if all(linked(x, y) for x, y in combinations(g, 2)) else "**미묶음 — 드리프트 후보**"
        lines.append(f"- {tag}: " + " / ".join(ref(i) for i in g))
    if not exact:
        lines.append("- 없음")
    lines += ["", "## ② 라벨 중복 (용인 불가)", ""]
    for (key, val), g in label_dups:
        lines.append(f"- `{key}` = \"{val}\": " + " / ".join(f"`{i['path']}`" for i in g))
    if not label_dups:
        lines.append("- 없음")
    lines += ["", f"## ③ 근사 중복 후보 (Jaccard ≥ {a.theta}) — 판정: 병합 / 묶기 / 유지", ""]
    for j, x, y in near[:50]:
        tag = "묶임" if linked(x, y) else "미묶음"
        lines.append(f"- {j:.2f} {tag}: {ref(x)}  ↔  {ref(y)}")
    if not near:
        lines.append("- 없음")
    if len(near) > 50:
        lines.append(f"- … {len(near) - 50}건 더")
    lines += ["", "## ⑤ 결론 라벨 형식 위반 (문장형이 아님)", ""]
    for it in bad_form[:50]:
        lines.append(f"- {ref(it)}")
    if not bad_form:
        lines.append("- 없음")
    lines += ["", "## ⑥ 용어집 옛 표기 잔존 (옛 → 표준)", ""]
    for old, std, it in term_hits[:80]:
        lines.append(f"- `{old}` → `{std}`: `{it['path']}`")
    if not term_hits:
        lines.append("- 없음")
    if len(term_hits) > 80:
        lines.append(f"- … {len(term_hits) - 80}건 더")
    Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
