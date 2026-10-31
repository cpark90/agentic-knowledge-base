---
id: https://agentic-knowledge-base.dev/id/chunk/8772ef79-5ed9-4276-91cb-187dfcf70688
type: artifact
level: executable
title_ko: 함수 judgement_lines (tools/run_evidence.py)
title: function judgement_lines in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/133cf34f-4423-4525-954f-2676a7e752f5]
part_of: https://agentic-knowledge-base.dev/id/composite/ed156a01-76a8-4195-b32e-c9096b040444
---
**함수** — `judgement_lines(meta_of, path_of, spec, ledger, read)` 다. 판정 쌍(judged_pairs 의 결과) → (TTL 줄들, 요약 한 줄, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judgement_lines(meta_of: dict, path_of: dict, spec: dict, ledger: dict,
                    read: tuple[dict, list[str], int, int]) -> tuple[list[str] | None, str, dict, set]:
    """판정 쌍(judged_pairs 의 결과) → (TTL 줄들, 요약 한 줄, 링크 → 증거 [(종류, 극성, 확신도)], 후보로 낸 링크들).
    행마다 agt:judgement 증거 하나와, 확정이 아닌 쌍의 후보 링크 개체.

    이미 확정된 쌍은 내지 않고 센다. 판정은 반박만 있어도 후보다 — invalid 는 실행 증거 전용이다(p9-evidence-ledger-with-belief).
    링크 IRI 를 풀지 못하면 (None, 사유, {}, set()) 다."""
    judged, judge_logs, stale, gone_pair = read
    lines: list[str] = []
    inputs: dict[str, list[tuple[str, str, float | None]]] = {}
    emitted: set[str] = set()
    judge_states: Counter[str] = Counter()
    for (a, kind, b) in sorted(judged):
        try:
            h = link_hash(work_id(a, spec), kind, work_id(b, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return None, "", {}, set()
        link = f"{ID_BASE}link/{h}"
        evs = []
        for log, judge, pol, conf in judged[(a, kind, b)]:
            tag = hashlib.sha256(f"{log}\x1f{judge}".encode("utf-8")).hexdigest()[:12]
            evs.append((f"{ID_BASE}evidence/{h}-judge-{tag}", log, pol, conf))
        evs = sorted(set(evs), key=lambda x: x[:3])
        ev_list = " , ".join(f"<{e}>" for e, _, _, _ in evs)
        if b in as_list(meta_of[a].get(kind)):   # 이미 확정 — 판정은 큐를 거르는 증거라 확정 뒤에는 내지 않는다 (사람의 확정이 앞선다)
            judge_states["confirmed-skipped"] += 1
            continue
        if kind == KIND and (a, b) in ledger:   # 실행 증거가 이미 개체를 냈다 — 상태는 실행 증거의 규칙이 정한다
            judge_states["attached"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:   # 판정은 반박만 있어도 후보다 — invalid 는 실행 증거 전용 (p9-evidence-ledger-with-belief)
            judge_states[LINK_STATE_CANDIDATE] += 1
            emitted.add(link)
            lines.append(f"\n<{link}>\n    a agt:Link , agt:CandidateLink ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{b}> ;\n"
                         f"    agt:linkKind agt:{kind} ;\n    agt:linkState \"{LINK_STATE_CANDIDATE}\" ;\n    agt:hasEvidence {ev_list} .")
        inputs[link] = [("agt:judgement", pol, conf) for _, _, pol, conf in evs]
        for e, log, pol, _ in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind agt:judgement ;\n    agt:evidenceRef <{log}> ;\n"
                         f"    agt:polarity \"{pol}\" .")

    note = (f"[run-evidence] 판정 쌍 {len(judged)} (" + (" · ".join(f"{k} {v}" for k, v in sorted(judge_states.items())) or kb_lib.NONE_MARK)
            + f") · 판정 증거 {sum(len(v) for v in judged.values())} · 판정 로그 {len(judge_logs)} · 낡은 판정 {stale} · 끝이 없는 쌍 행 {gone_pair}")
    return lines, note, inputs, emitted
```
<!-- 인용 끝 -->
