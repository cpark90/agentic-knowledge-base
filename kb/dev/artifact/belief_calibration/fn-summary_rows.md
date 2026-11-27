---
id: https://agentic-knowledge-base.dev/id/chunk/c6d3b385-f4f8-4953-b098-bb5cc8215967
type: artifact
level: executable
title_ko: 함수 summary_rows (tools/belief_calibration.py)
title: function summary_rows in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/f1ef7fed-44fb-45ef-bc75-8f33101fc8cb, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `summary_rows(results, judged, platt)` 다. 규칙별 요약 표 — A · B · 보정 전 C · 보정한 C(platt_result 의 결과) 순이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def summary_rows(results: dict, judged: bool, platt: dict) -> list[str]:
    """규칙별 요약 표 — A · B · 보정 전 C · 보정한 C(platt_result 의 결과) 순이다. 보정 전 C 는 참고 행이고 판정하지 않는다(결정이 정한 C 의
    값은 보정한 값이다). judged 가 거짓이면(독립 라벨 병기) 판정 열이 '판정에 쓰지 않는다'다. 보정한 C 가 맞추지 않았거나 보정 불가이면
    값 열은 없음이고 판정 열이 그 사유다."""
    none = kb_lib.NONE_MARK
    out = ["| 규칙 | 결정 | 값이 있는 항목 n | 참 비율 ȳ | B(R) | 기저율 Brier | 술어 1 | 술어 2 | 술어 1·2 판정 |",
           "|---|---|---|---|---|---|---|---|---|"]
    rows = [(f"{letter} `{slug}`" + (" (보정 전 참고)" if slug == "judge-mean" else ""), slug, results[slug],
             "보정 전 참고 — 판정에 쓰지 않는다" if slug == "judge-mean" else None) for slug, letter in RULE_ORDER]
    if platt["status"] == "ok":
        rows.append((PLATT_NAME, "judge-mean", platt["measure"], None))
    for name, slug, r, fixed in rows:
        if not r["n"]:
            out.append(f"| {name} | `{RULE_DECISION[slug]}` | 0 | {none} | {none} | {none} | {none} | {none} | "
                       f"{'표본 부족 — 판정하지 않는다' if judged else '판정에 쓰지 않는다'} |")
            continue
        if not judged:
            verdict = "판정에 쓰지 않는다"
        elif fixed:
            verdict = fixed
        elif r["n"] < SAMPLE_MIN:
            verdict = f"표본 부족(n < {SAMPLE_MIN}) — 판정하지 않는다"
        elif r["p2"] is None:
            verdict = f"구간 규칙 없음(n ≥ {BINS_UNDER}) — 판정하지 않는다"
        else:
            verdict = "합격" if r["p1"] and r["p2"] else "불합격"
        p2 = truth(r["p2"]) if r["p2"] is not None else f"구간 규칙 없음(n ≥ {BINS_UNDER})"
        out.append(f"| {name} | `{RULE_DECISION[slug]}` | {r['n']} | {kb_lib.pct(r['pos'], r['n'])} | {kb_lib.num(float(r['brier']))} | "
                   f"{kb_lib.num(float(r['base']))} | {truth(r['p1'])} | {p2} | {verdict} |")
    if platt["status"] != "ok":
        why = (f"표본 부족(n < {CALIBRATION_MIN}) — " + ("보정하지 않는다" if judged else "독립 라벨만으로 맞추지 않는다")
               if platt["status"] == "short" else "보정 불가 — 판정하지 않는다")
        out.append(f"| {PLATT_NAME} | `{RULE_DECISION['judge-mean']}` | {platt['n']} | {none} | {none} | {none} | {none} | {none} | {why} |")
    return out + [""]
```
<!-- 인용 끝 -->
