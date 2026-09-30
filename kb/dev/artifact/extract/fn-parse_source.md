---
id: https://agentic-knowledge-base.dev/id/chunk/1f4895e9-23ea-421e-8218-237de7a42713
type: artifact
level: executable
title_ko: 함수 parse_source (tools/extract.py)
title: function parse_source in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `parse_source(path)` 다. 소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_source(path: Path) -> tuple[list[str], int, list[Region]]:
    """소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들). 구역은 절 주석의 깊이로 중첩된다."""
    lines = path.read_text(encoding="utf-8").splitlines()
    tree = ast.parse("\n".join(lines))
    head_end = module_head_end(tree)
    head = Region(max(kb_lib.EXTRACT_MARKERS.values()), "모듈 머리", head_end + 1)
    head.is_head = True  # 가장 깊은 깊이를 줘서 어느 절 주석이든 이 구역을 닫는다 — 모듈 머리는 절을 담지 않는다
    top: list[Region] = [head]
    stack: list[Region] = [head]
    for i, line in enumerate(lines[head_end:], start=head_end + 1):
        m = kb_lib.EXTRACT_MARKER_RE.match(line)
        if not m:
            continue
        depth = kb_lib.EXTRACT_MARKERS[m.group(1)]
        while stack and stack[-1].depth >= depth:
            stack.pop().end = i - 1
        region = Region(depth, m.group(2).strip(), i)
        (stack[-1].children if stack else top).append(region)
        stack.append(region)
    while stack:
        stack.pop().end = len(lines)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            _place(top, node)
    _key_regions(top, lines)
    return lines, head_end, top
```
<!-- 인용 끝 -->
