---
id: https://agentic-knowledge-base.dev/id/chunk/83067d35-114e-4213-babf-d03d8791e97c
type: artifact
level: executable
title_ko: 함수 main (tools/validate.py)
title: function main in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/02c3daad-5974-4be8-80ea-4c6b338b45de, https://agentic-knowledge-base.dev/id/chunk/05336a2f-bef3-4bc3-9b6d-976a1e9adb9d, https://agentic-knowledge-base.dev/id/chunk/07104b21-b283-4e54-a921-6b9a61fb6e45, https://agentic-knowledge-base.dev/id/chunk/0bc1d5ff-d788-47b3-a1b4-43a27654be04, https://agentic-knowledge-base.dev/id/chunk/0eba15f1-9ab6-4d48-bb9a-8809fc98a603, https://agentic-knowledge-base.dev/id/chunk/386f974f-846c-47c9-99dc-ee866783f5c5, https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f, https://agentic-knowledge-base.dev/id/chunk/56006161-22a8-4cff-9d03-2ec71941b721, https://agentic-knowledge-base.dev/id/chunk/6bf4337c-24c7-4689-8354-d179c822e031, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/7848189e-1a29-4f71-9bab-09f2623ff65f, https://agentic-knowledge-base.dev/id/chunk/7b782704-6d75-4344-9b72-f812f73bbfb0, https://agentic-knowledge-base.dev/id/chunk/7cd61807-8e8e-44e7-a140-c95f9f82e4f9, https://agentic-knowledge-base.dev/id/chunk/9126a0ff-4c8a-4088-969f-2b596ee08bdd, https://agentic-knowledge-base.dev/id/chunk/9d1171df-d5e6-4602-9c49-05605607011c, https://agentic-knowledge-base.dev/id/chunk/a0953baf-5b58-4667-ba87-2c4653097756, https://agentic-knowledge-base.dev/id/chunk/a45854d1-6d8a-4a1a-890e-a55aa166d992, https://agentic-knowledge-base.dev/id/chunk/ba1f7e1e-92c3-4692-9023-f2fb9dddbbc4, https://agentic-knowledge-base.dev/id/chunk/d26c3802-192f-4414-81da-25abd63211fc, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e9b943fe-3fee-4433-8018-038f1deb41c6, https://agentic-knowledge-base.dev/id/chunk/f5bba732-244e-40a1-a3a0-f5c8e97043be, https://agentic-knowledge-base.dev/id/chunk/f5d521a5-98ba-4f17-ada0-7ddbb7162850, https://agentic-knowledge-base.dev/id/chunk/fd4f59ff-fa52-4ead-afda-fc34d6efe930]
part_of: https://agentic-knowledge-base.dev/id/composite/d0b4b228-df49-490d-b346-c659c4c6e8da
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ontology", nargs="*", default=[], help="T-Box 모듈 파일들 (*-ontology, *-rules)")
    ap.add_argument("--shapes", nargs="*", default=[], help="SHACL shape 파일들 (*-shapes)")
    ap.add_argument("--odd", nargs="*", default=[], help="ODD 파일들 (*-odd)")
    ap.add_argument("--data", nargs="*", default=[], help="A-Box 파일들 (*-kg, *-space)")
    ap.add_argument("--reason", action="store_true", help="SHACL 전에 OWL-RL 추론 적용")
    ap.add_argument("--residency", default="", help="수준 허용표의 원본 defs/kb.bzl — 주면 shape 가 그 표와 같은지 본다")
    ap.add_argument("--gates", default="", metavar="FILE",
                    help="게이트 등록부의 원본 defs/kb.bzl — 주면 게이트 `gate-registry` 가 켜진다. 코드의 태그 "
                         "집합이 GATES·TOOL_TAGS 리터럴과 같은지, 손으로 둔 상수가 없는지 본다 (그래프 없이도 돈다)")
    ap.add_argument("--gate-sources", nargs="*", default=[],
                    help="게이트 `gate-registry` 가 태그를 훑을 소스 전수 (tools/*.py). --gates 와 함께 쓴다")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 게이트 token-budget 이 sha256 을 고정값과 대조한다. "
                                               "없으면 runfiles 의 고정 파일을 쓴다 (ODD id:cond-tokenizer-lock)")
    ap.add_argument("--verify-queries", default="", help="안티패턴 SPARQL 디렉토리 (2.5절 verify 계층)")
    ap.add_argument("--chunk-files", nargs="*", default=[],
                    help="청크 파일들(*.md) — 주면 element-drop 의 frontmatter 키 전수 대조가 켜진다")
    ap.add_argument("--standard-vocab", nargs="*", default=[],
                    help="등록 표준 어휘 원문(PROV-O·SKOS 등). 주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다")
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help="docs/waivers.md — 게이트 id `shacl`(축 `파일`)로 면제된 파일의 shape 위반은 집계에서 "
                         "빼되 `WAIVED [{SHACL}]` 줄로 남긴다. focus node → 파일은 agt:assertionLocation 이 정한다")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    try:
        waivers = kb_lib.load_waivers(args.waivers) if args.waivers else []
    except (OSError, ValueError) as e:  # 면제 표를 읽을 수 없다 — 배선 문제이지 판정 실패가 아니다
        print(f"FAIL [{VALIDATE_TAG}] waiver 표 — {e}")
        return EXIT_CONFIG

    if args.gates:  # 게이트 등록부 — 그래프가 아니라 리터럴과 소스를 본다 (M1 단일 정의처, 2026-10-02)
        try:
            errors += check_gate_registry(args.gates, args.gate_sources)
        except ConfigFailure as e:  # 리터럴·소스를 읽을 수 없다 — 배선 문제
            print(f"FAIL {e}")
            return EXIT_CONFIG

    n_files = len(args.ontology) + len(args.odd) + len(args.data) + len(args.shapes)
    if n_files == 0:
        if not args.gates:
            print(f"SKIP [{VALIDATE_TAG}] 검사 대상 0건 — 그래프 파일이 없다 (PASS 가 아니다)")
            return EXIT_SKIP
        if errors:
            for e in errors:
                print(f"FAIL {e}")
            print(f"\nFAIL [{VALIDATE_TAG}] — {len(errors)}건")
            return EXIT_FAIL
        print(f"PASS [{VALIDATE_TAG}] — 게이트 등록부 {len(kb_lib.load_gates(args.gates))}개 · "
              f"도구 태그 {len(kb_lib.load_tool_tags(args.gates))}개, 소스 {len(args.gate_sources)}개")
        return 0
    try:
        onto_merged, onto_files = load_files(args.ontology)
        odd_merged, odd_files = load_files(args.odd)
        data_merged, data_files = load_files(args.data)
        shapes_merged, shapes_files = load_files(args.shapes)
        std_terms, std_namespaces = load_standard_vocab(args.standard_vocab)
    except SyntaxFailure as e:  # 파싱되지 않는 입력 — 게이트가 판정을 내릴 수 없다
        print(f"FAIL [{SYNTAX}] {e}")
        return EXIT_CONFIG
    except Exception as e:  # 표준 어휘 원문 등 부속 입력의 실패
        print(f"FAIL [{SYNTAX}] {', '.join(args.standard_vocab) or '?'}: 파싱 실패 — {e}")
        return EXIT_CONFIG

    errors += check_labels(onto_files)
    errors += check_boundary(onto_files)
    errors += check_vocab({**odd_files, **data_files}, onto_merged)
    if args.standard_vocab:
        errors += check_standard_vocab({**onto_files, **shapes_files, **odd_files, **data_files}, std_terms, std_namespaces)

    merged = onto_merged + odd_merged + data_merged
    located = {**odd_files, **data_files}  # 개체 → 파일: FAIL 메시지의 <경로> 자리
    if args.odd:
        errors += check_odd_refs(merged, odd_merged, located)
    if data_files:
        errors += check_dangling(merged, onto_merged if args.ontology else None, located)
        errors += check_space(merged, located)
        errors += check_specialization(merged, located)
        errors += check_writer(merged)
        try:
            errors += check_catalog(merged, odd_merged if args.odd else None, located)
        except ConfigFailure as e:  # 상한을 판정할 수 없다 — 배선·ODD 문제
            print(f"FAIL {e}")
            return EXIT_CONFIG
        if args.ontology:
            warnings += check_deprecated_concepts(merged, onto_merged)
    if args.shapes:
        if args.residency:
            try:
                errors += check_residency(shapes_merged, args.residency, args.shapes)
                errors += check_token_budget(shapes_merged, args.residency, args.shapes, args.vocab)
            except ConfigFailure as e:  # 표를 읽을 수 없다 — 배선 문제
                print(f"FAIL {e}")
                return EXIT_CONFIG
        errors += check_shacl(merged, shapes_merged, args.reason, args.shapes, waivers)
    errors += check_element_drop(onto_merged if args.ontology else None, args.chunk_files)
    if args.verify_queries:
        errors += check_verify(merged, args.verify_queries)

    for w in warnings:
        print(f"warn {w}")
    if warnings:
        print(f"warn — {len(warnings)}건 (게이트 실패 아님)")

    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [{VALIDATE_TAG}] — {len(errors)}건")
        return EXIT_FAIL

    print(f"PASS [{VALIDATE_TAG}] — 파일 {n_files}개, 트리플 {len(merged)}개")
    return 0
```
<!-- 인용 끝 -->
