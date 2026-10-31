---
id: https://agentic-knowledge-base.dev/id/chunk/58750c29-c6bb-4d83-b464-517f160f955d
type: artifact
level: executable
title_ko: 함수 check_gate_catalogue (tools/doccheck.py)
title: function check_gate_catalogue in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4b222206-08d6-4720-9b58-644cd8cdd017, https://agentic-knowledge-base.dev/id/chunk/7985ad2f-b7d8-45b2-8d1f-a688617bb614, https://agentic-knowledge-base.dev/id/chunk/7cd8593d-71b7-426d-836f-f3ce1157dc54, https://agentic-knowledge-base.dev/id/chunk/a7114439-153f-4210-a8f9-965a33ad05f4, https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952, https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e]
part_of: https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197
---
**함수** — `check_gate_catalogue(doc, lines, gates_path)` 다. 총람이 게이트 등록부의 투영인가 — (게이트 위반, 보고 줄).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gate_catalogue(doc: Path, lines: list[str], gates_path: str) -> tuple[list[str], list[str]]:
    """총람이 게이트 등록부의 투영인가 — (게이트 위반, 보고 줄).

    등록부(`defs/kb.bzl` 의 `GATES`)가 원본이고 총람 표는 그 생성 투영이다. 절 안의 생성 구간(두 표지 사이)을
    `kb_lib.gate_catalogue_table` 로 다시 그려 바이트로 비교한다 — 생성기 `gates2kg --catalogue` 와 같은 렌더러다.
    표지가 없거나 겹치거나 절 밖에 있으면 FAIL, 구간이 재생성과 다르면 FAIL 이다. 표 앞뒤의 산문은 손 문서라
    비교하지 않는다.
    """
    section, _ = gate_catalogue_section(lines)
    if not section:
        return [f"{doc}: `{GATE_CATALOGUE_HEADING}` 절이 없다 — 게이트 등록부의 투영이 사라졌다"], []
    try:
        gates = kb_lib.load_gates(gates_path)
        tiers = kb_lib.load_bzl_list(gates_path, "GATE_TIERS")
    except (OSError, ValueError) as e:
        return [f"{doc}: 게이트 등록부를 읽을 수 없다 — {e}"], []
    regen = f"python3 tools/gates2kg.py --catalogue {doc.as_posix()}"
    text = "\n".join(section)
    if kb_lib.gate_catalogue_block(text) is None:
        return [f"{doc}: 게이트 총람 절에 생성 구간 표지가 하나씩 정확히 있지 않다 — "
                f"{kb_lib.GATE_CATALOGUE_OPEN} 와 {kb_lib.GATE_CATALOGUE_CLOSE}"], []
    missing = sorted(g for g, s in gates.items() if not s.get("decision"))
    if missing:
        return [f"{doc}: 등록부에 decision 이 없는 게이트 — {', '.join(missing)} (원본 {gates_path})"], []
    expected = kb_lib.splice_gate_catalogue(text, kb_lib.gate_catalogue_table(gates, tiers, doc.as_posix()))
    if expected != text:
        return [f"{doc}: 게이트 총람 표가 등록부 {gates_path} 의 재생성과 다르다 — 손으로 고치지 않는다. "
                f"재생성: {regen}"], []
    return [], [f"report [{TAG}] 총람 표가 등록부 {len(gates)}개의 재생성과 같다"]
```
<!-- 인용 끝 -->
