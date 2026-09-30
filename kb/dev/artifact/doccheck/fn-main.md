---
id: https://agentic-knowledge-base.dev/id/chunk/16c7fdef-8fd8-4248-95ec-85ff4668d9bd
type: artifact
level: executable
title_ko: 함수 main (tools/doccheck.py)
title: function main in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984
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
    ap.add_argument("files", nargs="*", help="검사할 문서")
    args = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(args.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    repo = Repo(root, set(args.empty_dir))
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
