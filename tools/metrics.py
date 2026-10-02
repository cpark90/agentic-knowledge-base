#!/usr/bin/env python3
"""코어 지표 뷰 — 그래프에서 metrics.md를 생성한다 (노트 4.13절, 10.14절, 12.3절, 14.1절).

문서에 수치를 적으면 반드시 낡으므로(4.6절 뷰 원칙) 지표는 이 생성물을 인용한다.
  청크 수(plane·level·status) · 고아율(복합체 부분도 링크도 없는 청크, 4.13절) · 크기 분포 ·
  링크 밀도 · 가정 · 신뢰 등급(사람 검토) · CQ19 전방 추적 커버리지 · CQ20 후방 추적 커버리지 · 도입 1단계 통과 조건.
사용: metrics.py --out metrics.md --residency defs/kb.bzl <TTL...>
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, RDF, RDFS, URIRef

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준

AGT = kb_lib.AGT  # 네임스페이스의 단일 정의처는 kb_lib (STYLEGUIDE §7)
ID = kb_lib.ID
PROV = kb_lib.PROV
DEFAULT_ASSUMPTION = ID["asm-chunk-conventions"]  # 기본 가정 (dependency-graph-design §6 "기본 가정 후 좁힘", docs/rules.md 가정 절)
LINKS = list(kb_lib.TRACE_LINKS)  # 추적 링크 잎의 단일 정의처는 kb_lib (STYLEGUIDE §7) — 링크 밀도·TIM 이 보는 집합이다.
# `usesDefinition` 은 references 족의 잎 — 링크 개체는 없고 직접 트리플만 센다. 연결 성분은 여기에 구성 관계와
# `prov:specializationOf` 를 더한 `kb_lib.LINKAGE_PREDICATES` 를, CQ20 후방 추적은 `kb_lib.ASCRIPTION_PREDICATES` 를 본다
# 후보·구축·복원의 구분은 kb_lib.link_origins 하나다 — 후보 = linkState candidate 인 링크 개체(본문 추출 cites, extract_refs),
# 구축 = 구축 기록 증거뿐인 확정 링크 개체, 복원 = 증거 종류가 구축 기록이 아닌 확정 링크 개체(restored: 표시 → proposal).
# 복원 비율 = 복원 / (확정 구축 + 복원). weave audit 이 같은 함수를 쓴다 (유저 결정 2026-09-12 (b), p10-extracted-references-are-candidates)
# plane 순서·수준 순서·수준 허용표의 단일 정의처는 `defs/kb.bzl` 이다 (M1 단일 정의처, 2026-09-26).
# --residency 로 그 파일을 읽어 채운다 — 리스트를 제자리에서 채우므로 아래 함수들의 참조가 그대로 산다.
PLANES: list[str] = []
LEVELS: list[str] = []
RESIDENCY: dict[str, list[str]] = {}
GRADES = "ABCD"  # 판정 방법 등급 (3.9절) — 연언의 등급은 최저 = 가장 뒤의 글자 (assume_check 와 같은 정의)


# ══ 입력 — 인자와 청크의 분류 ════════════════════
# 인자를 읽고 그래프에서 청크의 plane·수준·상태·줄 수를 가른다.

# ── 인자 ────────────────────
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--notes", default="", help="설계 노트 md — 확정 문장 커버리지(1단계 의미 보존 대리)")
    ap.add_argument("--bodies", nargs="*", default=[], help="청크 파일들 — 노트 절 인용 스캔")
    ap.add_argument("--residency", required=True, help="plane·수준·수준 허용표의 원본 defs/kb.bzl (M1 단일 정의처)")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    return a


# ── 청크의 분류 ────────────────────
def classify_chunks(g):
    """청크 집합과 plane·level·status·본문 토큰 수·살아 있는 것을 돌려준다."""
    chunks = {s for s in g.subjects(AGT.tokenCount, None)}
    plane = {c: str(next(g.objects(c, RDF.type))).split("/")[-1].replace("Chunk", "").lower() for c in chunks}
    level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in chunks}
    status = {c: str(next(g.objects(c, AGT.status), "")) for c in chunks}
    tokens = {c: int(next(g.objects(c, AGT.tokenCount))) for c in chunks}
    live = {c for c in chunks if status[c] != "deprecated"}
    return chunks, plane, level, status, tokens, live



# ══ 축 — 고아·추적·성분·링크 구축 ════════════════════
# 고아율, CQ19 전방·CQ20 후방 추적, 연결 성분과 건너뜀, 링크 개체의 근거와 복원 비율이다.

# ── 고아와 링크 밀도 ────────────────────
def orphan_and_links(g, chunks):
    """고아 집합(복합체 부분도 링크도 없는 청크, 4.13절)과 링크 타입별 수를 돌려준다."""
    linked = set()
    for p in LINKS:
        for s, o in g.subject_objects(p):
            linked.add(s); linked.add(o)
    parts = {o for o in g.objects(None, AGT.hasDirectPart)}
    orphans = {c for c in chunks if c not in linked and c not in parts}
    link_count = Counter(g.qname(p) for p in LINKS for _ in g.subject_objects(p))
    return linked, parts, orphans, link_count


# ── 정제 완주 (CQ19) ────────────────────
def refinement_reach(g, live, plane, level):
    """요구에서 refines·serves 역방향으로 내려가 닿는 가장 낮은 수준의 분포를 돌려준다."""
    reqs = {c for c in live if plane[c] == "requirement"}
    # CQ19: 요구에서 refines 역방향으로 내려가 닿는 가장 낮은 level
    down = defaultdict(set)
    for s, o in g.subject_objects(AGT.refines):
        down[o].add(s)
    for s, o in g.subject_objects(AGT.serves):
        down[o].add(s)
    def deepest(r):
        seen, stack, best = set(), [r], -1
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in level and level[x] in LEVELS: best = max(best, LEVELS.index(level[x]))
            stack.extend(down.get(x, ()))
        return best
    reach = Counter(LEVELS[deepest(r)] if deepest(r) >= 0 else "none" for r in reqs)
    return reqs, reach


# ── 후방 추적 귀속 (CQ20) ────────────────────
def back_trace(g, live, plane, reqs):
    """복합체 관계와 요구로 거슬러 오르는 비요구 청크의 수를 돌려준다."""
    # CQ20: 요구가 아닌 살아 있는 청크 중 refines 연쇄로 요구에 닿는 비율 (복합체 부분은 대표 부분을 따라간다)
    up = defaultdict(set)
    # 귀속으로 거슬러 오르는 술어의 정의처는 kb_lib.ASCRIPTION_PREDICATES 다 — `refines`·`serves` 와 `prov:specializationOf`.
    # 분할 조각은 링크를 승계 청크에 두므로(p10-split-keeps-work-identity) 원 청크를 거쳐 요구에 닿는다
    for pred in kb_lib.ASCRIPTION_PREDICATES:
        for s, o in g.subject_objects(pred): up[s].add(o)
    comp_of = {}
    for comp, part in g.subject_objects(AGT.hasDirectPart): comp_of[part] = comp
    siblings = defaultdict(set)
    for part, comp in comp_of.items(): siblings[comp].add(part)
    def reaches_req(c):
        seen, stack = set(), [c]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            if x in reqs: return True
            stack.extend(up.get(x, ()))
            if x in comp_of: stack.extend(siblings[comp_of[x]])
        return False
    # 저작된 지식만 센다 — 관측(memory plane)은 실행의 부산물, 판정 주석(annotation plane)은 산출물에 대한 리뷰라
    # 둘 다 고립·귀속 지표의 대상이 아니다 (유저 승인 2026-09-23 · 2026-09-29, handoff/connected-components-
    # observations-2026-09-19 · handoff/verdict-in-metrics-2026-09-27). 제외 집합의 정의처는 kb_lib 상수 하나다.
    # 같은 정의를 연결 성분도 쓴다
    authored = [c for c in live if plane[c] not in kb_lib.LINKAGE_EXCLUDED_PLANES]
    nonreq = [c for c in authored if plane[c] != "requirement"]
    ascribed = sum(1 for c in nonreq if reaches_req(c))
    return comp_of, siblings, authored, nonreq, ascribed


# ── 신뢰 등급과 크기 분포 ────────────────────

SIZE_BANDS = (0.25, 0.50, 0.75, 0.90)  # 상한에 대한 비율의 칸 경계 — 마지막 칸이 "상한의 9/10 초과"다
# 칸의 제목 — 분모는 그 청크의 plane 상한이다. 분수로 적는 이유는 생성 문서 규약 G15 다: 백분율은 `n/d = p.p%`
# 꼴이어야 하고 분모 없는 `25%` 는 거부된다 — 칸 이름은 측정값이 아니라 구간이므로 분수·구간 서술로 적는다
SIZE_HEADER = "| 상한의 1/4 이하 | 1/2 이하 | 3/4 이하 | 9/10 이하 | 9/10 초과 |"


def size_bucket(ratio: float) -> int:
    """상한에 대한 비율 → 칸 번호. 경계 위는 다음 칸이고 마지막 칸은 9/10 초과다."""
    for i, edge in enumerate(SIZE_BANDS):
        if ratio <= edge:
            return i
    return len(SIZE_BANDS)


def trust_and_size(g, chunks, live, plane, tokens):
    """사람 검토 수·생성자 분포·크기 히스토그램·assumes 링크 수를 돌려준다.

    크기의 단위는 토큰이고 상한은 plane 별 프로파일 파라미터이므로(p1-chunk-unit-is-tokens) 히스토그램의 칸은
    절대 수가 아니라 **그 청크의 상한에 대한 비율**이다 — plane 이 섞인 분포에서 "상한 근처에 몰렸는가"를 한
    칸으로 읽으려면 분모가 청크마다 달라야 한다. 마지막 칸(9/10 초과)이 억지 분할의 신호다 (4.13절).
    """
    human = sum(1 for c in chunks for v in g.objects(c, AGT.verifiedBy) if str(v).startswith("human:"))
    gen = Counter(str(next(g.objects(c, AGT.generatedBy), "")) for c in chunks)
    hist = Counter(size_bucket(tokens[c] / kb_lib.body_token_limit(plane[c])) for c in live)
    assumes = sum(1 for _ in g.subject_objects(AGT.assumes))
    return human, gen, hist, assumes


# ── 연결 성분과 건너뜀 ────────────────────
def axis_proxies(g, live, plane, level, authored, comp_of, siblings):
    """저작된 지식의 연결 성분 수·주 성분 밖 성분들·수준 건너뜀·매트릭스 채움·수준 허용표 위반을 돌려준다."""
    # 세 축 대리 (14.1 정정본, p14-stage-pass-conditions): 연결 성분 · 매트릭스 채움률 · level 건너뜀 · 수준 허용표 위반
    parent = {c: c for c in authored}  # 관측·주석 제외 — 저작된 지식의 고립을 잰다
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a_, b_):
        if a_ in parent and b_ in parent: parent[find(a_)] = find(b_)
    for p_ in kb_lib.LINKAGE_PREDICATES:  # 추적 링크 잎 + 구성 관계 + prov:specializationOf (연결로 세는 술어의 단일 정의처)
        for s_, o_ in g.subject_objects(p_): union(s_, o_)
    for part_, comp_ in comp_of.items():
        for sib in siblings[comp_]: union(part_, sib)
    groups = defaultdict(list)
    for c in authored: groups[find(c)].append(c)
    # 성분을 크기 내림차순(동수는 작은 IRI)으로 두고 첫째를 주 성분으로 본다 — 나머지가 진단 대상이다
    ordered = sorted(groups.values(), key=lambda m: (-len(m), str(min(m, key=str))))
    components, outside = len(ordered), ordered[1:]
    skips = [(s_, o_) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level and level[s_] in LEVELS and level[o_] in LEVELS
             and LEVELS.index(level[s_]) - LEVELS.index(level[o_]) != 1]
    lvl_pairs = {(level[o_], level[s_]) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level}
    adjacent = [(LEVELS[i], LEVELS[i + 1]) for i in range(4)]
    filled = [p_ for p_ in adjacent if p_ in lvl_pairs]
    residency_bad = [c for c in live if plane[c] in RESIDENCY and level[c] not in RESIDENCY[plane[c]]]
    return components, outside, skips, filled, residency_bad


# ── 링크 구축과 복원 ────────────────────
def link_build(g):
    """링크 개체와 증거·후보·구축·복원·suspect 포화·TIM 채움을 돌려준다."""
    # 3단계 대리 — 링크마다 근거 · 구축/복원 비율 · plane×plane 매트릭스 채움 (TIM 이 허용하는 칸)
    link_ents = list(g.subjects(RDF.type, AGT.Link))
    with_ev = [l for l in link_ents if (l, AGT.hasEvidence, None) in g]
    origins = kb_lib.link_origins(g)  # 후보·구축·복원의 단일 정의 — 상태와 증거 종류 기준 (p10-restored-link-marking · p10-extracted-references-are-candidates)
    extracted_n, built_n, restored_total = origins["extracted"], origins["built"], origins["restored"]
    # suspect 포화율 — 선언된 트리거(kb_lib.SUSPECT_TRIGGERS)만 돈다. `when` 판정은 호스트 상태를 보므로 이 뷰 밖이고
    # assume_check 가 낸다. 포화율을 보지 않으면 트리거를 좁힌 것이 맞는지 알 수 없다 (handoff link-model-robustness-cde-2026-09-19)
    sat = kb_lib.suspect_saturation(g)
    trig_on = " · ".join(f"`{k}`" for k, _rule, _basis in kb_lib.suspect_triggers_on()) or kb_lib.NONE_MARK
    TIM = kb_lib.TIM_CELLS  # 허용 칸의 정의처는 kb_lib — weave audit 이 같은 매트릭스를 낸다. 복합체 IRI 의 plane 보정도 kb_lib.link_cells
    seen_cells = kb_lib.link_cells(g)
    tim_filled = [c for c in TIM if c in seen_cells]
    return link_ents, with_ev, origins, extracted_n, built_n, restored_total, sat, trig_on, TIM, tim_filled



# ══ 단계 대리 — 의미 보존·가정·V&V·스코프 ════════════════════
# 1단계 확정 문장 커버리지, 4단계 가정과 판정식 등급, 7단계 V&V KB, 2단계 역할 작업 집합이다.

# ── 확정 문장 커버리지 ────────────────────
def fixed_sentence_coverage(a, live, plane, parts, siblings):
    """설계 노트의 [확정] 절 중 청크가 인용한 절의 비율을 한 줄로 돌려준다."""
    # 1단계 의미 보존 대리 — 확정 문장 커버리지: [확정]이 있는 절 중 결정이 인용하는 절의 비율
    cov_line = "- 의미 보존: 확정 문장 커버리지 — `--notes` 없음"
    if a.notes:
        import re as _re
        text = Path(a.notes).read_text(encoding="utf-8")
        sec, cur = {}, None
        for ln in text.splitlines():
            m = _re.match(r"^## (\d+\.\d+) ", ln)
            if m: cur = m.group(1); sec.setdefault(cur, 0)
            elif cur and "[확정]" in ln: sec[cur] += 1
        with_fixed = {k for k, v in sec.items() if v}
        cited = set()
        for b_ in a.bodies:
            cited |= set(_re.findall(r"(?<![\d.])(\d{1,2}\.\d{1,2})절", Path(b_).read_text(encoding="utf-8")))  # "노트 N.N절"과 "(N.N절)" 둘 다
        missing = sorted(with_fixed - cited, key=lambda x: [int(t) for t in x.split(".")])
        cov_line = (f"- 의미 보존: 확정 문장 커버리지(절 단위) **{kb_lib.pct(len(with_fixed & cited), len(with_fixed))}** — "
                    f"[확정] {sum(sec.values())}문장, 결정 {sum(1 for c in live if plane[c]=='decision' and c not in parts) + len(siblings)}개. 인용 없는 절: " + (", ".join(missing) or "없음"))
    return cov_line


# ── 가정과 판정식 등급 ────────────────────
def assumption_facts(g, live, plane):
    """기본 가정만 가진 청크 수와 가정 개체·판정식 등급 분포·관측 수를 돌려준다."""
    # 가정 — 기본 가정만 가진 청크 (좁힘 진행률의 역수, docs/rules.md 가정 절)
    default_only = sum(1 for c in live if set(g.objects(c, AGT.assumes)) == {DEFAULT_ASSUMPTION})
    # 4단계 대리 (14.1 정정본: 무효화 이력 · 판정식 등급 · 인위 파괴 실험) — 판정식은 참조 조건 판정의 연언이라 등급은 참조 조건
    # 등급(ODD agt:verificationGrade)의 최저다 (tools/assume_check.py 와 같은 정의). 무효화 이력은 memory plane 의 관측 수다
    assumptions = sorted(g.subjects(RDF.type, AGT.Assumption), key=str)
    def asm_grade(asm):
        grades = [str(next(g.objects(c, AGT.verificationGrade), "?")) for c in g.objects(asm, AGT.refersTo)]
        return max(grades, key=lambda x: GRADES.index(x) if x in GRADES else len(GRADES)) if grades else "?"
    grade_dist = Counter(asm_grade(a_) for a_ in assumptions)
    grade_ab = sum(v for k, v in grade_dist.items() if k in "AB")
    observations = [c for c in live if plane[c] == "memory"]
    obs_recorded = sum(1 for c in observations if str(next(g.objects(c, AGT.generatedBy), "")) == kb_lib.ASSUME_CHECK_GENERATOR)
    return default_only, assumptions, grade_dist, grade_ab, observations, obs_recorded


# ── V&V KB ────────────────────
def vv_facts(g, chunks, live, plane):
    """V&V KB 의 청크 분포와 verifies 링크·기준 없는 verifies·검증 대응물을 돌려준다."""
    # 7단계 대리 — V&V KB (p8-vv-plane-instances: 코어의 두 번째 인스턴스, kb/vv/). KB 는 청크 위치(assertionLocation)로 가른다 (kb_lib.kb_of)
    loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in chunks}
    vv = {c for c in live if kb_lib.kb_of(loc[c]) == kb_lib.KB_VV}
    dev = live - vv
    vv_by = Counter(plane[c] for c in vv)
    verifies_links = list(g.subject_objects(AGT.verifies))
    no_criteria = [s for s, _ in verifies_links if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    verified_targets = {o for _, o in verifies_links}
    dev_reqs = {c for c in dev if plane[c] == "requirement"}
    goals = {c for c in vv if plane[c] == "requirement"}
    covered_reqs = {o for s, o in g.subject_objects(AGT.derivesFrom) if s in goals and o in dev_reqs}
    goals_with_criteria = {o for s, o in g.subject_objects(AGT.refines) if o in goals and plane.get(s) == "contract"}
    return vv, vv_by, verifies_links, no_criteria, verified_targets, dev_reqs, goals, covered_reqs, goals_with_criteria


# ── 역할 작업 집합과 스코프 ────────────────────
def role_worksets(g, live, plane, tokens, pct):
    """역할·앵커별 작업 집합이 예산 안인 비율과 ODD 에서 파생되지 않은 스코프를 돌려준다.

    예산의 단위는 토큰이다 (p1-chunk-unit-is-tokens — 옛 200줄의 같은 계수기 환산이 5,418 이다). 본문의 크기는
    그래프의 `agt:tokenCount` 를 그대로 쓰고, 머리·제목·라벨 행은 행마다 1 로 센다 — 행 하나가 적어도 토큰
    하나이므로 합계는 **하한**이고 이 비율은 상한 쪽으로 낙관적이다. 정확한 판정은 뷰 자신(`workset`)이 한다.
    """
    # 2단계 — 역할별 작업 집합(라벨 목록) 크기와 스코프 파생
    odd_conds = set(g.objects(None, AGT.hasCondition))
    role_rows, scope_bad = [], []
    nb = defaultdict(set)
    for p_ in LINKS + [AGT.hasDirectPart]:
        for s_, o_ in g.subject_objects(p_):
            nb[s_].add(o_); nb[o_].add(s_)
    BUDGET = kb_lib.CONTEXT_TOKEN_BUDGET  # 컨텍스트 예산 — 단위는 토큰이다 (단일 정의처 kb_lib)
    for role in g.subjects(RDF.type, AGT.Role):
        planes = set(g.objects(role, AGT.reads)) | set(g.objects(role, AGT.writes))
        in_scope = [c for c in live if next(g.objects(c, RDF.type)) in planes]
        ok = 0
        for anc in in_scope:  # 앵커마다: 헤더 2 + plane 제목 + 이웃 라벨 + (앵커+이웃) 본문
            nbs = [n for n in nb.get(anc, ()) if n in tokens and n in live and next(g.objects(n, RDF.type)) in planes]
            total = 2 + len({plane[x] for x in [anc] + nbs}) + 1 + len(nbs) + tokens[anc] + sum(tokens[n] for n in nbs)
            ok += total <= BUDGET
        role_rows.append(f"`{str(role).split('/')[-1].replace('role-','')}` {pct(ok, len(in_scope))}")
        scope = ID[str(role).split('/')[-1].replace('role-', 'scope-')]
        inc = set(g.objects(scope, AGT.includesCondition))
        if (scope, AGT.subsetOf, None) not in g or not inc or not inc <= odd_conds:
            scope_bad.append(str(scope).split('/')[-1])
    return role_rows, scope_bad, BUDGET



# ══ 보고 — 머리와 절 ════════════════════
# 머리 블록과 절을 조립한다. 절의 순서가 생성 문서의 순서다.

# ── 머리 블록 ────────────────────
def render_head(g, chunks, live, siblings, inputs):
    """생성 문서의 머리 블록 — 생성기·질의·입력·규모와 뷰 통지다."""
    head = kb_lib.gendoc_header(
        "metrics", "코어 지표", "tools/metrics.py",
        "그래프 union 과 청크 본문에서 — plane × level 분포 · 고아율 · 도입 단계 세 축의 대리 · 링크 밀도 · 크기 분포 · "
        "정제 완주(CQ19) · 후방 추적 귀속(CQ20) · 가정과 신뢰 등급. 연결 성분과 후방 추적 귀속은 **관측·주석 제외**다 — "
        "관측(memory plane)은 실행의 부산물, 판정 주석(annotation plane)은 산출물에 대한 리뷰라 둘 다 저작된 지식의 "
        "고립을 재는 지표의 대상이 아니다 (유저 승인 2026-09-23 · 2026-09-29, kb_lib.LINKAGE_EXCLUDED_PLANES). "
        "분할 조각의 `prov:specializationOf` 는 연결과 귀속에서 **연결로 센다** — 조각은 원 청크의 정체성을 나눠 "
        "가진 것이지 새 지식이 아니다 (p10-split-keeps-work-identity, kb_lib.LINKAGE_PREDICATES). "
        "수치를 문서에 적지 않고 여기서 인용한다 (4.6절 뷰 원칙)",
        "bazel build //kg:metrics", inputs,
        f"트리플 {len(g)} ({kb_lib.gendoc_union(inputs)}) · 청크 {len(chunks)}", kb_lib.gendoc_view_notice("청크의 frontmatter 와 본문"),
        input_kind="입력 파일",
        extra=[f"- 청크 {len(chunks)} (살아 있는 것 {len(live)}, deprecated {len(chunks)-len(live)}) · 복합체 {len(siblings)} · 트리플 {len(g)}"])
    return head


# ── 절 — 분포와 고아율 ────────────────────
def render_distribution(pct, chunks, live, plane, level, orphans):
    o = ["## plane × level (살아 있는 청크)", "", "| plane | " + " | ".join(LEVELS) + " | 합 |", "|---|" + "---|" * (len(LEVELS) + 1)]
    for p in PLANES:
        row = [sum(1 for c in live if plane[c] == p and level[c] == l) for l in LEVELS]
        o.append(f"| `{p}` | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    o += ["", "## 고아율 (4.13절 — 복합체 부분도 링크도 없는 청크)", "",
          f"- 전체: **{pct(len(orphans), len(chunks))}**",
          f"- 살아 있는 청크: **{pct(len(orphans & live), len(live))}** (목표 10% 미만) — 도입 1단계 통과 조건: **{'통과' if len(live) and len(orphans & live)/len(live) < 0.10 else '미통과'}**"]
    for p in PLANES:
        n = sum(1 for c in live if plane[c] == p)
        if n: o.append(f"  - `{p}`: {pct(sum(1 for c in orphans & live if plane[c] == p), n)}")
    return o


# ── 절 — 세 축·링크 구축·스코프 ────────────────────
def render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line, link_ents, with_ev, origins, extracted_n, built_n, restored_total, tim_filled, TIM, BUDGET, role_rows, scope_bad):
    o = []
    o += ["", "## 세 축 대리 — 1·3·5단계 (14.1 정정본: 의미 보존 · 구체화 · 유기적 연결)", "",
          f"- 연결: 저작된 지식의 연결 성분 **{components}**개 (살아 있는 청크 {len(live)} 중 관측·주석 {len(live) - len(authored)}건을 뺀 {len(authored)}개가 링크·복합체·`prov:specializationOf` 로 이어진 덩어리. 목표 1; 1보다 크면 아래 「주 성분 밖 청크」 절이 성분마다 목록을 낸다)",
          f"- 연결: level×level `refines` 매트릭스 채움 {pct(len(filled), 4)} — " + (", ".join(f"{a_}→{b_}" for a_, b_ in filled) or "없음") + " (목표 4/4 = 100.0%)",
          f"- 구체화: level을 한 단계씩 내려가지 않는 `refines` **{len(skips)}**건 (목표 0; 지금은 concrete→functional 직행이 구조적으로 허용됨 — abstract·logical 결정이 생기면 0이어야 한다)",
          f"- 구체화: 수준 허용표 위반 **{len(residency_bad)}**건 (목표 0)",
          cov_line,
          "- 의미 보존: 라벨 대표성은 실험 — 이 도구 밖"]
    o += ["", "## 3단계 대리 — 링크 구축 (14.1 정정본: 근거 · 한 단계씩 · 매트릭스 · 복원 비율)", "",
          f"- 의미 보존: 링크 개체 **{len(link_ents)}** (확정 {origins['confirmed']} · 후보 {origins['candidates']}) 중 증거 기록이 있는 것 **{pct(len(with_ev), len(link_ents))}** (목표 100.0%; 증거 종류 분포는 `audit` 링크 근거 절)",
          f"- 의미 보존: 구축 비율 — 확정 링크 개체 중 구축(구축 기록 증거뿐) {built_n} vs 복원 {restored_total}(구축 기록 아닌 증거 `proposal` 을 가진 링크 개체 — frontmatter `restored:` 표시) → 복원 비율 **{pct(restored_total, built_n + restored_total)}** (목표 20% 미만; 후보는 `bazel build //kg:link_candidates`, 확정은 `restored:` — p10-restored-link-marking)",
          f"- 의미 보존: 후보 링크 개체(`agt:CandidateLink`, linkState candidate — 본문 추출, 증거는 구축 기록) **{origins['candidates']}** — " + (" · ".join(f"`{k}` {v}" for k, v in sorted(origins['candidate_kinds'].items())) or "없음") + "; 본문 식별자 추출 직접 트리플 " + " · ".join(f"`{k}` {v}" for k, v in extracted_n.items()) + " (`usesConcept` 는 대상이 온톨로지 용어라 링크 치역 밖 — 후보 개체 없음; p10-extracted-references-are-candidates)",
          f"- 연결: plane×plane 매트릭스 — TIM 허용 칸 채움 **{pct(len(tim_filled), len(TIM))}** ({', '.join(f'{k}:{a_}→{b_}' for k, a_, b_ in tim_filled) or '없음'}); 빈 칸은 contract·schema·artifact·V&V 항목이 생겨야 찬다",
          "- 구체화: `refines` 한 단계씩 — 위 세 축 절의 건너뜀 수 참조"]
    o += ["", "## 2단계 대리 — ODD와 스코프", "",
          f"- 정의: 여기의 예산 준수율은 **앵커마다** 센다 — 스코프 안 청크 하나를 앵커로 잡고 그 1홉 이웃의 라벨과 본문을 펼친 크기가 "
          f"{BUDGET}토큰 이하인 앵커의 비율이다. 본문은 `agt:tokenCount`, 라벨·제목 행은 행마다 1 로 세므로 합계는 하한이다. "
          "`bazel build //kg:workset` 의 예산 판정은 **문서 전체**(앵커 없이 스코프 전체의 라벨 목록)를 어휘로 직접 세므로 "
          "두 수치는 같은 이름이되 다른 것을 센다",
          "- 구체화: 역할·앵커별 작업 집합(스코프 안 청크를 앵커로, 1홉 이웃 라벨 + 본문 펼침)이 예산 안인 비율: " + " · ".join(role_rows),
          f"- 구체화: ODD × plane 권한에서 파생되지 않은 스코프 **{len(scope_bad)}**건" + (f" — {', '.join(scope_bad)}" if scope_bad else "") + " (목표 0; 2026-09-26부터 게이트 `catalog` 가 같은 규칙을 강제하므로 이 수치는 그 게이트의 관측이다)",
          "- 연결: ODD 밖 참조는 게이트(odd-ref)가 0으로 강제. 첫 모니터링 이탈은 `bazel run //tools:odd_check`"]
    return o


# ── 절 — 성분 진단 ────────────────────
def render_component_diagnosis(g, plane, outside):
    """주 성분 밖의 청크 목록 — 성분마다 라벨·plane·경로다. 수만으로는 무엇이 떨어졌는지 알 수 없다."""
    o = ["", "## 주 성분 밖 청크 (연결 성분 진단)", ""]
    if not outside:
        o.append("- 없음 — 저작된 지식이 한 덩어리다 (연결 성분 1)")
        return o
    o += [f"- 주 성분 밖 성분 **{len(outside)}**개 · 청크 **{sum(len(m) for m in outside)}**건 — 링크·복합체·"
          "`prov:specializationOf` 가 주 성분에 닿지 않는 덩어리다. 성분 번호는 크기 내림차순(동수는 작은 IRI)이다", "",
          "| 성분 (청크 수) | 라벨 | plane | 경로 |", "|---|---|---|---|"]
    for i, members in enumerate(outside, 1):
        for c in sorted(members, key=str):
            loc = str(next(g.objects(c, AGT.assertionLocation), "")) or kb_lib.NONE_MARK
            lab = kb_lib.label_of(g, c).replace("|", "\\|")  # 표의 열 수를 지킨다 (G10)
            o.append(f"| {i} ({len(members)}) | {lab} | `{plane.get(c, kb_lib.NONE_MARK)}` | `{loc}` |")
    return o


# ── 절 — 가정과 V&V ────────────────────
def render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist, grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets, no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals):
    o = []
    o += ["", "## 4단계 대리 — 가정과 무효화 (14.1 정정본: 무효화 이력 · 판정식 등급 · 인위 파괴 실험)", "",
          f"- 의미 보존: 무효화 이력 — 관측(memory plane) **{len(observations)}**건, 그중 `assume_check --record` 의 판정 관측 {obs_recorded}건 (지금은 판정 관측 수 — 무효화 사건이 생기면 그 이력이 여기 쌓인다. provenance 는 관측이 `generatedBy`·`prov:wasDerivedFrom` 를 갖는 비율로 잰다 (목표 100.0%): {pct(sum(1 for c in observations if (c, AGT.generatedBy, None) in g and (c, PROV.wasDerivedFrom, None) in g), len(observations))})",
          f"- 구체화: 가정 개체 {len(assumptions)} · `assumes` 링크 {assumes} (가정 · 신뢰 등급 절과 같은 수) · 판정식 등급 분포(참조 조건 등급의 최저) " + (" · ".join(f"{k} {v}" for k, v in sorted(grade_dist.items())) or "없음") + f" — A·B 비율 **{pct(grade_ab, len(assumptions))}** (목표 100.0%), D **{grade_dist.get('D', 0)}**건 (목표 0)",
          f"- 연결: suspect 포화율 — 켜진 트리거({trig_on})가 suspect 로 유도하는 확정 링크 **{pct(sat['by_trigger'], sat['confirmed'])}** "
          f"(목표 포화 경고선 20% 미만 — 넘으면 트리거를 더 좁힌다). `agt:when` 을 가진 확정 링크 {sat['with_when']}건의 판정은 호스트 상태를 "
          "보므로 이 뷰 밖이고 `bazel run //tools:assume_check` 가 낸다. 선언의 원본은 `tools/kb_lib.py` 의 `SUSPECT_TRIGGERS` 이며 선언에 없는 종류는 돌지 않는다",
          "- 연결: 인위 파괴 실험은 `bazel run //tools:assume_check -- --break <cond>` — 계산된 직접 영향 집합과 실제 의존 집합(frontmatter 스캔)의 일치 여부를 그 보고가 낸다. 판정은 호스트 상태를 보므로 이 뷰 밖이다"]
    o += ["", "## 7단계 대리 — V&V (p8-vv-plane-instances · p8-pass-criteria · p8-scenario-ladder-rungs)", "",
          f"- 구체화: V&V KB(`kb/vv/`) 살아 있는 청크 **{len(vv)}** — 검증 목표(`requirement`) {vv_by['requirement']} · 시나리오(`decision`) {vv_by['decision']} · 합격 기준(`contract`) {vv_by['contract']} · 케이스(`schema`) {vv_by['schema']} · 검증기(`artifact`) {vv_by['artifact']} · 판정 주석(`annotation`) {vv_by['annotation']} · 실행 기록(`memory`) {vv_by['memory']}",
          f"- 연결: `verifies` 링크 **{len(verifies_links)}** (주어는 V&V 청크, 대상은 같은 수준의 개발 항목 — `defs/kb.bzl` 이 분석 시점에 강제) · 대상이 된 개발 항목 {len(verified_targets)}",
          f"- 의미 보존: 기준 없는 `verifies` **{len(no_criteria)}**건 (목표 0) — ( 주어가 합격 기준(`ContractChunk`)을 `refines` 해야 하며 verify 질의 `verifies-without-criteria` 가 거부한다)",
          f"- 연결: 검증 대응물이 있는 요구(검증 목표가 `derivesFrom` 으로 가리키는 개발 요구) **{pct(len(covered_reqs), len(dev_reqs))}** (목표 100.0% — 8.3절 functional 높이의 검증 대응물 필수) · 합격 기준이 달린 검증 목표 {pct(len(goals_with_criteria), len(goals))}"]
    return o


# ── 절 — 링크 밀도·크기·추적·가정 ────────────────────
def render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes, default_only, gen, human):
    o = []
    o += ["", "## 링크 밀도", "", f"- 링크 {sum(link_count.values())} / 살아 있는 청크 {len(live)} = **{kb_lib.num(sum(link_count.values())/max(len(live),1))}**/청크",
          "- 타입별: " + " · ".join(f"`{k}` {v}" for k, v in link_count.most_common()),
          f"- 링크 개체(`agt:Link`): {sum(1 for _ in g.subjects(RDF.type, AGT.Link))} · 증거 항목: {sum(1 for _ in g.subjects(RDF.type, AGT.Evidence))}"]
    o += ["", "## 크기 분포 (본문 토큰 수가 상한에 대해 차지하는 비율, 살아 있는 청크)", "",
          SIZE_HEADER, "|---|---|---|---|---|",
          "| " + " | ".join(str(hist[i]) for i in range(len(SIZE_BANDS) + 1)) + " |", "",
          f"- 상한의 9/10 초과 비율 {pct(hist[len(SIZE_BANDS)], len(live))} — 상한 근처에 몰리면 억지 분할 의심 (4.13절). "
          f"분모는 청크마다 그 plane 의 상한이다(저작 산문 {kb_lib.MAX_BODY_TOKENS} · artifact·memory "
          f"{kb_lib.BODY_TOKEN_LIMITS['artifact']} 토큰, p1-chunk-unit-is-tokens)"]
    o += ["", "## 정제 완주 (CQ19) · 후방 추적 귀속 (CQ20)", "",
          f"- 요구 {len(reqs)}건이 `refines`/`serves` 연쇄로 닿는 가장 낮은 수준: " + " · ".join(f"{k} {v}" for k, v in reach.most_common()),
          f"- executable까지 닿은 요구: **{pct(reach.get('executable', 0), len(reqs))}** (전방 추적 커버리지, 목표 100.0%)",
          f"- 요구로 거슬러 오르는 비요구 청크(관측·주석 제외): **{pct(ascribed, len(nonreq))}** (후방 추적 커버리지, 목표 100.0%)"]
    o += ["", "## 가정 · 신뢰 등급", "",
          f"- `assumes` 링크 {assumes} · 가정 개체 {sum(1 for _ in g.subjects(RDF.type, AGT.Assumption))}",
          f"- 기본 가정만 가진 청크(`assumes` 대상이 `id:asm-chunk-conventions` 하나뿐인 살아 있는 청크): **{pct(default_only, len(live))}** (좁힘 진행률의 역수 — 목표 0)",
          f"- 생성자: " + " · ".join(f"`{k}` {v}" for k, v in gen.most_common()) + f" · **사람 검토(`human:`) {human}건**",
          ""]
    return o


# ── 실행 ────────────────────
def main() -> int:
    a = parse_args()
    planes_, levels_, table_ = kb_lib.load_residency(a.residency)
    PLANES[:], LEVELS[:] = planes_, levels_
    RESIDENCY.update({p_: v_ for p_, v_ in table_.items() if set(v_) != set(levels_)})
    g = Graph()
    for f in a.files:
        if f.endswith(".ttl"):
            g.parse(f, format="turtle")
    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — `n/d = p.p%`, 0 분모는 없음)
    chunks, plane, level, status, tokens, live = classify_chunks(g)
    linked, parts, orphans, link_count = orphan_and_links(g, chunks)
    reqs, reach = refinement_reach(g, live, plane, level)
    comp_of, siblings, authored, nonreq, ascribed = back_trace(g, live, plane, reqs)
    human, gen, hist, assumes = trust_and_size(g, chunks, live, plane, tokens)
    components, outside, skips, filled, residency_bad = axis_proxies(g, live, plane, level, authored, comp_of, siblings)
    (link_ents, with_ev, origins, extracted_n, built_n, restored_total,
     sat, trig_on, TIM, tim_filled) = link_build(g)
    cov_line = fixed_sentence_coverage(a, live, plane, parts, siblings)
    (default_only, assumptions, grade_dist, grade_ab,
     observations, obs_recorded) = assumption_facts(g, live, plane)
    (vv, vv_by, verifies_links, no_criteria, verified_targets,
     dev_reqs, goals, covered_reqs, goals_with_criteria) = vv_facts(g, chunks, live, plane)
    role_rows, scope_bad, BUDGET = role_worksets(g, live, plane, tokens, pct)

    inputs = list(a.files) + ([a.notes] if a.notes else []) + list(a.bodies)
    head = render_head(g, chunks, live, siblings, inputs)
    o = render_distribution(pct, chunks, live, plane, level, orphans)
    o += render_axis_sections(pct, live, authored, components, filled, skips, residency_bad, cov_line,
                              link_ents, with_ev, origins, extracted_n, built_n, restored_total,
                              tim_filled, TIM, BUDGET, role_rows, scope_bad)
    o += render_component_diagnosis(g, plane, outside)
    o += render_stage_sections(g, pct, observations, obs_recorded, assumptions, assumes, grade_dist,
                               grade_ab, trig_on, sat, vv, vv_by, verifies_links, verified_targets,
                               no_criteria, covered_reqs, dev_reqs, goals_with_criteria, goals)
    o += render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes,
                              default_only, gen, human)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, o, inputs), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
