---
id: https://agentic-knowledge-base.dev/id/chunk/9cb93d1c-7ae3-49f8-8812-213367f8a3e4
type: artifact
level: executable
title_ko: 함수 round_observation (tools/vv_run.py)
title: function round_observation in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a]
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `round_observation(now, n, start, k, reason, prev_k)` 다. 라운드 기록 본문 — 실행 기록과 같은 frontmatter 꼴(memory, concrete, `process:vv_run`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def round_observation(now: datetime, n: int, start: datetime | None, k: int, reason: str, prev_k: int | None) -> str:
    """라운드 기록 본문 — 실행 기록과 같은 frontmatter 꼴(memory, concrete, `process:vv_run`). 본문은 종료 사유 개체 하나만 인용한다."""
    concept, ko, en = ROUND_REASONS[reason]
    stamp = kb_lib.utc_stamp(now)
    begin = kb_lib.utc_stamp(start) if start else kb_lib.NONE_MARK
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete",
            f"title_ko: 검증 라운드 {n} 종료 {stamp}: 신규 결함 {k} · 종료 사유 {ko}",
            f"title: Verification round {n} closed {stamp}: {k} new defects, ended by {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    since = f"직전 라운드 기록({begin}) 뒤부터" if start else "처음부터"
    if prev_k is None:
        rule = "첫 라운드라 정지 규칙의 비교 대상이 없다."
    elif k >= prev_k:
        rule = (f"신규 결함이 직전 라운드의 {prev_k}건에서 줄지 않아 정지 규칙이 성립한다 — 라운드 {n + 1} 을 열지 않고 채널로 되돌린다. "
                f"라운드 {n + 1} 기록은 정지 규칙 사유로만 남긴다.")
    else:
        rule = f"신규 결함이 직전 라운드의 {prev_k}건에서 줄었다 — 정지 규칙이 성립하지 않는다."
    body = [f"**관측** — {stamp} 에 `vv_run --round {reason}` 이 검증 라운드 {n} 의 끝을 기록했다. 구간은 {since} {stamp} 까지다. "
            f"그 구간에 저작된 판정 주석(`{VERDICT_DIR}/`) 중 판정 결과 주석(`{kb_lib.JUDGE_GENERATOR}`)을 뺀 신규 결함은 {k}건이고 "
            f"종료 사유는 `{concept}`({ko})다.", "",
            ROUND_TABLE_HEADER, "|---|---|---|---|---|", f"| {n} | {begin} | {stamp} | {k} | {ko} |", "",
            f"{rule} 판정은 verify 질의 `{STOP_RULE_QUERY}` 가 그래프에서 한다."]
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
