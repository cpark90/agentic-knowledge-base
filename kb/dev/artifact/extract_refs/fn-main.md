---
id: https://agentic-knowledge-base.dev/id/chunk/01ac7760-7311-4434-ab99-2fe9c1974531
type: artifact
level: executable
title_ko: 함수 main (tools/extract_refs.py)
title: function main in tools/extract_refs.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract-refs}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-19T14:57:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/444fc7bd-680b-4c09-aec8-0e5de0cc1175
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ontology", nargs="*", default=[],
                    help="온톨로지 모듈 파일들(*-ontology.ttl). 주면 agt:usesConcept 도 방출한다. 뒤에 `--` 를 두고 청크 파일을 잇는다")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    concepts: set[str] | None = set(load_concepts(args.ontology)) if args.ontology else None

    known, bodies, errors = set(), [], []
    spec: dict[str, str] = {}  # 조각 → 원본 — 후보 링크 IRI 의 뿌리 uuid (chunk2kg 와 같은 규칙)
    # 청크는 .md 뿐이다 — 매크로가 `-- $(SRCS)` 로 넘기면 온톨로지 .ttl 도 섞여 오므로 조용히 건너뛴다
    for path in sorted(p for p in args.files if p.endswith(".md")):
        try:
            iri, spec_of, body = read(path)
        except OSError as e:
            print(f"FAIL [extract-refs] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except ValueError as e:
            errors.append(str(e))
            continue
        known.add(iri)
        if spec_of:
            spec[iri] = spec_of
        bodies.append((path, iri, body))

    blocks, concept_blocks, concept_links = 0, 0, 0
    unknown: Counter[str] = Counter()
    unknown_where: dict[str, list[str]] = defaultdict(list)
    candidates: dict[str, dict] = {}  # 링크 IRI → {from, to, refs} — 뿌리 uuid 가 같은 인용은 후보 하나로 합친다
    lines = [PREAMBLE]
    for path, iri, body in bodies:
        cited = sorted({IRI.format(n) for n in CITE.findall(body)} - {iri})
        for target in cited:
            if target not in known:
                errors.append(f"{path}: 인용한 항목이 없다: {target}")
        cited = [c for c in cited if c in known]
        for target in cited:
            try:
                h = link_hash(work_id(iri, spec), CANDIDATE_KIND, work_id(target, spec))
            except SpecializationError as e:
                errors.append(f"[{SPECIALIZATION_GATE}] {path}: {e}")
                continue
            c = candidates.setdefault(f"{ID_BASE}link/{h}", {"from": [], "to": [], "refs": []})
            for key, val in (("from", iri), ("to", target), ("refs", iri)):
                if val not in c[key]:
                    c[key].append(val)

        used: list[str] = []
        if concepts is not None:
            mentioned = sorted(set(CONCEPT.findall(body)))
            used = [t for t in mentioned if t in concepts]
            for t in mentioned:
                if t not in concepts:
                    unknown[t] += 1
                    unknown_where[t].append(path)

        if not cited and not used:
            continue
        parts = []
        if cited:
            blocks += 1
            parts.append("    agt:cites " + " ,\n        ".join(f"<{c}>" for c in cited))
        if used:
            concept_blocks += 1
            concept_links += len(used)
            parts.append("    agt:usesConcept " + " ,\n        ".join(f"agt:{t}" for t in used))
        lines.append(f"\n<{iri}>\n" + " ;\n".join(parts) + " .")

    if errors:
        for e in errors:
            print(f"FAIL [extract-refs] {e}", file=sys.stderr)
        return EXIT_FAIL

    for link in sorted(candidates):  # 후보 링크 개체 — 상태 candidate, 증거는 구축 기록(본문 식별자), IRI 는 뿌리 uuid 해시
        c = candidates[link]
        ev = link.replace("/link/", "/evidence/", 1)
        lines.append(f"\n<{link}>\n    a agt:Link , agt:CandidateLink ;\n    agt:linkFrom " + " , ".join(f"<{x}>" for x in c["from"])
                     + " ;\n    agt:linkTo " + " , ".join(f"<{x}>" for x in c["to"])
                     + f" ;\n    agt:linkKind agt:{CANDIDATE_KIND} ;\n    agt:linkState \"{LINK_STATE_CANDIDATE}\" ;\n    agt:hasEvidence <{ev}> .")
        lines.append(f"\n<{ev}>\n    a agt:Evidence ;\n    agt:evidenceKind {EVIDENCE} ;\n    agt:evidenceRef " + " , ".join(f"<{x}>" for x in c["refs"])
                     + " ;\n    agt:polarity \"+\" .")

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[extract-refs] 인용한 항목 {blocks}개 · 후보 링크 개체(agt:CandidateLink, {CANDIDATE_KIND}) {len(candidates)}개", file=sys.stderr)
    if concepts is not None:
        print(f"[extract-refs] 개념을 사용한 항목 {concept_blocks}개, usesConcept 링크 {concept_links}개", file=sys.stderr)
        for term, n in sorted(unknown.items(), key=lambda kv: (-kv[1], kv[0])):
            where = ", ".join(sorted(set(unknown_where[term]))[:3])
            print(f"info [usesConcept] 온톨로지에 없는 표기 agt:{term} — 청크 {n}개 ({where}{' …' if len(set(unknown_where[term])) > 3 else ''})",
                  file=sys.stderr)
        if unknown:
            print(f"info [usesConcept] 온톨로지에 없는 표기 {len(unknown)}종 / 청크-표기 쌍 {sum(unknown.values())}개 — 링크로 만들지 않음",
                  file=sys.stderr)
    return 0
```
<!-- 인용 끝 -->
