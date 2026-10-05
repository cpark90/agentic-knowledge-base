---
id: https://agentic-knowledge-base.dev/id/chunk/37bb7c84-209b-4859-b4d3-f5e69f56cf66
type: artifact
level: executable
title_ko: 함수 main (tools/run_evidence.py)
title: function main in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:47:19Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/133cf34f-4423-4525-954f-2676a7e752f5, https://agentic-knowledge-base.dev/id/chunk/170cd5f1-d8ad-4bcc-b8d8-f89887a75a0c]
part_of: https://agentic-knowledge-base.dev/id/composite/e202036d-a930-4e1b-a919-03711832262b
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", required=True, help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [run-evidence] {args.residency}: 값 어휘를 읽을 수 없다 — {e}", file=sys.stderr)
        return kb_lib.EXIT_CONFIG

    meta_of: dict[str, dict] = {}
    path_of: dict[str, str] = {}
    conclusion: set[str] = set()
    spec: dict[str, str] = {}
    for path in sorted(p for p in args.files if p.endswith(".md")):
        try:
            meta, body = parse_chunk(path)
        except (OSError, ValueError) as e:
            print(f"FAIL [run-evidence] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        iri = meta.get("id")
        if not isinstance(iri, str):
            continue
        meta["__body"] = body
        meta_of[iri], path_of[iri] = meta, path
        if isinstance(meta.get(SPECIALIZATION_KEY), str):
            spec[iri] = meta[SPECIALIZATION_KEY]
        if meta.get("type") == "decision" and CONCLUSION_SLOT in body_slots(body.splitlines()):
            conclusion.add(iri)

    def in_kb(iri: str, kb: str) -> bool:
        return f"{kb}/" in path_of.get(iri, "")

    def file_chunk(iri: str) -> bool:
        """개발 KB 의 artifact 청크로 복합체의 부분이 아닌 것 — 파일 청크(선언 청크)와 손으로 쓴 산출물."""
        m = meta_of.get(iri, {})
        return m.get("type") == "artifact" and in_kb(iri, kb_lib.KB_DEV) and not m.get("part_of")

    # (A, D) → [(증거 접미, 참조들, 극성)]
    ledger: dict[tuple[str, str], list[tuple[str, list[str], str]]] = defaultdict(list)

    # 도장 — 살아 있는 process:bazel-test 도장의 파일 청크가 refines 하는 결정 결론
    for a in sorted(meta_of):
        m = meta_of[a]
        if not file_chunk(a) or not any(isinstance(v, dict) and v.get("by") == kb_lib.STAMP_ACTOR for v in as_list(m.get("verified"))):
            continue
        for d in as_list(m.get("refines")):
            if d in conclusion:
                ledger[(a, d)].append(("stamp", [a], "+"))

    # 실행 — 실행 기록의 케이스 행 × (케이스를 refines 하는 검증기가 verifies 하는 파일 청크) × (케이스가 verifies 하는 결정 결론)
    case_of = {Path(path_of[i]).stem: i for i in meta_of if path_of[i].startswith(CASE_DIR + "/") or f"/{CASE_DIR}/" in path_of[i]}
    artifacts_of_case: dict[str, set[str]] = defaultdict(set)
    for v, m in meta_of.items():
        if not in_kb(v, kb_lib.KB_VV) or m.get("type") != "artifact":
            continue
        targets = [a for a in as_list(m.get("verifies")) if file_chunk(a)]
        for c in as_list(m.get("refines")):
            artifacts_of_case[c].update(targets)
    unknown: Counter[str] = Counter()
    halves = 0
    runs = sorted(i for i, m in meta_of.items()
                  if f"{kb_lib.VV_RUN_DIR}/" in path_of[i] and isinstance(m.get("generated"), dict)
                  and m["generated"].get("by") == kb_lib.RUN_GENERATOR)
    for r in runs:
        stem = Path(path_of[r]).stem
        for slug, verdict, skipped in run_rows(meta_of[r]["__body"]):
            c = case_of.get(slug)
            if c is None:
                unknown[slug] += 1
                continue
            if verdict not in POLARITY:
                continue
            if verdict == "pass" and skipped:
                halves += 1
                continue
            for a in sorted(artifacts_of_case.get(c, ())):
                for d in as_list(meta_of[c].get("verifies")):
                    if d in conclusion:
                        ledger[(a, d)].append((f"{stem}-{slug}", [r, c], POLARITY[verdict]))

    lines, states = [PREAMBLE], Counter()
    for (a, d) in sorted(ledger):
        try:
            h = link_hash(work_id(a, spec), KIND, work_id(d, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        link = f"{ID_BASE}link/{h}"
        entries = ledger[(a, d)]
        evs = [(f"{ID_BASE}evidence/{h}-{suffix}", refs, pol) for suffix, refs, pol in entries]
        ev_list = " , ".join(f"<{e}>" for e, _, _ in evs)
        pols = {p for _, _, p in entries}
        if d in as_list(meta_of[a].get(KIND)):   # 이미 확정 — 증거 항목만 그 링크에 붙인다
            states["confirmed"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:
            cls, state = ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE) if "+" in pols else ("agt:Link", kb_lib.LINK_STATE_INVALID)
            states[state] += 1
            lines.append(f"\n<{link}>\n    a {cls} ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{d}> ;\n"
                         f"    agt:linkKind agt:{KIND} ;\n    agt:linkState \"{state}\" ;\n    agt:hasEvidence {ev_list} .")
        for e, refs, pol in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {EVIDENCE_KIND} ;\n    agt:evidenceRef "
                         + " , ".join(f"<{x}>" for x in refs) + f" ;\n    agt:polarity \"{pol}\" .")

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    both = sum(1 for k in ledger if {p for _, _, p in ledger[k]} == {"+", "-"})
    print(f"[run-evidence] satisfies 쌍 {len(ledger)} (" + " · ".join(f"{k} {v}" for k, v in sorted(states.items())) +
          f") · 증거 항목 {sum(len(v) for v in ledger.values())} · (+)(−) 공존 {both} · 실행 기록 {len(runs)}", file=sys.stderr)
    if halves:
        print(f"info [run-evidence] 건너뛴 명령이 있는 pass 행 {halves} — 증거로 읽지 않았다", file=sys.stderr)
    for slug, n in sorted(unknown.items()):
        print(f"info [run-evidence] 실행 기록의 케이스 `{slug}` 가 {CASE_DIR} 에 없다 — 행 {n}", file=sys.stderr)
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
