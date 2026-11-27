---
id: https://agentic-knowledge-base.dev/id/chunk/82004891-578d-47bc-a8cd-bed8c1120cda
type: artifact
level: executable
title_ko: 함수 limits_section (tools/belief_calibration.py)
title: function limits_section in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `limits_section(full, platt, c_labels)` 다. '해석의 한계' 절 — 보정 전 C 의 지위와 보정 조건, LOO 맞춤의 음성 표본 수, 보정 식의 매개변수 수, Brier·구간의 판별력에 관한 사실.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def limits_section(full: dict, platt: dict, c_labels: list[int]) -> list[str]:
    """'해석의 한계' 절 — 보정 전 C 의 지위와 보정 조건, LOO 맞춤의 음성 표본 수, 보정 식의 매개변수 수, Brier·구간의 판별력에 관한 사실.
    c_labels 는 C 값이 있는 항목의 라벨이다."""
    c = full["judge-mean"]
    neg = sum(1 for y in c_labels if not y)
    lines = ["## 해석의 한계", "",
             f"- 보정 전 C의 값은 판정 확신도의 평균 그대로이고 참고로만 낸다. 결정 `p9-belief-by-calibrated-judge`는 사람 라벨 표본이 "
             f"{CALIBRATION_MIN}건 이상이면 보정을 적용하고, 이 측정에서 C 값이 있는 항목은 {len(c_labels)}건이다.",
             f"- C 값이 있는 항목 가운데 라벨 0은 {neg}건이다. 따라서 하나씩 빼는 교차 검증에서 매 맞춤의 음성 표본은 "
             f"{max(neg - 1, 0)}건(음성 항목을 뺀 맞춤) 또는 {neg}건(양성 항목을 뺀 맞춤)이다.",
             "- 보정 식의 매개변수는 기울기 a와 절편 b의 2개다.",
             "- 항목 하나의 제곱 오차는 0 이상 1 이하이므로, 항목 하나가 B(R)를 바꾸는 폭은 1/n 이하다"
             + (f"(n {full['judge-mean']['n']}이면 {kb_lib.num(1 / full['judge-mean']['n'])})." if c["n"] else "."),
             "- 기저율 Brier는 ȳ(1 − ȳ)와 같다. 모든 항목에 같은 값 c를 내는 규칙의 Brier는 ȳ(1 − ȳ) + (c − ȳ)²이므로 기저율보다 낮을 수 없다. "
             "따라서 술어 1은 항목마다 다른 값을 내어 참과 거짓을 가르는 규칙만 통과한다."]
    sizes = [b for r in [full[s] for s, _ in RULE_ORDER] + [platt.get("measure", {})] for b in r.get("bins", []) if b["n"]]
    if sizes:
        small = min(sizes, key=lambda b: b["n"])
        lines.append(f"- 구간 표본 수가 작으면 허용폭이 넓어 술어 2의 판별력이 약하다. 이번 측정에서 가장 작은 구간은 n_k {small['n']}이고 "
                     f"허용폭은 [{kb_lib.num(small['lo'] / small['n'])}, {kb_lib.num(small['hi'] / small['n'])}]이다.")
    return lines + [""]
```
<!-- 인용 끝 -->
