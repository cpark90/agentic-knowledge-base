---
id: https://agentic-knowledge-base.dev/id/chunk/060d5b4a-ce00-45a6-893c-e9a0c787372f
type: artifact
level: executable
title_ko: 함수 load_bzl_dict (tools/kb_lib.py)
title: function load_bzl_dict in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
---
**함수** — `load_bzl_dict(path, name, allow_empty)` 다. `defs/kb.bzl` 의 문자열 → 문자열 사전 리터럴을 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_bzl_dict(path: str | Path, name: str, allow_empty: bool = False) -> dict[str, str]:
    """`defs/kb.bzl` 의 문자열 → 문자열 사전 리터럴을 읽는다 — `VIEWS` 처럼 키마다 값 하나인 자리.

    `load_gates` 와 같은 해법이다(Starlark 주석을 지운 뒤 `ast.literal_eval`). 못 읽으면 ValueError 다. 비어도
    ValueError 다 — 표가 조용히 비면 그 표의 투영도 조용히 빈다. `allow_empty` 는 비어 있는 것이 선언된 상태인
    표(`NORM_DOCS` — 문서를 옮기기 전)만 준다. 한 줄 꼴(`NAME = {}`)과 여러 줄 꼴을 둘 다 읽는다.
    """
    import ast

    text = Path(path).read_text(encoding="utf-8")
    m = (re.search(rf"^\s*{re.escape(name)}\s*=\s*\{{([^{{}}\n]*)\}}\s*$", text, re.M)  # 한 줄 꼴을 먼저 본다
         or re.search(rf"^\s*{re.escape(name)}\s*=\s*\{{(.*?)^\}}", text, re.M | re.S))
    if not m:
        raise ValueError(f"{path}: {name} 사전을 찾을 수 없다")
    table = ast.literal_eval("{" + re.sub(r"#[^\n]*", "", m.group(1)) + "}")
    if not table and not allow_empty:
        raise ValueError(f"{path}: {name} 가 비어 있다")
    return table
```
<!-- 인용 끝 -->
