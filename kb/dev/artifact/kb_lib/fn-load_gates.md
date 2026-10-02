---
id: https://agentic-knowledge-base.dev/id/chunk/e51ab77c-0ffd-4d58-a3cb-d622e9134952
type: artifact
level: executable
title_ko: 함수 load_gates (tools/kb_lib.py)
title: function load_gates in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81]
part_of: https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c
---
**함수** — `load_gates(path)` 다. `defs/kb.bzl` 의 `GATES` 리터럴을 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_gates(path: str | Path | None = None) -> dict[str, dict[str, str]]:
    """`defs/kb.bzl` 의 `GATES` 리터럴을 읽는다 — id → {tier, tool, ko, desc} (load_residency 와 같은 해법).

    `path` 가 없으면 `gates_bzl_path()` 가 찾는다. 리터럴을 못 읽으면 ValueError 다 — 등록부가 조용히 비면
    태그 집합 대조가 무력해지므로 통과시키지 않는다.
    """
    import ast

    p = Path(path) if path else gates_bzl_path()
    text = p.read_text(encoding="utf-8")
    m = re.search(rf"^\s*{re.escape(GATES_NAME)}\s*=\s*\{{(.*?)^\}}", text, re.M | re.S)
    if not m:
        raise ValueError(f"{p}: {GATES_NAME} 리터럴을 찾을 수 없다")
    body = re.sub(r"#[^\n]*", "", m.group(1))  # Starlark 주석 제거 — 값 안에 # 을 쓰지 않는다
    table = ast.literal_eval("{" + body + "}")
    if not table:
        raise ValueError(f"{p}: {GATES_NAME} 가 비어 있다 — 게이트 없는 하네스는 하네스가 아니다")
    return table
```
<!-- 인용 끝 -->
