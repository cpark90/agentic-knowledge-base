---
id: https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e
type: artifact
level: executable
title_ko: 함수 load_bzl_list (tools/kb_lib.py)
title: function load_bzl_list in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cf732fdc-d595-4d0b-8344-6af01989d95c
---
**함수** — `load_bzl_list(path, name)` 다. `defs/kb.bzl` 의 이름 목록 리터럴을 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_bzl_list(path: str | Path, name: str) -> tuple[str, ...]:
    """`defs/kb.bzl` 의 이름 목록 리터럴을 읽는다 — 리터럴 읽기의 정의처(`load_extracted_sources` 가 이것을 쓴다).

    값은 문자열 목록이고 Starlark 주석은 지운 뒤 `ast.literal_eval` 로 읽는다. 못 읽으면 ValueError 다 —
    판정 불가지 통과는 조용히 비는 것과 같다.
    """
    import ast

    text = Path(path).read_text(encoding="utf-8")
    m = (re.search(rf"^\s*{re.escape(name)}\s*=\s*\[([^\[\]\n]*)\]\s*$", text, re.M)  # 한 줄 꼴을 먼저 본다
         or re.search(rf"^\s*{re.escape(name)}\s*=\s*\[(.*?)^\]", text, re.M | re.S))  # 여러 줄 꼴
    if not m:
        raise ValueError(f"{path}: {name} 목록을 찾을 수 없다")
    body = re.sub(r"#[^\n]*", "", m.group(1))  # Starlark 주석 제거 — 값 안에 # 을 쓰지 않는다
    return tuple(ast.literal_eval("[" + body + "]"))
```
<!-- 인용 끝 -->
