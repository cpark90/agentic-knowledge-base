---
id: https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac
type: artifact
level: executable
title_ko: 함수 load_residency (tools/kb_lib.py)
title: function load_residency in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
---
**함수** — `load_residency(path)` 다. `defs/kb.bzl` 의 `PLANES`·`LEVELS`·`RESIDENCY` 를 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_residency(path: str | Path) -> tuple[list[str], list[str], dict[str, list[str]]]:
    """`defs/kb.bzl` 의 `PLANES`·`LEVELS`·`RESIDENCY` 를 읽는다 — (plane 순서, 수준 순서, plane → 허용 수준들).

    `PLANES`·`LEVELS` 리터럴은 `tools/chunk2kg.py` 의 `load_plane_level_state` 를 그대로 불러 쓴다 — 리터럴 읽기
    함수(정규식 + `ast.literal_eval`)의 정의처를 하나로 모은 것이다(`chunk2kg`가 rdflib 없이 타깃마다 돌아 이
    모듈을 반대로 import할 수 없으므로 방향은 이쪽에서만 간다, `weave`·`extract_refs`가 `chunk2kg.py` 를 srcs 로
    끌어 쓰는 것과 같은 방식). `RESIDENCY` 표는 이 파일이 정의처인 채로 남는다 — `LEVELS`·`PLANES` 만 참조하는 값
    치환이라 그 값을 chunk2kg 에서 받아 여기서 마무리한다. 표를 못 읽으면 ValueError — 판정 불가지 통과가 아니다.
    """
    import ast

    text = Path(path).read_text(encoding="utf-8")
    planes, levels, _states = load_plane_level_state(path)
    body = _BZL_RESIDENCY.search(text)
    if not body:
        raise ValueError(f"{path}: RESIDENCY 표를 찾을 수 없다")
    src = re.sub(r"#[^\n]*", "", body.group(1))  # Starlark 주석 제거 — 값 안에 # 을 쓰지 않는다
    for name, value in {"LEVELS": levels, "PLANES": planes}.items():
        src = re.sub(rf"(?<![\w\"']){name}(?![\w\"'])", repr(value), src)
    table = ast.literal_eval("{" + src + "}")
    return planes, levels, {p: list(v) for p, v in table.items()}
```
<!-- 인용 끝 -->
