#!/usr/bin/env python3
"""규범 문서 생성기 — 절 청크(`kb/dev/norm/<문서 stem>/`)와 결정의 규약 줄(`conventions.md`)에서 규범 문서를 생성한다.

규범 문서(`STYLEGUIDE.md`·`docs/rules.md`·`docs/method.md`·`AGENTS.md`)는 방법론 층의 투영이고 원본은 청크다 (결정
p12-norm-documents-from-section-chunks, 유저 답 Q19-b·Q21-a·Q22-b). 골격은 `norm` plane 의 절 청크이고 문장은 결정의
선택 넷째 청크 `conventions.md` 의 `규약:` 줄이다 (p4-convention-slot). 생성물은 소스 트리에 두고 커밋한다 — 도구가 없어도
문서가 읽혀야 하기 때문이다(`.claude/skills` 와 같은 생성 트리 파일). //:norms_drift_test 가 생성기를 다시 돌려 바이트로 비교한다.

문서 목록의 단일 정의처는 `defs/kb.bzl` 의 `NORM_DOCS`(문서 stem → 생성 파일 경로)다. 문서 하나는 복합체 하나이고 순서는
머리 청크(composite: 선언)의 `composite.ordered` 다. 직접 부분은 9 이하이므로(4.5절, p4-composite-as-part-of) 절이 많은 문서는
절을 묶음 복합체로 나눈다 — 묶음의 첫 절 청크가 `composite: {id, title_ko, title, part_of: <문서 복합체>, ordered: […]}` 로
선언하고 묶음 안 절 청크의 `part_of` 는 묶음 IRI 다. 묶음은 제목을 내지 않고 순서만 준다 — 절의 순서는 문서 복합체의 순서를
깊이 우선으로 펼친 것이다. 머리 청크의 본문이 문서 도입문·범례이고, 절 청크마다 제목(번호는 이 도구가
머리 청크의 `numbering` 꼴로 붙인다. `numbered: false` 인 절은 번호가 없다) → 본문 → 항목을 낸다. 항목은 `items` 의 `slug#k` 가 가리키는 줄이고 결정 링크는 그 문장의
첫 문장 끝에 둔다. 문장 안 링크는 청크 기준 상대경로라 출력 위치 기준으로 다시 계산한다. 머리 블록은 생성 트리 파일의 꼴이다
(`kb_lib.gendoc_header(stamped=False)` + `gendoc_tree_notice`) — 생성 시각·지문이 없고 바이트 비교가 그 자리의 건전성 장치다.
절 청크 하나는 항목 묶음 하나(목록 하나 또는 표 하나)를 갖고 본문은 그 묶음 앞의 산문이다. 묶음의 꼴은 `form`(bullets · ordered ·
table)이고, 표는 `columns` 를 열 머리로 행마다 줄의 `a | b | …` 를 칸으로 낸다. `link_column`(columns 의 마지막)이 있으면 그 열이
결정 링크이고, 없으면 표 바로 앞에 `원본:` 한 줄이 행의 결정(주·둘째 구분 없이)을 처음 나온 순서로 낸다. 묶음 뒤의 산문과 다음 묶음은 이어짐 절
청크(`continues: true` — 제목·깊이 없음, 번호를 소비하지 않음)가 담는다.

검사: 모든 살아 있는 `규약:` 줄은 적어도 한 문서에서 쓰이고(고아 줄 FAIL) 한 문서 안에서는 한 번까지만 쓰인다(이중 소비
FAIL). 서로 다른 문서가 같은 줄을 각각 한 번씩 싣는 것은 허용한다 — 두 규범 문서에 같은 문장을 실으려고 결정에 사본 줄을 두지 않게
하기 위해서다. 강도를 요구하는 문서(머리 청크의
`strength`, 기본 required)에서 강도 없는 줄은 FAIL 이다. 없는 결정·없는 줄을 가리키는 항목, `NORM_DOCS` 와 디렉토리 집합의
불일치, 절 청크의 구조 위반(선언·순서·머리 청크의 키·첫 절의 깊이·첫 절의 이어짐)도 FAIL 이다. 표 절에서는 강도가 붙은 줄과
링크 열을 뺀 열 수와 칸 수가 다른 줄이 FAIL 이고, 표 절의 줄에는 강도 요구가 적용되지 않는다.
사용: gen_norms.py [--check] [--root .] [--doc <stem>] [--residency defs/kb.bzl] [--norm-docs <NORM_DOCS 를 담은 파일>]
출력·종료: 생성 시점 거부는 `FAIL [gen-norms] …` EXIT_FAIL, --check 의 어긋남은 `FAIL [norms-drift] …` EXIT_FAIL,
읽을 수 없는 입력은 EXIT_CONFIG. 문서가 0개여도 검사(고아 줄)는 돌고 위반이 없으면 PASS 다 — 생성기이므로 SKIP 이 아니다.
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
    from tools.chunk2kg import (BODY_FENCE, NORM_COLUMNS_KEY, NORM_CONTINUES_KEY, NORM_FORM_DEFAULT, NORM_FORM_KEY,
                                NORM_FORM_TABLE, NORM_LINK_COLUMN_KEY, NORM_DEPTH_KEY, NORM_HEADING_KEY, NORM_ITEMS_KEY, NORM_NUMBERING,
                                NORM_NUMBERED_KEY, NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_TYPE, ORDERED_KEY, PART_OF_KEY,
                                apply_plane_level_state, load_plane_level_state, norm_bundle_errors, parse_chunk)
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    from chunk2kg import (BODY_FENCE, NORM_COLUMNS_KEY, NORM_CONTINUES_KEY, NORM_FORM_DEFAULT, NORM_FORM_KEY,
                          NORM_FORM_TABLE, NORM_LINK_COLUMN_KEY, NORM_DEPTH_KEY, NORM_HEADING_KEY, NORM_ITEMS_KEY, NORM_NUMBERING,
                          NORM_NUMBERED_KEY, NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_TYPE, ORDERED_KEY, PART_OF_KEY,
                          apply_plane_level_state, load_plane_level_state, norm_bundle_errors, parse_chunk)

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.GEN_NORMS_GATE, kb_lib.NORMS_DRIFT_GATE
NORM_DOCS_NAME = "NORM_DOCS"
NORM_ROOT = "kb/dev/norm"
DECISION_ROOT = "kb/dev/decision"
CONVENTIONS_FILE = kb_lib.DECISION_PART_FILES["conventions"]
CONCLUSION_FILE = kb_lib.DECISION_PART_FILES["conclusion"]
CONVENTION_LINE = re.compile(r"^규약:\s+(.*\S)\s*$")      # 줄 머리 `규약:` — chunk2kg.BODY_SLOT_KEYWORDS 의 같은 표지
STRENGTH = re.compile(r"^\[(지킴|권장)\]\s+(\S.*)$")       # 강도 — 문장의 성질이라 줄 머리에 둔다 (p4-convention-slot)
STRENGTH_DEFAULT = "required"
NORM_NUMBERED_DEFAULT = "true"  # 절 청크의 `numbered` — false 인 depth 2 절(부록)은 번호 없이 낸다
MD_LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^)\s]+)(\))")  # 인라인 링크·그림 — 대상만 다시 계산한다. 텍스트는 코드 스팬을 담을 수 있다
URL_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
NOTICE_TARGET = "//:norms_drift_test"


class GenNormsError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""


# ── 결정의 규약 줄 ────────────────────

def load_conventions(root: Path) -> dict[str, dict]:
    """결정 slug → {path, lines: [(강도 또는 None, 문장)…], live}. 규약 청크가 없는 결정은 `path` 가 None 이다.

    줄 순번 k 는 `lines` 의 1부터의 색인이다. 펜스 안의 `규약:` 은 예시이지 줄이 아니다. deprecated 규약 청크는 살아 있지
    않다 — 그 줄은 고아가 아니고 가리켜도 안 된다.
    """
    out: dict[str, dict] = {}
    base = root / DECISION_ROOT
    for d in sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []:
        entry = {"path": None, "lines": [], "live": False, "linkable": (d / CONCLUSION_FILE).is_file()}
        f = d / CONVENTIONS_FILE
        if f.is_file():
            meta, body = parse_chunk(str(f))
            if meta["type"] != "decision":
                raise GenNormsError(f"{rel(root, f)}: 규약 청크는 type: decision 이다 — 실제 {meta['type']!r} (p4-convention-slot)")
            fence = None
            for line in body.splitlines():
                m = BODY_FENCE.match(line)
                if fence:
                    if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                        fence = None
                    continue
                if m:
                    fence = m.group(1)
                    continue
                cm = CONVENTION_LINE.match(line)
                if not cm:
                    continue
                sm = STRENGTH.match(cm.group(1))
                entry["lines"].append((sm.group(1), sm.group(2)) if sm else (None, cm.group(1)))
            entry.update(path=rel(root, f), live=meta["status"] != "deprecated")
        out[d.name] = entry
    return out


# ── 규범 문서의 절 청크 ────────────────────

def load_doc(root: Path, stem: str) -> dict:
    """`kb/dev/norm/<stem>/` → {head: 메타, sections: [메타…], files: [경로…]} — 선언 순서대로. 구조 위반은 GenNormsError."""
    d = root / NORM_ROOT / stem
    metas = []
    for f in sorted(d.glob("*.md")):
        meta, body = parse_chunk(str(f))
        meta["_path"], meta["_body"] = rel(root, f), body
        if meta["type"] != NORM_TYPE:
            raise GenNormsError(f"{meta['_path']}: {NORM_ROOT}/ 의 청크는 type: {NORM_TYPE} 이다 — 실제 {meta['type']!r}")
        metas.append(meta)
    where = f"{NORM_ROOT}/{stem}"
    decls = [m for m in metas if isinstance(m.get("composite"), dict) and m["composite"].get("id")]
    roots = [m for m in decls if not m["composite"].get(PART_OF_KEY)]
    if len(roots) != 1:
        raise GenNormsError(f"{where}: 머리 청크(composite: 선언, composite.{PART_OF_KEY} 없음)는 정확히 하나다 — 실제 {len(roots)}개 "
                            f"(문서 하나 = 복합체 하나)")
    head = roots[0]
    comp = head["composite"]
    bundles = {m["composite"]["id"]: m for m in decls if m is not head}  # 묶음 복합체 IRI → 선언한 첫 절 청크
    comps = {comp["id"]: head, **bundles}
    for b, m in sorted(bundles.items()):
        if m["composite"][PART_OF_KEY] not in comps:
            raise GenNormsError(f"{m['_path']}: 묶음 복합체 {b} 의 composite.{PART_OF_KEY} 가 문서 복합체 {comp['id']} 또는 그 아래 묶음이 "
                                f"아니다 — 실제 {m['composite'][PART_OF_KEY]!r} (p4-composite-as-part-of)")
    stray = [m["_path"] for m in metas if m.get("part_of") not in comps]
    if stray:
        raise GenNormsError(f"{where}: part_of 가 문서의 복합체 {comp['id']} 또는 그 아래 묶음이 아닌 청크 — {stray}")
    by_id = {m["id"]: m for m in metas}
    for c, decl in sorted(comps.items()):  # 복합체마다 선언된 순서 = 직접 부분(절 청크 · 묶음) 전부 (p4-composite-order-is-declared)
        order = decl["composite"].get(ORDERED_KEY)
        parts = sorted([m["id"] for m in metas if m.get("part_of") == c] +
                       [b for b, m in bundles.items() if m["composite"][PART_OF_KEY] == c])
        if not order or sorted(order) != parts:
            raise GenNormsError(f"{decl['_path']}: 복합체 {c} 의 composite.{ORDERED_KEY} 가 직접 부분(절 청크 · 묶음 복합체) 전부를 빠짐없이 "
                                f"한 번씩 담아야 한다 — 절의 순서는 선언이다 (p4-composite-order-is-declared). 선언 {order} · 부분 {parts}")
        if order[0] != decl["id"]:
            raise GenNormsError(f"{decl['_path']}: composite.{ORDERED_KEY} 의 첫 부분은 선언 청크 자신이다 — 문서는 도입문(머리 청크)이, "
                                f"묶음은 선언한 첫 절 청크가 첫머리다")
    errors = norm_bundle_errors(head, [(m, m["_path"]) for m in metas])
    if errors:
        raise GenNormsError("; ".join(errors))
    order = flatten(comp["id"], comps, set())
    sections = [by_id[i] for i in order[1:]]  # 깊이 우선으로 펼친 절 — 묶음은 제목을 내지 않고 순서만 준다
    if sections and is_continuation(sections[0]):
        raise GenNormsError(f"{sections[0]['_path']}: 문서의 첫 절은 이어짐 절 청크({NORM_CONTINUES_KEY}: true)일 수 없다 — "
                            f"이어짐은 앞 절의 묶음 뒤를 잇는다")
    prev = 1
    for s in sections:
        if is_continuation(s):  # 깊이는 앞 절을 잇는다
            continue
        depth = int(s[NORM_DEPTH_KEY])
        if depth > prev + 1:
            raise GenNormsError(f"{s['_path']}: depth {depth} 가 앞 절의 깊이 {prev} 를 한 단계 넘게 건너뛴다 — 문서의 첫 절은 depth 2 다 (G8)")
        prev = depth
    return {"head": head, "sections": sections, "files": [m["_path"] for m in metas]}


def is_continuation(meta: dict) -> bool:
    """이어짐 절 청크(`continues: true`)인가 — 제목·깊이가 없고 번호를 소비하지 않으며 본문은 앞 묶음 뒤의 산문이다."""
    return meta.get(NORM_CONTINUES_KEY) == "true"


def form_of(meta: dict) -> str:
    return meta.get(NORM_FORM_KEY, NORM_FORM_DEFAULT)


def table_cells(text: str) -> list[str]:
    """표 절의 `규약:` 줄 `a | b | c` → 칸 목록. 이스케이프되지 않은 `|` 가 칸을 가른다 — `\\|` 는 칸 안의 글자다(코드 스팬 안도 같다)."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", text)]


