#!/usr/bin/env python3
"""문서 뷰 생성기 — 그래프와 청크 본문에서 ADR·요구 색인·변경 이력을 생성한다 (노트 4.6절 weave, method §9, p12-documents-are-generated).

문서는 저장하지 않고 질의로 생성한다. 생성물 머리에 생성 시각(UTC)과 쓴 질의를 적는다 — 사본이 원본으로 오인되지 않게
(p12-documents-are-generated). 생성물은 bazel-bin 에만 있다 (kb_weave 매크로: //kb/dev:adr · :requirements · :changelog).
  adr           살아 있는 결정 전부 — 결정 복합체마다 한 절(제목 = 결론 라벨, 상태, 수준, 결론·근거·대안 본문을 청크 파일에서 frontmatter 를
                뺀 그대로), 그 뒤 "단일 파일 결정" 절에 결정 복합체에 속하지 않는 살아 있는 결정(chunks/decision/, v1·harness 유래)을 같은
                형식으로. 둘 다 refines 하는 요구 라벨, supersedes 연쇄(대체한 옛 결정 라벨), sources, 가정 라벨을 낸다. 목차가 먼저다
  requirements  요구 색인 표 — 라벨 ko·en, EARS 패턴(agt:pattern), refines/serves 하는 살아 있는 결정 수, 정제 도달 최저 수준
                (metrics 의 CQ19 와 같은 정의: refines/serves 하류의 가장 낮은 level), IRI. INTENT.md 의 손 목록을 대체하는 뷰다
  changelog     supersedes 쌍(새 → 옛)을 새 결정의 generated.at 순으로, prov:wasRevisionOf 가 있으면 함께
  audit         감사 보고서 (로드맵 8단계 "복원과 감사", 요구 audit-self-sufficiency) — 입력은 그래프 union 과 관측 청크 본문(kb/vv/run/ 의
                실행 기록 · kb/dev/memory/ 의 가정 판정)뿐이다. 체계 밖 정보 0. 절: 리비전·입력 / 검증 현황(요구의 검증 대응물 · verifies 대상
                결정 · 사슬 수 · 기준 없는 verifies) / 최근 실행(케이스별 pass·fail·skip 그대로) / 판정 주석(주석 수 · 라벨 분포 · 해소 열림 ·
                그중 게이트를 막는 issue (blocking); p7-commentary-form) / 가정(최신 assume_check 관측) / 추적 매트릭스
                (kb_lib.TIM_CELLS — metrics 와 같은 정의) / 검증 표시(verified 주체 종류 · 검증 뒤 수정) / 링크 근거(증거 종류 · 복원 비율) /
                자족성 선언. bodies 에 //kb/vv:bodies·//kb/dev:bodies 를 준다 (//kg:audit)
그래프는 query·metrics 와 같은 union 을 kb_lib.load_union 으로 올린다. 본문은 --bodies 의 청크 파일에서 frontmatter id 로 찾는다.
사용: weave.py --kind adr|requirements|changelog|audit --out <파일> [--root .] <그래프 ttl …> [--bodies <청크 .md …>]
종료: 0 생성됨 · 2 입력 문제(kind 밖·그래프 파일 없음·본문 파싱 불가) — 뷰라 판정 실패(1)는 없다. 결정 0건은 빈 절이지 실패가 아니다
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import EARS_PATTERNS, apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402 — frontmatter 파서와 값 어휘의 단일 정의처

AGT, ID = kb_lib.AGT, kb_lib.ID
PROV = Namespace("http://www.w3.org/ns/prov#")
EXIT_OK, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG
TAG = kb_lib.WEAVE_TAG
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]  # metrics.py 와 같은 순서 (CQ19 정의)
PATTERN_VALUE = {URIRef(str(AGT) + v.split(":")[1]): k for k, v in EARS_PATTERNS.items()}  # agt:eventDriven → event-driven


# ── 모델 — 그래프와 본문의 적재 ────────────────────

class Model:
    """head 그래프의 청크·복합체를 뷰가 쓰는 형태로 — plane·level·status·라벨·위치·시각, 복합체 ↔ 부분."""

    def __init__(self, g: Graph):
        self.g = g
        self.chunks = {s for s in g.subjects(AGT.tokenCount, None)}
        self.plane = {c: self._plane(c) for c in self.chunks}
        self.level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in self.chunks}
        self.status = {c: str(next(g.objects(c, AGT.status), "")) for c in self.chunks}
        self.location = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in self.chunks}
        self.comp_of: dict = {}
        self.parts: dict = defaultdict(list)
        for comp, part in g.subject_objects(AGT.hasDirectPart):
            self.comp_of[part] = comp
            self.parts[comp].append(part)

    def _plane(self, c) -> str:
        for t in self.g.objects(c, RDF.type):
            name = str(t).split("/")[-1]
            if name.endswith("Chunk"):
                return name[: -len("Chunk")].lower()
        return ""

    def ko(self, node) -> str:
        return kb_lib.label_of(self.g, node, "ko")

    def en(self, node) -> str:
        return kb_lib.label_of(self.g, node, "en")

    def at(self, c) -> str:
        return str(next(self.g.objects(c, PROV.generatedAtTime), ""))

    def live(self, c) -> bool:
        return c in self.chunks and self.status[c] != "deprecated"

    def decision_roles(self, comp) -> dict:
        """복합체의 부분을 결론·근거·대안 역할로 — 파일명이 역할이다 (STYLEGUIDE §4). 결정 복합체가 아니면 빈 dict."""
        roles = {}
        for p in self.parts.get(comp, ()):
            if self.plane.get(p) != "decision":
                return {}
            loc = self.location.get(p, "")
            for role, fname in kb_lib.DECISION_PART_FILES.items():
                if loc.endswith("/" + fname):
                    roles[role] = p
        return roles if "conclusion" in roles else {}

    def decision_composites(self) -> list:
        """(복합체, 역할→부분) — 결론 위치 순. 살아 있는 것과 deprecated 를 다 낸다. 호출자가 거른다."""
        out = []
        for comp in self.g.subjects(RDF.type, AGT.Composite):
            roles = self.decision_roles(comp)
            if roles:
                out.append((comp, roles))
        return sorted(out, key=lambda cr: self.location[cr[1]["conclusion"]])

    def decision_unit(self, c):
        """청크가 속한 결정 단위 — 복합체면 복합체, 아니면 청크 자신 (단일 파일 결정)."""
        return self.comp_of.get(c, c)

    def unit_label(self, unit) -> str:
        """결정 단위의 라벨 — 복합체면 결론 라벨, 청크면 자기 라벨."""
        roles = self.decision_roles(unit) if unit not in self.chunks else {}
        return self.ko(roles["conclusion"]) if roles else self.ko(unit)

    def unit_ref(self, unit) -> str:
        """결정 단위의 자리 — 디렉토리(복합체) 또는 파일 stem."""
        roles = self.decision_roles(unit) if unit not in self.chunks else {}
        loc = self.location[roles["conclusion"]] if roles else self.location.get(unit, "")
        return Path(loc).parent.name if roles else Path(loc).stem


def load_bodies(paths: list[str]) -> dict:
    """청크 파일들 → {IRI: 본문} — frontmatter 는 chunk2kg 의 파서로 읽고 본문은 그 아래 전부."""
    out = {}
    for p in paths:
        if not p.endswith(".md"):
            continue
        meta, _ = parse_chunk(p)
        out[meta["id"]] = kb_lib.chunk_body(Path(p).read_text(encoding="utf-8"))
    return out


# 자기 자신을 다시 만드는 명령 (G6) — kind 마다 하나다
REPRODUCE = {"adr": "bazel build //kb/dev:adr", "requirements": "bazel build //kb/dev:requirements",
             "changelog": "bazel build //kb/dev:changelog", "audit": "bazel build //kg:audit"}


def head(kind: str, title: str, query: str, g: Graph, inputs: list[str], extra: list[str]) -> list[str]:
    """모든 생성물의 머리 블록 — 규약 G1~G7 (kb_lib.gendoc_header 가 단일 정의처, p12-documents-are-generated)."""
    return kb_lib.gendoc_header(kind, title, "tools/weave.py", query, REPRODUCE[kind], inputs,
                                f"트리플 {len(g)} ({kb_lib.gendoc_union(inputs)})", kb_lib.gendoc_view_notice("청크"), extra=extra)


def refs(m: Model, nodes) -> str:
    return " · ".join(f"{m.ko(n)} (`{kb_lib.compact_iri(str(n))}`)" for n in nodes) or "없음"


SKOS_NOTATION = URIRef("http://www.w3.org/2004/02/skos/core#notation")  # 현상의 질문지 표기(P1~P22)
RISK_MARK_DECLARED = "선언"   # frontmatter `exposes` — 저자가 적은 표지
RISK_MARK_EXTRACTED = "인용"  # 본문의 현상 IRI — extract_refs 가 뽑은 표지
COMPOSITES_HEADING = "결정 복합체"  # 결론·근거·대안이 세 파일로 갈린 결정 — 단일 파일 결정과 동격이므로 같은 깊이에 둔다
SINGLES_HEADING = "단일 파일 결정 (v1·harness 유래)"  # chunks/decision/d-*.md — 결론·근거·대안이 한 본문 안에 있다


anchors_of = kb_lib.heading_anchors  # GitHub 제목 앵커 규칙의 단일 정의처는 kb_lib (목차 링크, STYLEGUIDE §7)


# ── ADR — 결정 기록 ────────────────────

def decision_section(m: Model, bodies: dict, root: Path, level: str, title: str, ref: str, parts: list, levels_note: str, comp_line: str) -> list[str]:
    """결정 하나의 절 — 복합체(세 부분)와 단일 파일(부분 하나)이 같은 형식이다. 본문은 --bodies 에서, 없으면 --root 아래 assertionLocation 에서 읽는다."""
    con = parts[0]
    refines = sorted({t for p in parts for t in m.g.objects(p, AGT.refines)} | {t for p in parts for t in m.g.objects(p, AGT.serves)}, key=str)
    sources = sorted({t for p in parts for t in m.g.objects(p, PROV.wasDerivedFrom)}, key=str)
    assumes = sorted({t for p in parts for t in m.g.objects(p, AGT.assumes)}, key=str)
    o = [f"{level} {title}", "",
         f"- 영문: {m.en(con)} {kb_lib.GENDOC_QUOTE_LINE}",  # 라벨은 그래프에서 그대로 가져온 값이다 — 생성기가 고쳐 쓰지 않는다
         f"- 결정: `{ref}`{comp_line} · 상태 `{m.status[con]}` · 수준 {m.level[con]}{levels_note}",
         f"- 생성: {m.at(con)} ({next(m.g.objects(con, AGT.generatedBy), '')})",
         f"- 정제하는 요구: {refs(m, refines)}",
         f"- 대체한 결정: {supersedes_chain(m, parts)}",
         "- 출처: " + (" · ".join(source_ref(m, s) for s in sources) or "없음"),
         f"- 가정: {refs(m, assumes)}", ""]
    for p in parts:
        body = bodies.get(str(p))
        if body is None:
            f = root / m.location[p]
            body = kb_lib.chunk_body(f.read_text(encoding="utf-8")) if f.is_file() else f"본문 {kb_lib.NONE_MARK} — `{m.location[p]}` 가 --bodies 에도 --root 아래에도 없다"
        o += kb_lib.gendoc_quote(body)
    return o


def render_adr(m: Model, bodies: dict, inputs: list[str], root: Path) -> str:
    comps = m.decision_composites()
    live = [(c, r) for c, r in comps if m.status[r["conclusion"]] != "deprecated"]
    deprecated_n = len(comps) - len(live)
    decision_comps = {c for c, _ in comps}  # 손으로 쓴 복합체(composite-kg)의 부분인 옛 단일 파일 결정은 결정 복합체가 아니다
    singles_all = sorted((c for c in m.chunks if m.plane[c] == "decision" and m.comp_of.get(c) not in decision_comps), key=lambda c: m.location[c])
    singles = [c for c in singles_all if m.live(c)]
    o = head("adr", "결정 기록", "살아 있는 결정 전부 — 결정 복합체(`agt:Composite` 의 부분이 conclusion·rationale·alternatives 청크, 결론의 status ≠ deprecated)마다 "
             "결론 라벨 · 상태 · 수준 · 세 본문, 그 뒤 결정 복합체에 속하지 않는 살아 있는 `agt:DecisionChunk`(단일 파일)마다 라벨 · 상태 · 수준 · 본문. "
             "둘 다 `agt:refines`/`agt:serves` 대상 · `agt:supersedes` 연쇄 · `prov:wasDerivedFrom` · `agt:assumes` 를 낸다", m.g, inputs,
             [f"- 결정 복합체 {len(live)} (deprecated {deprecated_n} 제외) · 단일 파일 결정 {len(singles)} (v1·harness 유래 `chunks/decision/`, deprecated {len(singles_all) - len(singles)} 제외)"])
    titles_c = [m.ko(r["conclusion"]) for _, r in live]
    titles_s = [m.ko(c) for c in singles]
    # 결정은 복합체든 단일 파일이든 동격이므로 같은 깊이(h3)에 두고, 두 무리를 h2 로 묶는다 (G8 — 제목 계층은 한 단계씩)
    anchors = anchors_of(["목차", COMPOSITES_HEADING] + titles_c + [SINGLES_HEADING] + titles_s)
    a_comp, a_single = anchors[1], anchors[2 + len(live)]
    a_c, a_s = anchors[2:2 + len(live)], anchors[3 + len(live):]
    body = ["## 목차", "", f"- [{COMPOSITES_HEADING}](#{a_comp})"]
    for (c, _), title, a in zip(live, titles_c, a_c):
        body.append(f"  - [{title}](#{a}) — `{m.unit_ref(c)}`")
    body.append(f"- [{SINGLES_HEADING}](#{a_single})")
    for c, title, a in zip(singles, titles_s, a_s):
        body.append(f"  - [{title}](#{a}) — `{m.unit_ref(c)}`")
    body += ["", f"## {COMPOSITES_HEADING}", "",
             f"결론·근거·대안이 세 파일로 갈린 결정 {len(live)}건이다. 절 하나가 결정 하나이고 세 본문을 그대로 싣는다.", ""]
    for (comp, r), title in zip(live, titles_c):
        parts = [r[k] for k in ("conclusion", "rationale", "alternatives") if k in r]
        levels = " (" + " · ".join(f"{k} {m.level[r[k]]}" for k in ("rationale", "alternatives") if k in r) + ")"
        body += decision_section(m, bodies, root, "###", title, m.unit_ref(comp), parts, levels, f" · 복합체 `{kb_lib.compact_iri(str(comp))}`")
    body += [f"## {SINGLES_HEADING}", "",
             f"결론·근거·대안이 한 본문 안에 있는 옛 형식의 결정 {len(singles)}건이다. 손으로 쓴 복합체(`kg/composite-kg.ttl`)에 속한 것은 그 복합체를 적는다.", ""]
    for c, title in zip(singles, titles_s):
        comp = m.comp_of.get(c)
        comp_line = f" · 복합체 {m.ko(comp)} (`{kb_lib.compact_iri(str(comp))}`)" if comp is not None else ""
        body += decision_section(m, bodies, root, "###", title, m.unit_ref(c), [c], "", comp_line)
    return kb_lib.gendoc_assemble(o, body, inputs)


def supersedes_chain(m: Model, parts) -> str:
    """대체 연쇄 — 부분들이 supersedes 하는 옛 결정과 그 옛 결정이 다시 supersedes 하는 것 (순환은 끊는다)."""
    firsts = sorted({t for p in parts for t in m.g.objects(p, AGT.supersedes)}, key=str)
    if not firsts:
        return "없음"
    chains = []
    for first in firsts:
        chain, cur, seen = [], first, set()
        while cur is not None and cur not in seen:
            seen.add(cur)
            chain.append(f"{m.ko(cur)} (`{kb_lib.compact_iri(str(cur))}`, {m.status.get(cur, '?')})")
            nxt = sorted(m.g.objects(cur, AGT.supersedes), key=str)
            cur = nxt[0] if nxt else None
        chains.append(" ← ".join(chain))
    return " · ".join(chains)


def source_ref(m: Model, s) -> str:
    loc = next(m.g.objects(s, PROV.atLocation), None)
    return f"{m.ko(s)} (`{kb_lib.compact_iri(str(s))}`" + (f", `{loc}`)" if loc else ")")


# ── 요구 색인과 변경 이력 ────────────────────

def render_requirements(m: Model, inputs: list[str]) -> str:
    reqs = sorted((c for c in m.chunks if m.plane[c] == "requirement" and m.live(c)), key=lambda c: m.location[c])
    down = defaultdict(set)  # metrics.py CQ19 와 같은 정의 — refines/serves 를 거꾸로 내려간다
    for pred in (AGT.refines, AGT.serves):
        for s, t in m.g.subject_objects(pred):
            down[t].add(s)

    def deepest(r) -> str:
        seen, stack, best = set(), [r], -1
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            if x in m.level and m.level[x] in LEVELS:
                best = max(best, LEVELS.index(m.level[x]))
            stack.extend(down.get(x, ()))
        return LEVELS[best] if best >= 0 else "none"

    def refining_decisions(r) -> int:
        units = set()
        for s in down.get(r, ()):
            if m.plane.get(s) == "decision":
                unit = m.decision_unit(s)
                roles = m.decision_roles(unit) if unit not in m.chunks else {}
                alive = m.status[roles["conclusion"]] != "deprecated" if roles else m.live(s)
                if alive:
                    units.add(unit)
        return len(units)

    rows, patterns, reach = [], Counter(), Counter()
    for r in reqs:
        pat = next(m.g.objects(r, AGT.pattern), None)
        pat_s = PATTERN_VALUE.get(pat, str(pat).split("/")[-1]) if pat is not None else kb_lib.NONE_MARK
        d, n = deepest(r), refining_decisions(r)
        patterns[pat_s] += 1
        reach[d] += 1
        rows.append(f"| `{Path(m.location[r]).stem}` | {m.ko(r)} | {m.en(r)} | {pat_s} | {n} | {d} | `{kb_lib.compact_iri(str(r))}` |")
    o = head("requirements", "요구 색인", "살아 있는 `agt:RequirementChunk` 마다 라벨 ko·en · `agt:pattern` · 이 요구를 `agt:refines`/`agt:serves` 하는 살아 있는 결정 단위 수 "
             "· `refines`/`serves` 하류의 가장 낮은 level (metrics CQ19 와 같은 정의) · IRI", m.g, inputs,
             [f"- 요구 {len(reqs)} · EARS 패턴: " + (" · ".join(f"{k} {v}" for k, v in patterns.most_common()) or "없음")
              + " · 도달 수준: " + " · ".join(f"{k} {v}" for k, v in sorted(reach.items(), key=lambda kv: LEVELS.index(kv[0]) if kv[0] in LEVELS else 99))
              + f" · 정제 결정 없는 요구 {sum(1 for row in rows if '| 0 |' in row)}"])
    body = ["| 파일 | 요구 | title | EARS | 정제 결정 | 도달 수준 | IRI |", "|---|---|---|---|---|---|---|"] + rows + [""]
    return kb_lib.gendoc_assemble(o, body, inputs)


def render_changelog(m: Model, inputs: list[str]) -> str:
    pairs = []
    for new, old in m.g.subject_objects(AGT.supersedes):
        at = m.at(new)
        try:
            key = datetime.fromisoformat(at)
        except ValueError:
            key = datetime.max
        if key.tzinfo is None:  # 시간대 없는 값은 UTC 로 본다 — 정렬 키의 비교 가능성만 위한 것
            key = key.replace(tzinfo=timezone.utc)
        pairs.append((key, m.ko(new), new, old, at))
    pairs.sort(key=lambda p: (p[0], p[1], str(p[2]), str(p[3])))
    revisions = sorted(m.g.subject_objects(PROV.wasRevisionOf), key=lambda so: (str(so[0]), str(so[1])))
    o = head("changelog", "변경 이력", "`agt:supersedes` 쌍(새 → 옛)을 새 결정의 `prov:generatedAtTime` 순으로 · `prov:wasRevisionOf` 쌍 전부", m.g, inputs,
             [f"- supersedes {len(pairs)}쌍 · wasRevisionOf {len(revisions)}쌍"])
    body = ["## supersedes — 새 결정이 옛 결정을 대체한 순서", "",
          "| 시각 (새 결정 generated.at) | 새 결정 | 자리 | 옛 결정 | 옛 상태 |", "|---|---|---|---|---|"]
    for _, label, new, old, at in pairs:
        body.append(f"| {at} | {label} | `{m.unit_ref(m.decision_unit(new))}` | {m.ko(old)} (`{kb_lib.compact_iri(str(old))}`) | `{m.status.get(old, '?')}` |")
    body += ["", "## wasRevisionOf — 같은 정체성의 개정", ""]
    if revisions:
        body += ["| 개정 | 이전 |", "|---|---|"] + [f"| {m.ko(s)} (`{kb_lib.compact_iri(str(s))}`) | {m.ko(t)} (`{kb_lib.compact_iri(str(t))}`) |" for s, t in revisions] + [""]
    else:
        body += [f"{kb_lib.NONE_MARK} — 개정은 아직 `supersedes`(새 IRI)로만 기록됐다", ""]
    return kb_lib.gendoc_assemble(o, body, inputs)


# ══ audit — 감사 보고서 (로드맵 8단계, audit-self-sufficiency: 체계 밖 정보 없이 생성) ════════════════════
# 절 셋이다 — 재료(관측 본문의 표를 읽는 헬퍼) · 절마다 함수 하나(보고의 절) · 조립(머리 블록과 이음).
# 장으로 묶은 까닭은 절 하나의 직접 부분이 9를 넘었기 때문이고, 순서에 뜻이 없는 묶음을 만들지 않았다
# (p7-code-links-on-file-composite).

# ── 재료 — 관측 본문의 표와 시각을 읽는다 ────────────────────
RUN_REVISION = re.compile(r"리비전 `([^`]+)`(?: \(([^)]*)\))?")  # 실행 기록 본문의 리비전 표기 (vv_run.observation)
TABLE_RULE = re.compile(r":?-+:?")


def observation_table(body: str, header: str) -> list[list[str]]:
    """관측 본문에서 헤더 줄이 `header` 인 표의 데이터 행(셀 목록). 표가 없으면 빈 목록 — 관측 형식은 도구(vv_run·assume_check)가 정한다."""
    rows, inside = [], False
    for ln in body.splitlines():
        s_ = ln.strip()
        if not inside:
            inside = s_ == header
            continue
        if not s_.startswith("|"):
            break
        cells = [c.strip() for c in s_.strip("|").split("|")]
        if not all(TABLE_RULE.fullmatch(c) for c in cells):
            rows.append(cells)
    return rows


def as_dt(value: str):
    """ISO 8601 → aware datetime (시간대 없는 값은 UTC 로 본다). 파싱 불가면 None."""
    try:
        d = datetime.fromisoformat(value)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def round_section(days: Counter, judged: int) -> list[str]:
    """라운드(날짜)별 신규 주석 절 — 표와 계열 한 줄. 정지 규칙(V&V 기준 `verification-round-stop-rule`)의 입력이다.

    라운드 경계는 판정 주석의 `prov:generatedAtTime` 날짜다. 판정 결과 주석(`generated.by` 가 `process:judge`)은
    리뷰가 찾은 결함이 아니라 판정자의 응답 기록이라 집계에서 빠지고, 뺀 수는 `judged` 로 받아 절에 적는다.
    연속한 두 라운드의 신규 수가 줄지 않으면 다음 라운드를 열지 않는 것이 정지 규칙의 합격이다.
    """
    rows, prev = [], None
    for day in sorted(days):
        n = days[day]
        rows.append(f"| {day} | {n} | " + (kb_lib.NONE_MARK if prev is None else "줄지 않음 — 다음 라운드를 열지 않는다" if n >= prev else "줄었다") + " |")
        prev = n
    series = " · ".join(str(days[d]) for d in sorted(days)) or kb_lib.NONE_MARK
    return ["| 라운드(날짜) | 신규 주석 | 직전 라운드 대비 |", "|---|---|---|"] \
        + (rows or ["| " + " | ".join([kb_lib.NONE_MARK] * 3) + " |"]) \
        + ["", f"- 라운드 {len(days)} · 신규 계열 {series} · 집계에서 뺀 판정 결과 주석(`{kb_lib.JUDGE_GENERATOR}`) {judged}", ""]


# ── 절마다 함수 하나 — 각 함수가 자기 절의 본문 조각을 낸다 ────────────────────
# 가른 기준은 **무엇을 읽는가**다 — 실행·가정 절은 관측 본문을, 나머지는 그래프를 센다.

def _audit_verification(m: Model, g, dev: set, vv: set, pct) -> list[str]:
    """요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria)."""
    body: list[str] = []
    # 2. 검증 현황
    dev_reqs = {c for c in dev if m.plane[c] == "requirement"}
    goals = {c for c in vv if m.plane[c] == "requirement"}
    covered = {t for s, t in g.subject_objects(AGT.derivesFrom) if s in goals and t in dev_reqs}
    criteria_of = defaultdict(set)
    cases_of = defaultdict(set)
    verifiers_of = defaultdict(set)
    for s, t in g.subject_objects(AGT.refines):
        if s in vv and t in vv:
            if m.plane[s] == "contract" and t in goals:
                criteria_of[t].add(s)
            elif m.plane[s] == "schema" and m.plane[t] == "contract":
                cases_of[t].add(s)
            elif m.plane[s] == "artifact" and m.plane[t] == "schema":
                verifiers_of[t].add(s)
    chains = [gl for gl in goals if any(cases_of[cr] for cr in criteria_of[gl])]
    verifies = [(s, t) for s, t in g.subject_objects(AGT.verifies) if s in vv]
    no_criteria = [s for s, _ in verifies if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    units = {m.decision_unit(c) for c in dev if m.plane[c] == "decision"}
    verified_units = {m.decision_unit(t) for _, t in verifies if t in m.chunks and m.plane.get(t) == "decision"}
    body += ["## 검증 현황 — 요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria)", "",
          f"- 검증 대응물이 있는 요구(검증 목표가 `agt:derivesFrom` 으로 가리킴): **{pct(len(covered), len(dev_reqs))}** (목표 100.0%)",
          f"- `agt:verifies` 대상이 된 결정 단위: **{pct(len(verified_units), len(units))}** · verifies 링크 {len(verifies)}",
          f"- 사슬: 검증 목표 {len(goals)} · 합격 기준이 달린 목표 {sum(1 for gl in goals if criteria_of[gl])} · 케이스까지 이어진 목표 {len(chains)} · "
          f"검증기 {sum(len(v) for v in verifiers_of.values())} (합격 기준 {sum(len(v) for v in criteria_of.values())} · 케이스 {sum(len(v) for v in cases_of.values())})",
          f"- 기준 없는 `verifies`: **{len(no_criteria)}** (목표 0 — verify 질의 `verifies-without-criteria` 와 같은 정의)", ""]
    uncovered = sorted(dev_reqs - covered, key=lambda c: m.location[c])
    if uncovered:
        body += [f"검증 대응물 없는 요구 {len(uncovered)}건:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)}" for c in uncovered] + [""]
    return body


def _audit_risk_goals(m: Model, g, vv: set, pct) -> list[str]:
    """검증 목표가 노출하는 결함 요인 — 표지는 선언(`exposes`)과 추출(본문의 현상 IRI) 둘이다 (8.21절 G1·G5)."""
    body: list[str] = []
    goals = {c for c in vv if m.plane[c] == "requirement"}  # 검증 목표 — 2절과 같은 정의다
    # 2.5 위험에서 파생된 목표 — 검증 목표가 defect 요인(현상)을 가리키는가 (위험 분석 G1·G5, 노트 8.21·8.22절)
    # 파생의 표지는 둘이다. frontmatter `exposes`(agt:exposesFactor)는 저자가 선언한 것이고 본문의 현상 IRI 인용
    # (agt:usesConcept, extract_refs)은 추출된 것이다. 둘 다 있으면 선언을 적는다 — 선언이 더 검사 가능한 근거다.
    factor_classes = set(g.transitive_subjects(RDFS.subClassOf, AGT.DefectFactor))
    factors = {i for cl in factor_classes for i in g.subjects(RDF.type, cl)}
    exposed: dict = defaultdict(dict)
    for pred, mark in ((AGT.exposesFactor, RISK_MARK_DECLARED), (AGT.usesConcept, RISK_MARK_EXTRACTED)):
        for s, o in g.subject_objects(pred):
            if s in goals and o in factors:
                exposed[s].setdefault(o, mark)
    named = {f for fs in exposed.values() for f in fs}
    body += [f"## 위험에서 파생된 목표 — 검증 목표가 노출하는 결함 요인 (표지 둘 — {RISK_MARK_DECLARED}: `exposes` · {RISK_MARK_EXTRACTED}: 본문의 현상 IRI, 8.21절 G1·G5)", "",
             f"- 위험에서 파생된 검증 목표: **{pct(len(exposed), len(goals))}** — 나머지는 게이트·음성 시험을 사슬로 묶은 것이다",
             f"- 어느 목표에도 가리켜지지 않은 현상: **{pct(len(factors) - len(named), len(factors))}**", ""]
    if not exposed:
        body += [f"위험에서 파생된 검증 목표 {kb_lib.NONE_MARK} — 현상을 가리키는 목표가 없다. `exposes:` 또는 본문의 현상 IRI 인용이 표지다.", ""]
    else:
        body += ["| 검증 목표 | 노출하는 현상 | 표기 | 표지 |", "|---|---|---|---|"]
        for c in sorted(exposed, key=lambda c: m.location[c]):
            for f in sorted(exposed[c], key=lambda f: str(f)):
                note = str(next(g.objects(f, SKOS_NOTATION), "")) or kb_lib.NONE_MARK
                body += [f"| `{Path(m.location[c]).stem}` {m.ko(c)} | {m.ko(f)} (`{kb_lib.compact_iri(str(f))}`) | {note} | {exposed[c][f]} |"]
        body += [""]
    return body


def _audit_latest_run(m: Model, runs: list, latest_run, run_body: str, by_gen) -> list[str]:
    """`kb/vv/run/` 의 최신 실행 기록 요약 — 기록을 그대로 옮긴다 (agt:Run, append-only)."""
    body: list[str] = []
    # 3. 최근 실행 — 실행 기록을 그대로 요약한다
    body += ["## 최근 실행 — `kb/vv/run/` 의 최신 실행 기록 (agt:Run, append-only)", ""]
    if latest_run is None:
        body += ["실행 기록 없음 — `bazel run //tools:vv_run -- --record`", ""]
    else:
        rows = observation_table(run_body, kb_lib.RUN_CASE_TABLE_HEADER)
        verdicts = Counter(r[2] for r in rows if len(r) >= 3)
        body += [f"- {m.ko(latest_run)} (`{m.location[latest_run]}`, 생성 {m.at(latest_run)}, {by_gen(latest_run)}) — 실행 기록 전체 {len(runs)}건",
              "- 케이스 " + " · ".join(f"{v} **{verdicts.get(v, 0)}**" for v in kb_lib.RUN_VERDICTS) + " — SKIP 은 PASS 가 아니다", ""]
        first = run_body.split("\n", 1)[0].strip()
        if first:
            body += [f"> {first}", ""]
        if rows:
            body += [kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"] + ["| " + " | ".join(r) + " |" for r in rows] + [""]
        else:
            body += [f"- 본문에 케이스 표(헤더 `{kb_lib.RUN_CASE_TABLE_HEADER}`)가 없다", ""]
    return body


def _audit_comments(m: Model, g, live: set, pct, by_gen) -> list[str]:
    """판정 주석의 라벨 분포와 해소 상태 (p7-commentary-form — 막는 것은 issue (blocking) + 해소 열림 뿐이다)."""
    body: list[str] = []
    # 4. 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form: issue (blocking) + 해소 열림 만 게이트를 막는다)
    label_of = lambda c: str(next(g.objects(c, AGT.commentLabel), ""))        # noqa: E731
    deco_of = lambda c: str(next(g.objects(c, AGT.commentDecoration), ""))    # noqa: E731
    state_of = lambda c: str(next(g.objects(c, AGT.resolutionState), ""))     # noqa: E731
    comments = sorted((c for c in live if m.plane[c] == "annotation"), key=lambda c: m.location[c])
    open_ = [c for c in comments if state_of(c) == kb_lib.COMMENT_OPEN]
    blocking = [c for c in open_ if (label_of(c), deco_of(c)) == kb_lib.COMMENT_BLOCKING]
    body += ["## 판정 주석 — 주석의 라벨 분포와 해소 상태 (p7-commentary-form)", ""]
    if not comments:
        body += [f"살아 있는 주석 {kb_lib.NONE_MARK} — 판정 주석(`{kb_lib.KB_VV}/verdict/`)이 비어 있다. 게이트 "
                 f"`{kb_lib.BLOCKING_COMMENT_GATE}` 는 서 있고 막을 주석이 아직 없다.", ""]
    else:
        labels = Counter(label_of(c) or kb_lib.NONE_MARK for c in comments)
        states = Counter(state_of(c) or kb_lib.NONE_MARK for c in comments)
        body += [f"- 살아 있는 주석 **{len(comments)}** · 해소되지 않은 것(`해소: {kb_lib.COMMENT_OPEN}`) **{pct(len(open_), len(comments))}** · "
                 f"그중 게이트를 막는 `{kb_lib.COMMENT_BLOCKING[0]} ({kb_lib.COMMENT_BLOCKING[1]})` **{len(blocking)}** "
                 f"(목표 0 — 게이트 `{kb_lib.BLOCKING_COMMENT_GATE}`)", "",
                 "| 라벨 | 주석 수 | 그중 해소 열림 |", "|---|---|---|"]
        body += [f"| `{k}` | {v} | {sum(1 for c in open_ if (label_of(c) or kb_lib.NONE_MARK) == k)} |" for k, v in labels.most_common()]
        body += ["", "| 해소 상태 | 주석 수 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in states.most_common()] + [""]
        judged = {c for c in comments if by_gen(c) == kb_lib.JUDGE_GENERATOR}
        body += round_section(Counter(m.at(c)[:10] for c in comments if c not in judged), len(judged))
        if blocking:
            body += ["게이트를 막는 주석:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)} → "
                     + (" · ".join(m.ko(t) for t in g.objects(c, AGT.targets)) or kb_lib.NONE_MARK) for c in blocking] + [""]
    return body


def _audit_assumptions(m: Model, asm_obs: list, latest_asm, asm_body: str) -> list[str]:
    """`kb/dev/memory/` 의 최신 가정 판정 관측 요약 (assume_check)."""
    body: list[str] = []
    # 5. 가정 — 최신 assume_check 관측
    body += ["## 가정 — `kb/dev/memory/` 의 최신 가정 판정 관측 (assume_check)", ""]
    if latest_asm is None:
        body += ["가정 판정 관측 없음 — `bazel run //tools:assume_check -- --record`", ""]
    else:
        rows = observation_table(asm_body, kb_lib.ASSUME_CHECK_TABLE_HEADER)
        states = Counter(r[3] for r in rows if len(r) >= 4)
        body += [f"- {m.ko(latest_asm)} (`{m.location[latest_asm]}`, 생성 {m.at(latest_asm)}) — 가정 판정 관측 전체 {len(asm_obs)}건",
              "- 가정 " + (" · ".join(f"{k} **{v}**" for k, v in sorted(states.items())) or kb_lib.NONE_MARK + " — 본문에 가정 표가 없다"), ""]
        if rows:
            body += ["| 가정 | 판정 유형 | 등급 | 상태 |", "|---|---|---|---|"] + ["| " + " | ".join(r[:4]) + " |" for r in rows] + [""]
    return body


def _audit_matrix(g) -> list[str]:
    """추적 매트릭스 — plane × plane 의 TIM 허용 칸과 채움. metrics 3단계 대리와 같은 정의다."""
    body: list[str] = []
    # 6. 추적 매트릭스 — metrics 와 같은 정의 (kb_lib.TIM_CELLS · link_cells)
    seen = kb_lib.link_cells(g)
    filled = [c for c in kb_lib.TIM_CELLS if c in seen]
    outside = sorted(seen - set(kb_lib.TIM_CELLS))
    body += [f"## 추적 매트릭스 — plane × plane, TIM 허용 {len(kb_lib.TIM_CELLS)}칸 중 채움 **{len(filled)}** (metrics 3단계 대리와 같은 정의)", "",
          "| 링크 | 출발 plane | 도착 plane | 채움 |", "|---|---|---|---|"]
    body += [f"| `{k}` | `{a}` | `{b}` | {'채움' if (k, a, b) in seen else '빈 칸'} |" for k, a, b in kb_lib.TIM_CELLS]
    body += ["", f"- 허용표 밖에서 관측된 칸: {len(outside)}" + (" — " + ", ".join(f"`{k}`:{a}→{b}" for k, a, b in outside) if outside else ""), ""]
    return body


def _audit_verified(m: Model, g, live: set) -> list[str]:
    """`verified` 주체 종류별 청크 수와 검증 뒤 수정 (agt:TrustShape 가 게이트에서 강제하는 것)."""
    body: list[str] = []
    # 7. 검증 표시 — verified 주체 종류와 검증 뒤 수정 (trust shape)
    kinds = Counter()
    none_n, modified = 0, []
    for c in live:
        vbs = [str(v) for v in g.objects(c, AGT.verifiedBy)]
        if not vbs:
            none_n += 1
        for kind in {("human:" if v.startswith("human:") else "process:" if v.startswith("process:") else v.split("/")[0] + "/" if "/" in v else "기타") for v in vbs}:
            kinds[kind] += 1
        gen_at = as_dt(m.at(c))
        for v in g.objects(c, AGT.verifiedAt):
            va = as_dt(str(v))
            if gen_at and va and gen_at > va:
                modified.append(c)
                break
    body += ["## 검증 표시 — `verified` 주체 종류별 살아 있는 청크 수 (한 청크가 여러 종류를 가질 수 있다)", "",
          "| 주체 종류 | 청크 수 |", "|---|---|"] + [f"| `{k}` | {v} |" for k, v in sorted(kinds.items())] + [f"| 없음 (미검증) | {none_n} |", "",
          f"- 검증 뒤 수정(`prov:generatedAtTime` > `agt:verifiedAt`): **{len(modified)}** (목표 0 — `agt:TrustShape` 가 게이트에서 강제)", ""]
    return body


def _audit_links(m: Model, g, pct) -> list[str]:
    """링크 개체의 증거 종류 분포와 복원 비율 (kb_lib.link_origins — 증거 종류가 구축·복원의 기준이다)."""
    body: list[str] = []
    # 8. 링크 근거 — 증거 종류 분포와 복원 비율 (metrics 와 같은 구축·복원 정의: kb_lib.link_origins — 증거 종류 기준)
    links = list(g.subjects(RDF.type, AGT.Link))
    ev_kinds = Counter()
    for l in links:
        for ev in g.objects(l, AGT.hasEvidence):
            ev_kinds[str(next(g.objects(ev, AGT.evidenceKind), "")).split("/")[-1] or "없음"] += 1
    origins = kb_lib.link_origins(g)
    built, restored, no_ev = origins["built"], origins["restored"], origins["no_evidence"]
    states = Counter(str(next(g.objects(l, AGT.linkState), "")) or "없음" for l in links)
    restored_rows = [f"  - {m.ko(next(g.objects(l, AGT.linkFrom), l))} —`{str(next(g.objects(l, AGT.linkKind), '')).split('/')[-1]}`→ "
                     f"{m.ko(next(g.objects(l, AGT.linkTo), l))}" for l in origins["restored_links"]]
    body += ["## 링크 근거 — 링크 개체의 증거 종류와 복원 비율", "",
          f"- 링크 개체 `agt:Link` **{len(links)}** · 증거 없는 링크 {no_ev} (목표 0) · 상태 " + (" · ".join(f"`{k}` {v}" for k, v in sorted(states.items())) or "없음"),
          "- 증거 종류: " + (" · ".join(f"`{k}` {v}" for k, v in ev_kinds.most_common()) or "없음"),
          f"- 확정 {origins['confirmed']} = 구축 {built}(구축 기록 증거뿐) + 복원 {restored}(구축 기록 아닌 증거 `proposal` 을 가진 링크 개체 — frontmatter `restored:` 표시, "
          f"p10-restored-link-marking) → 복원 비율 **{pct(restored, built + restored)}** (목표 20% 미만; 후보는 `//kg:link_candidates`)",
          f"- 후보 {origins['candidates']} (`agt:CandidateLink` — 본문 추출, 증거는 구축 기록; p10-extracted-references-are-candidates): "
          + (" · ".join(f"`{k}` {v}" for k, v in sorted(origins["candidate_kinds"].items())) or "없음")
          + " · 본문 식별자 추출 직접 트리플 " + " · ".join(f"`{k}` {v}" for k, v in origins["extracted"].items())] + restored_rows + [""]
    return body


# ── 조립 — 머리 블록을 세우고 절을 순서대로 잇는다 ────────────────────

def render_audit(m: Model, bodies: dict, inputs: list[str]) -> str:
    g = m.g
    live = {c for c in m.chunks if m.live(c)}
    vv = {c for c in live if kb_lib.kb_of(m.location[c]) == kb_lib.KB_VV}
    dev = live - vv
    by_gen = lambda c: str(next(g.objects(c, AGT.generatedBy), ""))  # noqa: E731
    obs_all = [c for c in m.chunks if m.plane[c] == "memory"]
    runs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.VV_RUN_DIR + "/") and by_gen(c) == kb_lib.RUN_GENERATOR),
                  key=lambda c: (m.at(c), m.location[c]))
    asm_obs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.DEV_MEMORY_DIR + "/") and by_gen(c) == kb_lib.ASSUME_CHECK_GENERATOR),
                     key=lambda c: (m.at(c), m.location[c]))
    latest_run, latest_asm = (runs[-1] if runs else None), (asm_obs[-1] if asm_obs else None)
    run_body = bodies.get(str(latest_run), "") if latest_run is not None else ""
    asm_body = bodies.get(str(latest_asm), "") if latest_asm is not None else ""

    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — metrics 와 같은 정의)

    # 1. 리비전 — 그래프는 리비전을 담지 않는다. 실행 기록이 초기 상태(p8-reproducibility)로 담는다
    rev_m = RUN_REVISION.search(run_body)
    rev_line = (f"실행 기록의 리비전 `{rev_m.group(1)}`" + (f" ({rev_m.group(2)})" if rev_m.group(2) else "") + f" — `{Path(m.location[latest_run]).name}`"
                if rev_m else "실행 기록이 없어 리비전을 알 수 없다 — 그래프는 리비전을 담지 않는다")
    h = head("audit", "감사 보고서", "그래프 union 과 관측 청크 본문(`kb/vv/run/` 실행 기록 · `kb/dev/memory/` 가정 판정)만으로 — 검증 현황 · 최근 실행 · "
             "판정 주석 · 가정 · 추적 매트릭스(`kb_lib.TIM_CELLS`) · 검증 표시 · 링크 근거 · 자족성", g, inputs,
             [f"- 리비전: {rev_line}",
              f"- 입력의 종류: 그래프 union(head · 참조 · 시드 · 카탈로그 · 복합체 · ODD · 온톨로지) · 관측 본문 — 실행 기록 {len(runs)}건 · 가정 판정 {len(asm_obs)}건. "
              f"체계 밖 정보 0 (요구 `audit-self-sufficiency`)",
              f"- 살아 있는 청크 {len(live)} — 개발 KB {len(dev)} · V&V KB {len(vv)}"])
    body: list[str] = []

    # 절마다 함수 하나다 — 각 함수가 자기 절의 본문 조각을 내고 여기서 순서대로 잇는다. 절의 순서가 보고의 순서다.
    body += _audit_verification(m, g, dev, vv, pct)
    body += _audit_risk_goals(m, g, vv, pct)
    body += _audit_latest_run(m, runs, latest_run, run_body, by_gen)
    body += _audit_comments(m, g, live, pct, by_gen)
    body += _audit_assumptions(m, asm_obs, latest_asm, asm_body)
    body += _audit_matrix(g)
    body += _audit_verified(m, g, live)
    body += _audit_links(m, g, pct)

    # 9. 자족성 선언
    body += ["## 자족성 선언", "",
          "이 보고서의 모든 수치는 위 입력(그래프 union · 실행 기록 · 가정 판정 관측)에서 나왔다. 손으로 적은 수치는 없다. "
          "이 보고서를 다시 만드는 명령은 `bazel build //kg:audit` 이고 입력이 같으면 수치가 같다.", ""]
    return kb_lib.gendoc_assemble(h, body, inputs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", required=True, choices=kb_lib.WEAVE_KINDS)
    ap.add_argument("--out", required=True)
    ap.add_argument("--root", default=os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    ap.add_argument("--bodies", nargs="*", default=[], metavar="MD", help="청크 파일들 — adr 의 결론·근거·대안 본문, audit 의 관측 본문")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — bodies 를 읽을 때만 쓴다"
                                                      "(load_bodies → parse_chunk). 안 주면 --root 기준 defs/kb.bzl 를 쓴다")
    ap.add_argument("ttl", nargs="*", help="그래프 파일들 (없으면 kb_lib.UNION_GRAPH_PATHS + 온톨로지 모듈)")
    a = ap.parse_args()
    root = Path(a.root)
    if a.bodies:  # load_bodies 가 parse_chunk 를 부르므로 그때만 값 어휘가 있어야 한다
        residency = a.residency or str(root / "defs" / "kb.bzl")
        try:
            apply_plane_level_state(*load_plane_level_state(residency))
        except (OSError, ValueError) as e:
            print(f"CONFIG [{TAG}] {residency}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
    try:
        g = kb_lib.load_union(a.ttl, root)
        bodies = load_bodies(a.bodies) if a.kind in ("adr", "audit") else {}
    except ValueError as e:
        print(f"CONFIG [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    except OSError as e:
        print(f"CONFIG [{TAG}] {getattr(e, 'filename', '')}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    m = Model(g)
    inputs = (a.ttl or list(kb_lib.UNION_GRAPH_PATHS)) + list(a.bodies)
    text = {"adr": lambda: render_adr(m, bodies, inputs, root),
            "requirements": lambda: render_requirements(m, inputs),
            "changelog": lambda: render_changelog(m, inputs),
            "audit": lambda: render_audit(m, bodies, inputs)}[a.kind]()
    Path(a.out).write_text(text, encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
