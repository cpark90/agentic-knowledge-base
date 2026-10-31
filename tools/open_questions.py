#!/usr/bin/env python3
"""미결 집계 뷰 — 설계 공간과 단위 지식 본문의 선택 슬롯 `미확정:` 을 모아 open.md 를 생성한다 (p4-three-empty-values, p4-slot-answers-one-question).

미결을 문서가 아니라 항목 안에 두면 집계가 생성물이 되고, 답이 왔을 때 고칠 자리가 하나다. 상세 다섯 절(질문 / 이미 정해진 것 /
현재 상태 / 답이 가르는 것 / 선택지)을 가진 미결은 설계 공간(`space/*-space.md`, `agt:Space`)이다(유저 결정 Q54-a). 이 뷰는 미결
목록의 유일한 자리다 — 손으로 관리하던 색인 문서를 대체했고(지시 0095) 그 문서는 지시 0192 로 지웠다.

  입력  head 그래프(agt:bodySlot "미확정" 인 단위 지식의 라벨·plane·level·상태·본문 위치)와 그 단위 지식의 본문,
        설계 공간 그래프(`--spaces`, //space:design_space — 공간의 제목·spaceStatus·변수·후보 링크의 상태).
        슬롯 표지는 chunk2kg 가 본문에서 찾아 넣은 값이다 — 여기서 본문을 다시 훑지 않고 그래프가 대상을 고른다.
  계산  공간마다 한 행: 제목 · status · 변수(from 라벨 · kind) · 후보 수(state 별: open · eliminated · confirmed) ·
        그 공간을 상세로 가리키는 `미확정:` 슬롯의 단위 지식. 후보 state 는 링크 상태(kb_lib.SPACE_STATE_LINK)를 거꾸로 읽는다.
        슬롯 줄 `미확정: <질문>. 상세는 `<값>`[·`<값>`]다.` 의 상세 값이 공간 IRI 이면 그 공간의 행에 붙는다.
        공간을 가리키지 않는 슬롯(상세 없음·문서 경로)은 슬롯 미결 표에 질문 한 줄로 남는다. 상세 값이 IRI 인데 공간이
        아니면 해석하지 못한 상세로 따로 낸다. 미결이 없어도 절을 낸다.
  나이  공간 행과 슬롯 미결 행에 만든 날부터 이 뷰의 생성 시각까지의 일수를 붙인다(유저 답 Q116-a). 만든 날은 그 항목의
        `generated.at`(`prov:generatedAtTime`)이다. 밀폐 빌드는 git 의 첫 커밋 날짜를 읽지 못하고 `generated.at` 은 마지막 저작
        시각이므로 이 나이는 실제 나이의 하한이다. 그 한계를 뷰 머리에 적는다.
  판정  없음 — 뷰이고 게이트가 아니다. 미결의 해소는 공간의 status·후보 state 와 단위 지식의 슬롯을 고치는 것이고 사람이 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음·본문 없음)
사용: open_questions.py --out open.md [--spaces <design-space.ttl>] [--bodies <단위 지식 .md …>] [--root .] <TTL…>   (bazel build //kg:open)
"""
import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import rdflib
from rdflib import Graph, Namespace, RDF
from rdflib.namespace import PROV

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
SLOT = "미확정"  # 선택 슬롯의 표지 — 값 어휘의 단일 정의 위치는 chunk2kg.BODY_SLOT_KEYWORDS 다
# `미확정: <질문>. 상세는 `<값>`[·`<값>`]다.` — 상세 절은 선택이다. 질문만 적은 슬롯도 집계 대상이다
SLOT_LINE = re.compile(r"^" + SLOT + r":\s*(.+)$")
DETAIL = re.compile(r"상세는\s*((?:`[^`]+`\s*[·,]?\s*)+)다\.?\s*$")
TICK = re.compile(r"`([^`]+)`")
AGE_RULE = ("만든 날부터 이 뷰의 생성 시각까지의 일수다. 만든 날은 항목의 `generated.at`(`prov:generatedAtTime`)으로 잰다. "
            "밀폐 빌드는 git 의 첫 커밋 날짜를 읽지 못하고 `generated.at` 은 마지막 저작 시각이므로 이 나이는 실제 나이의 하한이다 (유저 답 Q116-a)")
# 후보 링크의 상태 → 본문 `state:` 어휘 (space2kg 가 쓴 사상의 역)
STATE_OF_LINK = {link: state for state, (_, link) in kb_lib.SPACE_STATE_LINK.items()}


