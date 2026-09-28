#!/usr/bin/env python3
"""가정 판정과 전파 — 도입 4단계 "가정과 무효화"의 첫 형태 (노트 6.5절·6.9절, method §7, p6-assumption-verification-methods,
p6-assumption-invalidation).

가정(`agt:Assumption`)마다 `agt:refersTo` 한 ODD 조건을 odd_check 의 판정 함수로 판정하고 연언(AND)으로 상태를 낸다.
  valid        — 참조 조건 전부 in
  invalidated  — 하나라도 out
  unverified   — 그 밖 (판정 불가한 조건이 있다)
판정 유형은 ODD `CHECKS.cmd` 가 있으면 "실행 검사", 없으면 "사람 확인" 이고, 판정식 등급은 참조 조건 등급의 최저(A~D)다.
새 어휘는 없다 — 가정 자체의 `when` 판정식은 후속이며, 첫 형태는 참조 조건 판정의 연언으로 판정식을 파생한다.

전파 (p6-assumption-invalidation "가정이 깨지면 의존 항목이 자동으로 무효화된다", r-007 전수조사 없이):
  직접 영향 집합  = invalidated 가정을 `agt:assumes` 하는 살아 있는 청크
  suspect 후보    = 직접 영향 집합에 링크(refines·serves·supersedes·cites·coUpdatesWith·overlapsWith — 직접 트리플과 agt:Link 개체 둘 다)로
                    닿는 하류(그 항목을 가리키는 쪽, 전이) + 복합체 형제. 그래프가 원본이므로 bazel rdeps 가 아니라 head 그래프에서 센다.
검증 실험 (14.1 정정본 4단계 "연결" 조건): `--break <cond-id>` 는 그 조건을 out 으로 가정한다. 그때 계산된 직접 영향 집합을
청크 파일 frontmatter(`assumes`)를 독립적으로 스캔한 실제 의존 집합과 비교해 정밀도·재현율을 보고에 적는다.

링크 상태의 물질화 (노트 9.11절 "상태는 저장값이 아니라 평가 결과", handoff link-model-robustness-cde-2026-09-19 반영 1·2):
  when 판정   확정 링크의 `agt:when` 을 kb_lib.when_eval 로 판정한다. 판정의 범위는 **ODD 속성 참조**이고 항은 `in(<조건>)`,
              결합은 `!`·`&&`·`||`·괄호, 리터럴은 true·false 다 (kb_lib.WHEN_GRAMMAR). 비교·산술·함수 호출은 판정하지 않고
              unverified 로 남긴다. 조건 판정은 여기서 새로 하지 않고 odd_check.judge_all 의 결과를 그대로 읽는다.
  트리거      kb_lib.SUSPECT_TRIGGERS 에 켜진 종류만 전파한다 — 지금은 supersedes 하나다. 추적 매트릭스가 suspect 로 포화하는
              것을 막기 위해 좁게 선언하고, 포화율은 `bazel build //kg:metrics` 의 한 줄로 관측한다.
  저장하지 않는다  suspect 는 그래프에 적히지 않는다. 이 보고와 metrics 에서만 물질화된다.

--record 는 실행 결과를 관측(memory plane, concrete, append-only — r-026·p0-run-as-observation)으로
kb/dev/memory/obs-<UTC>.md 에 쓴다. 이미 있는 파일은 덮지 않는다. 생성 뒤 tools/gen_build.py 를 돌려 BUILD 를 갱신한다.

사용: bazel run //tools:assume_check -- [--break <cond-id>…] [--record] [--out report.md] [--odd kb/odd/project-odd.yml] [TTL…]
종료: 전부 valid 0 (EXIT_OK) · invalidated 가정 또는 `when` 이 거짓인 링크 있음 1 (EXIT_FAIL) · unverified 만 있음 3 (EXIT_SKIP) ·
      입력 문제 2 (EXIT_CONFIG)
"""
from __future__ import annotations

import argparse
import os
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, RDF, RDFS, URIRef

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 네임스페이스·종료 코드의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402 — 실제 의존 집합은 frontmatter 를 그래프와 독립적으로 읽는다
from odd_check import judge_all, load_odd  # noqa: E402 — 조건 판정은 odd_check 와 같은 함수

