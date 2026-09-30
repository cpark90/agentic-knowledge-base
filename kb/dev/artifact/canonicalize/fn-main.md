---
id: https://agentic-knowledge-base.dev/id/chunk/04b68be9-58b9-4c04-8eab-6c48e91ef5cb
type: artifact
level: executable
title_ko: 함수 main (tools/canonicalize.py)
title: function main in tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
part_of: https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

    # `bazel run` 은 runfiles 디렉토리에서 실행되므로, 사용자가 준 상대 경로는
    # 호출 위치(BUILD_WORKING_DIRECTORY) 기준으로 되돌려 원본 파일을 가리키게 한다.
    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")

    dirty = []
    for f in args.files:
        p = Path(f)
        if workdir and not p.is_absolute() and args.write:
            p = Path(workdir) / p
        try:
            canon = canonical_text(p)
            current = p.read_text(encoding="utf-8")
        except Exception as e:  # OSError·rdflib 파서 — 판정 불가 입력
            print(f"FAIL [canon] {f}: 읽거나 파싱할 수 없다 — {e}")
            return EXIT_CONFIG
        if args.write:
            if current != canon:
                p.write_text(canon, encoding="utf-8")
                print(f"wrote {f}")
        else:
            if current != canon:
                dirty.append(f)

    if args.check and dirty:
        for f in dirty:
            print(f"FAIL [canon] {f}: 정규형과 다름 — bazel run //tools:canonicalize -- --write {f}")
        print(f"\nFAIL [canon] — {len(dirty)}건")
        return EXIT_FAIL
    if args.check:
        print(f"PASS [canon] — {len(args.files)}개 정규형")
    return 0
```
<!-- 인용 끝 -->
