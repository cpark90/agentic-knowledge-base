---
id: https://agentic-knowledge-base.dev/id/chunk/7ca2da27-a5fc-4b33-aa68-b855ee61d697
type: artifact
level: executable
title_ko: 함수 round_section (tools/weave.py)
title: function round_section in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `round_section(days, judged)` 다. 라운드(날짜)별 신규 주석 절 — 표와 계열 한 줄.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
