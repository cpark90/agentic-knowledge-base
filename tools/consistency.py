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
  ⑦ 단정성 — STYLEGUIDE §0 "산문은 단정 서술형"(유저 결정 2026-09-13) 가운데 게이트 `prose`(chunk_lint·doccheck: 경어·감탄)가
     거부하지 않는, 판단이 필요한 나머지: 추측 표현(것 같·듯하·수도 있·아마 …)·구어 후보(근데·그냥·좀·엄청·뭔가·약간)의
     파일·줄·표현 목록과, 대시 밀도(문장당 " — " 수; 문장 = 마침표 종결 또는 마침표 없는 종결 "다" 뒤에 `|`·`)`·닫는 따옴표·
     줄끝이 오는 곳 — 명사형 종결 "기각." 과 표 셀 "…다 |" 를 다 센다; 줄·불릿·셀 첫머리의 종결 없는 짧은 라벨 뒤의
     라벨 대시 "**결론** — "·"- 라벨 — " 는 구조적 구분자라 세지 않는다)가 1.0 을 넘는 청크(상위 20). 목록·정규식의 단일 정의처는 kb_lib(PROSE_HEDGES·PROSE_COLLOQUIAL·PROSE_SENTENCE_END·prose_segments).
     대시·문장 모두 산문 조각(prose_segments) 안에서만 센다 — 코드·따옴표 안은 산문이 아니다
  ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기(명세 문서 작성 규격 4.1·9.4절, 유저 승인 2026-09-22;
     결정 p4-three-empty-values). 셋을 본다: 메타 문장(다음과 같다·이 절에서는 …), 채움 문구(특이사항 없음·추후 결정한다 …),
     세 빈 값(`없음`·`해당 없음`·`미확정`) 밖의 표기(`N/A`·`TBD`·`미정`·표의 단독 대시 셀). 정의처는 kb_lib
     (PROSE_META·PROSE_FILLER·EMPTY_VALUE·EMPTY_VALUE_REJECTED·check_addition)
  ⑨ 목록 — 목록 규칙(같은 규격 4.3절): 손 번호(`2.` 이상 — 순서 목록의 항목은 모두 `1.` 로 쓴다) · 항목 9개 초과 ·
     중첩 3단계 이상 · 항목당 240자 초과 · 빈 항목. 같은 문법 형은 기계 판정이 되지 않아 보지 않는다. 항목 길이는
     소스 줄이 아니라 **글자**로 잰다 — 이어지는 들여쓴 줄을 합치고 연속 공백을 하나로 줄인 뒤 센다. 손 줄바꿈이
     110~120자라 소스 줄을 세면 접힌 자리가 그대로 위반이 된다 (STYLEGUIDE §0, 유저 승인 2026-09-22). 정의처는
     kb_lib(LIST_MAX_ITEMS·LIST_MAX_DEPTH·LIST_MAX_ITEM_CHARS·check_lists)

