---
id: https://agentic-knowledge-base.dev/id/chunk/e63b5c07-0a99-4f22-a27e-db9c5983093c
type: artifact
level: executable
title_ko: 함수 main (tools/gen_norms.py)
title: function main in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/060d5b4a-ce00-45a6-893c-e9a0c787372f, https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41, https://agentic-knowledge-base.dev/id/chunk/f535cb9d-5732-45d9-857d-ac0129c7eead]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    ap.add_argument("--doc", default="", help="이 문서 stem 만 낸다 — 판정은 문서 전체로 한다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root 기준")
    ap.add_argument("--norm-docs", default="", help=f"{NORM_DOCS_NAME} 리터럴을 담은 파일 — 안 주면 --residency 와 같다(고정물 시험의 자리)")
    a = ap.parse_args()
    root = Path(a.root)
    bzl = Path(a.residency) if a.residency else root / "defs" / "kb.bzl"
    try:
        apply_plane_level_state(*load_plane_level_state(bzl))
        docs = kb_lib.load_bzl_dict(a.norm_docs or bzl, NORM_DOCS_NAME, allow_empty=True)
    except (OSError, ValueError) as e:
        print(f"FAIL [{GEN}] {a.norm_docs or bzl}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    try:
        outputs = generate(root, docs, a.doc)
    except GenNormsError as e:
        for line in str(e).splitlines():
            print(f"FAIL [{GEN}] {line}")
        return EXIT_FAIL
    except ValueError as e:  # parse_chunk 의 frontmatter·절 키 규칙 — chunk2kg 의 판정을 생성 시점에 그대로 낸다
        print(f"FAIL [{GEN}] {e}")
        return EXIT_FAIL
    except OSError as e:
        print(f"FAIL [{GEN}] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    drift = []
    for out, content in outputs.items():
        p = root / out
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(out)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{out} (트리)", f"{out} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content, encoding="utf-8")
    if a.check:
        for out in drift:
            print(f"FAIL [{DRIFT}] {out}: 원본(절 청크 · 결정의 규약 줄)과 어긋난다 — python3 tools/gen_norms.py --root . 를 돌려 커밋하라")
        if drift:
            print(f"\nFAIL [{DRIFT}] — 어긋남 {len(drift)}건 / 생성 문서 {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT}] — 생성 문서 {len(outputs)}개가 원본과 일치")
        return EXIT_OK
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(drift))
    return EXIT_OK
```
<!-- 인용 끝 -->