AGT, ID = kb_lib.AGT, kb_lib.ID
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
GRADES = "ABCD"  # 판정 방법 등급 (3.9절) — 뒤로 갈수록 약하다. 연언의 등급은 최저 = 가장 뒤의 글자
# 전파에 쓰는 링크 — 청크 → 청크 (verifies 는 V&V 청크가 주어라 아직 없다). 방향: 주어가 목적어에 의존한다
PROPAGATE = [AGT.refines, AGT.serves, AGT.supersedes, AGT.cites, AGT.coUpdatesWith, AGT.overlapsWith]
# 기본 그래프 — `bazel run` 의 작업 디렉토리(runfiles)에 data 로 놓인다. 없으면 워크스페이스의 bazel-bin·소스에서 찾는다
DEFAULT_TTL = ["kg/chunks-kg.ttl", "kg/references-kg.ttl", "kg/base-kg.ttl", "kg/catalog-kg.ttl", "kg/composite-kg.ttl",
               "kb/odd/project-odd.ttl", "space/design-space.ttl"]  # 설계 공간의 후보 링크도 `when` 을 갖는다
CHUNK_DIRS = ("kb", "chunks")
MEMORY_DIR = "kb/dev/memory"
ODD_IRI = str(ID["odd-agentic-knowledge-base"])  # 관측의 출처 — ODD 개체 (base-kg 에 doc- 개체가 없다)
DEFAULT_ASSUMPTION = str(ID["asm-chunk-conventions"])
GENERATOR = kb_lib.ASSUME_CHECK_GENERATOR  # 관측의 generated.by — 정의처는 kb_lib (weave audit · metrics 가 같은 값으로 관측을 고른다)


def resolve(path: str, root: Path) -> Path | None:
    for cand in (Path(path), root / "bazel-bin" / path, root / path):
        if cand.is_file():
            return cand
    return None


def local(iri) -> str:
    return str(iri)[len(str(ID)):] if str(iri).startswith(str(ID)) else str(iri)


def worst_grade(grades: list[str]) -> str:
    known = [g for g in grades if g in GRADES]
    if not known or len(known) != len(grades):
        return "?"
    return max(known, key=GRADES.index)


def label_of(g: Graph, node) -> str:
    ko = next((str(l) for l in g.objects(node, RDFS.label) if getattr(l, "language", None) == "ko"), None)
    return ko or next((str(l) for l in g.objects(node, RDFS.label)), local(node))


def load_graph(paths: list[str], root: Path) -> tuple[Graph, list[str]]:
    g, missing = Graph(), []
    for p in paths:
        f = resolve(p, root)
        if f is None:
            missing.append(p)
            continue
        g.parse(str(f), format="turtle")
    return g, missing


def dependents(g: Graph) -> dict:
    """청크 → 그 청크를 가리키는 링크의 주어들 (하류 의존자). 직접 트리플과 agt:Link 개체(linkFrom·linkTo·linkKind) 둘 다."""
    rdep = defaultdict(set)
    kinds = set(PROPAGATE)
    for p in PROPAGATE:
        for s, o in g.subject_objects(p):
            rdep[o].add(s)
            if p in (AGT.coUpdatesWith, AGT.overlapsWith):  # 대칭 — 함께 갱신되는 쌍은 양쪽이 서로의 하류다
                rdep[s].add(o)
    for link in g.subjects(RDF.type, AGT.Link):
        k = next(g.objects(link, AGT.linkKind), None)
        if k not in kinds:
            continue
        f, t = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        if f is not None and t is not None:
            rdep[t].add(f)
    return rdep


def propagate(g: Graph, direct: set, live: set) -> tuple[set, set]:
    """직접 영향 집합에서 하류로 전이 폐포 + 복합체 형제 → (1홉 suspect 후보, 전이 suspect 후보). 둘 다 직접 집합을 뺀 살아 있는 청크."""
    rdep = dependents(g)
    comp_of = {part: comp for comp, part in g.subject_objects(AGT.hasDirectPart)}
    siblings = defaultdict(set)
    for part, comp in comp_of.items():
        siblings[comp].add(part)

    def step(x):
        out = set(rdep.get(x, ()))
        if x in comp_of:
            out |= siblings[comp_of[x]]
        return out

    hop1 = set().union(*(step(x) for x in direct)) if direct else set()
    seen, stack = set(direct), list(direct)
    while stack:
        x = stack.pop()
        for y in step(x):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return (hop1 - direct) & live, (seen - direct) & live


