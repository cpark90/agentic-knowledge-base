#!/usr/bin/env python3
"""믿음 정도 계산 규칙의 보정 측정 — 사람 정답 라벨 표본에서 규칙마다 Brier 점수와 구간별 이항 구간을 계산해 belief-calibration.md 를 생성한다
(합격 기준 belief-calibrated-against-human-labels, 설계 공간 degree-of-belief-space 의 닫기 기준, 유저 결정 Q181-a·Q182-a).

  표본  관측 기록 `kb/vv/run/label-*.md` 의 라벨 표(`문항` · `링크 IRI` · `라벨` · `지위` 열)의 행 하나가 항목 하나다. 라벨은 1 또는 0 이고,
        지위가 '독립'으로 시작하면 독립 사람 라벨이다(Q178-b). 같은 링크 IRI 가 두 행에 나오면 설정 문제로 끝난다.
  규칙 C judge-mean  판정 로그(`kb/vv/run/judge-*.md`, generated.by `process:judge`)의 쌍 행(`대상` 이 `<출발> ↔ <도착> · <종류>`)마다
        링크 IRI 를 chunk2kg 의 규칙대로 계산한다 — `link_hash(뿌리(출발), 종류, 뿌리(도착))`, 뿌리는 head 그래프의 `prov:specializationOf`
        사슬 끝(chunk2kg.work_id)이다. 옛 결정 IRI(`…/id/chunk-dNNNN`)는 사슬에 없으므로 그대로 해시되고, 라벨 기록의 링크 IRI 도 양 끝의
        전체 IRI 로 계산했으므로(기록 본문) 같은 값이 된다. 항목의 값은 그 링크 IRI 에 결합된 판정 행의 확신도('예'의 확률) 평균이고
        run_evidence.belief_of 의 C 정의를 그대로 부른다. 같은 (판정 로그, 판정자, 극성, 확신도)는 run_evidence 처럼 한 번 센다.
        판정 증거와 달리 입력 해시값으로 낡은 판정을 거르지 않는다 — 라벨은 표본 당시 주장의 판단이고 옛 끝점 파일은 지금 없어서,
        결합 열쇠는 양 끝 IRI 와 종류로 만든 링크 IRI 하나다(Q182-a). 링크 종류 어휘로도 거르지 않는다 — 표본에는 `cites` 가 있다.
        C 는 보정 전 값이다(결정 p9-belief-by-calibrated-judge — 보정은 확신도 구간마다 표본 하한 20을 채운 뒤에 적용한다).
  규칙 A kind-rank · B beta-binomial  그래프의 `agt:DegreeOfBelief` 노드(링크의 `agt:hasDegreeOfBelief`, `agt:beliefRule`, `agt:beliefValue`)
        에서 표본의 링크 IRI 와 같은 링크의 값만 읽는다. 값이 없는 항목은 그 규칙의 표본에서 빠지고, 다른 링크(뒤이은 링크)의 값을 빌려 오지
        않는다(Q182-a). 규칙 IRI → slug 는 run_evidence.BELIEF_RULES 다.
  계산  규칙마다 값이 있는 항목 n 개로 계산한다. 값과 라벨은 분수(fractions.Fraction)로 계산해 비교에 반올림이 끼지 않는다.
        술어 1  B(R) = mean (p_i − y_i)² 이 기저율 Brier mean (ȳ − y_i)² 보다 작으면 참이고 같으면 거짓이다. ȳ 는 같은 n 항목의 참 비율이다.
        술어 2  n < 50 이면 구간은 [0, 1/3) · [1/3, 2/3) · [2/3, 1] 셋이다. 경계값 1/3 은 둘째 구간, 2/3 은 셋째 구간, 1 은 셋째 구간에 든다.
                n ≥ 50 의 구간 수는 합격 기준이 정하지 않았으므로 이 도구는 판정하지 않고 그 사실을 낸다. 표본이 있는 구간 k 마다 n_k ·
                평균 예측 p̄_k · 관측 빈도 ō_k 를 내고, 허용폭은 Binomial(n_k, p̄_k) 의 2.5% 분위수 lo 와 97.5% 분위수 hi 를 n_k 로 나눈
                [lo/n_k, hi/n_k] 다. 분위수 q 는 F(x) ≥ q 인 가장 작은 정수 x 이고(F 는 정확 이항 누적분포, 순수 파이썬 분수 계산), 구간은
                닫힌 구간이라 성공 수가 lo 이상 hi 이하이면 든다. 한 구간이라도 벗어나면 거짓이다.
        술어 3  게이트 `belief-consistency` 의 PASS 다. 이 도구는 판정하지 않고 입력으로 받지 않는다.
        n < 20 인 규칙은 '표본 부족'으로 내고 판정하지 않는다 — 값은 참고로 따로 낸다. 술어 1·2가 참인 규칙 가운데 B(R)가 가장 작은 규칙이 선택이다.
        독립 사람 라벨만으로 같은 계산을 병기하되 판정에 쓰지 않는다(Q178-b).
  판정  없음 — 뷰이고 게이트가 아니다. 설계 공간을 닫는 일은 orchestrator 가 이 생성물을 인용해 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(라벨 기록 없음·라벨 표를 읽지 못함·같은 링크 IRI 의 두 행·그래프 파싱 실패)
사용: belief_calibration.py --out belief-calibration.md --records <kb/vv/run 의 .md …> --graphs <head·참조 그래프 TTL …>   (bazel build //kg:belief_calibration)
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import PROV

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.chunk2kg import ID_BASE, SpecializationError, link_hash, work_id
    from tools.run_evidence import BELIEF_RULES, belief_of
except ImportError:
    import kb_lib
    from chunk2kg import ID_BASE, SpecializationError, link_hash, work_id
    from run_evidence import BELIEF_RULES, belief_of

AGT = kb_lib.AGT
LABEL_PREFIX = "label-"                  # 사람 라벨 관측 기록의 파일명 접두 — 판정 로그(judge-)·실행 기록(run-)과 한 디렉토리에서 갈린다
LABEL_COLUMNS = ("문항", "링크 IRI", "라벨", "지위")  # 라벨 표에서 읽는 열 — 그 밖의 열은 읽기 위한 열이다
INDEPENDENT = "독립"                      # 지위 열의 독립 사람 라벨 표시 (Q178-b) — '확인'·'확인(약함)'은 hci 권장 뒤 사람 확인이다
RULE_ORDER = (("kind-rank", "A"), ("beta-binomial", "B"), ("judge-mean", "C"))   # 설계 공간 후보의 순서
RULE_DECISION = {"kind-rank": "p9-belief-by-evidence-kind-rank", "beta-binomial": "p9-belief-by-beta-binomial",
                 "judge-mean": "p9-belief-by-calibrated-judge"}
SAMPLE_MIN = 20                          # 합격 기준의 표본 하한 |S| ≥ 20
BINS_UNDER = 50                          # |S| < 50 이면 구간 셋 (합격 기준 술어 2)
BINS = ((Fraction(0), Fraction(1, 3), "[0, 1/3)"), (Fraction(1, 3), Fraction(2, 3), "[1/3, 2/3)"), (Fraction(2, 3), Fraction(1), "[2/3, 1]"))
Q_LO, Q_HI = Fraction(1, 40), Fraction(39, 40)   # 95% 구간의 양쪽 분위수 2.5% · 97.5%
CALIBRATION_MIN = 20                     # C 의 보정을 적용하는 확신도 구간당 표본 하한 (결정 p9-belief-by-calibrated-judge)
_GENERATED_BY = re.compile(r"^generated:\s*\{[^}]*?\bby:\s*([^,}\s]+)", re.MULTILINE)


def fail(msg: str) -> int:
    print(f"FAIL [belief-calibration] {msg}", file=sys.stderr)
    return kb_lib.EXIT_CONFIG


# ── 입력 읽기 — 라벨 표 · 판정 행 · 그래프의 믿음 정도 ────────────────────

def label_rows(path: Path) -> list[dict]:
    """라벨 기록 하나 → 항목들 [{문항, 링크 IRI, 라벨(int), 독립(bool), 기록}]. 표 머리가 LABEL_COLUMNS 를 모두 갖는 첫 표를 읽는다.
    표가 없거나 라벨이 0·1 이 아니면 ValueError 다."""
    lines = kb_lib.chunk_body(path.read_text(encoding="utf-8")).split("\n")
    for i, line in enumerate(lines):
        cols = [c.strip() for c in line.strip().split("|")[1:-1]] if line.strip().startswith("|") else []
        if not all(c in cols for c in LABEL_COLUMNS):
            continue
        rows = []
        for row in lines[i + 2:]:
            if not row.strip().startswith("|"):
                break
            cells = dict(zip(cols, (c.strip().strip("`").strip() for c in row.strip().split("|")[1:-1])))
            if cells.get("라벨") not in ("0", "1"):
                raise ValueError(f"{path}: 문항 {cells.get('문항')} 의 라벨 {cells.get('라벨')!r} 이 0 또는 1 이 아니다")
            rows.append({"문항": cells["문항"], "link": cells["링크 IRI"], "y": int(cells["라벨"]),
                         "independent": cells["지위"].startswith(INDEPENDENT), "record": path})
        return rows
    raise ValueError(f"{path}: 라벨 표(열 {' · '.join(LABEL_COLUMNS)})가 없다")


def judgement_entries(paths: list[Path], spec: dict) -> tuple[dict, dict]:
    """판정 로그들 → (링크 IRI → [(종류, 극성, 확신도 Fraction)], 링크 IRI → 판정 로그 이름 집합). 쌍 행이 아니거나 값이 yes·no 가 아니거나
    확신도를 읽지 못한 행은 건너뛴다. 같은 (판정 로그, 판정자, 극성, 확신도)는 한 번 센다(run_evidence.judgement_lines 와 같다)."""
    seen: dict[str, set] = defaultdict(set)
    logs: dict[str, set] = defaultdict(set)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        m = _GENERATED_BY.search(text)
        if not m or m.group(1) != kb_lib.JUDGE_GENERATOR:
            continue
        for row in kb_lib.judge_log_rows(text):
            pair = kb_lib.parse_pair_target(row["대상"])
            pol = kb_lib.JUDGE_NOUL_POLARITY.get(row["값"])
            if pair is None or pol is None or not kb_lib.JUDGE_CONFIDENCE.match(row.get("확신도", "")):
                continue
            a, b, kind = pair
            link = f"{ID_BASE}link/{link_hash(work_id(a, spec), kind, work_id(b, spec))}"
            seen[link].add((path.name, row["판정자 식별자"], pol, Fraction(row["확신도"])))
            logs[link].add(path.name)
    return {k: [("agt:judgement", pol, conf) for _, _, pol, conf in sorted(v)] for k, v in seen.items()}, logs


def graph_beliefs(g: Graph) -> dict[tuple[str, str], Fraction]:
    """그래프 → (링크 IRI, 규칙 slug) → 값. 규칙 IRI 가 BELIEF_RULES 밖이면 읽지 않는다. 같은 칸에 값이 둘이면 ValueError 다."""
    slug_of = {v: k for k, v in BELIEF_RULES.items()}
    out: dict[tuple[str, str], Fraction] = {}
    for link, node in g.subject_objects(AGT.hasDegreeOfBelief):
        rule, value = g.value(node, AGT.beliefRule), g.value(node, AGT.beliefValue)
        slug = slug_of.get(str(rule))
        if slug is None or value is None:
            continue
        key = (str(link), slug)
        v = Fraction(str(value))
        if key in out and out[key] != v:
            raise ValueError(f"링크 {link} 의 규칙 {slug} 값이 둘이다 ({out[key]} · {v})")
        out[key] = v
    return out


# ── 계산 — Brier · 구간 · 정확 이항 분위수 ────────────────────

def binom_quantile(n: int, p: Fraction, q: Fraction) -> int:
    """Binomial(n, p) 의 q 분위수 — 누적분포 F(x) ≥ q 인 가장 작은 정수 x. 분수로 정확히 계산한다(외부 의존 없음)."""
    acc = Fraction(0)
    for x in range(n + 1):
        acc += comb(n, x) * p ** x * (1 - p) ** (n - x)
        if acc >= q:
            return x
    return n


def bin_of(p: Fraction) -> int:
    """값 → 구간 번호. [0, 1/3) · [1/3, 2/3) · [2/3, 1] — 경계값은 위 구간에 든다."""
    return 0 if p < BINS[1][0] else 1 if p < BINS[2][0] else 2


def measure(pairs: list[tuple[Fraction, int]]) -> dict:
    """[(p_i, y_i)] → 측정 하나. n 이 0 이면 {'n': 0} 이다."""
    n = len(pairs)
    if not n:
        return {"n": 0}
    ybar = Fraction(sum(y for _, y in pairs), n)
    brier = sum((p - y) ** 2 for p, y in pairs) / n
    base = sum((ybar - y) ** 2 for _, y in pairs) / n
    bins = []
    for k, (_, _, name) in enumerate(BINS):
        items = [(p, y) for p, y in pairs if bin_of(p) == k]
        if not items:
            bins.append({"name": name, "n": 0})
            continue
        nk, hits = len(items), sum(y for _, y in items)
        pbar = sum(p for p, _ in items) / nk
        lo, hi = binom_quantile(nk, pbar, Q_LO), binom_quantile(nk, pbar, Q_HI)
        bins.append({"name": name, "n": nk, "pbar": pbar, "hits": hits, "lo": lo, "hi": hi, "inside": lo <= hits <= hi})
    p2 = all(b["inside"] for b in bins if b["n"]) if n < BINS_UNDER else None
    return {"n": n, "pos": sum(y for _, y in pairs), "ybar": ybar, "brier": brier, "base": base, "p1": brier < base, "p2": p2, "bins": bins}


# ── 출력 ────────────────────

def truth(v) -> str:
    return kb_lib.NONE_MARK if v is None else ("참" if v else "거짓")


def summary_rows(results: dict, judged: bool) -> list[str]:
    """규칙별 요약 표. judged 가 거짓이면(독립 라벨 병기) 판정 열이 '판정에 쓰지 않는다'다."""
    out = ["| 규칙 | 결정 | 값이 있는 항목 n | 참 비율 ȳ | B(R) | 기저율 Brier | 술어 1 | 술어 2 | 술어 1·2 판정 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for slug, letter in RULE_ORDER:
        r = results[slug]
        name = f"{letter} `{slug}`"
        if not r["n"]:
            out.append(f"| {name} | `{RULE_DECISION[slug]}` | 0 | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | "
                       f"{kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {'표본 부족 — 판정하지 않는다' if judged else '판정에 쓰지 않는다'} |")
            continue
        if not judged:
            verdict = "판정에 쓰지 않는다"
        elif r["n"] < SAMPLE_MIN:
            verdict = f"표본 부족(n < {SAMPLE_MIN}) — 판정하지 않는다"
        elif r["p2"] is None:
            verdict = f"구간 규칙 없음(n ≥ {BINS_UNDER}) — 판정하지 않는다"
        else:
            verdict = "합격" if r["p1"] and r["p2"] else "불합격"
        p2 = truth(r["p2"]) if r["p2"] is not None else f"구간 규칙 없음(n ≥ {BINS_UNDER})"
        out.append(f"| {name} | `{RULE_DECISION[slug]}` | {r['n']} | {kb_lib.pct(r['pos'], r['n'])} | {kb_lib.num(float(r['brier']))} | "
                   f"{kb_lib.num(float(r['base']))} | {truth(r['p1'])} | {p2} | {verdict} |")
    return out + [""]


def bin_rows(r: dict) -> list[str]:
    out = ["| 구간 | n_k | 평균 예측 p̄_k | 관측 빈도 ō_k | 성공 수 | 이항 구간 0.95 [lo/n_k, hi/n_k] | 안에 드는가 |",
           "|---|---|---|---|---|---|---|"]
    for b in r["bins"]:
        if not b["n"]:
            out.append(f"| {b['name']} | 0 | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 표본 없음 |")
            continue
        out.append(f"| {b['name']} | {b['n']} | {kb_lib.num(float(b['pbar']))} | {kb_lib.num(b['hits'] / b['n'])} | {b['hits']}/{b['n']} | "
                   f"[{kb_lib.num(b['lo'] / b['n'])}, {kb_lib.num(b['hi'] / b['n'])}] (성공 수 {b['lo']}~{b['hi']}) | {truth(b['inside'])} |")
    return out + [""]


def bins_section(title: str, results: dict, note: str) -> list[str]:
    out = [f"## {title}", "", note, ""]
    for slug, letter in RULE_ORDER:
        r = results[slug]
        out += [f"### {letter} `{slug}`", ""]
        out += bin_rows(r) if r["n"] else ["값이 있는 항목이 없다.", ""]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--records", nargs="+", required=True, help="kb/vv/run 의 .md — label-*.md 는 라벨 표, judge-*.md 는 판정 로그로 읽는다")
    ap.add_argument("--graphs", nargs="+", required=True, help="head·참조 그래프 TTL — prov:specializationOf 와 agt:DegreeOfBelief 를 읽는다")
    a = ap.parse_args()

    records = [Path(p) for p in a.records if p.endswith(".md")]
    label_files = sorted(p for p in records if p.name.startswith(LABEL_PREFIX))
    judge_files = sorted(p for p in records if p.name.startswith(kb_lib.JUDGE_LOG_PREFIX))
    if not label_files:
        return fail(f"라벨 기록({LABEL_PREFIX}*.md)이 입력에 없다 — 표본 없이 보정을 잴 수 없다")
    items: list[dict] = []
    try:
        for p in label_files:
            items += label_rows(p)
    except (OSError, ValueError) as e:
        return fail(str(e))
    dup = sorted({it["link"] for it in items if sum(1 for o in items if o["link"] == it["link"]) > 1})
    if dup:
        return fail(f"같은 링크 IRI 가 라벨 표의 두 행에 있다: {' · '.join(dup)} — 항목 하나는 링크 하나다")

    g = Graph()
    try:
        for p in a.graphs:
            g.parse(p, format="turtle")
        beliefs = graph_beliefs(g)
    except Exception as e:  # rdflib 의 파싱 예외는 형이 여럿이다
        return fail(f"그래프를 읽지 못했다: {e}")
    spec = {str(s): str(o) for s, o in g.subject_objects(PROV.specializationOf)}
    try:
        judged, judge_logs = judgement_entries(judge_files, spec)
    except (OSError, SpecializationError) as e:
        return fail(str(e))

    values: dict[str, dict[str, Fraction]] = {it["link"]: {} for it in items}
    for it in items:
        for slug in ("kind-rank", "beta-binomial"):
            if (it["link"], slug) in beliefs:
                values[it["link"]][slug] = beliefs[(it["link"], slug)]
        if it["link"] in judged:
            values[it["link"]]["judge-mean"] = belief_of(judged[it["link"]])["judge-mean"][0]

    def results_for(subset: list[dict]) -> dict:
        return {slug: measure([(values[it["link"]][slug], it["y"]) for it in subset if slug in values[it["link"]]]) for slug, _ in RULE_ORDER}

    full = results_for(items)
    indep_items = [it for it in items if it["independent"]]
    indep = results_for(indep_items)
    passed = sorted((full[s]["brier"], s) for s, _ in RULE_ORDER
                    if full[s]["n"] >= SAMPLE_MIN and full[s]["p1"] and full[s]["p2"])
    letter = dict(RULE_ORDER)

    lines = ["## 판정 요약", "",
             f"표본은 라벨 기록 {len(label_files)}개의 항목 {len(items)}건이고, 규칙마다 값이 있는 항목만 그 규칙의 표본이다. "
             f"값이 있는 항목이 {SAMPLE_MIN}건 미만인 규칙은 판정하지 않고 값만 참고로 낸다.", ""]
    lines += summary_rows(full, judged=True)
    lines += [f"- 술어 1·2 합격: " + (" · ".join(f"{letter[s]} `{s}`" for _, s in passed) or kb_lib.NONE_MARK),
              f"- 선택(술어 1·2 합격 가운데 B(R) 최소): " + (f"{letter[passed[0][1]]} `{passed[0][1]}`" if passed else kb_lib.NONE_MARK),
              "- 술어 3은 게이트 `belief-consistency`가 판정한다. 이 뷰는 그 PASS를 입력으로 받지 않으므로, 합격은 술어 1·2의 합격에 그 게이트의 "
              "PASS가 더해져야 성립한다.", ""]

    lines += ["## 표본", "",
              "항목마다 규칙의 값을 낸다. A·B는 그래프의 `agt:DegreeOfBelief`에서 같은 링크 IRI의 값만 읽고, C는 판정 로그의 쌍 행을 링크 IRI로 "
              "결합한 확신도 평균이다. 값이 없는 칸은 그 규칙의 표본에서 빠진다.", "",
              "| 문항 | 링크 IRI | 라벨 | 독립 사람 라벨 | A `kind-rank` | B `beta-binomial` | C `judge-mean` | C 판정 행 수 | C 판정 로그 |",
              "|---|---|---|---|---|---|---|---|---|"]
    for it in items:
        v = values[it["link"]]
        cells = [kb_lib.num(float(v[s])) if s in v else kb_lib.NONE_MARK for s, _ in RULE_ORDER]
        lines.append(f"| {it['문항']} | `{it['link']}` | {it['y']} | {'예' if it['independent'] else '아니다'} | {' | '.join(cells)} | "
                     f"{len(judged.get(it['link'], []))} | "
                     + (" · ".join(f"`{n}`" for n in sorted(judge_logs.get(it["link"], ()))) or kb_lib.NONE_MARK) + " |")
    lines.append("")

    lines += bins_section("신뢰도 구간 — 전체 표본", full,
                          f"구간은 [0, 1/3) · [1/3, 2/3) · [2/3, 1]이고 경계값 1/3과 2/3은 위 구간에 든다(표본 {BINS_UNDER}건 미만의 규칙). "
                          "허용폭은 Binomial(n_k, p̄_k)의 0.025 분위수 lo와 0.975 분위수 hi를 n_k로 나눈 닫힌 구간이다. 분위수는 정확 이항 "
                          "누적분포가 처음으로 그 확률 이상이 되는 성공 수이고, 성공 수가 lo 이상 hi 이하이면 안에 든다. "
                          f"값이 있는 항목이 {SAMPLE_MIN}건 미만인 규칙의 표는 참고다.")

    lines += ["## 독립 사람 라벨 병기", "",
              f"독립 사람 라벨 {len(indep_items)}건만으로 같은 계산을 한 값이다(Q178-b). 합격 판정은 전체 표본의 값으로 하고 이 절은 판정에 쓰지 않는다. "
              f"값이 있는 항목이 {SAMPLE_MIN}건 미만이면 표본 부족이다.", ""]
    lines += summary_rows(indep, judged=False)
    lines += bins_section("독립 사람 라벨의 신뢰도 구간", indep, "구간과 허용폭의 계산은 전체 표본과 같다. 판정에 쓰지 않는다.")

    c = full["judge-mean"]
    c_bins = " · ".join(f"{b['name']} {b['n']}" for b in c["bins"]) if c["n"] else kb_lib.NONE_MARK
    filled = sum(1 for b in c.get("bins", []) if b["n"] >= CALIBRATION_MIN)
    lines += ["## 해석의 한계", "",
              f"- C `judge-mean`의 값은 판정 확신도의 평균 그대로이고 보정하지 않은 값이다. 결정 `p9-belief-by-calibrated-judge`는 확신도 구간마다 "
              f"표본 하한 {CALIBRATION_MIN}을 채운 뒤에 보정을 적용한다. C 값이 있는 표본 항목의 구간별 수는 {c_bins}이고, 하한을 채운 구간은 "
              f"{filled}개다. 이 뷰는 보정을 적용하지 않는다.",
              "- 항목 하나의 제곱 오차는 0 이상 1 이하이므로, 항목 하나가 B(R)를 바꾸는 폭은 1/n 이하다"
              + (f"(n {full['judge-mean']['n']}이면 {kb_lib.num(1 / full['judge-mean']['n'])})." if c["n"] else "."),
              "- 기저율 Brier는 ȳ(1 − ȳ)와 같다. 모든 항목에 같은 값 c를 내는 규칙의 Brier는 ȳ(1 − ȳ) + (c − ȳ)²이므로 기저율보다 낮을 수 없다. "
              "따라서 술어 1은 항목마다 다른 값을 내어 참과 거짓을 가르는 규칙만 통과한다."]
    sizes = [b for s, _ in RULE_ORDER for b in full[s].get("bins", []) if b["n"]]
    if sizes:
        small = min(sizes, key=lambda b: b["n"])
        lines.append(f"- 구간 표본 수가 작으면 허용폭이 넓어 술어 2의 판별력이 약하다. 이번 측정에서 가장 작은 구간은 n_k {small['n']}이고 "
                     f"허용폭은 [{kb_lib.num(small['lo'] / small['n'])}, {kb_lib.num(small['hi'] / small['n'])}]이다.")
    lines.append("")

    inputs = list(a.graphs) + [str(p) for p in label_files + judge_files]
    head = kb_lib.gendoc_header(
        "belief-calibration", "믿음 정도 계산 규칙의 보정 측정", "tools/belief_calibration.py",
        "라벨 기록(`kb/vv/run/label-*.md`)의 링크 IRI에 판정 로그(`kb/vv/run/judge-*.md`)의 쌍 행과 그래프의 `agt:DegreeOfBelief`를 결합하고, "
        "규칙마다 Brier 점수와 구간별 정확 이항 구간을 계산한다(합격 기준 belief-calibrated-against-human-labels)",
        "bazel build //kg:belief_calibration", inputs,
        f"표본 {len(items)} · 독립 사람 라벨 {len(indep_items)} · 판정 로그 {len(judge_files)} · 믿음 정도 값 {len(beliefs)}",
        kb_lib.gendoc_view_notice("라벨 기록과 판정 로그, 그래프의 원본"))
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, inputs), encoding="utf-8")
    print(f"[belief-calibration] {a.out} — 표본 {len(items)} · " +
          " · ".join(f"{letter[s]} n {full[s]['n']}" for s, _ in RULE_ORDER), file=sys.stderr)
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
