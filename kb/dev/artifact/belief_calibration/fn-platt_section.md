---
id: https://agentic-knowledge-base.dev/id/chunk/78fce3c0-989d-4891-8e73-65fc35fe2541
type: artifact
level: executable
title_ko: 함수 platt_section (tools/belief_calibration.py)
title: function platt_section in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7669e3bf-cc66-40bb-b8db-155171086ea6, https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2]
part_of: https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6
---
**함수** — `platt_section(platt, indep_pairs)` 다. 보정한 C 의 절 — 보정 조건과 식, 전체 표본 맞춤(기록)과 LOO 맞춤의 (a, b), LOO 값의 Brier, 독립 라벨 부분 Brier.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def platt_section(platt: dict, indep_pairs: list[tuple[Fraction, int]]) -> list[str]:
    """보정한 C 의 절 — 보정 조건과 식, 전체 표본 맞춤(기록)과 LOO 맞춤의 (a, b), LOO 값의 Brier, 독립 라벨 부분 Brier.
    indep_pairs 는 독립 사람 라벨 항목의 (LOO 보정값, 라벨)이다 — 전체 표본에서 그 항목을 뺀 맞춤의 값이고 독립 라벨만의 맞춤이 아니다."""
    none, num = kb_lib.NONE_MARK, kb_lib.num
    out = [f"## 보정한 C — {PLATT_NAME}", "",
           f"결정 `p9-belief-by-calibrated-judge`의 보정이다. C 값이 있는 사람 라벨 항목이 {CALIBRATION_MIN}건 이상이면 적용한다. 입력은 "
           f"보정 전 C 값 p를 [{PLATT_EPS:g}, 1 − {PLATT_EPS:g}]로 자른 로짓 x이고, 식은 q = σ(a·x + b)이며 a·b는 라벨의 로그 우도를 "
           f"최대화하는 뉴턴법으로 맞춘다. 매개변수 변화량의 최댓값이 {PLATT_TOL:g} 미만이면 수렴이고, 반복 상한 {PLATT_MAX_ITER}번 안에 "
           "수렴하지 않거나 표본이 분리되면 보정 불가로 내고 판정하지 않는다. 항목 i의 보정값 q_i는 i를 뺀 나머지 표본으로 맞춘 식의 값이고"
           "(하나씩 빼는 교차 검증), 술어 1·2는 q_i로 판정한다.", ""]
    if platt["status"] == "short":
        return out + [f"보정하지 않았다. C 값이 있는 항목이 {platt['n']}건이고 하한 {CALIBRATION_MIN}건 미만이다.", ""]
    full = platt["full"]
    full_cells = f"{num(full[0])} | {num(full[1])} | {full[2]}" if not isinstance(full, str) else f"{none} | {none} | 보정 불가: {full}"
    out += ["| 맞춤 | 기울기 a | 절편 b | 반복 수 | 쓰임 |", "|---|---|---|---|---|",
            f"| 전체 표본 {platt['n']}건 | {full_cells} | 보정 식의 기록이다. 판정에 쓰지 않는다 |"]
    if platt["status"] == "fail":
        return out + ["", f"{platt['reason']}. 그래서 보정한 C의 값을 내지 않고 판정하지 않는다.", ""]
    fa, fb, fi = ([f[k] for f in platt["folds"]] for k in range(3))
    m = platt["measure"]
    out += [f"| 하나씩 뺀 맞춤 {len(fa)}번 (최솟값~최댓값) | {num(min(fa))}~{num(max(fa))} | {num(min(fb))}~{num(max(fb))} | "
            f"최대 {max(fi)} | 항목마다 보정값 q_i를 낸다. 술어 1·2 판정에 쓴다 |", "",
            f"- LOO 값의 Brier는 {num(float(m['brier']))}이고 같은 {m['n']}건의 기저율 Brier는 {num(float(m['base']))}이다.",
            f"- 전체 표본으로 맞춘 식을 같은 표본에 적용한 Brier는 내지 않는다. 맞춘 표본으로 평가하지 않는다(결정의 평가 방식)."]
    if indep_pairs:
        im = measure(indep_pairs)
        out.append(f"- 독립 사람 라벨 부분 Brier는 {num(float(im['brier']))}이고 같은 {im['n']}건의 기저율 Brier는 {num(float(im['base']))}이다. "
                   "이 값은 전체 표본 LOO 값 가운데 독립 사람 라벨 항목만 모은 평균 제곱 오차이고, 각 값은 그 항목을 뺀 나머지 전체 표본으로 "
                   "맞춘 식에서 나왔다. 독립 라벨만으로 맞춘 값이 아니며 판정에 쓰지 않는다.")
    return out + [""]
```
<!-- 인용 끝 -->
