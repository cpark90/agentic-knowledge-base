---
id: https://agentic-knowledge-base.dev/id/chunk/cebecea7-272d-4c2a-8361-dec695b1d188
type: artifact
level: executable
title_ko: 함수 main (tools/belief_calibration.py)
title: function main in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/06ac1ac0-5466-4c53-9241-85ddecb10af6, https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/71602697-5642-4dd6-af8c-54ac2af76cb7, https://agentic-knowledge-base.dev/id/chunk/7669e3bf-cc66-40bb-b8db-155171086ea6, https://agentic-knowledge-base.dev/id/chunk/78fce3c0-989d-4891-8e73-65fc35fe2541, https://agentic-knowledge-base.dev/id/chunk/82004891-578d-47bc-a8cd-bed8c1120cda, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/a02757cf-661e-45f1-b13e-7a3916c3a854, https://agentic-knowledge-base.dev/id/chunk/a9090c58-4abc-453a-a64f-e0b2991ca4c8, https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/c560e205-9ac6-4bcc-8726-2749915945a6, https://agentic-knowledge-base.dev/id/chunk/c6d3b385-f4f8-4953-b098-bb5cc8215967, https://agentic-knowledge-base.dev/id/chunk/e3dfa007-25f8-4aa0-9b65-c4124af23269, https://agentic-knowledge-base.dev/id/chunk/f21b98bb-fdc6-42fa-9b87-cc35fc2f64c6]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
    c_items = [it for it in items if "judge-mean" in values[it["link"]]]
    platt = platt_result([(values[it["link"]]["judge-mean"], it["y"]) for it in c_items])
    q_of = {it["link"]: f[3] for it, f in zip(c_items, platt.get("folds", []))}
    indep_platt = platt_result([(values[it["link"]]["judge-mean"], it["y"]) for it in indep_items if it in c_items])
    letter = dict(RULE_ORDER)
    names = {s: f"{letter[s]} `{s}`" for s, _ in RULE_ORDER if s != "judge-mean"}
    cands = [(full[s], names[s]) for s in names] + ([(platt["measure"], PLATT_NAME)] if platt["status"] == "ok" else [])
    passed = sorted(((r["brier"], name) for r, name in cands if r["n"] >= SAMPLE_MIN and r["p1"] and r["p2"]), key=lambda t: t[0])

    lines = ["## 판정 요약", "",
             f"표본은 라벨 기록 {len(label_files)}개의 항목 {len(items)}건이고, 규칙마다 값이 있는 항목만 그 규칙의 표본이다. "
             f"값이 있는 항목이 {SAMPLE_MIN}건 미만인 규칙은 판정하지 않고 값만 참고로 낸다.", ""]
    lines += summary_rows(full, judged=True, platt=platt)
    lines += [f"- 후보는 A `kind-rank`와 B `beta-binomial`, {PLATT_NAME}이다. 결정 `p9-belief-by-calibrated-judge`가 정한 C의 값은 보정한 "
              "값이므로 보정 전 C는 참고로만 내고 후보에서 뺀다.",
              f"- 술어 1·2 합격: " + (" · ".join(name for _, name in passed) or kb_lib.NONE_MARK),
              f"- 선택(술어 1·2 합격 가운데 B(R) 최소): " + (passed[0][1] if passed else kb_lib.NONE_MARK),
              "- 술어 3은 게이트 `belief-consistency`가 판정한다. 이 뷰는 그 PASS를 입력으로 받지 않으므로, 합격은 술어 1·2의 합격에 그 게이트의 "
              "PASS가 더해져야 성립한다.", ""]

    lines += ["## 표본", "",
              "항목마다 규칙의 값을 낸다. A·B는 그래프의 `agt:DegreeOfBelief`에서 같은 링크 IRI의 값만 읽고, C는 판정 로그의 쌍 행을 링크 IRI로 "
              "결합한 확신도 평균이다. Platt 보정 LOO 값은 그 항목을 뺀 나머지로 맞춘 식의 값이다. 값이 없는 칸은 그 규칙의 표본에서 빠진다.", "",
              "| 문항 | 링크 IRI | 라벨 | 독립 사람 라벨 | A `kind-rank` | B `beta-binomial` | C `judge-mean` 보정 전 | C Platt 보정 LOO q_i | "
              "C 판정 행 수 | C 판정 로그 |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for it in items:
        v = values[it["link"]]
        cells = [kb_lib.num(float(v[s])) if s in v else kb_lib.NONE_MARK for s, _ in RULE_ORDER]
        cells.append(kb_lib.num(q_of[it["link"]]) if it["link"] in q_of else kb_lib.NONE_MARK)
        lines.append(f"| {it['문항']} | `{it['link']}` | {it['y']} | {'예' if it['independent'] else '아니다'} | {' | '.join(cells)} | "
                     f"{len(judged.get(it['link'], []))} | "
                     + (" · ".join(f"`{n}`" for n in sorted(judge_logs.get(it["link"], ()))) or kb_lib.NONE_MARK) + " |")
    lines.append("")

    lines += bins_section("신뢰도 구간 — 전체 표본", full,
                          f"구간은 [0, 1/3) · [1/3, 2/3) · [2/3, 1]이고 경계값 1/3과 2/3은 위 구간에 든다(표본 {BINS_UNDER}건 미만의 규칙). "
                          "허용폭은 Binomial(n_k, p̄_k)의 0.025 분위수 lo와 0.975 분위수 hi를 n_k로 나눈 닫힌 구간이다. 분위수는 정확 이항 "
                          "누적분포가 처음으로 그 확률 이상이 되는 성공 수이고, 성공 수가 lo 이상 hi 이하이면 안에 든다. "
                          f"값이 있는 항목이 {SAMPLE_MIN}건 미만인 규칙의 표는 참고다. 보정 전 C의 표는 참고이고 판정은 보정한 C의 표로 한다.")
    lines += [f"### {PLATT_NAME}", ""] + (bin_rows(platt["measure"]) if platt["status"] == "ok" else ["보정한 C의 값이 없다.", ""])
    lines += platt_section(platt, [(Fraction(q_of[it["link"]]), it["y"]) for it in indep_items if it["link"] in q_of])

    lines += ["## 독립 사람 라벨 병기", "",
              f"독립 사람 라벨 {len(indep_items)}건만으로 같은 계산을 한 값이다(Q178-b). 합격 판정은 전체 표본의 값으로 하고 이 절은 판정에 쓰지 않는다. "
              f"값이 있는 항목이 {SAMPLE_MIN}건 미만이면 표본 부족이다.", ""]
    lines += summary_rows(indep, judged=False, platt=indep_platt)
    lines += bins_section("독립 사람 라벨의 신뢰도 구간", indep, "구간과 허용폭의 계산은 전체 표본과 같다. 판정에 쓰지 않는다.")

    lines += limits_section(full, platt, [it["y"] for it in c_items])

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
          " · ".join(f"{letter[s]} n {full[s]['n']}" for s, _ in RULE_ORDER) + f" · C Platt 보정 {platt['status']}", file=sys.stderr)
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
