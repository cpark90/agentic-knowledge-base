---
id: https://agentic-knowledge-base.dev/id/chunk/e47a408f-6915-46d9-a923-6ff0b572ca18
type: artifact
level: executable
title_ko: 함수 main (tools/space2kg.py)
title: function main in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9875f781-35a4-413a-beae-89f20bb6ea33, https://agentic-knowledge-base.dev/id/chunk/a8dde51e-2d80-4281-9dad-fcf5f948abdb, https://agentic-knowledge-base.dev/id/chunk/cd2d5603-718a-4f3a-886a-3ce4d6b89880]
part_of: https://agentic-knowledge-base.dev/id/composite/2716ece9-44f6-48ff-b2ab-1ad0ea6fa6c0
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(design_space 규칙이 명시로 넘긴다)")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    enc = None
    if a.files:  # parse_chunk 를 실제로 부를 때만 값 어휘가 있어야 한다 — 아직 `-space` 청크가 없으면(빈 grap) 필요 없다
        try:
            chunk2kg.apply_plane_level_state(*chunk2kg.load_plane_level_state(a.residency))
        except (OSError, ValueError) as e:
            print(f"FAIL [{GATE}] {a.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        try:  # agt:Space 는 agt:Chunk 의 하위라 크기 사실(agt:tokenCount)을 갖는다 — 계수기는 고정된 어휘 하나다
            enc = kb_lib.load_tokenizer(a.vocab or None)
        except FileNotFoundError as e:
            print(f"FAIL [{GATE}] 어휘 파일 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except ValueError as e:
            print(f"FAIL [{GATE}] {e}", file=sys.stderr)
            return EXIT_FAIL

    blocks, errors, seen = [], [], {}
    for path in sorted(a.files):
        try:
            space = parse_space(path)
        except OSError as e:
            print(f"FAIL [{GATE}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        except (SpaceError, ValueError) as e:
            errors.append(str(e))
            continue
        iri = space["meta"]["id"]
        if iri in seen:
            errors.append(f"{path}: IRI {iri} 가 {seen[iri]} 와 중복 — 변수 하나가 파일 하나다")
            continue
        seen[iri] = path
        blocks.append(space)
    variables: dict = {}  # (출발 항목, 링크 타입) → 파일 — 같은 변수를 두 파일이 선언하면 거부한다
    for space in blocks:
        if space["var"] in variables:
            errors.append(f"{space['path']}: 변수 {space['var'][0]} × agt:{space['var'][1]} 가 {variables[space['var']]} 에도 있다 — "
                          f"변수 하나가 파일 하나다 (p9-candidate-storage)")
            continue
        variables[space["var"]] = space["path"]
    if errors:
        for e in errors:
            print(f"FAIL [{GATE}] {e}", file=sys.stderr)
        return EXIT_FAIL

    out: list = []
    for space in blocks:
        out += emit(space, enc)
    body = "\n\n".join(b for _, b in sorted(out))
    Path(a.out).write_text(PREAMBLE + ("\n" + body + "\n" if body else ""), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
