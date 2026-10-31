---
id: https://agentic-knowledge-base.dev/id/chunk/37bb7c84-209b-4859-b4d3-f5e69f56cf66
type: artifact
level: executable
title_ko: 함수 main (tools/run_evidence.py)
title: function main in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/12124054-d49f-44e2-be10-6fbdb102b578, https://agentic-knowledge-base.dev/id/chunk/133cf34f-4423-4525-954f-2676a7e752f5, https://agentic-knowledge-base.dev/id/chunk/170cd5f1-d8ad-4bcc-b8d8-f89887a75a0c, https://agentic-knowledge-base.dev/id/chunk/3149b98e-06cf-4a59-94b6-8bb92aef0b70, https://agentic-knowledge-base.dev/id/chunk/33676d8e-31ee-4546-8550-deab439480eb, https://agentic-knowledge-base.dev/id/chunk/67eb756b-e7f0-4da2-af55-90f4bc3058e9, https://agentic-knowledge-base.dev/id/chunk/6df5b1b2-44cf-407f-94c2-73b8f6e9093c, https://agentic-knowledge-base.dev/id/chunk/7d5d8898-16f3-47f6-a6e3-e5e8a50f08c8, https://agentic-knowledge-base.dev/id/chunk/871169c2-b1e9-4386-8e2c-e9140c2becff, https://agentic-knowledge-base.dev/id/chunk/8772ef79-5ed9-4276-91cb-187dfcf70688, https://agentic-knowledge-base.dev/id/chunk/ee388c6a-08aa-4ec5-a1ad-cb4faf563811]
part_of: https://agentic-knowledge-base.dev/id/composite/e202036d-a930-4e1b-a919-03711832262b
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out")
    ap.add_argument("--residency", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("--coedit-record", action="store_true", help="git 에서 동시 편집 쌍을 뽑아 관측 하나를 쓴다 (bazel run 모드)")
    ap.add_argument("--root", default=os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), help="--coedit-record 의 저장소 뿌리")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.coedit_record:
        try:
            return coedit_record(Path(args.root).resolve())
        except (OSError, subprocess.CalledProcessError) as e:
            print(f"FAIL [run-evidence] {args.root}: git 이력을 읽을 수 없다 — {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
    if not (args.out and args.residency):
        ap.error("--out 과 --residency 가 필요하다 (--coedit-record 가 아닐 때)")
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
        """개발 KB 의 artifact 단위 지식으로 복합체의 부분이 아닌 것 — 파일 단위 지식(선언 단위 지식)과 손으로 쓴 산출물."""
        m = meta_of.get(iri, {})
        return m.get("type") == "artifact" and in_kb(iri, kb_lib.KB_DEV) and not m.get("part_of")

    # (A, D) → [(증거 접미, 참조들, 극성)]
    ledger: dict[tuple[str, str], list[tuple[str, list[str], str]]] = defaultdict(list)

    # 도장 — 살아 있는 process:bazel-test 도장의 파일 단위 지식이 refines 하는 결정 결론
    for a in sorted(meta_of):
        m = meta_of[a]
        if not file_chunk(a) or not any(isinstance(v, dict) and v.get("by") == kb_lib.STAMP_ACTOR for v in as_list(m.get("verified"))):
            continue
        for d in as_list(m.get("refines")):
            if d in conclusion:
                ledger[(a, d)].append(("stamp", [a], "+"))

    # 실행 — 실행 기록의 테스트 케이스 행 × (테스트 케이스를 돌린 검증기가 verifies 하는 파일 단위 지식) × (테스트 케이스가 verifies 하는 결정 결론)
    def in_dir(iri: str, d: str) -> bool:
        return path_of[iri].startswith(d + "/") or f"/{d}/" in path_of[iri]

    case_of = {Path(path_of[i]).stem: i for i in meta_of if in_dir(i, CASE_DIR)}
    refines = {i: as_list(m.get("refines")) for i, m in meta_of.items()}
    verifiers = [i for i in meta_of if in_dir(i, VERIFIER_DIR)]
    runners = kb_lib.case_verifiers(refines, case_of.values(), verifiers)
    unknown: Counter[str] = Counter()
    halves = 0
    runs = sorted(i for i, m in meta_of.items()
                  if f"{kb_lib.VV_RUN_DIR}/" in path_of[i] and isinstance(m.get("generated"), dict)
                  and m["generated"].get("by") == kb_lib.RUN_GENERATOR)
    old_runs = [r for r in runs if not after_chain_since(meta_of[r]["generated"].get("at"))]
    for r in runs:
        if r in old_runs:
            continue
        stem = Path(path_of[r]).stem
        for slug, verdict, skipped in run_rows(meta_of[r]["__body"], meta_of[r]["generated"].get("at")):
            c = case_of.get(slug)
            if c is None:
                unknown[slug] += 1
                continue
            if verdict not in POLARITY:
                continue
            if verdict == "pass" and skipped:
                halves += 1
                continue
            for w in sorted(runners.get(c, ())):
                for a in (x for x in as_list(meta_of[w].get("verifies")) if file_chunk(x)):
                    for d in as_list(meta_of[c].get("verifies")):
                        if d in conclusion:
                            ledger[(a, d)].append((f"{stem}-{slug}", [r, c, w], POLARITY[verdict]))

    # 동시 편집·공동 커버 — 확정 링크(frontmatter)에만 붙는 지지 증거. 링크 IRI 는 chunk2kg 와 같은 (뿌리 uuid, 종류, 뿌리 uuid) 해시다
    obs_path, coedit, coedit_unresolved = kb_lib.coedit_pairs([path_of[i] for i in meta_of], set(meta_of))
    obs = next((i for i in meta_of if path_of[i] == obs_path), None)
    cover = kb_lib.co_cover(refines, {i: as_list(m.get("verifies")) for i, m in meta_of.items()}, case_of.values(), verifiers,
                            [i for i in meta_of if file_chunk(i)])
    extra: list[tuple[str, str, str, str, list[str]]] = []   # (링크 출발, 종류, 도착, 증거 종류, 참조들)
    for a in sorted(meta_of):
        for key in LINK_KEYS:
            for b in as_list(meta_of[a].get(key)):
                if obs and frozenset((a, b)) in coedit:
                    extra.append((a, key, b, "agt:coEditHistory", [obs]))
                if key == "verifies" and (a, b) in cover:
                    extra.append((a, key, b, "agt:testCoverage", sorted(cover[(a, b)])))

    lines = [PREAMBLE.format(since=CHAIN_SINCE, coedit=obs_path or kb_lib.NONE_MARK)]
    ledger_out, states, ledger_inputs, ledger_emitted = ledger_lines(meta_of, path_of, spec, ledger)
    if ledger_out is None:
        return kb_lib.EXIT_CONFIG
    lines += ledger_out

    extra_kinds: Counter[str] = Counter()
    for a, key, b, kind, refs in extra:
        try:
            h = link_hash(work_id(a, spec), key, work_id(b, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        suffix = "coedit" if kind == "agt:coEditHistory" else "cover"
        e = f"{ID_BASE}evidence/{h}-{suffix}"
        extra_kinds[kind] += 1
        lines.append(f"\n<{ID_BASE}link/{h}>\n    agt:hasEvidence <{e}> .")
        lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {kind} ;\n    agt:evidenceRef "
                     + " , ".join(f"<{x}>" for x in refs) + " ;\n    agt:polarity \"+\" .")

    judge_lines, judge_note, judge_inputs, judge_emitted = judgement_lines(meta_of, path_of, spec, ledger, judged_pairs(meta_of, path_of))
    if judge_lines is None:
        return kb_lib.EXIT_CONFIG
    lines += judge_lines
    # 믿음 정도 — 후보로 낸 링크만, 그 링크의 실행 증거와 판정 증거를 입력으로 (상태는 위에서 이미 정해졌고 이 값은 그것을 바꾸지 않는다)
    belief_out, belief_n = belief_lines({link: ledger_inputs.get(link, []) + judge_inputs.get(link, [])
                                         for link in ledger_emitted | judge_emitted})
    lines += belief_out
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    both = sum(1 for k in ledger if {p for _, _, p in ledger[k]} == {"+", "-"})
    print(f"[run-evidence] satisfies 쌍 {len(ledger)} (" + " · ".join(f"{k} {v}" for k, v in sorted(states.items())) +
          f") · 증거 항목 {sum(len(v) for v in ledger.values())} · (+)(−) 공존 {both} · 실행 기록 {len(runs)}"
          f"(사슬 적용 {len(runs) - len(old_runs)} · {CHAIN_SINCE} 앞이라 소급하지 않음 {len(old_runs)})", file=sys.stderr)
    print(f"[run-evidence] 확정 링크의 동시 편집 {extra_kinds['agt:coEditHistory']} · 공동 커버 {extra_kinds['agt:testCoverage']} "
          f"(관측 {obs_path or kb_lib.NONE_MARK} · 쌍 {len(coedit)} · 풀지 못한 항목 {coedit_unresolved})", file=sys.stderr)
    print(judge_note, file=sys.stderr)
    print(f"[run-evidence] 믿음 정도 — 후보 링크 {len(ledger_emitted | judge_emitted)} 곁에 " +
          (" · ".join(f"{slug} {belief_n[slug]}" for slug in sorted(BELIEF_RULES)) or kb_lib.NONE_MARK) +
          " (열린 계산 규칙 셋, 상태 전이에 들지 않는다)", file=sys.stderr)
    if halves:
        print(f"info [run-evidence] 건너뛴 명령이 있는 pass 행 {halves} — 증거로 읽지 않았다", file=sys.stderr)
    for slug, n in sorted(unknown.items()):
        print(f"info [run-evidence] 실행 기록의 테스트 케이스 `{slug}` 가 {CASE_DIR} 에 없다 — 행 {n}", file=sys.stderr)
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
