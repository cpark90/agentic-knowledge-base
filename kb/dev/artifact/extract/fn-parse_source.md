---
id: https://agentic-knowledge-base.dev/id/chunk/1f4895e9-23ea-421e-8218-237de7a42713
type: artifact
level: executable
title_ko: 함수 parse_source (tools/extract.py)
title: function parse_source in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/09909df0-d231-4cd6-ae92-f2867a75a9f9, https://agentic-knowledge-base.dev/id/chunk/1a73eeae-6541-4952-9318-7b2bac9e9ecc, https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b, https://agentic-knowledge-base.dev/id/chunk/37924901-a32a-4452-97a3-3e3201ef5117, https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9, https://agentic-knowledge-base.dev/id/chunk/6e1136b2-9f7d-4699-b88e-a3ccf6cc8d38, https://agentic-knowledge-base.dev/id/chunk/8382b3eb-033b-4299-a06a-a544995b0ea1, https://agentic-knowledge-base.dev/id/chunk/ed759600-6622-448e-be33-8fab9ae6b4eb]
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `parse_source(path, wiring)` 다. 소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들, 최상위 import 노드들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_source(path: Path, wiring: tuple = ()) -> tuple[list[str], int, list[Region], list]:
    """소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들, 최상위 import 노드들). 구역은 절 주석의 깊이로 중첩된다.

    import 를 함께 돌려주는 까닭은 `uses` 의 치역 경계 해소가 "이 이름이 어느 모듈의 정의인가" 를 최상위
    import 에서 풀어서다 — 소스를 두 번 파싱하지 않는다 (`module_imports`).
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    tree = ast.parse("\n".join(lines))
    head_end = module_head_end(tree, path.suffix == STARLARK_SUFFIX)
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
    wired = {top_name(n): n for n in tree.body if top_name(n) in wiring}
    stray = sorted(set(wiring) - set(wired))
    if stray:
        raise ExtractError(f"{path}: 등록부 `{WIRING_KEY}` 의 이름이 소스의 최상위에 없다 — {' · '.join(stray)}. "
                           f"배선 목록은 소스의 최상위 정의·대입 이름이다 — 지운 정의는 목록에서도 지운다")
    for node in tree.body:
        if top_name(node) in wired:
            _place(top, node, skip=True)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            _place(top, node)
    top = _prune(top, lines)
    _key_regions(top, lines)
    return lines, head_end, top, module_imports(tree)
```
<!-- 인용 끝 -->