def flatten(comp_iri: str, comps: dict, seen: set) -> list[str]:
    """복합체의 `composite.ordered` 를 깊이 우선으로 펼친 절 청크 IRI 목록 — 묶음 IRI 를 만나면 그 묶음의 순서로 들어간다.

    문서 복합체의 직접 부분은 9 이하다(4.5절, p4-composite-as-part-of). 절이 더 많은 문서는 절을 묶음 복합체로 나누고, 묶음은
    문서 출력에 보이지 않는다 — 펼친 순서가 곧 절의 순서다. 순환(`composite.part_of` 사슬)은 GenNormsError 다.
    """
    if comp_iri in seen:
        raise GenNormsError(f"{comps[comp_iri]['_path']}: 묶음 복합체 {comp_iri} 의 composite.{PART_OF_KEY} 사슬이 순환한다 (4.5절 비순환)")
    seen.add(comp_iri)
    out = []
    for x in comps[comp_iri]["composite"][ORDERED_KEY]:
        out += flatten(x, comps, seen) if x in comps else [x]
    return out


def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()


# ── 링크와 항목의 조립 ────────────────────

def rebase_links(text: str, src: str, out: str) -> str:
    """청크(`src`, 루트 상대) 기준 상대 링크 → 출력(`out`) 기준. 링크 밖의 코드 스팬·펜스 안, 절대 URL, 문서 안 앵커는 그대로다."""
    src_dir, out_dir = os.path.dirname(src), os.path.dirname(out) or "."

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if URL_SCHEME.match(target) or target.startswith(("#", "/")):
            return m.group(0)
        path, sep, anchor = target.partition("#")
        new = os.path.relpath(os.path.normpath(os.path.join(src_dir, path)), out_dir).replace(os.sep, "/")
        return m.group(1) + new + sep + anchor + m.group(3)

    # 펜스 밖은 문단 단위로 읽는다 — 코드 스팬은 문단 안에서 줄을 넘을 수 있으므로(CommonMark 6.1) 줄 단위로 읽으면 다음 줄에서
    # 닫히는 백틱이 뒤의 링크 텍스트 안 백틱과 짝지어져 링크가 다시 계산되지 않는다
    lines, para, fence = [], [], None

    def flush() -> None:
        if para:
            lines.extend(_rebase_line("\n".join(para), fix).split("\n"))
            para.clear()

    for line in text.split("\n"):
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            lines.append(line)
            continue
        if m:
            flush()
            fence = m.group(1)
            lines.append(line)
            continue
        if not line.strip():
            flush()
            lines.append(line)
            continue
        para.append(line)
    flush()
    return "\n".join(lines)


