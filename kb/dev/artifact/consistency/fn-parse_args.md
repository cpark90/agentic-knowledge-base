---
id: https://agentic-knowledge-base.dev/id/chunk/6a2ce90d-fc6f-4a07-85c9-c5f648738065
type: artifact
level: executable
title_ko: 함수 parse_args (tools/consistency.py)
title: function parse_args in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/c10c407c-9993-4ba9-a09f-bfdc6e910b5e
---
**함수** — `parse_args()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_args():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--theta", type=float, default=0.5)
    ap.add_argument("--theta-cohesion", type=float, default=None, help="묶인 쌍의 응집 하한 (기본 θ/2)")
    ap.add_argument("--glossary", default="")
    ap.add_argument("--waivers", default="",
                    help=f"docs/waivers.md — 게이트 id {GATE_TERM}·{ADDITION_GATE}·{EMPTY_VALUE_GATE}·{LIST_RULES_GATE}, 축 파일")
    ap.add_argument("--residency", default=os.path.join(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."), "defs/kb.bzl"),
                    help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다(kb_consistency 매크로가 명시로 넘긴다)")
    ap.add_argument("chunks", nargs="+")
    return ap.parse_args()
```
<!-- 인용 끝 -->
