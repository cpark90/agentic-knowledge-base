---
id: https://agentic-knowledge-base.dev/id/chunk/7db8af6e-60b5-47c0-9736-9ff0aba5fc88
type: artifact
level: executable
title_ko: 함수 write_catalogue (tools/gates2kg.py)
title: function write_catalogue in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7cd8593d-71b7-426d-836f-f3ce1157dc54, https://agentic-knowledge-base.dev/id/chunk/a7114439-153f-4210-a8f9-965a33ad05f4, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e]
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
---
**함수** — `write_catalogue(doc, gates_path)` 다. 문서의 게이트 총람 생성 구간을 등록부에서 다시 그려 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_catalogue(doc: str, gates_path: str) -> int:
    """문서의 게이트 총람 생성 구간을 등록부에서 다시 그려 쓴다 — 표지 밖의 손 산문은 그대로다."""
    try:
        gates = kb_lib.load_gates(gates_path)
        tiers = kb_lib.load_bzl_list(gates_path, "GATE_TIERS")
        text = Path(doc).read_text(encoding="utf-8")
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] 총람 입력을 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    missing = sorted(g for g, s in gates.items() if not s.get("decision"))
    if missing:
        print(f"FAIL [{TAG}] {gates_path}: decision 이 없는 게이트 — {', '.join(missing)}", file=sys.stderr)
        return EXIT_FAIL
    new = kb_lib.splice_gate_catalogue(text, kb_lib.gate_catalogue_table(gates, tiers, doc))
    if new is None:
        print(f"FAIL [{TAG}] {doc}: 생성 구간 표지가 하나씩 정확히 있지 않다 — "
              f"{kb_lib.GATE_CATALOGUE_OPEN} 와 {kb_lib.GATE_CATALOGUE_CLOSE}", file=sys.stderr)
        return EXIT_FAIL
    if new != text:
        Path(doc).write_text(new, encoding="utf-8")
    print(f"PASS [{TAG}] — 총람 {doc}: 게이트 {len(gates)}개", file=sys.stderr)
    return 0
```
<!-- 인용 끝 -->
