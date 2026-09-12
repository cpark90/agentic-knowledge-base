#!/usr/bin/env python3
"""정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 청크 파일에서 보고한다 (p4-redundancy-as-safety-margin).

게이트가 아니라 **보고**다: 병합·묶기·유지의 판정은 사람 또는 승인된 판정자가 하고(9.8절), 이 도구는
후보를 추린다. 재검증 시점(커밋)마다 생성하고 저장하지 않는다 (4.6절 뷰 원칙).

  ① 정확 중복 — 본문 sha256 앞 12자(contentHash)가 같은 살아 있는 청크 쌍
  ② 라벨 중복 — title_ko 또는 title 이 같은 청크 (용인 불가: 라벨은 인터페이스)
  ③ 근사 중복 후보 — 본문 문자 5-gram 집합의 Jaccard ≥ θ (기본 0.5). 유사도는 후보 추림에만 쓴다
  ④ 묶임과 응집 — ①·③ 쌍이 coUpdatesWith 로 묶여 있는가(안 묶인 중복이 드리프트 후보), 그리고 묶인 쌍의 현재 본문
     Jaccard 가 θ_cohesion(기본 θ/2) 미만인가 — 응집 저하 후보: 묶었으나 본문이 갈라짐, suspect 판정 대상.
     저장된 이전 값과의 비교가 아니라 절대 임계다 — 뷰는 저장하지 않으므로(4.6절) 비교할 캐시가 없다.
     학습 모델 임베딩은 ODD 명시 제외(project-odd.yml EXCLUSIONS_REVIEWED)라 유사도는 문자 n-gram 으로만 잰다
  ⑤ 결론 라벨 형식 — 결정의 결론(conclusion.md 또는 단일 파일 결정)의 title_ko 가 문장형(…다)으로 끝나는가.
     근거·대안 라벨은 명사구가 관례라 보지 않는다 (label-representativeness-protocol (c) ④: "결정 라벨은 결론 문장형")
  ⑥ 용어 — docs/glossary.md 의 "옛 표기"가 살아 있는 청크 본문에 남아 있는가. **tier 1 (기계 치환)만** 위반이다 —
     tier 2 는 유저 결정, tier 3 은 문맥 공존(바꾸지 않음), — 는 옛 표기 없음. tier 열이 없으면 전부 1 로 보고 info 를 남긴다.
     docs/waivers.md 의 게이트 id `term-drift`(축 파일)에 면제된 파일의 히트는 집계에서 빼되 목록에 남긴다 (C)

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(용어집·waiver 표·청크 파싱 불가). 보고 뷰라 판정 실패(1)는 없다
사용: consistency.py --out consistency.md [--theta 0.5] [--theta-cohesion θ/2] [--glossary docs/glossary.md] [--waivers docs/waivers.md] <청크 .md …>
"""
import argparse
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import parse_chunk  # noqa: E402
from kb_lib import EXIT_CONFIG, EXIT_OK, load_waivers, waived  # noqa: E402

GATE_TERM = "term-drift"  # ⑥ 의 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다
LIVE = {"draft", "stable", "suspect"}


def body_of(path: str) -> str:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = lines[1:].index("---") + 1
    return "\n".join(l for l in lines[end + 1:]).strip()


def shingles(text: str, n: int = 5) -> set:
    s = re.sub(r"\s+", " ", text)
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}


