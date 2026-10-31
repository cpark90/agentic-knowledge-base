#!/usr/bin/env python3
"""정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 단위 지식 파일에서 보고한다 (p4-redundancy-as-safety-margin).

게이트가 아니라 **보고**다: 병합·묶기·유지의 판정은 사람 또는 승인된 판정자가 하고(9.8절), 이 도구는
후보를 추린다. 재검증 시점(커밋)마다 생성하고 저장하지 않는다 (4.6절 뷰 원칙).

  ① 정확 중복 — 본문 sha256 앞 12자(contentHash)가 같은 살아 있는 단위 지식 쌍
  ② 라벨 중복 — title_ko 또는 title 이 같은 단위 지식 (용인 불가: 라벨은 인터페이스)
  ③ 근사 중복 후보 — 본문 문자 5-gram 집합의 Jaccard ≥ θ (기본 0.5). 유사도는 후보 추림에만 쓴다
  ④ 묶임과 응집 — ①·③ 쌍이 coUpdatesWith 로 묶여 있는가(안 묶인 중복이 드리프트 후보), 그리고 묶인 쌍의 현재 본문
     Jaccard 가 θ_cohesion(기본 θ/2) 미만인가 — 응집 저하 후보: 묶었으나 본문이 갈라짐, suspect 판정 대상.
     저장된 이전 값과의 비교가 아니라 절대 임계다 — 뷰는 저장하지 않으므로(4.6절) 비교할 캐시가 없다.
     학습 모델 임베딩은 ODD 명시 제외(project-odd.yml EXCLUSIONS_REVIEWED)라 유사도는 문자 n-gram 으로만 잰다
  ⑤ 결론 라벨 형식 — 결정의 결론(conclusion.md)의 title_ko 가 문장형(…다)으로 끝나는가.
     근거·대안 라벨은 명사구가 관례라 보지 않는다 (label-representativeness-protocol (c) ④: "결정 라벨은 결론 문장형")
  ⑥ 용어 — docs/glossary.md 의 "옛 표기"가 살아 있는 단위 지식 본문에 남아 있는가. **tier 1 (기계 치환)만** 위반이다 —
     tier 2 는 유저 결정, tier 3 은 문맥 공존(바꾸지 않음), — 는 옛 표기 없음. tier 열이 없으면 전부 1 로 보고 info 를 남긴다.
     docs/waivers.md 의 게이트 id `term-drift`(축 파일)에 면제된 파일의 히트는 집계에서 빼되 목록에 남긴다 (C)
  ⑦ 단정성 — STYLEGUIDE §0 "산문은 단정 서술형"(유저 결정 2026-09-13) 가운데 게이트 `prose`(chunk_lint·doccheck: 경어·감탄)가
     거부하지 않는, 판단이 필요한 나머지: 추측 표현(것 같·듯하·수도 있·아마 …)·구어 후보(근데·그냥·좀·엄청·뭔가·약간)의
     파일·줄·표현 목록과, 대시 밀도(문장당 " — " 수; 문장 = 마침표 종결 또는 마침표 없는 종결 "다" 뒤에 `|`·`)`·닫는 따옴표·
     줄끝이 오는 곳 — 명사형 종결 "기각." 과 표 셀 "…다 |" 를 다 센다; 줄·불릿·셀 첫머리의 종결 없는 짧은 라벨 뒤의
     라벨 대시 "**결론** — "·"- 라벨 — " 와 줄 가운데 굵은 라벨 뒤의 대시 "… **대안** — " 는 구조적 구분자라 세지 않는다)가 1.0 을 넘는 단위 지식(상위 20). 목록·정규식의 단일 정의 위치는 kb_lib(PROSE_HEDGES·PROSE_COLLOQUIAL·PROSE_SENTENCE_END·prose_segments).
     대시·문장 모두 산문 조각(prose_segments) 안에서만 센다 — 코드·따옴표 안은 산문이 아니다
  ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기(명세 문서 작성 규격 4.1·9.4절, 유저 승인 2026-09-22;
     결정 p4-three-empty-values). 셋을 본다: 메타 문장(다음과 같다·이 절에서는 …), 채움 문구(특이사항 없음·추후 결정한다 …),
     세 빈 값(`없음`·`해당 없음`·`미확정`) 밖의 표기(`N/A`·`TBD`·`미정`·표의 단독 대시 셀). 단일 정의 위치는 kb_lib
     (PROSE_META·PROSE_FILLER·EMPTY_VALUE·EMPTY_VALUE_REJECTED·check_addition)
  ⑨ 목록 — 목록 규칙(같은 규격 4.3절): 손 번호(`2.` 이상 — 순서 목록의 항목은 모두 `1.` 로 쓴다) · 항목 9개 초과 ·
     중첩 3단계 이상 · 항목당 240자 초과 · 빈 항목. 같은 문법 형은 기계 판정이 되지 않아 보지 않는다. 항목 길이는
     소스 줄이 아니라 **글자**로 잰다 — 이어지는 들여쓴 줄을 합치고 연속 공백을 하나로 줄인 뒤 센다. 손 줄바꿈이
     110~120자라 소스 줄을 세면 접힌 자리가 그대로 위반이 된다 (STYLEGUIDE §0, 유저 승인 2026-09-22). 단일 정의 위치는
     kb_lib(LIST_MAX_ITEMS·LIST_MAX_DEPTH·LIST_MAX_ITEM_CHARS·check_lists)
  ⑩ 중복 확정 후보 — ③의 근사 중복 중 `coUpdatesWith` 미묶음 쌍(+①의 미묶음 정확 중복)을 판정자 질문("이 두 블록은
     같은 주장을 담는가?")의 입력 후보로 다시 낸다(judge-without-service-2026-09-30 기계 환원 ②). 후보 생성까지이고
     병합·묶기·유지의 확정은 판정자(사람 또는 세션 판정자) 몫이다 — ③과 같은 데이터를 판정 관점으로 다시 읽은 것이라
     수치가 갈리지 않는다.
  ⑪ 자리 후보 — 둘 이상의 등록 본문 슬롯(`agt:bodySlot`)을 가진 단위 지식에서, 한 슬롯의 영역 안에 **다른** 슬롯의 표지
     낱말이 한글 음절 경계 밖(조사가 붙지 않은 자리)으로 등장하면 후보로 낸다 — "이 문장이 그 슬롯에 있어야 하는가"의
     판정자 질문 입력이다(judge-without-service-2026-09-30 기계 환원 ②). 슬롯이 하나뿐인 단위 지식(결정 세 단위 지식·V&V
     시나리오 세 단위 지식)는 대상이 아니다. 확정은 판정자 몫이고 이 축은 후보만 낸다 — 낱말 재등장이 전부 오배치는
     아니므로 오탐이 있을 수 있다(게이트가 아니라 보고인 이유).
  ⑫ 문장 구성 — 결정 p0-sentence-composition(유저 답 Q104-a, 2026-10-23)의 규칙 가운데 정규식으로 셀 수 있는 넷을 센다.
     규칙 3은 코드와 따옴표와 링크 대상 밖의 산문 기호(`=`·`+`·`→`·`×`)이고, 규칙 4는 마침표로 끝난 문장이 서술어 대신
     명사나 명사형으로 끝난 수다(제목과, 문장 하나뿐인 목록 항목·표 셀은 명사구 허용이라 빼고 세 빈 값도 뺀다). 규칙 5는
     가운뎃점으로 셋 이상을 이은 연쇄이고, 규칙 6은 뒤에 같은 문장의 말이 이어지는 괄호다(번호 괄호와 영문 병기는 뺀다).
     넷 다 보고이고 판정은 리뷰가 한다. 정규식은 이 파일의 COMPOSITION_* 가 단일 정의 위치다

⑧·⑨ 의 **판정은 게이트 `chunk_lint`** 가 한다 — 게이트 id 는 `addition`(메타 문장·채움 문구)·`empty-value`(빈 값 표기)·
`list-rules`(목록 규칙)이고, 보고 수치가 0 이 된 2026-09-22 에 올렸다(반영 계획 7번, STYLEGUIDE §2 — 강화는 약화가 아니다).
이 절은 목록과 맥락을 주는 보고로 남는다. 둘이 같은 함수(kb_lib.check_addition·check_lists)를 쓰므로 수치가 갈리지 않는다.
⑥ 과 같은 규약으로 waivers.md 의 면제는 집계에서 빼되 목록에 남긴다. ⑩·⑪ 은 후보 생성까지이고 게이트가 아니다 —
확정에는 판정자(세션 판정자 또는 사람)가 필요하다(`tools/judge.py`).

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(용어집·waiver 표·단위 지식 파싱 불가). 보고 뷰라 판정 실패(1)는 없다
사용: consistency.py --out consistency.md [--theta 0.5] [--theta-cohesion θ/2] [--glossary docs/glossary.md] [--waivers docs/waivers.md] <단위 지식 .md …>
"""
import argparse
import os
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import (BODY_FENCE, BODY_SLOT_KEYWORD, BODY_SLOT_SPAN,  # noqa: E402
                      apply_plane_level_state, body_slot_mark, load_plane_level_state, parse_chunk)
