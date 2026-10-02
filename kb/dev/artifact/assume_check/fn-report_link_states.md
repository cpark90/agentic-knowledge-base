---
id: https://agentic-knowledge-base.dev/id/chunk/91c67aff-4114-4bf6-a319-b4aa40cbc5f1
type: artifact
level: executable
title_ko: 함수 report_link_states (tools/assume_check.py)
title: function report_link_states in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9, https://agentic-knowledge-base.dev/id/chunk/badba8ff-e4ce-4780-8483-a93e7c6631a5, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/5dac7240-2471-496d-a65c-f55a8a067a41
---
**함수** — `report_link_states(g, states, sat, by_trigger, when_unverified, space_rows)` 다. 링크 상태의 물질화 — `when` 판정과 트리거, 그리고 설계 공간의 양립 제약.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_link_states(g: Graph, states: dict, sat: dict, by_trigger: dict, when_unverified,
                       space_rows: list) -> list[str]:
    """링크 상태의 물질화 — `when` 판정과 트리거, 그리고 설계 공간의 양립 제약."""
    body: list[str] = []
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
    return body
```
<!-- 인용 끝 -->
