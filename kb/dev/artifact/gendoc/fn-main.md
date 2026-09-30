---
id: https://agentic-knowledge-base.dev/id/chunk/20316b94-1015-4306-8624-0463e63dd849
type: artifact
level: executable
title_ko: 함수 main (tools/gendoc.py)
title: function main in tools/gendoc.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gendoc}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/b6587551-3784-48fb-ae97-e98493afa24b
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--empty-dir", action="append", default=[], metavar="DIR",
                    help="파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지)")
    ap.add_argument("files", nargs="*", help="검사할 생성 문서")
    a = ap.parse_args()

    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    empty = {d.strip("/") for d in a.empty_dir}

    def exists(rel: str) -> bool:
        return (not rel) or (root / rel).exists() or rel.strip("/") in empty

    docs: list[Path] = []
    for f in a.files:
        p = Path(f)
        if not p.is_absolute() and workdir:
            p = Path(workdir) / p
        p = Path(os.path.abspath(p))
        try:
            docs.append(p.relative_to(root))
        except ValueError:
            print(f"FAIL [{TAG}] {f}: 루트 {root} 밖의 파일이다", file=sys.stderr)
            return EXIT_CONFIG
    missing = [str(d) for d in docs if not (root / d).is_file()]
    if missing:
        print(f"FAIL [{TAG}] 입력 문서가 없다: " + ", ".join(missing), file=sys.stderr)
        return EXIT_CONFIG
    if not docs:
        print(f"SKIP [{TAG}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    errors: list[str] = []
    for doc in sorted(set(docs)):
        text = (root / doc).read_text(encoding="utf-8")
        doc_errors, _g17 = kb_lib.check_gendoc(doc.as_posix(), text, exists)  # g17 은 보고 전용 — 게이트는 안 본다
        errors += [f"{doc}:{ln}: {why}" for ln, why in doc_errors]
    if errors:
        for e in errors:
            print(f"FAIL [{TAG}] {e}")
        print(f"\nFAIL [{TAG}] — {len(errors)}건 (생성 문서 {len(docs)}개). "
              f"규약의 단일 정의처는 `tools/kb_lib.py` 의 `gendoc_header`·`check_gendoc` 이다 — 게이트가 아니라 생성기를 고친다")
        return EXIT_FAIL
    print(f"PASS [{TAG}] — 생성 문서 {len(docs)}개")
    return EXIT_OK
```
<!-- 인용 끝 -->
