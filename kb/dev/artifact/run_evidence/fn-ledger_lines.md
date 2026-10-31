---
id: https://agentic-knowledge-base.dev/id/chunk/ee388c6a-08aa-4ec5-a1ad-cb4faf563811
type: artifact
level: executable
title_ko: 함수 ledger_lines (tools/run_evidence.py)
title: function ledger_lines in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/133cf34f-4423-4525-954f-2676a7e752f5]
part_of: https://agentic-knowledge-base.dev/id/composite/e202036d-a930-4e1b-a919-03711832262b
---
**함수** — `ledger_lines(meta_of, path_of, spec, ledger)` 다. satisfies 증거 기록 (A, D) → [(증거 접미, 참조들, 극성)] → (TTL 줄들, 상태별 수, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def ledger_lines(meta_of: dict, path_of: dict, spec: dict, ledger: dict) -> tuple[list[str] | None, Counter, dict, set]:
    """satisfies 증거 기록 (A, D) → [(증거 접미, 참조들, 극성)] → (TTL 줄들, 상태별 수, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).

    상태는 p9-evidence-ledger-with-belief 의 전이 규칙 그대로다 — (+)가 하나라도 있으면 후보, 실행(−)만 있으면 invalid, 이미 확정이면
    증거 항목만 붙인다. 증거 기록만 읽고 확률로 합산한 값을 읽지 않는다. 링크 IRI 를 풀지 못하면 (None, …) 다."""
    lines: list[str] = []
    states: Counter[str] = Counter()
    inputs: dict[str, list[tuple[str, str, float | None]]] = {}
    emitted: set[str] = set()
    for (a, d) in sorted(ledger):
        try:
            h = link_hash(work_id(a, spec), KIND, work_id(d, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return None, states, {}, set()
        link = f"{ID_BASE}link/{h}"
        entries = ledger[(a, d)]
        evs = [(f"{ID_BASE}evidence/{h}-{suffix}", refs, pol) for suffix, refs, pol in entries]
        ev_list = " , ".join(f"<{e}>" for e, _, _ in evs)
        pols = {p for _, _, p in entries}
        inputs[link] = [(EVIDENCE_KIND, pol, None) for _, _, pol in entries]
        if d in as_list(meta_of[a].get(KIND)):   # 이미 확정 — 증거 항목만 그 링크에 붙인다
            states["confirmed"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:
            cls, state = ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE) if "+" in pols else ("agt:Link", kb_lib.LINK_STATE_INVALID)
            states[state] += 1
            if state == LINK_STATE_CANDIDATE:
                emitted.add(link)
            lines.append(f"\n<{link}>\n    a {cls} ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{d}> ;\n"
                         f"    agt:linkKind agt:{KIND} ;\n    agt:linkState \"{state}\" ;\n    agt:hasEvidence {ev_list} .")
        for e, refs, pol in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {EVIDENCE_KIND} ;\n    agt:evidenceRef "
                         + " , ".join(f"<{x}>" for x in refs) + f" ;\n    agt:polarity \"{pol}\" .")
    return lines, states, inputs, emitted
```
<!-- 인용 끝 -->