def _code_span_end(s: str, i: int) -> int:
    """`s[i]` 에서 시작하는 백틱 열이 여는 코드 스팬의 끝(닫는 열 다음 위치) — 같은 길이의 닫는 열이 없으면 -1 (CommonMark 6.1)."""
    j = _tick_run_end(s, i)
    n = j - i
    while True:
        k = s.find("`" * n, j)
        if k < 0:
            return -1
        m = _tick_run_end(s, k)
        if m - k == n:
            return m
        j = m


def _tick_run_end(s: str, i: int) -> int:
    """`s[i]` 에서 시작하는 백틱 열의 끝 위치."""
    return len(s) - len(s[i:].lstrip("`"))


def _spans_closed(s: str) -> bool:
    """`s` 안의 코드 스팬이 전부 `s` 안에서 닫히는가 — 링크 텍스트가 코드 스팬의 중간에서 끝나면 링크가 아니다."""
    i = 0
    while (i := s.find("`", i)) >= 0:
        end = _code_span_end(s, i)
        if end < 0:
            return False
        i = end
    return True


def _rebase_line(line: str, fix) -> str:
    """한 줄의 인라인 링크 대상을 `fix` 로 바꾼다 — 왼쪽부터 읽으며 링크를 코드 스팬보다 먼저 시도한다.

    링크 텍스트 안의 코드 스팬(`[`x`](경로)`)은 링크의 일부라 대상을 다시 계산한다. 링크 밖에서 열린 코드 스팬은 통째로 옮긴다 —
    백틱 안에 적은 링크 꼴 예시는 링크가 아니다.
    """
    out, i = [], 0
    while i < len(line):
        ch = line[i]
        if ch in "![":
            m = MD_LINK.match(line, i)
            if m and _spans_closed(m.group(1)):
                out.append(fix(m))
                i = m.end()
                continue
        elif ch == "`":
            end = _code_span_end(line, i)
            if end >= 0:
                out.append(line[i:end])
                i = end
                continue
            end = _tick_run_end(line, i)  # 닫히지 않는 백틱 열은 글자다
            out.append(line[i:end])
            i = end
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def first_sentence_end(text: str) -> tuple[int, bool] | None:
    """첫 문장의 끝 마침표 위치와 그 마침표가 굵은 span 을 닫는가 — 코드 스팬·괄호 안의 마침표와 `4.5절` 은 끝이 아니다."""
    code, depth = False, 0
    for i, ch in enumerate(text):
        if ch == "`":
            code = not code
        elif code:
            continue
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            nxt = text[i + 1:i + 2]
            if nxt == "" or nxt.isspace():
                return i, False
            if text[i + 1:i + 3] == "**" and text[i + 3:i + 4] in ("", " "):
                return i, True
    return None