def actual_dependents(root: Path, assumption: str) -> tuple[set, list[str]]:
    """실제 의존 집합 — 청크 파일의 frontmatter `assumes` 를 그래프와 독립적으로 스캔한다 (살아 있는 청크만)."""
    found, unparsable = set(), []
    for d in CHUNK_DIRS:
        for p in sorted((root / d).rglob("*.md")):
            try:
                meta = parse_chunk(str(p))[0]
            except ValueError as e:
                if "frontmatter가 없다" not in str(e):  # frontmatter 없는 md(README)는 청크가 아니다
                    unparsable.append(str(e))
                continue
            if meta.get("status") != "deprecated" and assumption in (meta.get("assumes") or []):
                found.add(URIRef(meta["id"]))
    return found, unparsable


def evaluate(g: Graph, cond_rows: list[dict]) -> list[dict]:
    """가정마다 상태·등급·유형·참조 조건 — 판정식은 참조 조건 판정의 연언이다."""
    by_iri = {r["iri"]: r for r in cond_rows}
    out = []
    for asm in sorted(g.subjects(RDF.type, AGT.Assumption), key=str):
        conds = sorted((str(c) for c in g.objects(asm, AGT.refersTo)), key=str)
        rows = [by_iri.get(c) for c in conds]
        states = [r["state"] if r else "unverified" for r in rows]  # ODD 문서에 없는 조건은 판정 불가
        status = "invalidated" if "out" in states else "valid" if states and all(s == "in" for s in states) else "unverified"
        cmds = [bool(r and r["cmd"]) for r in rows]
        kind = "실행 검사" if cmds and all(cmds) else "사람 확인" if not any(cmds) else "실행 검사·사람 확인"
        out.append({"iri": asm, "label": label_of(g, asm), "conds": conds, "states": states, "status": status, "kind": kind,
                    "grade": worst_grade([r["grade"] if r else "?" for r in rows]),
                    "expr": " ∧ ".join(f"in({local(c)})" for c in conds) or "(참조 조건 없음)"})
    return out