def jaccard(a: set, b: set) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def old_terms(glossary: str) -> tuple[list, bool]:
    """glossary 표의 셋째 열(옛 표기)에서 **tier 1** 용어를 뽑는다 — '·'로 나뉜 항목 각각 → ([(옛, 표준)], tier 열 유무).

    tier 는 헤더에서 `tier` 열을 찾아 읽는다(값 1·2·3·—). 열이 없으면 전부 1 로 본다. 표준 용어이기도 한 옛 표기
    ("검증"·"프로파일")의 예외는 코드에 없다 — 그 자리는 tier 3 이 맡는다 (agrtls-practices-review-2026-09-12 B).
    """
    rows, tier_col = [], None
    for line in Path(glossary).read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0].startswith("표준 용어"):
            tier_col = next((i for i, c in enumerate(cells) if c.strip("`").lower() == "tier"), None)
            continue
        if len(cells) < 4 or all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    out = []
    for r in rows:
        tier = r[tier_col].strip("`") if tier_col is not None and tier_col < len(r) else "1"
        if tier != "1":
            continue
        for t in re.split(r"\s*·\s*", r[2]):
            t = t.strip()
            if t and t != "—" and len(t) >= 2:
                out.append((t, r[0]))
    return out, tier_col is not None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--theta", type=float, default=0.5)
    ap.add_argument("--theta-cohesion", type=float, default=None, help="묶인 쌍의 응집 하한 (기본 θ/2)")
    ap.add_argument("--glossary", default="")
    ap.add_argument("--waivers", default="", help="docs/waivers.md — 게이트 id term-drift, 축 파일")
    ap.add_argument("chunks", nargs="+")
    a = ap.parse_args()
    theta_c = a.theta_cohesion if a.theta_cohesion is not None else a.theta / 2

    def config_fail(msg: str) -> int:
        print(f"CONFIG [consistency] {msg}", file=sys.stderr)
        return EXIT_CONFIG

    try:
        waivers = load_waivers(a.waivers) if a.waivers else []
    except (OSError, ValueError) as e:
        return config_fail(str(e))
    try:
        terms, has_tier = old_terms(a.glossary) if a.glossary else ([], True)
    except OSError as e:
        return config_fail(f"용어집을 읽을 수 없다 — {e}")

    items = []
    for p in a.chunks:
        if not p.endswith(".md"):
            continue
        try:
            meta, n = parse_chunk(p)
        except ValueError as e:
            return config_fail(f"청크를 파싱할 수 없다 — {e}")
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
        j = jaccard(sx, sy)
        if j >= a.theta:
            near.append((j, x, y))
    near.sort(key=lambda t: -t[0])

    # ④ 묶임과 응집 — coUpdatesWith 로 묶인 쌍(살아 있는 입력 안의 것만)의 현재 본문 Jaccard 가 θ_cohesion 미만이면
    #    응집 저하 후보. 이전 값과 비교하지 않는다 — 뷰는 저장하지 않으므로 캐시가 없다 (4.6절). 절대 임계
    bound = sorted({tuple(sorted((x["id"], c))) for x in items for c in x["co"] if c in by_id and c != x["id"]})
    cohesion = [(jaccard(sh[xi], sh[yi]), by_id[xi], by_id[yi]) for xi, yi in bound]
    cohesion_low = sorted((t for t in cohesion if t[0] < theta_c), key=lambda t: t[0])

    # ⑤ 결론 라벨 형식 — 결정의 결론만 문장형. 판정은 경로 basename: conclusion.md 이거나
    #    근거·대안(rationale.md·alternatives.md)이 아닌 단일 파일 결정(chunks/decision/d-*.md)
    def is_conclusion(it):
        return it["type"] == "decision" and Path(it["path"]).name not in ("rationale.md", "alternatives.md")

    bad_form = [it for it in items if is_conclusion(it) and not re.search(r"(다|음|함|없음|있음)$", it["title_ko"])]

    # ⑥ 용어 — tier 1 만. 면제 파일(waivers.md, term-drift)의 히트는 집계에서 빼되 목록에 남긴다
    term_hits, term_waived = [], []
    for old, std in terms:
        for it in items:
            if old in it["body"] or old in it["title_ko"]:
                (term_waived if waived(waivers, GATE_TERM, it["path"], "파일") else term_hits).append((old, std, it))

    def ref(it):
        return f"`{it['path']}` — {it['title_ko']}"

    total_pairs = len(exact) and sum(len(g) * (len(g) - 1) // 2 for g in exact)
    unlinked_exact = [g for g in exact if not all(linked(x, y) for x, y in combinations(g, 2))]
    unlinked_near = [(j, x, y) for j, x, y in near if not linked(x, y)]

    lines = ["# consistency — 정합성 보고 (생성물, 저장하지 않는다)", "",
             f"살아 있는 청크 {len(items)} · θ = {a.theta} · θ_cohesion = {theta_c:g}", "",
             "## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 정확 중복 묶음 | {len(exact)} (쌍 {total_pairs}) — coUpdatesWith 미묶음 {len(unlinked_exact)} |",
             f"| 라벨 중복 | {len(label_dups)} (용인 불가) |",
             f"| 근사 중복 후보 (Jaccard ≥ θ) | {len(near)} — 미묶음 {len(unlinked_near)} |",
             f"| 묶인 쌍 중 응집 저하 (coUpdatesWith, Jaccard < θ_cohesion) | {len(cohesion_low)} / 묶인 쌍 {len(bound)} |",
             f"| 결론 라벨 형식 위반 | {len(bad_form)} |",
             f"| 용어집 옛 표기 잔존 (tier 1) | {len(term_hits)} — 면제 {len(term_waived)}건(waivers.md) |",
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
    lines += ["", f"## ④ 묶인 쌍의 응집 저하 (coUpdatesWith 쌍 {len(bound)}, Jaccard < {theta_c:g}) — 판정: suspect / 유지", ""]
    for j, x, y in cohesion_low[:50]:
        lines.append(f"- {j:.2f} **응집 저하 — 묶었으나 본문이 갈라짐**: {ref(x)}  ↔  {ref(y)}")
    if not cohesion_low:
        lines.append("- 없음")
    if len(cohesion_low) > 50:
        lines.append(f"- … {len(cohesion_low) - 50}건 더")
    lines += ["", "## ⑤ 결론 라벨 형식 위반 (문장형이 아님)", ""]
    for it in bad_form[:50]:
        lines.append(f"- {ref(it)}")
    if not bad_form:
        lines.append("- 없음")
    lines += ["", "## ⑥ 용어집 옛 표기 잔존 (옛 → 표준, tier 1 만)", ""]
    if a.glossary and not has_tier:
        lines.append("- info: 용어집에 `tier` 열이 없다 — 옛 표기를 전부 tier 1(기계 치환)로 본다")
    for old, std, it in term_hits[:80]:
        lines.append(f"- `{old}` → `{std}`: `{it['path']}`")
    if not term_hits:
        lines.append("- 없음")
    if len(term_hits) > 80:
        lines.append(f"- … {len(term_hits) - 80}건 더")
    if term_waived:
        lines.append(f"- 면제 {len(term_waived)}건(waivers.md, `{GATE_TERM}`) — 집계에서 뺐다:")
        lines += [f"  - `{old}` → `{std}`: `{it['path']}`" for old, std, it in term_waived[:80]]
    Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