def with_links(text: str, links: list[str]) -> str:
    """결정 링크를 첫 문장 끝(마침표 앞)에 둔다 — 링크 위치의 정규화 규칙 하나다 (p12-norm-documents-from-section-chunks).

    첫 문장이 굵은 span 안에서 끝나면(`**…다.** …`) 마침표를 span 밖으로 옮겨 `**…다** (링크). …` 로 낸다.
    """
    cite = "(" + ", ".join(links) + ")"
    pos = first_sentence_end(text)
    if pos is None:
        return f"{text} {cite}"
    i, bold = pos
    if bold:
        return f"{text[:i]}** {cite}.{text[i + 3:]}"
    return f"{text[:i]} {cite}{text[i:]}"


def decision_link(slug: str, out: str) -> str:
    target = os.path.relpath(f"{DECISION_ROOT}/{slug}/{CONCLUSION_FILE}", os.path.dirname(out) or ".").replace(os.sep, "/")
    return f"[`{slug}`]({target})"


# ── 문서 전체의 판정과 생성 ────────────────────

def plan(root: Path, docs: dict[str, str], conventions: dict) -> tuple[dict, dict]:
    """문서 stem → 적재된 문서, (slug, k) → 쓰인 자리 (문서 stem, 절 청크 경로) 목록. 항목의 실재·강도를 여기서 판정하고 위반은 모아 GenNormsError 로 낸다."""
    errors: list[str] = []
    loaded, uses = {}, {}
    for stem in sorted(docs):
        doc = load_doc(root, stem)
        required = doc["head"].get(NORM_STRENGTH_KEY, STRENGTH_DEFAULT) == STRENGTH_DEFAULT
        for s in doc["sections"]:
            table = form_of(s) == NORM_FORM_TABLE
            cols = s.get(NORM_COLUMNS_KEY) or []
            width = len(cols) - (1 if NORM_LINK_COLUMN_KEY in s else 0)  # 줄이 채우는 칸 — 링크 열은 생성기가 채운다
            for it in s.get("_norm_items") or []:
                for x in [it] + it["sub"]:
                    slug, k = x["ref"]
                    c = conventions.get(slug)
                    if c is None:
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 결정 {slug!r} 가 {DECISION_ROOT}/ 에 없다")
                        continue
                    if not c["live"] or not 1 <= k <= len(c["lines"]):
                        have = len(c["lines"]) if c["live"] else 0
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 가 없는 줄을 가리킨다 — {DECISION_ROOT}/{slug}/{CONVENTIONS_FILE} 의 "
                                      f"살아 있는 `규약:` 줄은 {have}개다 (p4-convention-slot)")
                        continue
                    uses.setdefault((slug, k), []).append((stem, s["_path"]))
                    if table:
                        strength, text = c["lines"][k - 1]
                        if strength is not None:
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 는 표 절의 행인데 줄에 강도 [{strength}] 가 있다 — 표의 줄은 "
                                          f"강도를 갖지 않는다. 줄을 `규약: a | b | …` 로 쓴다")
                        cells = table_cells(text)
                        if len(cells) != width:
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 칸 수 {len(cells)} 가 표의 열 수 {width}(링크 열 제외 "
                                          f"columns {cols}) 와 다르다 — 줄은 `a | b | …` 꼴이고 칸 안의 `|` 는 `\\|` 로 쓴다")
                        elif not all(cells):
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 에 빈 칸이 있다 — 빈 값은 `{kb_lib.NONE_MARK}` 으로 적는다 (G14)")
                    elif required and c["lines"][k - 1][0] is None:
                        errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 줄에 강도가 없다 — 문서 {stem} 은 강도를 요구한다"
                                      f"(머리 청크 strength: required). 줄을 `규약: [지킴] …` 또는 `규약: [권장] …` 으로 쓴다")
                    for extra in x["links"]:
                        if not conventions.get(extra, {}).get("linkable"):
                            errors.append(f"{s['_path']}: 항목 {slug}#{k} 의 링크 결정 {extra!r} 의 결론 청크가 없다 — "
                                          f"{DECISION_ROOT}/{extra}/{CONCLUSION_FILE}")
        loaded[stem] = doc
    for slug, c in sorted(conventions.items()):
        if not c["live"]:
            continue
        for k in range(1, len(c["lines"]) + 1):
            used = uses.get((slug, k), [])
            if not used:
                errors.append(f"{c['path']}: 줄 {slug}#{k} 를 어느 규범 문서도 싣지 않는다(고아 줄) — 줄은 적어도 한 문서에서 "
                              f"쓰인다. 절 청크의 items 에 `{slug}#{k}` 를 더한다 (p12-norm-documents-from-section-chunks)")
            for stem in sorted({d for d, _ in used}):
                paths = sorted(path for d, path in used if d == stem)
                if len(paths) > 1:
                    errors.append(f"{c['path']}: 줄 {slug}#{k} 가 문서 {stem} 안에서 {len(paths)}번 쓰였다(이중 소비) — {paths}. "
                                  f"한 문서 안에서는 한 줄을 한 번까지만 싣는다. 다른 문서가 같은 줄을 싣는 것은 허용한다")
    if errors:
        raise GenNormsError("\n".join(errors))
    return loaded, uses


