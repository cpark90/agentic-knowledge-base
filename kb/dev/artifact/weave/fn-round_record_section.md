---
id: https://agentic-knowledge-base.dev/id/chunk/89bffa35-e0b8-4811-aa3d-d9cbd0e35c83
type: artifact
level: executable
title_ko: 함수 round_record_section (tools/weave.py)
title: function round_record_section in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `round_record_section(m, defects, rounds, judged)` 다. 라운드 기록별 신규 주석 절 — 라운드 경계가 날짜가 아니라 `vv_run --round` 의 기록이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def round_record_section(m: Model, defects: list, rounds: list, judged: int) -> list[str]:
    """라운드 기록별 신규 주석 절 — 라운드 경계가 날짜가 아니라 `vv_run --round` 의 기록이다 (유저 답 Q39-c).

    new(n) 은 직전 기록 시각 뒤부터 기록 n 의 시각까지 저작된 주석 수이고(첫 라운드는 처음부터) 마지막 기록 뒤의 주석은 진행 중 구간이다.
    라운드 n 의 신규 수가 라운드 n−1 의 것 이상인데 라운드 n+1 이 정지 규칙이 아닌 사유로 닫혔으면 그 행에 위반을 적는다 —
    판정은 verify 질의 `round-stop-rule-violated` 가 게이트에서 하고 이 절은 같은 정의로 보인다.
    """
    stop = AGT.roundEndedByStopRule
    rows, counts, prev_at, violations = [], [], None, 0
    for i, (at, c, reason) in enumerate(rounds):
        n = sum(1 for t in defects if t <= at and (prev_at is None or t > prev_at))
        trend = kb_lib.NONE_MARK if not counts else "줄지 않음 — 다음 라운드를 열지 않는다" if n >= counts[-1] else "줄었다"
        broken = len(counts) >= 2 and counts[-1] >= counts[-2] and reason != stop
        violations += broken
        rows.append(f"| {i + 1} | `{Path(m.location[c]).name}` | {kb_lib.utc_stamp(at)} | {n} | {trend} | {m.ko(reason)}"
                    + (" — **정지 규칙 위반**" if broken else "") + " |")
        counts.append(n)
        prev_at = at
    tail = sum(1 for t in defects if t > prev_at)
    rows.append(f"| 진행 중 | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {tail} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} |")
    return ["| 라운드 | 기록 | 구간 끝 | 신규 주석 | 직전 라운드 대비 | 종료 사유 |", "|---|---|---|---|---|---|"] + rows \
        + ["", f"- 라운드 기록 {len(rounds)} · 신규 계열 {' · '.join(map(str, counts))} · 마지막 기록 뒤 신규 {tail} · "
               f"집계에서 뺀 판정 결과 주석(`{kb_lib.JUDGE_GENERATOR}`) {judged} · 정지 규칙 위반 {violations} "
               "(verify 질의 `round-stop-rule-violated` 와 같은 정의)", ""]
```
<!-- 인용 끝 -->
