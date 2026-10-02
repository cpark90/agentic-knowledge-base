---
id: https://agentic-knowledge-base.dev/id/chunk/16c7fdef-8fd8-4248-95ec-85ff4668d9bd
type: artifact
level: executable
title_ko: 함수 main (tools/doccheck.py)
title: function main in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/145ba81b-fdd4-4cf8-aa11-b8ceb3165a08, https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/2674f907-6204-42f7-a25e-6789137904d6, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/4daa5f81-6009-493b-af58-f97f9a3f388c, https://agentic-knowledge-base.dev/id/chunk/58750c29-c6bb-4d83-b464-517f160f955d, https://agentic-knowledge-base.dev/id/chunk/6550bab7-f62f-40fd-893e-4d46be446f2f, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/cbb17652-19dd-4e9e-833d-0e61dfbd4110, https://agentic-knowledge-base.dev/id/chunk/d8304dd3-dfe1-49f3-bb99-12294f298b9c]
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--target-only", action="append", nargs="+", default=[], metavar="FILE",
                    help="링크 대상으로만 쓰고 안에서 나가는 링크는 검사하지 않는 문서 (반복 가능, 검사할 문서 뒤에 둔다)")
    ap.add_argument("--empty-dir", action="append", default=[], metavar="DIR",
                    help="파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지) — kb_doccheck_test 의 empty_dirs")
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help="docs/waivers.md — 게이트 id prose(축 파일)로 면제된 문서의 산문 위반은 세지 않는다. 없으면 면제 없음")
    ap.add_argument("--report", action="store_true",
                    help="보고 모드 — 문서(위치 인자, 없으면 진입점 문서 넷)의 수치를 생성물의 같은 이름 값과 대조한다. "
                         "이 모드의 위치 인자는 루트 밖 절대 경로를 허용한다. 판정이 아니므로 종료 코드는 0 이다")
    ap.add_argument("--gates", default="", metavar="FILE",
                    help="게이트 등록부의 원본 defs/kb.bzl — 주면 `docs/tools.md` 게이트 총람이 그 리터럴의 투영인지 "
                         "본다. 표의 `id` 열에 등록부 밖의 id 가 있으면 FAIL 이고, 반대 방향(총람에 없는 등록 id)은 보고다")
    ap.add_argument("files", nargs="*", help="검사할 문서 (--report 면 대조할 문서 — 없으면 진입점 문서 넷)")
    args = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(args.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    repo = Repo(root, set(args.empty_dir))
    if args.report:  # 게이트가 아니다 — 어긋난 쌍이 있어도 0 이다 (현상 agt:documentLag 의 관측 수단)
        # 위치 인자가 있으면 REPORT_DOCS(진입점 문서 넷) 대신 그 목록을 대조 대상으로 쓴다(2026-10-01, vnv 요청) —
        # 이 경로는 루트 밖 절대 경로를 허용한다(`report_doc_path`, `to_rel` 과 달리 거부하지 않는다).
        docs = tuple(report_doc_path(f, root, workdir) for f in args.files) if args.files else REPORT_DOCS
        for line in report_numbers(root, repo, docs)[0]:
            print(line)
        return 0
    try:
        skip = {to_rel(f, root, workdir) for group in args.target_only for f in group}
        docs = [d for d in (to_rel(f, root, workdir) for f in args.files) if d not in skip]
        missing = [str(d) for d in docs if not (root / d).is_file()]
        if missing:
            raise ValueError("입력 문서가 없다: " + ", ".join(missing))
    except ValueError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not docs:
        print(f"SKIP [{TAG}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP
    wpath = args.waivers
    if wpath and not os.path.isabs(wpath) and workdir:
        wpath = os.path.join(workdir, wpath)
    try:
        waivers = kb_lib.load_waivers(wpath) if wpath else []
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] waiver 표 — {e}", file=sys.stderr)
        return EXIT_CONFIG

    errors: list[tuple[str, str]] = []  # (게이트 id, 메시지) — 링크·경로는 doccheck, 산문은 prose
    reports: list[str] = []  # 보고 줄 — 판정이 아니다 (게이트 총람의 누락은 저작 판단이다)
    gates_path = args.gates
    if gates_path and not os.path.isabs(gates_path) and workdir:
        gates_path = os.path.join(workdir, gates_path)
    links = paths = segments = 0
    for doc in sorted(set(docs)):
        lines = repo.read(doc.as_posix())
        links += sum(1 for _, l in prose_lines(lines) for _ in find_links(CODE_SPAN.sub(" ", l)))
        paths += sum(1 for _, l in prose_lines(lines) for m in CODE_SPAN.finditer(l) if m.group(2).strip().startswith(PATH_PREFIXES))
        errors += [(TAG, e) for e in check_links(doc, lines, repo)]
        errors += [(TAG, e) for e in check_paths(doc, lines, repo)]
        text = "\n".join(lines)
        segments += len(kb_lib.prose_segments(text))
        prose_errors, _, _ = kb_lib.check_prose(doc.as_posix(), text, waivers)
        errors += [(PROSE, f"{doc}:{ln}: {reason}") for ln, reason in prose_errors]
        if args.gates and GATE_CATALOGUE_HEADING in text:  # 게이트 총람을 담은 문서 하나 (docs/tools.md)
            catalogue_errors, catalogue_report = check_gate_catalogue(doc, lines, gates_path)
            errors += [(TAG, e) for e in catalogue_errors]
            reports += catalogue_report

    for line in reports:
        print(line)
    if errors:
        for tag, e in errors:
            print(f"FAIL [{tag}] {e}")
        n_prose = sum(1 for tag, _ in errors if tag == PROSE)
        print(f"\nFAIL [{TAG}] — {len(errors)}건 (문서 {len(docs)}개; 링크·경로 {len(errors) - n_prose}, 산문 {n_prose})")
        return EXIT_FAIL
    print(f"PASS [{TAG}] — 문서 {len(docs)}개, 링크 {links}개, 백틱 경로 {paths}개, 산문 조각 {segments}줄")
    return 0
```
<!-- 인용 끝 -->