def render_item(x: dict, conventions: dict, out: str, indent: str = "", marker: str = "-") -> str:
    slug, k = x["ref"]
    strength, text = conventions[slug]["lines"][k - 1]
    text = rebase_links(text, conventions[slug]["path"], out)
    body = with_links(text, [decision_link(s, out) for s in [slug] + x["links"]])
    return f"{indent}{marker} " + (f"**[{strength}]** " if strength else "") + body


def render_list(s: dict, conventions: dict, out: str) -> list[str]:
    """목록 묶음 — bullets 는 `-`, ordered 는 항목마다 `1.`(목록 규칙). 하위 항목은 상위 표지의 폭만큼 들여 같은 표지로 낸다."""
    marker = "1." if form_of(s) == "ordered" else "-"
    indent = " " * (len(marker) + 1)
    lines = []
    for it in s.get("_norm_items") or []:
        lines.append(render_item(it, conventions, out, marker=marker))
        lines += [render_item(x, conventions, out, indent, marker) for x in it["sub"]]
    return lines


def render_table(s: dict, conventions: dict, out: str) -> list[str]:
    """표 묶음 — 행은 항목 하나, 칸은 줄의 `a | b | …` 다. 링크 열이 있으면 그 칸이 결정 링크(` · ` 로 이음)이고, 없으면 표 바로
    앞에 `원본:` 한 줄(행의 주 결정과 `+ slug2` 의 둘째 결정을 구분 없이 처음 나온 순서로 중복 없이)을 낸다."""
    cols = s[NORM_COLUMNS_KEY]
    linked = NORM_LINK_COLUMN_KEY in s
    rows, mains = [], []
    for it in s.get("_norm_items") or []:
        slug, k = it["ref"]
        cells = [rebase_links(c, conventions[slug]["path"], out) for c in table_cells(conventions[slug]["lines"][k - 1][1])]
        if linked:
            cells.append(" · ".join(decision_link(x, out) for x in [slug] + it["links"]))
        rows.append("| " + " | ".join(cells) + " |")
        for x in [slug] + it["links"]:  # 링크 열이 없으면 원본 줄이 행의 결정 링크를 내는 유일한 자리다 — 둘째 결정도 싣는다
            if x not in mains:
                mains.append(x)
    lines = [] if linked else ["원본: " + " · ".join(decision_link(x, out) for x in mains) + ".", ""]
    return lines + ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)] + rows


