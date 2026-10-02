---
id: https://agentic-knowledge-base.dev/id/chunk/58750c29-c6bb-4d83-b464-517f160f955d
type: artifact
level: executable
title_ko: 함수 check_gate_catalogue (tools/doccheck.py)
title: function check_gate_catalogue in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/488bd7ba-cb14-4e6c-94f4-119987372f1f, https://agentic-knowledge-base.dev/id/chunk/7985ad2f-b7d8-45b2-8d1f-a688617bb614, https://agentic-knowledge-base.dev/id/chunk/c32e7981-57d1-4c87-bd5a-a41189661360, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952]
part_of: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197
---
**함수** — `check_gate_catalogue(doc, lines, gates_path)` 다. 총람이 게이트 등록부의 투영인가 — (게이트 위반, 보고 줄).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gate_catalogue(doc: Path, lines: list[str], gates_path: str) -> tuple[list[str], list[str]]:
    """총람이 게이트 등록부의 투영인가 — (게이트 위반, 보고 줄).

    등록부(`defs/kb.bzl` 의 `GATES`·`TOOL_TAGS`)가 원본이고 총람은 손으로 쓴 투영이다 (3단계에서 생성 뷰로
    바꾼다). **게이트로 올리는 방향은 하나다** — 표의 `id` 열에 등록부 밖의 id 가 있으면 FAIL. 그 반대 방향
    (등록됐으나 총람에 없는 id)은 보고다: 총람 표는 노트 6.7절의 규칙 단위로 묶여 있고 하네스 자체의 게이트는
    표 아래 산문이 적으므로, 누락은 저작 판단이 필요하고 기계가 가를 수 없다.
    """
    section, _ = gate_catalogue_section(lines)
    if not section:
        return [f"{doc}: `{GATE_CATALOGUE_HEADING}` 절이 없다 — 게이트 등록부의 투영이 사라졌다"], []
    try:
        gates = kb_lib.load_gates(gates_path)
        tool_tags = kb_lib.load_tool_tags(gates_path)
    except (OSError, ValueError) as e:
        return [f"{doc}: 게이트 등록부를 읽을 수 없다 — {e}"], []
    registered = set(gates) | set(tool_tags)
    in_table = gate_catalogue_ids(section)
    errors = [f"{doc}: 총람 표의 `{GATE_CATALOGUE_ID_COLUMN}` 열에 등록부 밖의 id `{gid}` 가 있다 — "
              f"원본은 {gates_path} 의 GATES 이고 총람은 그 투영이다"
              for gid in sorted(in_table - registered)]
    tokens = {m.group(1) for line in section for m in BACKTICK_TOKEN.finditer(line)}
    absent = sorted(registered - tokens)
    report = [f"report [{TAG}] 총람에 없는 등록 게이트 {len(absent)}개 — {', '.join(absent)}" if absent else
              f"report [{TAG}] 총람이 등록부 {len(registered)}개를 모두 적는다"]
    return errors, report
```
<!-- 인용 끝 -->
