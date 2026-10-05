---
id: https://agentic-knowledge-base.dev/id/chunk/d28af6b7-569b-4e83-b929-346995aa2fcb
type: artifact
level: executable
title_ko: 함수 item_table (tools/vv_run.py)
title: function item_table in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `item_table(items)` 다. 보고의 항목 표 데이터 행 — 케이스 표와 검증기 표가 같은 열을 쓴다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def item_table(items: list[dict]) -> list[str]:
    """보고의 항목 표 데이터 행 — 케이스 표와 검증기 표가 같은 열을 쓴다."""
    rows = []
    for c in items:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        spec = c["spec"]
        machine = " · ".join(filter(None, [f"자극 {len(spec['files'])}" if spec.get("files") else "",
                                           f"기대 {len(spec['expect'])}" if spec.get("expect") else ""])) or kb_lib.NONE_MARK
        rows.append(f"| `{c['slug']}` | {c['label']} | {ran} 실행 · {len(c['commands']) - ran} 건너뜀 | {machine} | **{c['verdict']}** | {c['secs']:.1f}s |")
    return rows
```
<!-- 인용 끝 -->
