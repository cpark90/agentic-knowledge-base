---
id: https://agentic-knowledge-base.dev/id/chunk/7cd8593d-71b7-426d-836f-f3ce1157dc54
type: artifact
level: executable
title_ko: 함수 gate_catalogue_table (tools/kb_lib.py)
title: function gate_catalogue_table in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/81809a6f-d845-4673-8a0f-b53283ae332c
---
**함수** — `gate_catalogue_table(gates, tiers, doc)` 다. 등록부 → 총람 표의 줄들.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gate_catalogue_table(gates: dict[str, dict[str, str]], tiers: tuple[str, ...] | list[str], doc: str) -> list[str]:
    """등록부 → 총람 표의 줄들. 행 순서는 실행 계층(`GATE_TIERS` 선언 순)과 id 다.

    `doc` 은 표가 들어갈 문서의 저장소 상대 경로이고 결정 링크의 상대 경로를 정한다. 셀은 등록부의 값을 그대로
    옮긴다 — `|` 는 셀 구분자라 이스케이프한다.
    """
    order = {t: i for i, t in enumerate(tiers)}
    base = os.path.dirname(doc) or "."

    def cell(s: str) -> str:
        return s.replace("|", "\\|")

    lines = ["| " + " | ".join(GATE_CATALOGUE_HEADER) + " |", "|" + "---|" * len(GATE_CATALOGUE_HEADER)]
    for gid in sorted(gates, key=lambda g: (order.get(gates[g]["tier"], len(order)), g)):
        s = gates[gid]
        link = os.path.relpath(f"{DECISION_DIR}/{s['decision']}/conclusion.md", base).replace(os.sep, "/")
        lines.append(f"| `{gid}` | {cell(s['ko'])} | {cell(s['desc'])} | {s['tier']} | `{s['tool']}` | "
                     f"[`{s['decision']}`]({link}) |")
    return lines
```
<!-- 인용 끝 -->
