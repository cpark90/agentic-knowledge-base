#!/usr/bin/env python3
"""복원 후보 생성기 뷰 — frontmatter 링크가 없는 청크 쌍의 링크 후보를 체계 안 증거만으로 낸다 (로드맵 8단계 복원,
p10-link-by-construction · p10-candidate-and-confirmed-link · p10-link-judgement-evidence).

게이트가 아니라 **후보 생성기**다. 입력은 그래프 union 뿐이고(체계 밖 정보 0) 판정은 사람이 후보마다 한다 — 채택하면 앵커 청크의
frontmatter 에 링크 키와 `restored:` 를 적는다 (p10-restored-link-marking). 결과는 저장하지 않는다 (4.6절 뷰 원칙).
  단위  살아 있는 청크(status ≠ deprecated). 결정 복합체(conclusion·rationale·alternatives)는 한 단위이고 앵커는 결론이다 — 링크 키는
        결론에 적는다. 손으로 쓴 복합체(kg/composite-kg.ttl)의 부분은 각각 단위이되 형제끼리는 후보가 아니다
  근거  체계 안 증거만, 검사 가능성 순 (kb/ontology/related/trace/evidence-ontology.ttl):
        (a) 본문 식별자 — A 본문이 B 를 agt:cites 하는데 frontmatter 링크가 없다 → constructionRecord (본문 식별자는 구축 기록이다)
        (b) 테스트 공동 커버 — 같은 V&V 청크가 verifies 하는 두 개발 청크 → testCoverage
        (c) 개념 공유 — agt:usesConcept 교집합 ≥ --min-shared (기본 3) → proposal (도구 제안 — 확정 근거가 아니며 동률만 깬다)
        (d) 승계 — 조각 F 가 prov:specializationOf O 이면 O 를 가리키던 확정 링크(linkState confirmed, 종류는 LINK_KEYS) X→O 마다
            X→F 후보 → constructionRecord, 값 "승계: O" (p10-split-keeps-work-identity). 종류는 원 링크의 종류를 우선한다
        임베딩 유사도는 쓰지 않는다 (ODD 가 학습 임베딩을 명시 제외). 같은 세션 읽음은 하네스가 아직 기록하지 않는다
  종류  TIM 허용 칸(kb_lib.TIM_CELLS)에서 고른다 — 인용 방향(대칭 근거는 IRI 순)을 먼저, 다음 역방향, 칸이 없으면 overlapsWith
        (relatedTo 족의 약한 잎 — 관계는 있으나 이름이 아직 없는 자리, overlap-ontology). 그것은 링크 키라 채택이 복원 비율에 든다.
        supersedes 는 시간축이라 후보가 아니다. 한 칸에 종류가 여럿이면 refines > derivesFrom > satisfies > constrains > serves > verifies 순.
        승계 후보는 원 링크의 종류가 제약을 통과하면 그것을 쓴다
  제약  defs/kb.bzl _check_links 와 같은 규칙 — refines·serves 는 더 높은 수준으로·plane 순서 역행 금지·같은 KB, serves 대상은 요구,
        verifies 는 주어 kb/vv·대상 개발 KB·같은 수준. 자기 자신·deprecated·복합체 형제·이미 링크된 쌍·KB 를 가로지르는 overlapsWith 는 탈락
  상한  앵커(주어)당 k ≤ --k (기본 7, 로드맵 입력표) — 근거 강도 → 공유 개념 수 → 대상 라벨 순. 넘치는 것은 탈락으로 센다
사용: link.py --out link-candidates.md [--k 7] [--min-shared 3] <TTL...>   (bazel build //kg:link_candidates)
종료: 0 생성됨 · 2 입력 문제(그래프 파일 없음·파싱 불가) — 뷰라 판정 실패(1)는 없다. 후보 0건은 빈 표이지 실패가 아니다
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import LINK_KEYS, RESTORED_KEY  # noqa: E402 — frontmatter 링크 키의 단일 정의처

AGT, PROV = kb_lib.AGT, kb_lib.PROV
EXIT_OK, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG
TAG = kb_lib.LINK_TAG
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]  # defs/kb.bzl 와 같은 순서 (6.2절 정제 계층)
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory"]  # 5.2절 단방향 순서
RELATED_KEYS = ("coUpdatesWith", "conflictsWith", "relatedTo", "overlapsWith")  # relatedTo 족 — 이미 이어진 쌍을 가리는 데 쓴다
RELATED = "overlapsWith"  # 칸이 없을 때의 종류 — relatedTo 자신이 아니라 그 아래 약한 잎이다 (overlap-ontology)
# 증거 종류의 강도 — 검사 가능성 순 (evidence-ontology, p10-link-judgement-evidence). 작을수록 강하다
EVIDENCE_RANK = {"constructionRecord": 0, "testCoverage": 1, "proposal": 2}
# 한 TIM 칸에 종류가 여럿일 때의 우선순위 — 정제가 먼저, 다음 의미 의존, serves 는 refines 의 약한 형태, verifies 는 vnv 가 적는다
KIND_PREFERENCE = ("refines", "derivesFrom", "satisfies", "constrains", "serves", "verifies", "allocates", "generates")
# 탈락 사유 — 요약의 분포 열쇠
R_SELF, R_DEPRECATED, R_SIBLING, R_LINKED = "자기 자신(같은 단위)", "deprecated", "복합체 형제", "이미 링크됨"
R_DIRECTION, R_CROSS_KB, R_CAP = "TIM 칸은 있으나 단방향·수준 규칙 위반", "KB 가로지름 (overlapsWith 불가 — verifies 뿐)", "상한 k 초과"


# ── 단위와 매트릭스 제약 ────────────────────

class Units:
    """살아 있는 청크를 단위로 — 결정 복합체(결론 부분이 있는 것)는 결론이 대표하고, 나머지 청크는 자기 자신이 단위다."""

    def __init__(self, g):
        self.g = g
        self.plane = kb_lib.chunk_planes(g)
        self.chunks = set(self.plane)
        self.status = {c: str(next(g.objects(c, AGT.status), "")) for c in self.chunks}
        self.level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in self.chunks}
        self.loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in self.chunks}
        self.live = {c for c in self.chunks if self.status[c] != "deprecated"}
        self.comp_of: dict = {}
        parts = defaultdict(list)
        for comp, part in g.subject_objects(AGT.hasDirectPart):
            self.comp_of[part] = comp
            parts[comp].append(part)
        self.unit_of: dict = {}
        concl_name = "/" + kb_lib.DECISION_PART_FILES["conclusion"]
        for comp, ps in parts.items():
            concl = sorted((p for p in ps if self.loc.get(p, "").endswith(concl_name)), key=str)
            if concl and all(self.plane.get(p) == "decision" for p in ps):  # 결정 복합체 — 앵커는 결론 (STYLEGUIDE §4, weave 와 같은 규칙)
                for p in ps:
                    if p in self.chunks:
                        self.unit_of[p] = concl[0]
        for c in self.chunks:
            self.unit_of.setdefault(c, c)
        self.members = defaultdict(set)
        for c, u in self.unit_of.items():
            self.members[u].add(c)

    def alive(self, u) -> bool:
        return u in self.live

    def kb(self, u) -> str:
        return kb_lib.kb_of(self.loc.get(u, ""))

    def ko(self, u) -> str:
        return kb_lib.label_of(self.g, u, "ko")

    def sibling(self, a, b) -> bool:
        ca = self.comp_of.get(a)
        return ca is not None and ca == self.comp_of.get(b)

    def stem(self, c) -> str:
        return Path(self.loc.get(c, str(c))).stem


def tim_kinds(pa: str, pb: str) -> list:
    """(출발 plane, 도착 plane) 칸이 허용하는 링크 종류 — supersedes 제외, KIND_PREFERENCE 순."""
    kinds = {k for k, x, y in kb_lib.TIM_CELLS if x == pa and y == pb and k != "supersedes"}
    return sorted(kinds, key=lambda k: KIND_PREFERENCE.index(k) if k in KIND_PREFERENCE else len(KIND_PREFERENCE))


def violation(u: Units, kind: str, a, b) -> str | None:
    """defs/kb.bzl _check_links 의 구조 규칙 — 위반이면 사유, 아니면 None."""
    la = LEVELS.index(u.level[a]) if u.level[a] in LEVELS else -1
    lb = LEVELS.index(u.level[b]) if u.level[b] in LEVELS else -1
    if kind in ("refines", "serves"):
        if lb >= la:
            return "refines/serves 대상은 더 높은 수준이어야 한다 (6.2절)"
        if PLANES.index(u.plane[b]) > PLANES.index(u.plane[a]):
            return "plane 단방향 위반 (5.2절)"
        if u.kb(a) != u.kb(b):
            return "refines/serves 는 KB 안에서만이다 (7.5절)"
        if kind == "serves" and u.plane[b] != "requirement":
            return "serves 의 대상은 requirement 뿐이다 (6.8절)"
    elif kind == "verifies":
        if u.kb(a) != kb_lib.KB_VV:
            return "verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)"
        if u.kb(b) == kb_lib.KB_VV:
            return "verifies 의 대상은 개발 KB 청크다"
        if u.level[a] != u.level[b]:
            return "verifies 는 같은 수준끼리다 (8.3절)"
    return None


# ── 증거 수집과 보고 ────────────────────

def resolve(u: Units, key: frozenset, prefer: dict, hint: dict | None = None):
    """쌍 → (앵커, 종류, 대상) 또는 탈락 사유. 인용 방향(없으면 IRI 순)을 먼저, 다음 역방향, TIM 칸이 없으면 같은 KB 안에서 overlapsWith.

    hint(쌍 → 종류)는 승계 후보의 원 링크 종류다 — 인용 방향에서 제약을 통과하면 TIM 우선순위보다 먼저 쓴다.
    """
    a, b = prefer.get(key) or tuple(sorted(key, key=str))
    kind = (hint or {}).get(key)
    if kind and kind in tim_kinds(u.plane[a], u.plane[b]) and violation(u, kind, a, b) is None:
        return (a, kind, b)
    had_cell = False
    for x, y in ((a, b), (b, a)):
        for kind in tim_kinds(u.plane[x], u.plane[y]):
            had_cell = True
            if violation(u, kind, x, y) is None:
                return (x, kind, y)
    if had_cell:
        return R_DIRECTION
    if u.kb(a) != u.kb(b):
        return R_CROSS_KB
    return (a, RELATED, b)


def gather(u: Units, min_shared: int):
    """증거 수집 → (쌍 → 증거 목록 [(강도, 종류, 값, 정렬용 공유 수)], 쌍 → 인용 방향, 탈락 분포, 쌍 → 승계 종류)."""
    g = u.g
    dropped: Counter = Counter()
    evidence: dict = defaultdict(list)
    prefer: dict = {}
    hint: dict = {}

    def pair(s, o, kind: str, value: str, shared: int, directed: bool):
        us, uo = u.unit_of.get(s), u.unit_of.get(o)
        if us is None or uo is None:
            return
        if not (u.alive(us) and u.alive(uo)):
            dropped[R_DEPRECATED] += 1
            return
        if us == uo:
            dropped[R_SELF] += 1
            return
        if u.sibling(us, uo):
            dropped[R_SIBLING] += 1
            return
        key = frozenset((us, uo))
        evidence[key].append((EVIDENCE_RANK[kind], kind, value, shared))
        if directed:
            prefer.setdefault(key, (us, uo))

    # (a) 본문 식별자 — extract_refs 의 agt:cites (인용한 쪽이 앵커 후보)
    for s, o in sorted(g.subject_objects(AGT.cites), key=lambda so: (str(so[0]), str(so[1]))):
        pair(s, o, "constructionRecord", u.stem(o), 0, True)
    # (b) 테스트 공동 커버 — 같은 V&V 청크가 verifies 하는 두 개발 단위
    covers = defaultdict(set)
    for s, o in g.subject_objects(AGT.verifies):
        if s in u.live and o in u.unit_of:
            covers[s].add(u.unit_of[o])
    for s in sorted(covers, key=str):
        targets = sorted(covers[s], key=str)
        for i, a in enumerate(targets):
            for b in targets[i + 1:]:
                pair(a, b, "testCoverage", u.stem(s), 0, False)
    # (c) 개념 공유 — 단위별 agt:usesConcept 합집합의 교집합
    concepts = defaultdict(set)
    for s, o in g.subject_objects(AGT.usesConcept):
        if s in u.live:
            concepts[u.unit_of[s]].add(str(o).split("/")[-1])
    units = sorted(concepts, key=str)
    for i, a in enumerate(units):
        for b in units[i + 1:]:
            shared = sorted(concepts[a] & concepts[b])
            if len(shared) >= min_shared:
                pair(a, b, "proposal", f"{len(shared)} ({', '.join('agt:' + t for t in shared[:3])}{', …' if len(shared) > 3 else ''})", len(shared), False)
    # (d) 승계 — 조각 F 가 O 를 특수화하면 O 를 가리키던 확정 링크 X→O 마다 X→F (원 링크의 종류를 힌트로)
    for frag, orig in sorted(g.subject_objects(PROV.specializationOf), key=lambda so: (str(so[0]), str(so[1]))):
        if frag not in u.chunks or orig not in u.chunks:
            continue
        for link in sorted(g.subjects(AGT.linkTo, orig), key=str):
            if str(next(g.objects(link, AGT.linkState), "")) != kb_lib.LINK_STATE_CONFIRMED:
                continue
            kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
            if kind not in LINK_KEYS or kind == "supersedes":
                continue
            for x in sorted(g.objects(link, AGT.linkFrom), key=str):
                before = len(evidence.get(frozenset((u.unit_of.get(x), u.unit_of.get(frag))), []))
                pair(x, frag, "constructionRecord", f"승계: {u.stem(orig)}", 0, True)
                key = frozenset((u.unit_of.get(x), u.unit_of.get(frag)))
                if len(evidence.get(key, [])) > before:
                    hint.setdefault(key, kind)
    return evidence, prefer, dropped, hint


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--k", type=int, default=7, help="앵커(주어)당 후보 상한 (로드맵 입력표 k ≤ 7)")
    ap.add_argument("--min-shared", type=int, default=3, help="개념 공유 후보의 agt:usesConcept 교집합 하한")
    ap.add_argument("--root", default=".")
    ap.add_argument("files", nargs="*", help="그래프 파일들 (없으면 kb_lib.UNION_GRAPH_PATHS + 온톨로지 모듈)")
    a = ap.parse_args()
    if a.k < 1 or a.min_shared < 1:
        print(f"CONFIG [{TAG}] --k 와 --min-shared 는 1 이상이다 — 실제 k={a.k} min-shared={a.min_shared}", file=sys.stderr)
        return EXIT_CONFIG
    try:
        g = kb_lib.load_union(a.files, Path(a.root))
    except (ValueError, OSError, SyntaxError) as e:
        print(f"CONFIG [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    u = Units(g)

    # 이미 frontmatter 링크(직접 술어 LINK_KEYS + relatedTo 족)가 있는 쌍 — 단위 기준, 방향 무관
    linked = set()
    for key in LINK_KEYS + RELATED_KEYS:
        for s, o in g.subject_objects(AGT[key]):
            us, uo = u.unit_of.get(s), u.unit_of.get(o)
            if us is not None and uo is not None and us != uo:
                linked.add(frozenset((us, uo)))

    evidence, prefer, dropped, hint = gather(u, a.min_shared)
    by_anchor: dict = defaultdict(list)
    for key in sorted(evidence, key=lambda k: tuple(sorted(map(str, k)))):
        if key in linked:
            dropped[R_LINKED] += 1
            continue
        r = resolve(u, key, prefer, hint)
        if isinstance(r, str):
            dropped[r] += 1
            continue
        anchor, kind, target = r
        evs = sorted(evidence[key])
        by_anchor[anchor].append({"kind": kind, "target": target, "evs": evs, "rank": evs[0][0], "shared": max(e[3] for e in evs)})
    candidates = []
    for anchor in sorted(by_anchor, key=lambda x: (u.ko(x), str(x))):
        rows = sorted(by_anchor[anchor], key=lambda c: (c["rank"], -c["shared"], u.ko(c["target"]), str(c["target"])))
        dropped[R_CAP] += max(0, len(rows) - a.k)
        for c in rows[:a.k]:
            c["anchor"] = anchor
            candidates.append(c)

    kinds = Counter(e[1] for c in candidates for e in c["evs"])
    primary = Counter(c["evs"][0][1] for c in candidates)
    link_kinds = Counter(c["kind"] for c in candidates)
    ttl = [f for f in (a.files or list(kb_lib.UNION_GRAPH_PATHS)) if f.endswith(".ttl")]
    live_units = [x for x in u.members if u.alive(x)]
    head = kb_lib.gendoc_header(
        "link-candidates", "복원 후보 생성기 뷰", "tools/link.py",
        f"살아 있는 단위(결정 복합체는 결론이 앵커) 쌍 중 frontmatter 링크(`{'`·`'.join(LINK_KEYS)}` + relatedTo 족)가 없는 쌍에 대해 "
        f"(a) `agt:cites` → constructionRecord · (b) 같은 V&V 청크의 `agt:verifies` → testCoverage · (c) `agt:usesConcept` 교집합 ≥ {a.min_shared} → proposal · "
        f"(d) 조각 F 가 `prov:specializationOf` O 이면 O 를 가리키던 확정 링크 X→O 마다 X→F → constructionRecord(값 \"승계: O\"). "
        f"종류는 `kb_lib.TIM_CELLS` 허용 칸(인용 방향 → 역방향 → 칸이 없으면 `agt:overlapsWith`), 제약은 `defs/kb.bzl` `_check_links` 와 같다. 앵커당 k ≤ {a.k}",
        "bazel build //kg:link_candidates", ttl, f"트리플 {len(g)} ({kb_lib.gendoc_union(ttl)}) — 체계 밖 정보 0",
        kb_lib.gendoc_view_notice("앵커 청크의 frontmatter (`p10-candidate-and-confirmed-link` · `p10-restored-link-marking`)"),
        input_kind="그래프 파일",
        extra=[f"- 살아 있는 청크 {len(u.live)} · 단위 {len(live_units)} · 증거가 있는 쌍 {len(evidence)}",
               "- 판정은 사람이 후보마다 하고 확정은 앵커 청크의 frontmatter 에 적는다"])
    o = ["## 요약", "", "| 항목 | 값 |", "|---|---|",
         f"| 후보 수 | {len(candidates)} |",
         "| 근거 종류 분포 (첫 근거 기준) | " + (" · ".join(f"{k} {v}" for k, v in sorted(primary.items(), key=lambda kv: EVIDENCE_RANK[kv[0]])) or kb_lib.NONE_MARK) + " |",
         "| 근거 종류 분포 (모든 근거) | " + (" · ".join(f"{k} {v}" for k, v in sorted(kinds.items(), key=lambda kv: EVIDENCE_RANK[kv[0]])) or kb_lib.NONE_MARK) + " |",
         "| 링크 종류 분포 | " + (" · ".join(f"`{k}` {v}" for k, v in sorted(link_kinds.items())) or kb_lib.NONE_MARK) + " |",
         f"| 앵커 수 | {len(by_anchor)} |",
         f"| 탈락 수 | {sum(dropped.values())} — " + (" · ".join(f"{k} {v}" for k, v in sorted(dropped.items(), key=lambda kv: (-kv[1], kv[0]))) or kb_lib.NONE_MARK) + " |", "",
         "## 후보", "",
         "| # | 앵커 (ko) | 앵커 파일 | 링크 종류 | 대상 (ko) | 대상 IRI | 근거 종류 | 근거 값 (인용 식별자 / 케이스 슬러그 / 공유 개념 수 / 승계: 원본) | 판정 (채택 / 기각) |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(candidates, 1):
        o.append(f"| {i} | {cell(u.ko(c['anchor']))} | `{u.loc.get(c['anchor'], '')}` | `{c['kind']}` | {cell(u.ko(c['target']))} | `{kb_lib.compact_iri(str(c['target']))}` | "
                 + " · ".join(e[1] for e in c["evs"]) + " | " + " · ".join(cell(e[2]) for e in c["evs"]) + f" | {kb_lib.NONE_MARK} |")
    if not candidates:
        o.append("| " + " | ".join([kb_lib.NONE_MARK] * 2 + [f"후보 {kb_lib.NONE_MARK}"] + [kb_lib.NONE_MARK] * 6) + " |")
    o += ["", "## 확정 절차", "",
          f"1. 후보를 채택하면 앵커 청크의 frontmatter 에 링크 키와 복원 표시를 적는다 — `<링크 종류>: [<대상 IRI>]` 와 `{RESTORED_KEY}: [<대상 IRI>]`. "
          "대상 IRI 는 표의 `id:` 를 `https://agentic-knowledge-base.dev/id/` 로 푼 전체 IRI 다. 결정 복합체의 앵커는 결론 청크다. "
          f"`{RESTORED_KEY}` 의 IRI 가 같은 청크의 링크 대상에 없으면 `chunk2kg` 가 `FAIL [{kb_lib.RESTORED_GATE}]` 로 거부한다 (p10-restored-link-marking).",
          "2. 효과 — 그 링크 개체(`agt:Link`)에 후보의 출처 증거 `agt:proposal` 이 확정 기록 `agt:constructionRecord`(사람이 frontmatter 에 적은 행위)와 "
          "함께 붙고, `bazel build //kg:metrics`·`//kg:audit` 의 복원 비율에 복원으로 센다. `linkState` 는 `confirmed` 다 — frontmatter 에 적힌 것은 확정이다.",
          f"3. `{RELATED}` 후보도 다른 후보와 같이 적는다 — `{RELATED}: [<대상 IRI>]` 와 `{RESTORED_KEY}: [<대상 IRI>]` 다. 그 잎은 링크 키(LINK_KEYS)라 "
          "링크 개체와 복원 표시를 받고 복원 비율에 든다. 함께 갱신할 의무까지 판정했으면 `coUpdatesWith` 로 올려 적는다 — 그 키는 직접 트리플뿐이라 복원 표시를 "
          "받지 않는다. `verifies` 후보의 앵커는 V&V 청크이므로 vnv 가 적는다 (`kb/vv/` 는 vnv 의 write plane).",
          "4. `python3 tools/gen_build.py --root . && bazel test //...` — `refines`·`serves`·`supersedes`·`verifies` 는 Bazel deps 라 "
          "BUILD 를 재생성한다. 나머지 링크 키(`overlapsWith` 를 포함해)는 deps 가 아니라 그래프 트리플뿐이므로 BUILD 가 바뀌지 않는다.",
          "5. 기각은 관측 한 줄(memory plane)로 남긴다. 후보는 저장하지 않으므로 다음 생성에서 다시 나온다.", ""]
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, ttl, input_kind="그래프 파일"), encoding="utf-8")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