import kb_lib  # noqa: E402 — 규약 상수·머리 블록·비율 표기의 단일 정의 위치 (STYLEGUIDE §7)
from kb_lib import (ADDITION_GATE, EMPTY_VALUE_GATE, EXIT_CONFIG, EXIT_OK, LIST_MAX_DEPTH, LIST_MAX_ITEM_CHARS,  # noqa: E402
                    LIST_MAX_ITEMS, LIST_RULES_GATE, LIVE_STATES, PROSE_LABEL_DASH, PROSE_SENTENCE_END,
                    check_addition, check_lists, check_prose, load_waivers, prose_segments, waived)
from gen_norms import CONVENTION_LINE, TABLE_CELL_SEP  # noqa: E402 — 규약 줄과 표 칸 경계의 단일 정의 위치 (⑫ 규칙 6)

GATE_TERM = "term-drift"  # ⑥ 의 게이트 id — waivers.md 가 이 이름으로 면제를 선언한다
# ⑦ 대시 밀도의 라벨 대시 보강 — 줄 가운데의 굵은 라벨("… 기각한다. **대안** — …") 뒤 대시도 구분자다. 굵은 부분이
# "다"·마침표로 끝나면 절이므로 라벨이 아니다. 줄·셀 첫머리의 라벨은 kb_lib.PROSE_LABEL_DASH 가 이미 맡는다
BOLD_LABEL_DASH = re.compile(r"\*\*[^*\n]{0,39}[^*\n다.\s]\*\*[ \t]*—[ \t]")
# ⑫ 문장 구성(결정 p0-sentence-composition, 유저 답 Q104-a) — 규칙 3·4·5·6 의 정규식 대리. 보고이고 게이트가 아니다
COMPOSITION_SYMBOL = re.compile(r"[=+→×]+")       # 규칙 3 — 이어진 기호(`==`·`+=`)는 한 번으로 센다
COMPOSITION_LINK_TARGET = re.compile(r"\]\([^)\s]*\)|<https?://[^>\s]+>|https?://\S+")  # 링크 대상 — 산문이 아니다
COMPOSITION_HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
COMPOSITION_ITEM = re.compile(r"^\s*(?:>\s*)?(?:[-*+]|\d+[.)])\s+")
COMPOSITION_PERIOD = re.compile(r"\.(?=\**(?:[\"”」'’\s]|$))")  # 문장 끝 마침표 — "4.2절" 처럼 글자가 이어지면 아니다
# 규칙 4 — 서술어 종결(평서 "다", 의문 "까", 명령 "라", 청유 "자")이 아닌 한글 음절로 끝나는 문장은 명사형 끝맺음이다
COMPOSITION_PREDICATE_END = set("다까라자")
COMPOSITION_TRAILING = re.compile(r"(?:\s*\([^()]*\)|[\s*\"”」'’])+$")  # 문장 끝의 출처 괄호·굵게·닫는 따옴표
COMPOSITION_CHAIN_BREAK = re.compile(r"[,.;:()\[\]|—]")  # 가운뎃점 연쇄를 끊는 구두점 — 연쇄는 한 구 안에서만 센다
COMPOSITION_ENUM_PAREN = re.compile(r"^\s*(?:[a-zA-Z0-9]{1,2}|[가-하])\s*$")  # "(a)"·"(1)"·"(가)" — 번호이지 괄호 삽입이 아니다
COMPOSITION_GLOSS_PAREN = re.compile(r"^[^가-힣]{1,40}$")  # "정제 수준(refinement level)" — 규칙 8 의 영문 병기다
LIVE = set(LIVE_STATES)  # 게이트 chunk_lint 와 같은 대상 집합 (kb_lib 단일 정의 위치)
_PLACEMENT_RE_CACHE: dict[str, re.Pattern] = {}  # ⑪ 자리 후보 — 표지 낱말별 정규식 캐시


