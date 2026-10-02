---
id: https://agentic-knowledge-base.dev/id/chunk/13764782-d9fa-4695-8725-3cc97d1f54ee
type: artifact
level: executable
title_ko: 함수 main (tools/tokens.py)
title: function main in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/132c7aa3-afb6-446f-be54-deeaff4e3460, https://agentic-knowledge-base.dev/id/chunk/63cf4a6b-7be3-4c38-8be4-9a039b8d5aec, https://agentic-knowledge-base.dev/id/chunk/84687e20-5870-4ee0-be02-862d00aafbff]
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chunks", nargs="*", help="청크 파일. 없으면 청크 디렉토리 전부를 훑는다")
    ap.add_argument("--vocab", default="", help="어휘 파일 경로. 없으면 runfiles 의 고정 파일을 쓴다")
    ap.add_argument("--out", default="", help="보고를 쓸 경로")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    try:
        vocab = kb_lib.tokenizer_vocab_path(a.vocab or None)
        enc = kb_lib.load_tokenizer(vocab)
    except FileNotFoundError as e:
        print(f"FAIL [{GATE}] 어휘 파일 — {e}")
        return EXIT_CONFIG
    except ValueError as e:
        print(f"FAIL [{GATE}] {e}")
        return EXIT_FAIL
    try:
        paths = [Path(c) for c in a.chunks] if a.chunks else discover(root)
        rows = measure(paths, root, enc)
    except OSError as e:
        print(f"FAIL [{GATE}] 입력 — 읽을 수 없다: {e}")
        return EXIT_CONFIG
    if not rows:
        print(f"SKIP [{GATE}] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP
    text = render(rows, paths, vocab)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return EXIT_OK
```
<!-- 인용 끝 -->
