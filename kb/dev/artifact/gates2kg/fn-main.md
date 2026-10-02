---
id: https://agentic-knowledge-base.dev/id/chunk/cdf1f234-455a-45ff-aa45-cc7d4fb9f6cb
type: artifact
level: executable
title_ko: 함수 main (tools/gates2kg.py)
title: function main in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T16:06:51Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4023eaae-fb57-4924-bb9b-beb8a2530ff2, https://agentic-knowledge-base.dev/id/chunk/5626d1aa-8b86-4c12-ab4c-ec1e76b25bb5, https://agentic-knowledge-base.dev/id/chunk/90fe8a83-bd07-4bb1-bd2c-fcdad7d246b7, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e]
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description="게이트 등록부 → 게이트 그래프 (-kg.ttl)")
    ap.add_argument("--out", required=True, help="출력 TTL 경로 (접미사 규약 0.2절의 `-kg`)")
    ap.add_argument("--gates", required=True, help="게이트 등록부의 원본 defs/kb.bzl")
    ap.add_argument("--registry", nargs="*", default=[], help="등록부 사이드카들 (tools/<도구>.chunks.yml) — agt:enforcedBy 의 대상")
    a = ap.parse_args()
    try:
        gates = kb_lib.load_gates(a.gates)
        tiers = kb_lib.load_bzl_list(a.gates, "GATE_TIERS")
        outside = kb_lib.load_bzl_list(a.gates, "GATE_TOOLS_OUTSIDE_PYTHON")
        layer = kb_lib.load_bzl_scalar(a.gates, kb_lib.GATE_LAYER_NAME)
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {a.gates}: 게이트 등록부를 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    ttl = emit(gates, tiers, layer, tool_composites(a.registry), outside, a.gates)
    try:
        Path(a.out).write_text(ttl, encoding="utf-8")
    except OSError as e:
        print(f"FAIL [{TAG}] {a.out}: 쓸 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    print(f"PASS [{TAG}] — 게이트 {len(gates)}개, 판정 도구 개체 {len(tool_composites(a.registry))}개", file=sys.stderr)
    return 0
```
<!-- 인용 끝 -->