def render(stem: str, out: str, doc: dict, conventions: dict) -> str:
    """문서 하나 — 머리 블록 + (G12) 목차 + 인용 구역(도입문 · 절마다 제목 → 본문 → 항목) + (G4) 입력 파일 절."""
    head = doc["head"]
    numbering = head.get(NORM_NUMBERING_KEY)
    prefix, n = "", None
    if numbering:
        m = NORM_NUMBERING.match(str(numbering))
        prefix, n = m.group(1), int(m.group(2))
    inner: list[str] = []
    intro = rebase_links(head["_body"].strip(), head["_path"], out)
    if intro:
        inner += [intro, ""]
    inputs = set(doc["files"])
    n_items = 0
    for s in doc["sections"]:
        if not is_continuation(s):  # 이어짐 절 청크는 제목이 없고 번호를 소비하지 않는다
            depth = int(s[NORM_DEPTH_KEY])
            title = s[NORM_HEADING_KEY].strip()
            if depth == 2 and n is not None and s.get(NORM_NUMBERED_KEY, NORM_NUMBERED_DEFAULT) != "false":  # 번호 없는 절은 번호를 소비하지 않는다
                title = f"{prefix}{n}. {title}"
                n += 1
            inner += ["#" * depth + " " + title, ""]
        body = rebase_links(s["_body"].strip(), s["_path"], out)
        if body:
            inner += [body, ""]
        items = s.get("_norm_items") or []
        if items:
            inner += (render_table if form_of(s) == NORM_FORM_TABLE else render_list)(s, conventions, out) + [""]
        for it in items:
            for x in [it] + it["sub"]:
                inputs.add(conventions[x["ref"][0]]["path"])
            n_items += 1 + len(it["sub"])
    while inner and not inner[-1]:
        inner.pop()
    comp = head["composite"]
    header = kb_lib.gendoc_header(
        Path(out).name, comp["title_ko"], "tools/gen_norms.py",
        f"`{NORM_ROOT}/{stem}/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다",
        "python3 tools/gen_norms.py --root .", sorted(inputs), f"절 {len(doc['sections'])} · 규약 줄 {n_items}",
        kb_lib.gendoc_tree_notice(f"`{NORM_ROOT}/{stem}/` 의 절 청크와 결정의 `{CONVENTIONS_FILE}`", NOTICE_TARGET),
        input_kind="원본 파일", stamped=False)
    # 인용 구역을 줄 단위로 넘긴다 — 구역 안에도 제목 계층·목차 규칙이 적용되므로(G12) gendoc_assemble 이 본문의 실제 줄 수와
    # 제목을 세어 목차를 세운다. 원소 하나로 넘기면 120줄을 넘는 문서도 한 줄로 세어져 목차가 빠진다
    body = "\n".join(kb_lib.gendoc_quote("\n".join(inner))).split("\n") if inner else []
    return kb_lib.gendoc_assemble(header, body, sorted(inputs), input_kind="원본 파일", stamped=False)


