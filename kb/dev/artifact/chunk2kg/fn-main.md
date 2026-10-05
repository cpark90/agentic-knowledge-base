---
id: https://agentic-knowledge-base.dev/id/chunk/e042a28e-3260-47b6-91ff-019d92fc068a
type: artifact
level: executable
title_ko: 함수 main (tools/chunk2kg.py)
title: function main in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/040b7a8d-10e8-4e6e-96db-b8495e467218, https://agentic-knowledge-base.dev/id/chunk/17fdb102-0df9-45f2-93ff-c64b4df55d44, https://agentic-knowledge-base.dev/id/chunk/321d9509-8da2-4406-9fa3-a287cafc8d55, https://agentic-knowledge-base.dev/id/chunk/3bc19461-0841-4806-aafd-93fdbc5f9ab3, https://agentic-knowledge-base.dev/id/chunk/46cd72ea-813e-4ee5-b990-fede1470c237, https://agentic-knowledge-base.dev/id/chunk/51b67d04-6982-40f6-ae74-88b58c403ecb, https://agentic-knowledge-base.dev/id/chunk/9081dacd-219d-4944-b3c6-d5d9a6955f49, https://agentic-knowledge-base.dev/id/chunk/a99e95b4-6c01-4945-a6eb-6efe898579e1, https://agentic-knowledge-base.dev/id/chunk/abf3ca16-b991-4326-8c10-b4581d03a6d2, https://agentic-knowledge-base.dev/id/chunk/b03385a6-0433-4102-a7ab-1753e57cb89a, https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b, https://agentic-knowledge-base.dev/id/chunk/dae11730-e07f-47c6-becd-61b72a819b12, https://agentic-knowledge-base.dev/id/chunk/e1d9652e-f3b3-470b-bf7f-f8fa31f8be68, https://agentic-knowledge-base.dev/id/chunk/f178c885-f133-4f49-a296-18b123272948]
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fragment", action="store_true", help="타깃 하나의 조각 — 전문(preamble) 없이 블록만 (kb_chunk·kb_decision 액션)")
    ap.add_argument("--merge", action="store_true", help="조각들을 병합해 -kg 를 만든다 (kb_kg_merge)")
    ap.add_argument("--ordered", action="append", default=[], metavar="IRI",
                    help="이 묶음의 복합체가 선언한 부분의 순서 — 부분마다 한 번, 선언 순서대로 반복해 준다(`--ordered A --ordered B`). "
                         "목록형(nargs)이 아닌 이유는 청크 파일이 위치 인자라 목록이 그것을 삼키기 때문이다. 생성 BUILD 의 명시 "
                         "인자(kb_decision·kb_composite 의 ordered)가 넘긴다. 복합체 하나를 선언하는 실행에만 준다. "
                         "frontmatter composite.ordered 와 함께 있으면 같아야 한다")
    ap.add_argument("--convention-target", action="append", default=[], metavar="SLUG=IRI",
                    help="결정 디렉토리 이름 → 결정 복합체 IRI — 절 청크(type: norm)의 items 가 가리키는 결정마다 한 번. "
                         "생성 BUILD 의 kb_composite.conventions 가 넘긴다(gen_build 가 결정 디렉토리에서 푼다). 입력에 결정의 "
                         "결론 청크가 있으면 그 디렉토리 이름도 스스로 푼다 (p12-norm-documents-from-section-chunks)")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — --merge 가 아니면 필수다"
                                                      "(kb_chunk·kb_decision 의 head 액션이 --residency defs/kb.bzl 로 넘긴다)")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다. "
                                                "agt:tokenCount 가 이 어휘로 센 수다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.merge:  # 병합은 이미 방출된 조각을 잇기만 한다 — parse_chunk 를 부르지 않으므로 값 어휘가 필요 없다
        return merge(args.out, args.files)
    if not args.residency:
        print(f"FAIL [{TAG}] --residency 가 없다 — defs/kb.bzl 이 이 액션의 입력이 아니다. 매크로·BUILD 에 //defs:kb.bzl 를 더한다",
              file=sys.stderr)
        return EXIT_CONFIG
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {args.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    try:  # 어휘는 한 번만 적재한다 — 액션 하나가 청크 여럿을 받는다 (복합체·결정)
        enc = load_tokenizer(args.vocab or None)
    except FileNotFoundError as e:
        print(f"FAIL [{TAG}] 어휘 파일 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    except ValueError as e:  # 해시가 고정값과 다르다 — 계수기가 재현되지 않는다
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL

    blocks, seen = [], {}
    composites: dict = {}   # iri -> {labels, members[]}
    part_refs: list = []    # (chunk_iri, composite_iri, path)
    errors = []
    space_errors = []       # 게이트 id `space` — FAIL [space] (설계 공간 청크가 head 생성기로 왔다)
    restored_errors = []    # 게이트 id `restored` — FAIL [restored] (복원 표시가 링크 대상에 없다)
    spec_errors = []        # 게이트 id `specialization` — FAIL [specialization] (자기 참조·사슬 순환)
    spec: dict = {}         # 조각 IRI → 원본 IRI — 링크 IRI 의 뿌리 계산 (단일 실행에서는 여기서, --merge 에서는 블록에서 읽는다)
    conventions = parse_convention_targets(args.out, args.convention_target, errors)  # 결정 slug → 결정 복합체 IRI
    parsed: list = []       # (경로, 메타, 본문) — 절 청크의 결정 slug 를 풀려면 입력 전부를 먼저 읽어야 한다
    for path in sorted(args.files):
        try:
            meta, body = parse_chunk(path)
        except OSError as e:
            print(f"FAIL [{TAG}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except SpecializationError as e:
            spec_errors.append(str(e))
            continue
        except ValueError as e:
            errors.append(str(e))
            continue
        if meta["id"] in seen:
            errors.append(f"{path}: IRI {meta['id']} 가 {seen[meta['id']]} 와 중복 — 한 청크는 한 파일이다")
            continue
        seen[meta["id"]] = path
        if meta["type"] == SPACE_TYPE:  # 후보는 head 로 올라가지 않는다 — 그래야 deps 가 되지 않는다 (p9-candidate-storage)
            space_errors.append(f"{path}: 설계 공간 청크(type: {SPACE_TYPE})는 head 그래프로 올리지 않는다 — 후보 링크는 확정 링크와 자리가 "
                                f"다르고 결코 deps 가 되지 않는다. tools/space2kg.py 로 올린다 (//space:design_space, p9-candidate-storage)")
            continue
        restored_errors += check_restored(path, meta)
        if SPECIALIZATION_KEY in meta:
            spec[meta["id"]] = meta[SPECIALIZATION_KEY]
        comp = meta.get("composite")
        if comp:
            if not (isinstance(comp, dict) and comp.get("id") and comp.get("title_ko") and comp.get("title")):
                errors.append(f"{path}: composite 는 {{id, title_ko, title}} 이어야 한다")
            elif comp["id"] in composites:
                errors.append(f"{path}: 복합체 {comp['id']} 가 {composites[comp['id']]['path']} 와 중복 선언됨")
            else:
                composites[comp["id"]] = {"ko": comp["title_ko"], "en": comp["title"], "members": [], "path": path,
                                          "order": comp.get(ORDERED_KEY),  # 선언된 순서 — 없으면 None
                                          "parent": comp.get(PART_OF_KEY)}  # 상위 복합체 — 없으면 None (뿌리)
        if meta.get("part_of"):
            part_refs.append((meta["id"], meta["part_of"], path))
        if meta["type"] == "decision" and Path(path).name == "conclusion.md" and isinstance(comp, dict) and comp.get("id"):
            conventions.setdefault(Path(path).parent.name, comp["id"])  # 입력 안의 결정 — 디렉토리 이름이 slug 다
        meta["_path"] = path
        parsed.append((path, meta, body))
    blocks += emit_parsed(parsed, conventions, enc, errors)  # 방출은 slug 사상이 다 모인 뒤다
    errors += attach_parts(composites, part_refs)  # 청크·복합체 부분을 복합체에 붙이고 사슬을 본다
    if args.ordered:  # 생성 BUILD 의 명시 인자 — 중첩 묶음에서는 부분 집합이 같은 복합체 하나를 고른다
        errors += order_errors(args.out, args.ordered, "--ordered")
        target = [c for c in composites.values() if c["order"] is not None and c["order"] == args.ordered]
        if not target:
            target = [c for c in composites.values() if c["order"] is None and sorted(m for m, _ in c["members"]) == sorted(args.ordered)]
        if len(target) != 1:
            errors.append(f"{args.out}: --ordered 가 가리키는 복합체를 하나로 고를 수 없다 — 선언된 복합체 {len(composites)}개 가운데 "
                          f"frontmatter composite.{ORDERED_KEY} 또는 부분 집합이 인자와 같은 것이 {len(target)}개다 "
                          f"(defs/kb.bzl 의 kb_decision·kb_composite 가 묶음마다 뿌리 복합체의 순서를 한 번 넘긴다)")
        else:
            target[0]["order"] = args.ordered
    errors += norm_composite_errors(composites, parsed)  # 규범 문서 — 머리 청크와 절 청크의 구분
    comp_blocks = []
    for iri, c in sorted(composites.items()):
        if not c["members"]:
            errors.append(f"{c['path']}: 복합체 {iri} 에 부분이 없다 — 멤버 청크가 part_of 로 가리켜야 한다")
            continue
        part_iris = sorted(m for m, _ in c["members"])
        order = c["order"]
        if order is not None and sorted(order) != part_iris:
            errors.append(f"{c['path']}: composite.{ORDERED_KEY} 가 부분 집합과 다르다 — 선언 {sorted(order)} · 부분 {part_iris}. "
                          f"순서 목록은 부분 전부를 빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared)")
            continue
        parts = " ,\n        ".join(f"<{m}>" for m in part_iris)
        block = (f"<{iri}>\n    a agt:Composite{' , co:List' if order else ''} ;\n"
                 f'    rdfs:label "{esc(c["en"])}"@en ;\n'
                 f'    rdfs:label "{esc(c["ko"])}"@ko ;\n'
                 f"    agt:hasDirectPart {parts}")
        if order:  # co:List — 색인은 1 부터의 양의 정수다 (Collections Ontology: co:item / co:ListItem / co:index / co:itemContent)
            items = " ,\n        ".join(f'[ a co:ListItem ; co:index "{n}"^^xsd:positiveInteger ; co:itemContent <{m}> ]'
                                       for n, m in enumerate(order, start=1))
            block += f" ;\n    co:item {items}"
        comp_blocks.append(block + " .")

    if not args.fragment:  # 단일 실행은 묶음 전체를 아니 뿌리 uuid 로 링크 IRI 를 계산한다 — --merge 와 같은 결과. 조각은 원 IRI 그대로
        blocks, spec_errors2 = rebase_links(blocks, spec)
        spec_errors += spec_errors2
    if errors or restored_errors or spec_errors or space_errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        for e in space_errors:
            print(f"FAIL [{SPACE_GATE}] {e}", file=sys.stderr)
        for e in restored_errors:
            print(f"FAIL [{RESTORED_GATE}] {e}", file=sys.stderr)
        for e in spec_errors:
            print(f"FAIL [{SPECIALIZATION_GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL

    body = "\n\n".join([b for _, b in sorted(blocks)] + comp_blocks)  # 정규 순서: 청크 IRI 순, 그다음 복합체 IRI 순 — union 과 merge 가 바이트 동일
    Path(args.out).write_text((body if args.fragment else PREAMBLE + "\n" + body) + "\n", encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
