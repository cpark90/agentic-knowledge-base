---
id: https://agentic-knowledge-base.dev/id/chunk/fd705af7-dd6d-489f-9d6f-620aecadba08
type: artifact
level: executable
title_ko: 함수 scan_gate_tags (tools/kb_lib.py)
title: function scan_gate_tags in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
---
**함수** — `scan_gate_tags(paths)` 다. 소스 파일에서 게이트 태그를 전수로 뽑는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def scan_gate_tags(paths) -> dict[str, list[str]]:
    """소스 파일에서 게이트 태그를 전수로 뽑는다 — 태그 id → 나온 자리들 (게이트 `gate-registry` 의 입력).

    `FAIL [<id>]` 꼴과 메시지 머리의 `[<id>]` 꼴 둘을 본다. 주석과 docstring 은 세지 않는다 — 설명문의
    예시가 태그로 세어지면 등록부 대조가 설명문을 따라가게 된다. 파이썬은 `ast` 로 문자열 노드만 보고
    Starlark(`.bzl`)는 파서가 없어 본문 전수를 본다.
    """
    import ast

    hits: dict[str, list[str]] = {}
    for path in paths:
        p = Path(path)
        text = p.read_text(encoding="utf-8")
        if p.suffix == ".py":
            tree = ast.parse(text)
            skip = set()
            for node in ast.walk(tree):
                if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    if ast.get_docstring(node, clean=False) is not None and isinstance(node.body[0], ast.Expr):
                        skip.add(id(node.body[0].value))
            for node in ast.walk(tree):
                if id(node) in skip:
                    continue
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    chunk = node.value
                elif isinstance(node, ast.JoinedStr):
                    chunk = "".join(v.value if isinstance(v, ast.Constant) else "\x00" for v in node.values)
                else:
                    continue
                found = [m.group(1) for m in GATE_TAG_RE.finditer(chunk)]
                head = GATE_TAG_HEAD_RE.match(chunk)
                if head:
                    found.append(head.group(1))
                for gid in found:
                    hits.setdefault(gid, []).append(f"{p.as_posix()}:{node.lineno}")
        else:
            for m in GATE_TAG_RE.finditer(text):
                hits.setdefault(m.group(1), []).append(f"{p.as_posix()}:{text[:m.start()].count(chr(10)) + 1}")
    return hits
```
<!-- 인용 끝 -->