# ══ 본문과 슬롯의 읽기 ════════════════════
# 단위 지식 본문의 조각·shingle, 본문 슬롯의 영역과 자리 후보, 용어집의 옛 표기를 읽는 자리다.

# ── 본문 조각과 shingle ────────────────────
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


# ── 슬롯 영역·자리 후보·용어집 ────────────────────
def slot_regions(body_text: str) -> dict[str, list[int]]:
    """등록된 슬롯 표지(chunk2kg.BODY_SLOT_MARKERS 의 굵은 span·BODY_SLOT_KEYWORD 의 줄 머리 `키워드:`)로 본문을
    나눈 조각의 줄 인덱스 — {표지: [줄 인덱스, …]}. 두 표지 종류(굵은 span·키워드 콜론)를 다 본다 — 어느 한쪽만
    보면 `미확정:` 같은 키워드 슬롯의 줄이 앞선 굵은 슬롯의 영역으로 잘못 편입된다(측정 2026-09-30).

    자리 판정은 chunk2kg.body_slot_mark 하나(표지는 자리로 판정한다 · 한정어의 길이와 꼴)를 재사용한다 —
    판정을 고치면 방출과 이 보고가 같이 바뀐다(STYLEGUIDE §7 단일 정의 위치, 이 함수는 그 판정을 구간으로만 편다).
    """
    lines = body_text.splitlines()
    regions: dict[str, list[int]] = {}
    fence: str | None = None
    current: str | None = None
    for i, line in enumerate(lines):
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            if current:
                regions[current].append(i)
            continue
        if m:
            fence = m.group(1)
            if current:
                regions[current].append(i)
            continue
        kw = BODY_SLOT_KEYWORD.match(line)
        hit = kw.group(1) if kw else None
        if not hit:
            for span in BODY_SLOT_SPAN.finditer(line):
                hit = body_slot_mark(line, span) or None
                if hit:
                    break
        if hit:
            current = hit
            regions.setdefault(current, [])
        if current:
            regions[current].append(i)
    return regions


def _placement_regex(mark: str):
    """표지 낱말이 한글 음절에 붙지 않은 자리(조사가 붙지 않은 자리)에서 발견되는가의 정규식 — 캐시로 재사용한다."""
    if mark not in _PLACEMENT_RE_CACHE:
        _PLACEMENT_RE_CACHE[mark] = re.compile(r"(?<![가-힣])" + re.escape(mark) + r"(?![가-힣])")
    return _PLACEMENT_RE_CACHE[mark]


def _legitimate_spans(line: str) -> list[tuple[int, int]]:
    """이 줄에서 필드 자리에 정당하게 선언된 굵은 슬롯 표지의 문자 구간 — 한 줄에 여러 필드(이해관계자 · 관심사)가
    ` · ` 로 이어질 때 뒤 필드의 표지어를 "다른 슬롯이 자리 밖에서 발견됨"으로 오판하지 않게 뺀다."""
    spans = []
    for span in BODY_SLOT_SPAN.finditer(line):
        if body_slot_mark(line, span):
            spans.append(span.span())
    return spans


def placement_candidates(it: dict) -> list[tuple[str, str, str]]:
    """자리 후보 — [(현재 슬롯, 발견된 다른 슬롯 표지, 그 줄)]. 슬롯이 둘 미만인 단위 지식은 대상이 아니다 (⑪)."""
    slots = it.get("slots") or []
    if len(slots) < 2:
        return []
    lines = it["body"].splitlines()
    regions = slot_regions(it["body"])
    out = []
    for own, idxs in regions.items():
        others = [m for m in slots if m != own]
        for i in idxs:
            line = lines[i]
            legit = _legitimate_spans(line)
            for other in others:
                for m in _placement_regex(other).finditer(line):
                    if any(a <= m.start() < b for a, b in legit):
                        continue  # 이 줄의 정당한 필드 선언이다 — 자리 밖 출현이 아니다
                    out.append((own, other, line.strip()[:160]))
                    break
    return out


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


# ══ 축 ①~⑫ 의 판정 ════════════════════
# 살아 있는 단위 지식의 본문 사이에서 중복·응집·라벨 형식·용어·단정성·첨가·목록·후보·문장 구성을 센다.

# ── 축 ①~③ 중복 — 정확·라벨·근사 ────────────────────
def analyse_duplicates(items, theta):
    """① 정확 중복 · ② 라벨 중복 · ③ 근사 중복 후보와 shingle 집합을 돌려준다."""
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
        if j >= theta:
            near.append((j, x, y))
    near.sort(key=lambda t: -t[0])
    return exact, label_dups, near, sh