⑧·⑨ 의 **판정은 게이트 `chunk_lint`** 가 한다 — 게이트 id 는 `addition`(메타 문장·채움 문구)·`empty-value`(빈 값 표기)·
`list-rules`(목록 규칙)이고, 보고 수치가 0 이 된 2026-09-22 에 올렸다(반영 계획 7번, STYLEGUIDE §2 — 강화는 약화가 아니다).
이 절은 목록과 맥락을 주는 보고로 남는다. 둘이 같은 함수(kb_lib.check_addition·check_lists)를 쓰므로 수치가 갈리지 않는다.
⑥ 과 같은 규약으로 waivers.md 의 면제는 집계에서 빼되 목록에 남긴다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(용어집·waiver 표·청크 파싱 불가). 보고 뷰라 판정 실패(1)는 없다
사용: consistency.py --out consistency.md [--theta 0.5] [--theta-cohesion θ/2] [--glossary docs/glossary.md] [--waivers docs/waivers.md] <청크 .md …>
"""
import argparse
import os
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402
import kb_lib  # noqa: E402 — 규약 상수·머리 블록·비율 표기의 단일 정의처 (STYLEGUIDE §7)
from kb_lib import (ADDITION_GATE, EMPTY_VALUE_GATE, EXIT_CONFIG, EXIT_OK, LIST_MAX_DEPTH, LIST_MAX_ITEM_CHARS,  # noqa: E402
                    LIST_MAX_ITEMS, LIST_RULES_GATE, LIVE_STATES, PROSE_LABEL_DASH, PROSE_SENTENCE_END,
                    check_addition, check_lists, check_prose, load_waivers, prose_segments, waived)

GATE_TERM = "term-drift"  # ⑥ 의 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다
LIVE = set(LIVE_STATES)  # 게이트 chunk_lint 와 같은 대상 집합 (kb_lib 단일 정의처)


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
    ap.add_argument("--waivers", default="",
                    help=f"docs/waivers.md — 게이트 id {GATE_TERM}·{ADDITION_GATE}·{EMPTY_VALUE_GATE}·{LIST_RULES_GATE}, 축 파일")
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(kb_consistency 매크로가 명시로 넘긴다)")
    ap.add_argument("chunks", nargs="+")
    a = ap.parse_args()
    theta_c = a.theta_cohesion if a.theta_cohesion is not None else a.theta / 2

    def config_fail(msg: str) -> int:
        print(f"CONFIG [consistency] {msg}", file=sys.stderr)
        return EXIT_CONFIG

    try:
        apply_plane_level_state(*load_plane_level_state(a.residency))
    except (OSError, ValueError) as e:
        return config_fail(f"{a.residency}: 읽을 수 없다 — {e}")
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

    # ⑦ 단정성 — 게이트 prose 가 거부하지 않는 나머지(추측·구어·대시 밀도)를 보고한다. 판정은 사람 몫이다.
    #    대시 밀도 = 산문 조각 안의 " — " 수 / max(1, 문장 수). 문장 = PROSE_SENTENCE_END(마침표 종결, 또는 마침표 없는 종결 "다" +
    #    | ) 닫는 따옴표 줄끝). "다." 만 세면 209/621, 종결 "다" 기반은 130 — 명사형 종결·인용 괄호를 놓쳐 대안 양식이 전부
    #    걸렸다(대리의 결함). 마침표 종결까지 세면 28 — 그 상위는 라벨 대시("- 라벨 — 설명", "| 셀 | `id` — 설명")의 불릿·표
    #    청크라 라벨 대시를 뺀다(PROSE_LABEL_DASH) → 1. 문장 없이 절 대시만 있는 청크는 여전히 잡힌다
    # ⑧ 첨가 · ⑨ 목록 — 같은 본문을 한 번만 읽어 ⑦ 과 함께 센다. 셋 다 보고이고 판정은 사람 몫이다
    hedge_hits, colloq_hits, dash_dense = [], [], []
    meta_hits, filler_hits, empty_hits, list_hits = [], [], [], []
    meta_waived, filler_waived, empty_waived, list_waived = [], [], [], []
    for it in items:
        text = Path(it["path"]).read_text(encoding="utf-8")
        _, hedges, colloquial = check_prose(it["path"], text)
        hedge_hits += [(it, ln, expr) for ln, expr in hedges]
        colloq_hits += [(it, ln, expr) for ln, expr in colloquial]
        m_hits, f_hits, e_hits = check_addition(text)
        # 면제(waivers.md, 축 파일)는 집계에서 빼되 목록에 남긴다 — ⑥ 이 선례다
        for gate, hits, out, out_w in ((ADDITION_GATE, m_hits, meta_hits, meta_waived),
                                       (ADDITION_GATE, f_hits, filler_hits, filler_waived),
                                       (EMPTY_VALUE_GATE, e_hits, empty_hits, empty_waived)):
            dst = out_w if waived(waivers, gate, it["path"], "파일") else out
            dst.extend((it, ln, expr, quote) for ln, expr, quote in hits)
        lw = waived(waivers, LIST_RULES_GATE, it["path"], "파일")
        (list_waived if lw else list_hits).extend((it, ln, why) for ln, why in check_lists(text))
        segs = [seg for _, seg in prose_segments(text)]
        dashes = sum(seg.count(" — ") - len(PROSE_LABEL_DASH.findall(seg)) for seg in segs)  # 라벨 대시는 절 연결이 아니다
        sentences = sum(len(PROSE_SENTENCE_END.findall(seg)) for seg in segs)
        density = dashes / max(sentences, 1)
        if density > 1.0:
            dash_dense.append((density, dashes, sentences, it))
    dash_dense.sort(key=lambda t: (-t[0], t[3]["path"]))
    # ⑨ 의 위반을 규칙별로 센다 — 규칙마다 다음 행동이 다르다(번호는 치환, 줄 수·항목 수는 분할)
    LIST_KINDS = (("손 번호", "손 번호"), ("항목 수", "개다"), ("중첩", "중첩"), ("항목 길이", "자다"), ("빈 항목", "빈 목록"))
    list_kinds = [(name, sum(1 for _, _, why in list_hits if key in why)) for name, key in LIST_KINDS]
    list_kinds = [(k, v) for k, v in list_kinds if v]

    def ref(it):
        return f"`{it['path']}` — {it['title_ko']}"

    total_pairs = len(exact) and sum(len(g) * (len(g) - 1) // 2 for g in exact)
    unlinked_exact = [g for g in exact if not all(linked(x, y) for x, y in combinations(g, 2))]
    unlinked_near = [(j, x, y) for j, x, y in near if not linked(x, y)]

    dup_ids = {i["id"] for g in exact for i in g} | {i["id"] for _, x, y in near for i in (x, y)}
    head = kb_lib.gendoc_header(
        "consistency", "정합성 보고", "tools/consistency.py",
        f"살아 있는 청크의 본문 사이에서 — 정확 중복(contentHash 동일) · 라벨 중복 · 근사 중복 후보(5-shingle Jaccard ≥ {a.theta}) · "
        f"coUpdatesWith 로 묶인 쌍의 응집 저하(Jaccard < {theta_c:g}) · 결론 라벨 형식 · 용어집 옛 표기 · 단정성(추측·구어·대시 밀도) · "
        "첨가(메타 문장·채움 문구·빈 값 이상 표기) · 목록 규칙(손 번호·항목 수·중첩·항목 길이·빈 항목). "
        "병합·묶기·유지 판정은 사람이 하고, ⑧·⑨ 의 통과·실패 판정은 게이트 chunk_lint 가 한다",
        "bazel build //kb:consistency", a.chunks,
        f"청크 {len(items)}개 · θ = {a.theta} · θ_cohesion = {theta_c:g}",
        kb_lib.gendoc_view_notice("각 청크의 본문"), input_kind="청크 파일")
    lines = ["## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 정확 중복 묶음 | {len(exact)} (쌍 {total_pairs}) — coUpdatesWith 미묶음 {len(unlinked_exact)} |",
             f"| 라벨 중복 | {len(label_dups)} (용인 불가) |",
             f"| 근사 중복 후보 (Jaccard ≥ θ) | {len(near)} — 미묶음 {len(unlinked_near)} |",
             f"| 묶인 쌍 중 응집 저하 (coUpdatesWith, Jaccard < θ_cohesion) | {len(cohesion_low)} / 묶인 쌍 {len(bound)} |",
             f"| 결론 라벨 형식 위반 | {len(bad_form)} |",
             f"| 용어집 옛 표기 잔존 (tier 1) | {len(term_hits)} — 면제 {len(term_waived)}건(waivers.md) |",
             f"| 추측 표현 (⑦, 보고) | {len(hedge_hits)}건 / 청크 {len({h[0]['id'] for h in hedge_hits})} |",
             f"| 구어 후보 (⑦, 보고) | {len(colloq_hits)}건 / 청크 {len({h[0]['id'] for h in colloq_hits})} |",
             f"| 대시 밀도 > 1.0 (⑦, 문장당 \" — \") | {len(dash_dense)} / {len(items)} |",
             f"| 메타 문장 (⑧, 게이트 `{ADDITION_GATE}`) | {len(meta_hits)}건 / 청크 {len({h[0]['id'] for h in meta_hits})}"
             f" — 면제 {len(meta_waived)}건(waivers.md) |",
             f"| 채움 문구 (⑧, 게이트 `{ADDITION_GATE}`) | {len(filler_hits)}건 / 청크 {len({h[0]['id'] for h in filler_hits})}"
             f" — 면제 {len(filler_waived)}건(waivers.md) |",
             f"| 빈 값 이상 표기 (⑧, 게이트 `{EMPTY_VALUE_GATE}`) | {len(empty_hits)}건 / 청크 {len({h[0]['id'] for h in empty_hits})}"
             f" — 면제 {len(empty_waived)}건(waivers.md) |",
             f"| 목록 규칙 위반 (⑨, 게이트 `{LIST_RULES_GATE}`) | {len(list_hits)}건 / 청크 {len({h[0]['id'] for h in list_hits})}"
             f" — 면제 {len(list_waived)}건(waivers.md) — " +
             (" · ".join(f"{k} {v}" for k, v in list_kinds) or kb_lib.NONE_MARK) + " |",
             f"| **중복률** (정확·근사 관련 청크 / 전체) | {kb_lib.pct(len(dup_ids), len(items))} |",
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
        lines.append(f"- {kb_lib.num(j)} {tag}: {ref(x)}  ↔  {ref(y)}")
    if not near:
        lines.append("- 없음")
    if len(near) > 50:
        lines.append(f"- … {len(near) - 50}건 더")
    lines += ["", f"## ④ 묶인 쌍의 응집 저하 (coUpdatesWith 쌍 {len(bound)}, Jaccard < {theta_c:g}) — 판정: suspect / 유지", ""]
    for j, x, y in cohesion_low[:50]:
        lines.append(f"- {kb_lib.num(j)} **응집 저하 — 묶었으나 본문이 갈라짐**: {ref(x)}  ↔  {ref(y)}")
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
    lines += ["", "## ⑦ 단정성 — 추측·구어·대시 밀도 (보고; 경어·감탄은 게이트 `prose` 가 거부한다)", "",
              "### 추측 표현 (것 같·듯하·듯싶·아닐까·않을까·수도 있·아마도·아마) — 판정: 단정으로 고침 / 삭제 / 유지", ""]
    for it, ln, expr in hedge_hits[:50]:
        lines.append(f"- `{expr}`: `{it['path']}:{ln}` — {it['title_ko']}")
    if not hedge_hits:
        lines.append("- 없음")
    if len(hedge_hits) > 50:
        lines.append(f"- … {len(hedge_hits) - 50}건 더")
    lines += ["", "### 구어 후보 (근데·그냥·좀·엄청·뭔가·약간) — `되게`·`진짜`는 정상 용법이 많아 후보에 넣지 않는다", ""]
    for it, ln, expr in colloq_hits[:50]:
        lines.append(f"- `{expr}`: `{it['path']}:{ln}` — {it['title_ko']}")
    if not colloq_hits:
        lines.append("- 없음")
    if len(colloq_hits) > 50:
        lines.append(f"- … {len(colloq_hits) - 50}건 더")
    lines += ["", "### 대시 밀도 > 1.0 (문장당 \" — \" 수, 줄·불릿·셀 첫머리의 라벨 대시 제외; 문장 = 마침표 종결 또는 종결 \"다\" + `|`·`)`·닫는 따옴표·줄끝; 상위 20)", ""]
    for density, dashes, sentences, it in dash_dense[:20]:
        lines.append(f"- {kb_lib.num(density)} (대시 {dashes} / 문장 {sentences}): {ref(it)}")
    if not dash_dense:
        lines.append("- 없음")
    if len(dash_dense) > 20:
        lines.append(f"- … {len(dash_dense) - 20}건 더")

    def listing(hits, limit, render):
        out = [render(h) for h in hits[:limit]] or [f"- {kb_lib.NONE_MARK}"]
        return out + ([f"- … {len(hits) - limit}건 더"] if len(hits) > limit else [])

    def cite(it, ln, expr, quote):
        return f"- `{expr}`: `{it['path']}:{ln}` — {quote}"

    def waived_tail(hits, gate, render):
        if not hits:
            return []
        return [f"- 면제 {len(hits)}건(waivers.md, `{gate}`) — 집계에서 뺐다:"] + ["  " + render(h) for h in hits[:50]]

    lines += ["", "## ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기 (보고)", "",
              "### 메타 문장 (다음과 같다 · 이 절에서는 · 아래에서 설명한다 · 앞서 말했듯) — 판정: 주장 문장으로 바꿈 / 삭제", ""]
    lines += listing(meta_hits, 50, lambda h: cite(*h)) + waived_tail(meta_waived, ADDITION_GATE, lambda h: cite(*h))
    lines += ["", "### 채움 문구 (특이사항 없음 · 일반적인 방식을 따른다 · 추후 결정한다) — 판정: 세 빈 값 중 하나로 바꿈 / 실질 답으로 채움", ""]
    lines += listing(filler_hits, 50, lambda h: cite(*h)) + waived_tail(filler_waived, ADDITION_GATE, lambda h: cite(*h))
    lines += ["", f"### 빈 값 이상 표기 — 빈 자리는 `{'` · `'.join(kb_lib.EMPTY_VALUE)}` 셋으로만 적는다 (p4-three-empty-values)", ""]
    lines += listing(empty_hits, 50, lambda h: cite(*h)) + waived_tail(empty_waived, EMPTY_VALUE_GATE, lambda h: cite(*h))
    lines += ["", f"## ⑨ 목록 — 손 번호 · 항목 {LIST_MAX_ITEMS}개 이하 · 중첩 {LIST_MAX_DEPTH}단계 이하 · 항목당 {LIST_MAX_ITEM_CHARS}자 이하 · 빈 항목 (보고)", "",
              "| 규칙 | 위반 |", "|---|---|"]
    lines += [f"| {name} | {count} |" for name, count in list_kinds] or [f"| {kb_lib.NONE_MARK} | 0 |"]
    lines += ["", "### 위반 목록 (항목 길이는 이어지는 들여쓴 줄을 합치고 공백을 정규화한 뒤 센 글자 수다)", ""]
    _list_ref = lambda h: f"- `{h[0]['path']}:{h[1]}` — {h[2]}"  # noqa: E731
    lines += listing(list_hits, 60, _list_ref) + waived_tail(list_waived, LIST_RULES_GATE, _list_ref)
    lines.append("")
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.chunks, input_kind="청크 파일"), encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
