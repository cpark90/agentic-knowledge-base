---
id: https://agentic-knowledge-base.dev/id/chunk/82fb6ab2-dfdf-4445-9207-e0a74ab2ab02
type: artifact
level: executable
title_ko: 함수 command_table (tools/vv_run.py)
title: function command_table in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9dc7489b-268b-4ce2-9f99-fdb748499729]
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `command_table(items)` 다. 보고의 명령 표 데이터 행 — 명령 하나가 한 행이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def command_table(items: list[dict]) -> list[str]:
    """보고의 명령 표 데이터 행 — 명령 하나가 한 행이다."""
    rows = []
    for c in items:
        for x in c["commands"]:
            if x["skip"] is None:
                t = x.get("tests")
                note = (f"테스트 {t[0]} · 실행 {t[1]} · 캐시 {t[0] - t[1]}" if t else "요약 줄 없음" if x["cmd"].startswith("bazel test ") else "") + \
                       ("" if not x["mismatch"] else " · **어긋남**")
                rows.append(f"| `{c['slug']}` | `{x['cmd']}` | {x['rc']} | {expect_note(x.get('expect'))} | {x['secs']:.1f}s | {note or kb_lib.NONE_MARK} |")
            else:
                rows.append(f"| `{c['slug']}` | `{x['cmd']}` | SKIP | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {x['skip']} |")
    return rows
```
<!-- 인용 끝 -->
