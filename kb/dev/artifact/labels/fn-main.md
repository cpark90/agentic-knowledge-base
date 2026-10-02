---
id: https://agentic-knowledge-base.dev/id/chunk/2de0214e-da86-4ca9-bb6b-de72b5dcefca
type: artifact
level: executable
title_ko: 함수 main (tools/labels.py)
title: function main in tools/labels.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-labels}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20, https://agentic-knowledge-base.dev/id/chunk/f13654f3-9b08-41f4-a1f1-9688dccc4dd0]
part_of: https://agentic-knowledge-base.dev/id/composite/fba87a37-4ad2-4ccb-b556-a27d4ef6b9d2
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(kb_index 매크로가 명시로 넘긴다)")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [labels] {args.residency}: 읽을 수 없다 — {e}", file=sys.stderr)
        return kb_lib.EXIT_CONFIG

    groups: dict = defaultdict(list)
    for path in args.files:
        meta, body = parse_chunk(path)
        # 색인의 크기 열은 **줄 수**다 — 파일의 서술이고 크기 규칙(토큰)이 아니다. 본문은 parse_chunk 가 뗀 것 하나다
        groups[str(Path(path).parent)].append((meta, len(body.splitlines()), path))
    by_plane: dict = defaultdict(list)
    for d in sorted(groups):
        by_plane[plane_of(d)].append(d)

    head = kb_lib.gendoc_header(
        "index", "라벨 목록", "tools/labels.py",
        "청크 파일마다 frontmatter 의 한글 라벨 · 영문 라벨 · plane/level · 상태 · 본문 줄 수 · 복합체 여부를 "
        "plane 디렉토리와 항목 디렉토리로 묶어 — 라벨 목록이 본문보다 먼저 읽히는 것의 파일 형태다 (4.4절)",
        "bazel build //kb/dev:index", args.files,
        f"청크 {len(args.files)}개 · 디렉토리 {len(groups)}개",
        kb_lib.gendoc_view_notice("각 청크의 frontmatter"), input_kind="청크 파일")

    out: list[str] = []
    for plane in sorted(by_plane):
        out += [f"## {plane}", ""]
        for d in by_plane[plane]:
            if d != plane:
                out += [f"### {d}", ""]
            out.append(kb_lib.GENDOC_QUOTE_OPEN)  # 라벨은 청크에서 그대로 옮긴 값이다 — 생성기가 고쳐 쓰지 않는다
            for meta, n, path in sorted(groups[d], key=lambda t: (t[0]["type"], t[0]["level"], t[0]["title_ko"])):
                comp = " · 복합체" if meta.get("composite") else ""
                # 링크는 저장소 루트 기준이다 — 이 파일은 전 패키지를 한 파일로 합치므로 파일명 상대 링크가 성립하지 않는다 (G13)
                out.append(f"- [{meta['title_ko']}](/{kb_lib.gendoc_input_name(path)}) — {meta['title']} · "
                           f"{meta['type']}/{meta['level']} · {meta['status']} · {n}줄{comp}")
            out += [kb_lib.GENDOC_QUOTE_CLOSE, ""]
    Path(args.out).write_text(kb_lib.gendoc_assemble(head, out, args.files, input_kind="청크 파일"), encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