# ── 축 ④~⑥ 응집·라벨 형식·용어 ────────────────────
def analyse_cohesion(items, by_id, sh, theta_c):
    """④ 묶임과 응집 — coUpdatesWith 로 묶인 쌍(살아 있는 입력 안의 것만)의 현재 본문 Jaccard 가 θ_cohesion 미만이면
    응집 저하 후보. 이전 값과 비교하지 않는다 — 뷰는 저장하지 않으므로 캐시가 없다 (4.6절). 절대 임계
    """
    bound = sorted({tuple(sorted((x["id"], c))) for x in items for c in x["co"] if c in by_id and c != x["id"]})
    cohesion = [(jaccard(sh[xi], sh[yi]), by_id[xi], by_id[yi]) for xi, yi in bound]
    cohesion_low = sorted((t for t in cohesion if t[0] < theta_c), key=lambda t: t[0])
    return bound, cohesion_low


def analyse_label_form(items):
    """⑤ 결론 라벨 형식 — 결정의 결론만 문장형. 판정은 kb_lib.decision_role_marker(경로) == 결론 이다:
    conclusion.md 는 결론이고 근거·대안·규약·시나리오의 자극·요인·배제 자극은 결론이 아니다
    """
    def is_conclusion(it):
        return it["type"] == "decision" and kb_lib.decision_role_marker(it["path"]) == "결론"

    return [it for it in items if is_conclusion(it) and not re.search(r"(다|음|함|없음|있음)$", it["title_ko"])]


def analyse_terms(items, terms, waivers):
    """⑥ 용어 — tier 1 만. 면제 파일(waivers.md, term-drift)의 히트는 집계에서 빼되 목록에 남긴다."""
    term_hits, term_waived = [], []
    for old, std in terms:
        for it in items:
            if old in it["body"] or old in it["title_ko"]:
                (term_waived if waived(waivers, GATE_TERM, it["path"], "파일") else term_hits).append((old, std, it))
    return term_hits, term_waived


# ── 축 ⑦~⑨ 단정성·첨가·목록 — 본문을 한 번만 읽는다 ────────────────────
def analyse_prose(items, waivers):
    """⑦ 단정성 — 게이트 prose 가 거부하지 않는 나머지(추측·구어·대시 밀도)를 보고한다. 판정은 사람 몫이다.

    대시 밀도 = 산문 조각 안의 " — " 수 / max(1, 문장 수). 문장 = PROSE_SENTENCE_END(마침표 종결, 또는 마침표 없는 종결 "다" +
    | ) 닫는 따옴표 줄끝). "다." 만 세면 209/621, 종결 "다" 기반은 130 — 명사형 종결·인용 괄호를 놓쳐 대안 양식이 전부
    걸렸다(대리의 결함). 마침표 종결까지 세면 28 — 그 상위는 라벨 대시("- 라벨 — 설명", "| 셀 | `id` — 설명")의 불릿·표
    단위 지식이라 라벨 대시를 뺀다(PROSE_LABEL_DASH) → 1. 문장 없이 절 대시만 있는 단위 지식은 여전히 잡힌다.
    ⑧ 첨가 · ⑨ 목록 — 같은 본문을 한 번만 읽어 ⑦ 과 함께 센다. 셋 다 보고이고 판정은 사람 몫이다.
    """
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
        dashes = sum(seg.count(" — ") - label_dashes(seg) for seg in segs)  # 라벨 대시는 절 연결이 아니다
        sentences = sum(len(PROSE_SENTENCE_END.findall(seg)) for seg in segs)
        density = dashes / max(sentences, 1)
        if density > 1.0:
            dash_dense.append((density, dashes, sentences, it))
    dash_dense.sort(key=lambda t: (-t[0], t[3]["path"]))
    return {"hedge_hits": hedge_hits, "colloq_hits": colloq_hits, "dash_dense": dash_dense,
            "meta_hits": meta_hits, "filler_hits": filler_hits, "empty_hits": empty_hits, "list_hits": list_hits,
            "meta_waived": meta_waived, "filler_waived": filler_waived, "empty_waived": empty_waived,
            "list_waived": list_waived, "list_kinds": list_rule_counts(list_hits)}


def label_dashes(seg: str) -> int:
    """⑦ 의 분자에서 뺄 라벨 대시 수 — 줄·셀 첫머리 라벨(kb_lib.PROSE_LABEL_DASH)과 줄 가운데 굵은 라벨(BOLD_LABEL_DASH) 뒤의
    대시다. 같은 대시를 두 정규식이 함께 잡을 수 있어 대시 위치의 합집합으로 센다."""
    spots = {m.end() - 2 for m in PROSE_LABEL_DASH.finditer(seg)} | {m.end() - 2 for m in BOLD_LABEL_DASH.finditer(seg)}
    return len(spots)


def list_rule_counts(list_hits):
    """⑨ 의 위반을 규칙별로 센다 — 규칙마다 다음 행동이 다르다(번호는 치환, 줄 수·항목 수는 분할)."""
    LIST_KINDS = (("손 번호", "손 번호"), ("항목 수", "개다"), ("중첩", "중첩"), ("항목 길이", "자다"), ("빈 항목", "빈 목록"))
    list_kinds = [(name, sum(1 for _, _, why in list_hits if key in why)) for name, key in LIST_KINDS]
    return [(k, v) for k, v in list_kinds if v]