def observation(now: datetime, cond_rows: list[dict], asms: list[dict], impact: dict, live_n: int, broke: list[str],
                broke_show: list[str], check: dict | None, sat: dict) -> str:
    """관측 청크 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory). 42줄 안이다."""
    stamp = kb_lib.utc_stamp(now)  # G3 표기 하나 — frontmatter 와 본문이 같은 꼴을 쓴다 (유저 승인 2026-09-23)
    n_inv = sum(1 for a in asms if a["status"] == "invalidated")
    n_unv = sum(1 for a in asms if a["status"] == "unverified")
    total_direct = len(set().union(*(impact[a["iri"]][0] for a in asms)) if asms else set())
    ko = f"가정 판정 {stamp}: 가정 {len(asms)} · 무효 {n_inv}"
    en = f"Assumption check {stamp}: {len(asms)} assumptions, {n_inv} invalidated"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{DEFAULT_ASSUMPTION}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    act = (f"`--break {' '.join(broke_show)}` 로 조건 {len(broke)}건을 이탈로 가정한 인위 파괴 실험이다" if broke
           else "`--break` 없는 실측이다")
    body = [f"**관측** — {stamp} 에 `assume_check` 가 ODD 조건 {len(cond_rows)}건을 판정하고 "
            f"가정 {len(asms)}건의 상태를 계산했다. {act}.", "",
            "| 조건 | 등급 | 판정 |", "|---|---|---|"]
    body += [f"| `{local(r['iri'])}` | {r['grade']} | {r['state']}{' (--break)' if r['name'] in broke else ''} |" for r in cond_rows]
    body += ["", "| 가정 | 판정 유형 | 등급 | 상태 | 직접 영향 | suspect 후보(전이) |", "|---|---|---|---|---|---|"]
    body += [f"| `{local(a['iri'])}` | {a['kind']} | {a['grade']} | {a['status']} | {len(impact[a['iri']][0])} | {len(impact[a['iri']][2])} |"
             for a in asms]
    body += ["", f"situation 요약 — 살아 있는 청크 {live_n}, 무효 가정 {n_inv}, 판정 불가 가정 {n_unv}, 직접 영향 집합 {total_direct}.",
             f"링크 요약 — 확정 링크 {sat['confirmed']}, `when` 을 가진 것 {sat['with_when']}, suspect 포화율 "
             f"{kb_lib.pct(sat['suspect'], sat['confirmed'])} (`when` 거짓 {sat['by_when']}, 트리거 {sat['by_trigger']})."]
    if check:
        body.append(f"검증 실험 — 계산된 직접 영향 집합 {check['computed']} 대 실제 의존 집합(frontmatter 스캔) {check['actual']}: "
                    f"정밀도 {check['precision']}, 재현율 {check['recall']}, {'일치' if check['equal'] else '불일치'}.")
    return "\n".join(head + body) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--odd", default="kb/odd/project-odd.yml", help="OpenODD 문서 (워크스페이스 상대)")
    ap.add_argument("--break", dest="broken", action="append", default=[], metavar="COND",
                    help="이 조건(id:cond-… 의 슬러그 또는 ODD 속성명)을 out 으로 가정한다 — 인위 파괴 실험. 반복 가능")
    ap.add_argument("--record", action="store_true", help=f"결과를 관측으로 {MEMORY_DIR}/obs-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("ttl", nargs="*", help=f"그래프 TTL (기본: {' '.join(DEFAULT_TTL)})")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    now = datetime.now(timezone.utc).replace(microsecond=0)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [assume_check] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG

    odd_path = root / a.odd
    if not odd_path.is_file():
        print(f"FAIL [assume_check] {a.odd}: ODD 문서가 없다")
        return EXIT_CONFIG
    doc = load_odd(odd_path)
    attrs = doc.get("ATTRIBUTES") or {}
    by_slug = {str(v.get("iri", "")).replace("id:", ""): k for k, v in attrs.items()}  # cond-… → 속성명
    forced, unknown = {}, []
    for b in a.broken:
        name = b if b in attrs else by_slug.get(b)
        if name:
            forced[name] = "out"
        else:
            unknown.append(b)
    if unknown:
        print(f"FAIL [assume_check] --break 대상이 ODD 에 없다: {', '.join(unknown)} — ODD 조건(id:cond-…)만 깨뜨릴 수 있다 (0.4절)")
        return EXIT_CONFIG
    g, missing = load_graph(a.ttl or DEFAULT_TTL, root)
    if missing:
        print(f"FAIL [assume_check] 그래프를 찾을 수 없다: {', '.join(missing)} — bazel run //tools:assume_check 로 돌리면 data 로 놓인다")
        return EXIT_CONFIG

    cond_rows = judge_all(doc, root, forced)
    asms = evaluate(g, cond_rows)
    chunks = set(g.subjects(AGT.lineCount, None))
    live = {c for c in chunks if str(next(g.objects(c, AGT.status), "")) != "deprecated"}
    impact = {}
    for asm in asms:
        direct = {c for c in g.subjects(AGT.assumes, asm["iri"]) if c in live} if asm["status"] == "invalidated" else set()
        hop1, trans = propagate(g, direct, live) if direct else (set(), set())
        impact[asm["iri"]] = (direct, hop1, trans)
    broke_names = list(forced)
    broke_show = [str((attrs.get(n) or {}).get("iri", n)).replace("id:", "") for n in broke_names]  # 보고에는 조건 id 로
    check = None
    if broke_names:  # 검증 실험 — 깨진 가정 전부의 계산된 직접 영향 집합 vs frontmatter 스캔의 실제 의존 집합
        computed = set().union(*(impact[x["iri"]][0] for x in asms if x["status"] == "invalidated")) if asms else set()
        actual, unparsable = set(), []
        for x in asms:
            if x["status"] == "invalidated":
                found, bad = actual_dependents(root, str(x["iri"]))
                actual |= found
                unparsable += bad
        tp = len(computed & actual)
        check = {"computed": len(computed), "actual": len(actual), "equal": computed == actual, "unparsable": unparsable,
                 "precision": f"{tp}/{len(computed)}", "recall": f"{tp}/{len(actual)}",
                 "only_computed": sorted(local(x) for x in computed - actual), "only_actual": sorted(local(x) for x in actual - computed)}

    # 링크 상태의 물질화 — 저장하지 않고 여기서만 계산한다 (노트 9.11절)
    states = kb_lib.odd_states(cond_rows)
    when_false, when_unverified = kb_lib.suspect_by_when(g, states)
    by_trigger = kb_lib.suspect_by_trigger(g)
    sat = kb_lib.suspect_saturation(g, when_false)
    space_rows = []  # `-space` 의 양립 제약 — 링크의 when 과 같은 식 언어다 (space-ontology agt:compatibilityConstraint)
    for sp in sorted(g.subjects(AGT.spaceStatus, None), key=str):
        for c in sorted((str(x) for x in g.objects(sp, AGT.compatibilityConstraint)), key=str):
            verdict_c, left_c = kb_lib.when_eval(c, states)
            space_rows.append((local(sp), c, verdict_c, left_c))

    # 보고
    n_inv = sum(1 for x in asms if x["status"] == "invalidated")
    n_unv = sum(1 for x in asms if x["status"] == "unverified")
    verdict = ("**무효 가정 있음**" if n_inv else "**`when` 이 거짓인 링크 있음**" if when_false
               else "판정 불가 가정 있음 (unverified)" if n_unv else "정상 — 모든 가정이 valid")
    broke_note = (f" · 인위 파괴 `--break {' '.join(broke_show)}`" if broke_names else "")
    rep = kb_lib.gendoc_header(
        "assume_check", "가정 판정과 전파", "tools/assume_check.py",
        f"ODD 조건을 판정 방법으로 실제 판정한 뒤, 가정마다 그 참조 조건 판정의 연언으로 valid·invalidated·unverified 를 정하고 "
        f"깨진 가정을 `assumes` 하는 살아 있는 청크(직접 영향)와 그 하류(suspect 후보)를 낸다 (6.9절){broke_note}",
        "bazel run //tools:assume_check", [str(odd_path)] + [str(root / f) for f in (a.ttl or DEFAULT_TTL)],
        f"가정 {len(asms)} · 살아 있는 청크 {len(live)}",
        kb_lib.gendoc_view_notice("ODD 조건 정의와 청크의 `assumes` 링크"),
        extra=[f"- 결과: {verdict} · 가정 {len(asms)} (valid {len(asms) - n_inv - n_unv} · invalidated {n_inv} · unverified {n_unv})",
               f"- 링크: 확정 {sat['confirmed']} · `when` 을 가진 것 {sat['with_when']} · suspect 로 유도된 것 "
               f"**{kb_lib.pct(sat['suspect'], sat['confirmed'])}** (`when` 거짓 {sat['by_when']} · 트리거 {sat['by_trigger']})"])
    inputs = [str(odd_path)] + [str(root / f) for f in (a.ttl or DEFAULT_TTL)]
    body = ["## 조건 판정 (odd_check 와 같은 판정)", "", "| 조건 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"]
    body += [f"| `{local(r['iri'])}` | {r['title_ko']} | {r['grade']} | {r['state']}{' (--break)' if r['name'] in broke_names else ''} |" for r in cond_rows]
    body += ["", "## 가정 — 판정식은 참조 조건 판정의 연언, 등급은 그 최저", "",
            "| 가정 | 판정 유형 | 판정식 | 등급 | 상태 | assumes 하는 살아 있는 청크 | 직접 영향 | suspect 후보 (1홉 / 전이) |",
            "|---|---|---|---|---|---|---|---|"]
    for x in asms:
        n_assumes = sum(1 for c in g.subjects(AGT.assumes, x["iri"]) if c in live)
        d, h1, tr = impact[x["iri"]]
        body.append(f"| `{local(x['iri'])}` {x['label']} | {x['kind']} | {x['expr']} | {x['grade']} | **{x['status']}** | {n_assumes} | {len(d)} | {len(h1)} / {len(tr)} |")
    for x in asms:
        d, h1, tr = impact[x["iri"]]
        if not d:
            continue
        body += ["", f"### 직접 영향 집합 — `{local(x['iri'])}` ({len(d)}건, suspect 후보 전이 {len(tr)}건)", ""]
        body += [f"- {label_of(g, c)} (`{local(c)}`)" for c in sorted(d, key=lambda c: label_of(g, c))[:40]]
        if len(d) > 40:
            body.append(f"- … 외 {len(d) - 40}건")
    body += ["", "## 링크 상태의 물질화 — `when` 판정과 트리거 (노트 9.11절: 상태는 저장값이 아니라 평가 결과)", "",
             f"- `when` 판정의 범위: {kb_lib.WHEN_GRAMMAR}. 그 밖의 구문은 판정하지 않고 unverified 로 남긴다 (0.4절 restrictive)",
             f"- 확정 링크 {sat['confirmed']} 중 `when` 을 가진 것 {sat['with_when']} · suspect 로 유도된 것 "
             f"**{kb_lib.pct(sat['suspect'], sat['confirmed'])}** — `when` 거짓 {sat['by_when']} · 트리거 {sat['by_trigger']} · 판정 불가 {len(when_unverified)}",
             "", "| 트리거 (링크 종류) | 전파 규칙 | 켜짐 | 근거 |", "|---|---|---|---|"]
    body += [f"| `{k}` | {rule} | {'켜짐' if on else '꺼짐'} | {basis} |" for k, rule, on, basis in kb_lib.SUSPECT_TRIGGERS]
    body += ["", "선언에 없는 링크 종류는 돌지 않는다 — 기본이 꺼짐이다. 선언의 원본은 `tools/kb_lib.py` 의 `SUSPECT_TRIGGERS` 다.", ""]
    rows = [(l, k, st, dv or kb_lib.NONE_MARK, why) for l, k, st, _v, dv, why in kb_lib.when_verdicts(g, states)]
    rows += [(l, str(next(g.objects(l, AGT.linkKind), "")).split("/")[-1], kb_lib.LINK_STATE_CONFIRMED,
              kb_lib.LINK_STATE_SUSPECT, why) for l, why in sorted(by_trigger.items(), key=lambda kv: str(kv[0]))]
    body += ["| 링크 | 종류 | 저장 상태 | 유도 상태 | 사유 |", "|---|---|---|---|---|"]
    body += [f"| `{local(l)}` | `{k or kb_lib.NONE_MARK}` | {st or kb_lib.NONE_MARK} | {dv} | {why} |" for l, k, st, dv, why in rows[:40]] \
            or [f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | `when` 을 가졌거나 트리거가 지목한 링크 {kb_lib.NONE_MARK} |"]
    if len(rows) > 40:
        body.append(f"| … | … | … | … | 외 {len(rows) - 40}건 |")
    body += ["", "| 설계 공간 | 양립 제약 | 판정 | 남긴 것 |", "|---|---|---|---|"]
    body += [f"| `{sp}` | `{c}` | {v} | {' · '.join(lft) or kb_lib.NONE_MARK} |" for sp, c, v, lft in space_rows] \
            or [f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 양립 제약 {kb_lib.NONE_MARK} |"]
    body.append("")  # 표 뒤의 빈 줄 (G 규약) — 뒤따르는 절이 없을 때도 표가 닫힌다
    if check:
        body += ["", "## 검증 실험 — 계산된 영향 집합 = 실제 의존 집합 (14.1 정정본 4단계 연결 조건)", "",
                f"- 계산된 직접 영향 집합(그래프 `agt:assumes`): **{check['computed']}** · 실제 의존 집합(청크 파일 frontmatter `assumes` 스캔): **{check['actual']}**",
                f"- 정밀도 {check['precision']} · 재현율 {check['recall']} → **{'일치' if check['equal'] else '불일치'}**"]
        if check["only_computed"]:
            body.append("- 그래프에만 있는 것: " + ", ".join(check["only_computed"][:10]))
        if check["only_actual"]:
            body.append("- 파일에만 있는 것: " + ", ".join(check["only_actual"][:10]))
        if check["unparsable"]:
            body.append(f"- 판독 불가 파일 {len(check['unparsable'])}건: " + " · ".join(check["unparsable"][:3]))
    if n_inv:
        body += ["", "무효 가정의 직접 영향 집합은 `invalidated`, suspect 후보는 `suspect` 표시 대상이다 — 표시는 재검증 시점에 일괄로 한다 (method §7). 삭제가 아니다."]
    text = kb_lib.gendoc_assemble(rep, body, inputs)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")

    if a.record:
        mem = root / MEMORY_DIR
        mem.mkdir(parents=True, exist_ok=True)
        target = mem / f"obs-{now.strftime('%Y%m%dT%H%M%SZ')}.md"
        if target.exists():
            print(f"FAIL [assume_check] {target.relative_to(root)}: 이미 있다 — 관측은 append-only 다 (r-026)")
            return EXIT_CONFIG
        target.write_text(observation(now, cond_rows, asms, impact, len(live), broke_names, broke_show, check, sat), encoding="utf-8")
        print(f"관측 기록: {target.relative_to(root)} — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    return EXIT_FAIL if (n_inv or when_false) else EXIT_SKIP if (n_unv or when_unverified) else EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
