---
id: https://agentic-knowledge-base.dev/id/chunk/4575d9a3-a280-4905-a59f-154e4dac2ae0
type: artifact
level: executable
title_ko: 함수 main (tools/weave.py)
title: function main in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/18d615ae-85a5-4737-825a-7674dc3b3ce9, https://agentic-knowledge-base.dev/id/chunk/3abf45b4-eb13-4c63-80e4-83848c227928, https://agentic-knowledge-base.dev/id/chunk/4650cc1b-20d3-4c11-8858-478478d8b2c2, https://agentic-knowledge-base.dev/id/chunk/4ed2982d-49b2-4313-856e-6b86a53fb3b0, https://agentic-knowledge-base.dev/id/chunk/53b29448-345d-4abe-b57a-44a8f6ed1d5d, https://agentic-knowledge-base.dev/id/chunk/5b372e8e-c287-4ed0-b9d6-16c0366ee0c8, https://agentic-knowledge-base.dev/id/chunk/74d3682e-98df-428f-a8dd-776e8c5027e8, https://agentic-knowledge-base.dev/id/chunk/c72423ba-8082-4594-8317-046edbd135ed, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1, https://agentic-knowledge-base.dev/id/chunk/fc1144d8-e0cf-4dc0-a8f5-0d9822fb0334]
part_of: https://agentic-knowledge-base.dev/id/composite/17bed729-be8b-4186-8432-0a0e0f1b5673
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", required=True, choices=kb_lib.WEAVE_KINDS)
    ap.add_argument("--out", required=True)
    ap.add_argument("--root", default=os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    ap.add_argument("--bodies", nargs="*", default=[], metavar="MD", help="단위 지식 파일들 — adr 의 결론·근거·대안 본문, audit 의 관측 본문")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — bodies 를 읽을 때만 쓴다"
                                                      "(load_bodies → parse_chunk). 안 주면 이 모듈의 defs/kb.bzl(kb_lib.default_residency)을 쓴다")
    ap.add_argument("--spaces", nargs="*", default=[], help="설계 공간 그래프(//space:design_space) — union 에 섞지 않고 audit 의 증거 극성 절에만 쓴다")
    ap.add_argument("--questions", nargs="*", default=[], metavar="MD", help="질문지들(//harness:records) — questions 가 harness/user/Q-*.md · "
                                                                             "archive/Q-*.md · archive/legacy/*.md 만 읽고 나머지는 건너뛴다")
    ap.add_argument("ttl", nargs="*", help="그래프 파일들 (없으면 kb_lib.UNION_GRAPH_PATHS + 온톨로지 모듈)")
    a = ap.parse_args()
    root = Path(a.root)
    if a.bodies:  # load_bodies 가 parse_chunk 를 부르므로 그때만 값 어휘가 있어야 한다
        residency = a.residency or kb_lib.default_residency()  # 이 모듈의 값 어휘 원본 (task 0327 손질 6)
        try:
            apply_plane_level_state(*load_plane_level_state(residency))
        except (OSError, ValueError) as e:
            print(f"CONFIG [{TAG}] {residency}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
    try:
        g = kb_lib.load_union(a.ttl, root)
        bodies = load_bodies(a.bodies) if a.kind in ("adr", "audit") else {}
        citing = load_citing(a.bodies) if a.kind == "questions" else []
        gs = Graph()
        for f in a.spaces:
            gs.parse(f, format="turtle")
    except ValueError as e:
        print(f"CONFIG [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    except OSError as e:
        print(f"CONFIG [{TAG}] {getattr(e, 'filename', '')}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    m = Model(g)
    sheets = [p for p in a.questions if SHEET_FILE.search(kb_lib.gendoc_input_name(p))]
    legacy = [p for p in a.questions if LEGACY_FILE.search(kb_lib.gendoc_input_name(p))]
    inputs = (a.ttl or list(kb_lib.UNION_GRAPH_PATHS)) + list(a.spaces) + list(a.bodies) + sheets + legacy
    text = {"adr": lambda: render_adr(m, bodies, inputs, root),
            "requirements": lambda: render_requirements(m, inputs),
            "changelog": lambda: render_changelog(m, inputs),
            "audit": lambda: render_audit(m, bodies, inputs, gs, a.spaces),
            "questions": lambda: render_questions(m, citing, sheets, legacy, inputs)}[a.kind]()
    Path(a.out).write_text(text, encoding="utf-8")
    return EXIT_OK
```
<!-- 인용 끝 -->
