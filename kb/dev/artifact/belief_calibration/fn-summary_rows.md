---
id: https://agentic-knowledge-base.dev/id/chunk/c6d3b385-f4f8-4953-b098-bb5cc8215967
type: artifact
level: executable
title_ko: 함수 summary_rows (tools/belief_calibration.py)
title: function summary_rows in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/f1ef7fed-44fb-45ef-bc75-8f33101fc8cb, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `summary_rows(results, judged)` 다. 규칙별 요약 표.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
