---
id: https://agentic-knowledge-base.dev/id/chunk/2df3a3fc-2a35-47a4-b103-ee43239c8b3a
type: artifact
level: executable
title_ko: 함수 record_rows (tools/vv_run.py)
title: function record_rows in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/dda506f2-0686-4187-a9dc-b23cf1e83388]
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `record_rows(items)` 다. 실행 기록의 케이스 표·검증기 표의 데이터 행 — 두 표의 열은 같다(항목 · 실행 명령 · 결과 · 소요).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def record_rows(items: list[dict]) -> list[str]:
    """실행 기록의 케이스 표·검증기 표의 데이터 행 — 두 표의 열은 같다(항목 · 실행 명령 · 결과 · 소요)."""
    rows = []
    for c in items:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        skipped = len(c["commands"]) - ran
        note = tests_note(c["commands"])
        rows.append(f"| `{c['slug']}` | {ran} 실행 · {skipped} 건너뜀{' (' + note + ')' if note else ''} | {c['verdict']} | {c['secs']:.1f}s |")
    return rows
```
<!-- 인용 끝 -->