def generate(root: Path, docs: dict[str, str], only: str = "") -> dict[str, str]:
    """{출력 경로(루트 상대): 내용} — `only` 가 있으면 그 문서만 낸다. 판정은 언제나 문서 전체로 한다(고아·이중 소비)."""
    norm_dirs = sorted(p.name for p in (root / NORM_ROOT).iterdir() if p.is_dir()) if (root / NORM_ROOT).is_dir() else []
    if sorted(docs) != norm_dirs:
        raise GenNormsError(f"{NORM_ROOT}: 문서 디렉토리 {norm_dirs} 와 defs/kb.bzl 의 {NORM_DOCS_NAME} 키 {sorted(docs)} 가 다르다 — "
                            f"문서 목록의 단일 정의처는 {NORM_DOCS_NAME} 이고 디렉토리마다 항목 하나다")
    outs = list(docs.values())
    bad = [o for o in outs if not o.endswith(".md") or o.startswith(("/", "../")) or outs.count(o) > 1]
    if bad:
        raise GenNormsError(f"defs/kb.bzl {NORM_DOCS_NAME}: 출력 경로는 저장소 상대의 서로 다른 .md 파일이다 — {sorted(set(bad))}")
    if only and only not in docs:
        raise GenNormsError(f"--doc {only}: {NORM_DOCS_NAME} 에 없는 문서다 — {sorted(docs)}")
    conventions = load_conventions(root)
    loaded, _uses = plan(root, docs, conventions)
    return {docs[s]: render(s, docs[s], loaded[s], conventions) for s in sorted(docs) if not only or s == only}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    ap.add_argument("--doc", default="", help="이 문서 stem 만 낸다 — 판정은 문서 전체로 한다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root 기준")
    ap.add_argument("--norm-docs", default="", help=f"{NORM_DOCS_NAME} 리터럴을 담은 파일 — 안 주면 --residency 와 같다(고정물 시험의 자리)")
    a = ap.parse_args()
    root = Path(a.root)
    bzl = Path(a.residency) if a.residency else root / "defs" / "kb.bzl"
    try:
        apply_plane_level_state(*load_plane_level_state(bzl))
        docs = kb_lib.load_bzl_dict(a.norm_docs or bzl, NORM_DOCS_NAME, allow_empty=True)
    except (OSError, ValueError) as e:
        print(f"FAIL [{GEN}] {a.norm_docs or bzl}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    try:
        outputs = generate(root, docs, a.doc)
    except GenNormsError as e:
        for line in str(e).splitlines():
            print(f"FAIL [{GEN}] {line}")
        return EXIT_FAIL
    except ValueError as e:  # parse_chunk 의 frontmatter·절 키 규칙 — chunk2kg 의 판정을 생성 시점에 그대로 낸다
        print(f"FAIL [{GEN}] {e}")
        return EXIT_FAIL
    except OSError as e:
        print(f"FAIL [{GEN}] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    drift = []
    for out, content in outputs.items():
        p = root / out
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(out)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{out} (트리)", f"{out} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content, encoding="utf-8")
    if a.check:
        for out in drift:
            print(f"FAIL [{DRIFT}] {out}: 원본(절 청크 · 결정의 규약 줄)과 어긋난다 — python3 tools/gen_norms.py --root . 를 돌려 커밋하라")
        if drift:
            print(f"\nFAIL [{DRIFT}] — 어긋남 {len(drift)}건 / 생성 문서 {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT}] — 생성 문서 {len(outputs)}개가 원본과 일치")
        return EXIT_OK
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(drift))
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