# ── 축 ⑩~⑪ 판정자에게 넘길 후보 ────────────────────
def analyse_candidates(items, exact, near, linked):
    """⑩ 중복 확정 후보 — ①·③의 미묶음 쌍을 판정자 질문("이 두 블록은 같은 주장을 담는가?")의 입력으로 다시 낸다.

    ⑪ 자리 후보 — 슬롯 표지가 둘 이상인 단위 지식에서, 다른 슬롯의 표지 낱말이 자리 밖으로 등장하는 문장.
    """
    total_pairs = len(exact) and sum(len(g) * (len(g) - 1) // 2 for g in exact)
    unlinked_exact = [g for g in exact if not all(linked(x, y) for x, y in combinations(g, 2))]
    unlinked_near = [(j, x, y) for j, x, y in near if not linked(x, y)]
    dup_candidates = ([(1.0, x, y) for g in unlinked_exact for x, y in combinations(g, 2)]
                      + [(j, x, y) for j, x, y in unlinked_near])
    dup_candidates.sort(key=lambda t: -t[0])
    placement = [(it, own, other, quote) for it in items for own, other, quote in placement_candidates(it)]
    return total_pairs, unlinked_exact, unlinked_near, dup_candidates, placement


# ── 축 ⑫ 문장 구성 — 규칙 3·4·5·6 의 정규식 대리 ────────────────────
def composition_units(text: str) -> list[tuple[str, list[tuple[int, str]]]]:
    """산문 조각(kb_lib.prose_segments)을 단위로 묶는다 → [(종류, [(줄 번호, 조각)…])]. 종류는 제목·문단·목록 항목·표 셀이다.

    손 줄바꿈으로 접힌 문단과 목록 항목은 이어지는 줄을 한 단위로 합친다 — 줄 끝의 괄호가 다음 줄의 서술로 이어지는지
    보려면 문단 단위로 읽어야 한다. 링크 대상(`](…)`·URL)은 산문이 아니라 먼저 지운다. 빈 줄은 prose_segments 가
    내지 않으므로 줄 번호가 끊기면 단위도 끊긴다.
    """
    units: list[tuple[str, list[tuple[int, str]]]] = []
    prev_ln = None
    for ln, seg in prose_segments(text):
        seg = COMPOSITION_LINK_TARGET.sub(lambda m: "]" if m.group(0).startswith("]") else " ", seg)
        body = re.sub(r"^\s*>\s?", "", seg)
        if COMPOSITION_HEADING.match(body):
            units.append(("제목", [(ln, body)]))
        elif body.lstrip().startswith("|"):
            units += [("셀", [(ln, cell)]) for cell in body.strip().strip("|").split("|") if cell.strip()]
        elif COMPOSITION_ITEM.match(body):
            units.append(("항목", [(ln, COMPOSITION_ITEM.sub("", body, count=1))]))
        elif units and prev_ln == ln - 1 and units[-1][0] in ("문단", "항목"):
            units[-1][1].append((ln, body))
        else:
            units.append(("문단", [(ln, body)]))
        prev_ln = ln
    return units


def _joined(pieces: list[tuple[int, str]]) -> tuple[str, list[tuple[int, int]]]:
    """단위의 조각을 공백 하나로 잇는다 → (글, [(시작 위치, 줄 번호)…]). 위치에서 줄 번호를 되찾는 데 쓴다."""
    text, starts = "", []
    for ln, seg in pieces:
        if text:
            text += " "
        starts.append((len(text), ln))
        text += seg.strip()
    return text, starts


def _convention_stops(pieces: list[tuple[int, str]]) -> set[int]:
    """`규약:` 줄의 문장 끝 위치 → {이은 글의 위치}. _joined 와 같은 셈으로 위치를 낸다.

    규약 줄은 줄마다 항목 하나이므로 줄 끝이 문장 끝이다. 표 절의 줄 `규약: a | b | c` 는 gen_norms 가 칸으로 나누는
    경계(TABLE_CELL_SEP)마다 칸이 끝나므로 그 경계도 문장 끝이다. 단위가 손 줄바꿈으로 이은 규약 줄 여럿이어도 줄마다 센다.
    """
    stops, pos = set(), 0
    for i, (_, seg) in enumerate(pieces):
        piece = seg.strip()
        pos += 1 if i else 0
        if CONVENTION_LINE.match(piece):
            stops.add(pos + len(piece))
            stops.update(pos + m.start() for m in TABLE_CELL_SEP.finditer(piece))
        pos += len(piece)
    return stops


def _line_at(starts: list[tuple[int, int]], pos: int) -> int:
    return max((ln for s, ln in starts if s <= pos), default=starts[0][1])


def _paren_groups(text: str):
    """최상위 괄호 묶음 → [(여는 위치, 닫는 위치 + 1)]. 짝 없는 닫는 괄호("1)")는 무시한다."""
    out, depth, start = [], 0, 0
    for i, ch in enumerate(text):
        if ch in "(（":
            if depth == 0:
                start = i
            depth += 1
        elif ch in ")）" and depth:
            depth -= 1
            if depth == 0:
                out.append((start, i + 1))
    return out


def check_composition(text: str) -> dict[str, list[tuple[int, str]]]:
    """한 파일의 문장 구성 대리 → {규칙: [(줄 번호, 표현)…]}. 결정 p0-sentence-composition 의 규칙 3·4·5·6 이다.

    - 기호: 산문 조각(코드·따옴표·링크 대상 밖)의 `=`·`+`·`→`·`×`. 목록 표지 `+ ` 는 지운 뒤 센다
    - 명사형 끝맺음: 마침표로 끝난 문장의 끝 음절(끝 괄호·굵게·따옴표를 걷어 낸 뒤)이 한글이고 서술어 종결(다·까·라·자)이
      아니다. 제목은 보지 않고, 목록 항목과 표 셀이 문장 하나뿐이면 명사구 불릿·셀로 보아 세지 않는다(STYLEGUIDE 허용)
    - 가운뎃점 연쇄: 쉼표·마침표·괄호·대시 따위로 끊기지 않은 한 구 안에서 가운뎃점으로 비지 않은 셋 이상을 이은 것
    - 문장 가운데 괄호: 괄호 뒤에 같은 문장의 말이 이어진다. 괄호 뒤가 문장 끝(마침표·느낌표·물음표·셀 경계·단위 끝)이면
      세지 않고, 번호 괄호("(a)")와 앞말에 붙은 영문 병기("정제 수준(refinement level)", 규칙 8)도 세지 않는다.
      `규약:` 줄의 줄 끝과 표 칸 경계(` | `)도 문장 끝이다(_convention_stops)
    """
    hits: dict[str, list[tuple[int, str]]] = {"symbol": [], "noun_end": [], "chain": [], "paren": []}
    for kind, pieces in composition_units(text):
        unit, starts = _joined(pieces)
        stops = _convention_stops(pieces)
        for m in COMPOSITION_SYMBOL.finditer(unit):
            hits["symbol"].append((_line_at(starts, m.start()), unit[max(0, m.start() - 16):m.end() + 16].strip()))
        for piece in COMPOSITION_CHAIN_BREAK.split(unit):
            run: list[str] = []
            for part in piece.split("·") + [""]:
                if part.strip():
                    run.append(part.strip())
                    continue
                if len(run) >= 3:
                    expr = "·".join([run[0].split()[-1]] + run[1:-1] + [run[-1].split()[0]])
                    hits["chain"].append((_line_at(starts, unit.find(piece)), expr))
                run = []
        if kind == "제목":
            continue
        ends = [m.start() for m in COMPOSITION_PERIOD.finditer(unit)]
        single = len(ends) == 1 and not unit[ends[0] + 1:].strip(" *\"”」'’")
        if not (kind in ("항목", "셀") and single):
            prev = 0
            for e in ends:
                sentence = COMPOSITION_TRAILING.sub("", unit[prev:e])
                prev = e + 1
                last = sentence[-1:] if sentence else ""
                if sentence.rsplit(" — ", 1)[-1].strip(" *") in kb_lib.EMPTY_VALUE:
                    continue  # "**검증 대응물** — 없음." — 세 빈 값(p4-three-empty-values)은 값 표기이지 문장이 아니다
                if "가" <= last <= "힣" and last not in COMPOSITION_PREDICATE_END:
                    hits["noun_end"].append((_line_at(starts, e), "…" + sentence[-24:].lstrip() + "."))
        for a, b in _paren_groups(unit):
            inner = unit[a + 1:b - 1]
            if COMPOSITION_ENUM_PAREN.match(inner):
                continue
            if a and not unit[a - 1].isspace() and re.search(r"[A-Za-z]", inner) and COMPOSITION_GLOSS_PAREN.match(inner):
                continue
            rest = unit[b:].lstrip(" *\"”」'’")
            if not rest or rest[0] in ".!?。" or any(b <= x <= len(unit) - len(rest) for x in stops):
                continue
            hits["paren"].append((_line_at(starts, a), unit[max(0, a - 12):b + 12].strip()))
    return hits


COMPOSITION_RULES = (("symbol", "산문 기호 (규칙 3)"), ("noun_end", "명사형 끝맺음 (규칙 4)"),
                     ("chain", "가운뎃점 연쇄 (규칙 5)"), ("paren", "문장 가운데 괄호 (규칙 6)"))


def analyse_composition(items):
    """⑫ 문장 구성 — 규칙마다 [(항목, 줄, 표현)…]. 보고이고 게이트가 아니다 — 판정은 리뷰가 한다(p0-sentence-composition)."""
    out: dict[str, list] = {key: [] for key, _ in COMPOSITION_RULES}
    for it in items:
        for key, hits in check_composition(Path(it["path"]).read_text(encoding="utf-8")).items():
            out[key] += [(it, ln, expr) for ln, expr in hits]
    return out


# ══ 입력과 보고 ════════════════════
# 인자와 단위 지식을 읽고 머리·요약·절을 조립해 생성 문서를 쓴다.

# ── 입력 — 인자와 살아 있는 단위 지식 ────────────────────
def parse_args():
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
    return ap.parse_args()


def load_items(paths):
    """단위 지식 경로 → 살아 있는 항목 목록. 파싱 실패는 ValueError 로 올라가 main 이 CONFIG 로 바꾼다."""
    items = []
    for p in paths:
        if not p.endswith(".md"):
            continue
        meta, body = parse_chunk(p)
        if meta.get("status") not in LIVE:
            continue
        items.append({"path": p, "id": meta["id"], "type": meta["type"], "level": meta["level"],
                      "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
                      "hash": meta["_content_hash"], "body": body_of(p), "lines": len(body.splitlines()),
                      "co": set(meta.get("coUpdatesWith", []) or []), "slots": meta.get("_body_slots", [])})
    return items


# ── 보고 — 머리와 요약 ────────────────────
def render_head(a, theta_c, items):
    return kb_lib.gendoc_header(
        "consistency", "정합성 보고", "tools/consistency.py",
        f"살아 있는 단위 지식의 본문 사이에서 — 정확 중복(contentHash 동일) · 라벨 중복 · 근사 중복 후보(5-shingle Jaccard ≥ {a.theta}) · "
        f"coUpdatesWith 로 묶인 쌍의 응집 저하(Jaccard < {theta_c:g}) · 결론 라벨 형식 · 용어집 옛 표기 · 단정성(추측·구어·대시 밀도) · "
        "첨가(메타 문장·채움 문구·빈 값 이상 표기) · 목록 규칙(손 번호·항목 수·중첩·항목 길이·빈 항목) · "
        "중복 확정 후보(⑩) · 자리 후보(⑪, 다른 슬롯 표지어 재등장) · "
        "문장 구성(⑫, 산문 기호·명사형 끝맺음·가운뎃점 연쇄·문장 가운데 괄호). "
        "병합·묶기·유지 판정은 사람이 하고, ⑧·⑨ 의 통과·실패 판정은 게이트 chunk_lint 가 한다. ⑩·⑪ 은 판정자(사람 또는 "
        "세션 판정자, `tools/judge.py`)에게 넘길 후보 생성까지다. ⑫ 는 보고이고 판정은 리뷰가 한다",
        "bazel build //kb:consistency", a.chunks,
        f"단위 지식 {len(items)}개 · θ = {a.theta} · θ_cohesion = {theta_c:g}",
        kb_lib.gendoc_view_notice("각 단위 지식의 본문"), input_kind="단위 지식 파일")


def render_summary(items, exact, total_pairs, unlinked_exact, label_dups, near, unlinked_near,
                   cohesion_low, bound, bad_form, term_hits, term_waived, p, dup_candidates, placement, dup_ids, comp):
    return (["## 요약", "",
            "| 항목 | 값 |", "|---|---|",
            f"| 정확 중복 묶음 | {len(exact)} (쌍 {total_pairs}) — coUpdatesWith 미묶음 {len(unlinked_exact)} |",
            f"| 라벨 중복 | {len(label_dups)} (용인 불가) |",
            f"| 근사 중복 후보 (Jaccard ≥ θ) | {len(near)} — 미묶음 {len(unlinked_near)} |",
            f"| 묶인 쌍 중 응집 저하 (coUpdatesWith, Jaccard < θ_cohesion) | {len(cohesion_low)} / 묶인 쌍 {len(bound)} |",
            f"| 결론 라벨 형식 위반 | {len(bad_form)} |",
            f"| 용어집 옛 표기 잔존 (tier 1) | {len(term_hits)} — 면제 {len(term_waived)}건(waivers.md) |",
            f"| 추측 표현 (⑦, 보고) | {len(p['hedge_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['hedge_hits']})} |",
            f"| 구어 후보 (⑦, 보고) | {len(p['colloq_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['colloq_hits']})} |",
            f"| 대시 밀도 > 1.0 (⑦, 문장당 \" — \") | {len(p['dash_dense'])} / {len(items)} |",
            f"| 메타 문장 (⑧, 게이트 `{ADDITION_GATE}`) | {len(p['meta_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['meta_hits']})}"
            f" — 면제 {len(p['meta_waived'])}건(waivers.md) |",
            f"| 채움 문구 (⑧, 게이트 `{ADDITION_GATE}`) | {len(p['filler_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['filler_hits']})}"
            f" — 면제 {len(p['filler_waived'])}건(waivers.md) |",
            f"| 빈 값 이상 표기 (⑧, 게이트 `{EMPTY_VALUE_GATE}`) | {len(p['empty_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['empty_hits']})}"
            f" — 면제 {len(p['empty_waived'])}건(waivers.md) |",
            f"| 목록 규칙 위반 (⑨, 게이트 `{LIST_RULES_GATE}`) | {len(p['list_hits'])}건 / 단위 지식 {len({h[0]['id'] for h in p['list_hits']})}"
            f" — 면제 {len(p['list_waived'])}건(waivers.md) — " +
            (" · ".join(f"{k} {v}" for k, v in p["list_kinds"]) or kb_lib.NONE_MARK) + " |",
            f"| **중복률** (정확·근사 관련 단위 지식 / 전체) | {kb_lib.pct(len(dup_ids), len(items))} |",
            f"| 중복 확정 후보 (⑩, 판정자 몫) | {len(dup_candidates)} |",
            f"| 자리 후보 (⑪, 판정자 몫) | {len(placement)}건 / 단위 지식 {len({q[0]['id'] for q in placement})} |"]
            + [f"| {name} (⑫, 보고) | {len(comp[key])}건 / 단위 지식 {len({h[0]['id'] for h in comp[key]})} |"
               for key, name in COMPOSITION_RULES] + [""])


# ── 보고 — 절 ①~⑥ ────────────────────
def render_duplicate_sections(a, exact, label_dups, near, theta_c, bound, cohesion_low, bad_form,
                              term_hits, term_waived, has_tier, linked, ref):
    lines = ["## ① 정확 중복 (contentHash 동일)", ""]
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
    if len(bad_form) > 50:
        lines.append(f"- … {len(bad_form) - 50}건 더")
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
    return lines


# ── 보고 — 절 ⑦ 단정성 ────────────────────
def render_prose_sections(hedge_hits, colloq_hits, dash_dense, ref):
    lines = ["", "## ⑦ 단정성 — 추측·구어·대시 밀도 (보고; 경어·감탄은 게이트 `prose` 가 거부한다)", "",
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
    return lines


# ── 보고 — 절 ⑧~⑨ 첨가와 목록 ────────────────────
def listing(hits, limit, render):
    out = [render(h) for h in hits[:limit]] or [f"- {kb_lib.NONE_MARK}"]
    return out + ([f"- … {len(hits) - limit}건 더"] if len(hits) > limit else [])


def cite(it, ln, expr, quote):
    return f"- `{expr}`: `{it['path']}:{ln}` — {quote}"


def waived_tail(hits, gate, render):
    if not hits:
        return []
    return [f"- 면제 {len(hits)}건(waivers.md, `{gate}`) — 집계에서 뺐다:"] + ["  " + render(h) for h in hits[:50]]


def render_addition_sections(p):
    lines = ["", "## ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기 (보고)", "",
             "### 메타 문장 (다음과 같다 · 이 절에서는 · 아래에서 설명한다 · 앞서 말했듯) — 판정: 주장 문장으로 바꿈 / 삭제", ""]
    lines += listing(p["meta_hits"], 50, lambda h: cite(*h)) + waived_tail(p["meta_waived"], ADDITION_GATE, lambda h: cite(*h))
    lines += ["", "### 채움 문구 (특이사항 없음 · 일반적인 방식을 따른다 · 추후 결정한다) — 판정: 세 빈 값 중 하나로 바꿈 / 실질 답으로 채움", ""]
    lines += listing(p["filler_hits"], 50, lambda h: cite(*h)) + waived_tail(p["filler_waived"], ADDITION_GATE, lambda h: cite(*h))
    lines += ["", f"### 빈 값 이상 표기 — 빈 자리는 `{'` · `'.join(kb_lib.EMPTY_VALUE)}` 셋으로만 적는다 (p4-three-empty-values)", ""]
    lines += listing(p["empty_hits"], 50, lambda h: cite(*h)) + waived_tail(p["empty_waived"], EMPTY_VALUE_GATE, lambda h: cite(*h))
    lines += ["", f"## ⑨ 목록 — 손 번호 · 항목 {LIST_MAX_ITEMS}개 이하 · 중첩 {LIST_MAX_DEPTH}단계 이하 · 항목당 {LIST_MAX_ITEM_CHARS}자 이하 · 빈 항목 (보고)", "",
              "| 규칙 | 위반 |", "|---|---|"]
    lines += [f"| {name} | {count} |" for name, count in p["list_kinds"]] or [f"| {kb_lib.NONE_MARK} | 0 |"]
    lines += ["", "### 위반 목록 (항목 길이는 이어지는 들여쓴 줄을 합치고 공백을 정규화한 뒤 센 글자 수다)", ""]
    _list_ref = lambda h: f"- `{h[0]['path']}:{h[1]}` — {h[2]}"  # noqa: E731
    lines += listing(p["list_hits"], 60, _list_ref) + waived_tail(p["list_waived"], LIST_RULES_GATE, _list_ref)
    return lines


# ── 보고 — 절 ⑩~⑪ 후보 ────────────────────
def render_candidate_sections(dup_candidates, placement, ref):
    lines = ["", "## ⑩ 중복 확정 후보 (①·③의 미묶음 쌍 — 판정자 질문: 이 두 블록은 같은 주장을 담는가?)", ""]
    for j, x, y in dup_candidates[:50]:
        lines.append(f"- {kb_lib.num(j)}: {ref(x)}  ↔  {ref(y)}")
    if not dup_candidates:
        lines.append("- 없음")
    if len(dup_candidates) > 50:
        lines.append(f"- … {len(dup_candidates) - 50}건 더")
    lines += ["", "## ⑪ 자리 후보 (다른 슬롯 표지어 재등장 — 판정자 질문: 이 문장이 그 슬롯에 있어야 하는가?)", ""]
    for it, own, other, quote in placement[:50]:
        lines.append(f"- `{own}` 영역에서 `{other}` 발견: {ref(it)} — \"{quote}\"")
    if not placement:
        lines.append("- 없음")
    if len(placement) > 50:
        lines.append(f"- … {len(placement) - 50}건 더")
    lines.append("")
    return lines


# ── 보고 — 절 ⑫ 문장 구성 ────────────────────
def render_composition_section(comp, limit=30):
    """규칙마다 건수가 많은 단위 지식부터 사례(파일, 줄, 표현)를 항목마다 셋까지 낸다 — 몰린 항목을 먼저 고치게 한다."""
    lines = ["## ⑫ 문장 구성 — 결정 p0-sentence-composition 의 규칙 3, 4, 5, 6 을 정규식으로 센 대리 (보고; 판정은 리뷰가 한다)", ""]
    for key, name in COMPOSITION_RULES:
        hits = comp[key]
        per = defaultdict(int)
        for it, _, _ in hits:
            per[it["path"]] += 1
        hits = sorted(hits, key=lambda h: (-per[h[0]["path"]], h[0]["path"], h[1]))
        seen: dict[str, int] = defaultdict(int)
        shown = []
        for h in hits:  # 한 항목이 목록을 다 차지하지 않게 항목마다 사례를 셋까지 낸다
            seen[h[0]["path"]] += 1
            if seen[h[0]["path"]] <= 3:
                shown.append(h)
        lines += [f"### {name} — {len(hits)}건 / 단위 지식 {len(per)}개", ""]
        lines += listing(shown, limit, lambda h: f"- `{h[2].replace('`', chr(39))}`: `{h[0]['path']}:{h[1]}` (이 항목 {per[h[0]['path']]}건)")
        lines.append("")
    return lines


# ── 실행 ────────────────────
def main() -> int:
    a = parse_args()
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
    try:
        items = load_items(a.chunks)
    except ValueError as e:
        return config_fail(f"단위 지식을 파싱할 수 없다 — {e}")
    by_id = {it["id"]: it for it in items}

    def linked(x, y):
        return y["id"] in x["co"] or x["id"] in y["co"]

    def ref(it):
        return f"`{it['path']}` — {it['title_ko']}"

    exact, label_dups, near, sh = analyse_duplicates(items, a.theta)
    bound, cohesion_low = analyse_cohesion(items, by_id, sh, theta_c)
    bad_form = analyse_label_form(items)
    term_hits, term_waived = analyse_terms(items, terms, waivers)
    p = analyse_prose(items, waivers)
    total_pairs, unlinked_exact, unlinked_near, dup_candidates, placement = analyse_candidates(items, exact, near, linked)
    comp = analyse_composition(items)

    dup_ids = {i["id"] for g in exact for i in g} | {i["id"] for _, x, y in near for i in (x, y)}
    head = render_head(a, theta_c, items)
    lines = render_summary(items, exact, total_pairs, unlinked_exact, label_dups, near, unlinked_near,
                           cohesion_low, bound, bad_form, term_hits, term_waived, p, dup_candidates, placement, dup_ids, comp)
    lines += render_duplicate_sections(a, exact, label_dups, near, theta_c, bound, cohesion_low, bad_form,
                                       term_hits, term_waived, has_tier, linked, ref)
    lines += render_prose_sections(p["hedge_hits"], p["colloq_hits"], p["dash_dense"], ref)
    lines += render_addition_sections(p)
    lines += render_candidate_sections(dup_candidates, placement, ref)
    lines += render_composition_section(comp)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.chunks, input_kind="단위 지식 파일"), encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