# ── 본문의 미확정 슬롯과 설계 공간을 모아 낸다 ────────────────────

def cell(s: str) -> str:
    """표 셀 — 줄바꿈과 파이프를 없앤다. 빈 값은 세 빈 값의 첫 값이다."""
    return " ".join(str(s).split()).replace("|", "\\|") or kb_lib.NONE_MARK


def question_of(body: str) -> tuple[str, list[str]]:
    """본문 → (질문, 상세 값들). 상세 값은 공간 IRI 또는 문서 경로다. 슬롯 줄이 없으면 ('', [])."""
    for line in body.split("\n"):
        m = SLOT_LINE.match(line.strip())
        if not m:
            continue
        text = m.group(1).strip()
        d = DETAIL.search(text)
        if not d:
            return text, []
        return text[:d.start()].strip().rstrip(".").strip(), TICK.findall(d.group(1))
    return "", []


def age_days(g: Graph, node, now: datetime):
    """항목의 나이(일) — `prov:generatedAtTime` 부터 now 까지의 온전한 일수. 시각이 없거나 읽을 수 없으면 None."""
    raw = str(next(g.objects(node, PROV.generatedAtTime), ""))
    try:
        at = datetime.fromisoformat(raw)
    except ValueError:
        return None
    at = at if at.tzinfo else at.replace(tzinfo=timezone.utc)
    return max((now - at).days, 0)


def age_cell(days) -> str:
    """나이 셀 — 일수다. 시각이 없으면 생성 문서의 빈 값 표기(`kb_lib.NONE_MARK`)를 쓴다."""
    return kb_lib.NONE_MARK if days is None else str(days)


