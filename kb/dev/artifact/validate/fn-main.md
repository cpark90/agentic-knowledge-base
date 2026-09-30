---
id: https://agentic-knowledge-base.dev/id/chunk/83067d35-114e-4213-babf-d03d8791e97c
type: artifact
level: executable
title_ko: 함수 main (tools/validate.py)
title: function main in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
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
    ap.add_argument("--verify-queries", default="", help="안티패턴 SPARQL 디렉토리 (2.5절 verify 계층)")
    ap.add_argument("--chunk-files", nargs="*", default=[],
                    help="청크 파일들(*.md) — 주면 element-drop 의 frontmatter 키 전수 대조가 켜진다")
    ap.add_argument("--standard-vocab", nargs="*", default=[],
                    help="등록 표준 어휘 원문(PROV-O·SKOS 등). 주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다")
    args = ap.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    n_files = len(args.ontology) + len(args.odd) + len(args.data) + len(args.shapes)
    if n_files == 0:
        print("SKIP [validate] 검사 대상 0건 — 그래프 파일이 없다 (PASS 가 아니다)")
        return EXIT_SKIP
    try:
        onto_merged, onto_files = load_files(args.ontology)
        odd_merged, odd_files = load_files(args.odd)
        data_merged, data_files = load_files(args.data)
        shapes_merged, shapes_files = load_files(args.shapes)
        std_terms, std_namespaces = load_standard_vocab(args.standard_vocab)
    except SyntaxFailure as e:  # 파싱되지 않는 입력 — 게이트가 판정을 내릴 수 없다
        print(f"FAIL [syntax] {e}")
        return EXIT_CONFIG
    except Exception as e:  # 표준 어휘 원문 등 부속 입력의 실패
        print(f"FAIL [syntax] {', '.join(args.standard_vocab) or '?'}: 파싱 실패 — {e}")
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
                errors += check_line_budget(shapes_merged, args.residency, args.shapes)
            except ConfigFailure as e:  # 표를 읽을 수 없다 — 배선 문제
                print(f"FAIL {e}")
                return EXIT_CONFIG
        errors += check_shacl(merged, shapes_merged, args.reason, args.shapes)
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
        print(f"\nFAIL [validate] — {len(errors)}건")
        return EXIT_FAIL

    print(f"PASS [validate] — 파일 {n_files}개, 트리플 {len(merged)}개")
    return 0
```
<!-- 인용 끝 -->