def space_rows(g: Graph, now: datetime) -> list[dict]:
    """설계 공간 그래프 → 공간마다 제목·status·변수·후보 state 별 수·본문 위치."""
    rows = []
    for s in set(g.subjects(RDF.type, AGT.Space)):
        counts = dict.fromkeys(kb_lib.SPACE_STATES, 0)
        for link in g.objects(s, AGT.hasCandidate):
            st = STATE_OF_LINK.get(str(next(g.objects(link, AGT.linkState), "")), "")
            if st:
                counts[st] += 1
        frm = next(g.objects(s, AGT.variableFrom), None)
        rows.append({
            "iri": str(s), "ko": kb_lib.label_of(g, s, "ko"),
            "status": str(next(g.objects(s, AGT.spaceStatus), "")),
            "loc": str(next(g.objects(s, AGT.assertionLocation), "")),
            "from_ko": kb_lib.label_of(g, frm, "ko") if frm is not None else "",
            "from_iri": kb_lib.compact_iri(str(frm)) if frm is not None else "",
            "kind": str(next(g.objects(s, AGT.variableKind), "")).split("/")[-1],
            "counts": counts, "slots": [], "age": age_days(g, s, now),
        })
    rows.sort(key=lambda r: (r["status"] != "open", r["loc"]))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--spaces", nargs="*", default=[], help="설계 공간 그래프(//space:design_space)")
    ap.add_argument("--bodies", nargs="*", default=[], help="단위 지식 .md — 그래프의 assertionLocation 과 접미로 맞춘다")
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

    now = datetime.now(timezone.utc)  # 나이의 기준 — 머리 블록의 생성 시각과 같은 실행에서 잰다
    spaces = space_rows(g, now)
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
             "age": age_days(g, c, now),
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
        f"그 공간을 상세로 가리키는 선택 슬롯 `{SLOT}:` 의 단위 지식을 내고, head 그래프에서 공간을 가리키지 않는 슬롯"
        f"(`agt:bodySlot \"{SLOT}\"`)을 질문 · 단위 지식(라벨·IRI) · plane/level · 상세 문서로 낸다. 미결 목록의 유일한 자리다",
        "bazel build //kg:open", list(a.files) + list(a.spaces),
        f"공간 {len(spaces)}개(open {n_open}) · 슬롯 미결 {len(rows)}개",
        kb_lib.gendoc_view_notice("설계 공간(`space/*-space.md`)과 미결을 안은 단위 지식의 `미확정:` 슬롯"),
        input_kind="그래프 파일", extra=[f"- 나이: {AGE_RULE}"])
    oldest_space = max((s["age"] for s in spaces if s["status"] == "open" and s["age"] is not None), default=None)
    oldest_slot = max((r["age"] for r in rows if r["age"] is not None), default=None)

    lines = ["## 요약", "",
             "| 항목 | 값 |", "|---|---|",
             f"| 설계 공간 | {len(spaces)} |",
             f"| 열린 공간(status open) | {n_open} |",
             f"| 공간을 가리키는 슬롯 | {n_slots} |",
             f"| 공간을 가리키지 않는 슬롯 미결 | {len(rows)} |",
             f"| 슬롯 미결을 안은 단위 지식 | {len({r['loc'] for r in rows})} |",
             f"| 슬롯 미결의 지식 종류 분포 | " + (" · ".join(f"{p} {sum(1 for r in rows if r['plane'] == p)}"
                                                    for p in sorted({r["plane"] for r in rows})) or kb_lib.NONE_MARK) + " |",
             f"| 상세 문서가 있는 슬롯 미결 | {kb_lib.pct(sum(1 for r in rows if r['docs']), len(rows))} |",
             f"| 가장 오래된 열린 공간의 나이(일) | {age_cell(oldest_space)} |",
             f"| 가장 오래된 슬롯 미결의 나이(일) | {age_cell(oldest_slot)} |",
             f"| 해석하지 못한 상세 IRI | {len(unresolved)} |",
             f"| 슬롯은 있으나 질문을 못 읽은 단위 지식 | {len(missing)} |",
             "", "## 설계 공간", "",
             "공간 하나가 미결 하나다. 후보 열은 `state` 별 수이고 순서는 open · eliminated · confirmed 다. "
             "open 공간을 먼저, 같은 status 안에서는 파일 순으로 낸다. 나이 열의 규칙은 머리 블록에 있다.", "",
             "| 공간 | status | 나이(일) | 변수 (from · kind) | 후보 open/eliminated/confirmed | 가리키는 슬롯 |", "|---|---|---|---|---|---|"]
    for s in spaces:
        # 링크가 아니라 코드 스팬이다 — 생성물은 bazel-bin/kg/ 에 놓이므로 소스 기준 상대경로가 성립하지 않는다 (STYLEGUIDE §9)
        slots = "<br>".join(f"{cell(r['ko'])} `{r['iri']}`" for r in s["slots"]) or kb_lib.NONE_MARK
        frm = f"{cell(s['from_ko'])}<br>`{s['from_iri']}` · {cell(s['kind'])}" if s["from_iri"] else kb_lib.NONE_MARK
        c = s["counts"]
        lines.append(f"| {cell(s['ko'])}<br>`{s['loc']}` | {cell(s['status'])} | {age_cell(s['age'])} | {frm} | "
                     f"{'/'.join(str(c[k]) for k in kb_lib.SPACE_STATES)} | {slots} |")
    if not spaces:
        lines.append("| " + " | ".join([kb_lib.NONE_MARK] * 6) + " |")

    lines += ["", "## 슬롯 미결", "",
              "공간을 가리키지 않는 `미확정:` 슬롯이다. 질문 한 줄이 미결의 전부이거나 상세가 문서 경로다.", "",
              "| 질문 | 단위 지식 | plane/level | 상태 | 나이(일) | 상세 |", "|---|---|---|---|---|---|"]
    for r in rows:
        detail = "<br>".join(f"`{d}`" for d in r["docs"]) or kb_lib.NONE_MARK
        lines.append(f"| {cell(r['q'])} | {cell(r['ko'])}<br>`{r['iri']}` | {cell(r['plane'])}/{cell(r['level'])} | "
                     f"{cell(r['status'])} | {age_cell(r['age'])} | {detail} |")
    if not rows:
        lines.append("| " + " | ".join([kb_lib.NONE_MARK] * 6) + " |")

    lines += ["", "## 해석하지 못한 상세", "",
              "슬롯의 상세 값이 IRI 인데 설계 공간 그래프에 그 공간이 없다. 공간이 지워졌거나 IRI 가 틀렸다.", ""]
    lines += [f"- `{loc}` → `{d}`" for loc, d in sorted(unresolved)] or [f"- {kb_lib.NONE_MARK}"]
    lines += ["", "## 슬롯을 읽지 못한 단위 지식", "",
              f"슬롯 표지는 있으나 `{SLOT}: <질문>` 줄을 본문에서 찾지 못한 단위 지식이다. 본문이 `--bodies` 에도 `--root` 아래에도 없거나 슬롯의 형태가 다르다.", ""]
    lines += [f"- `{loc}`" for loc in sorted(missing)] or [f"- {kb_lib.NONE_MARK}"]
    lines.append("")
    inputs = list(a.files) + list(a.spaces)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, inputs, input_kind="그래프 파일"), encoding="utf-8")
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
