---
id: https://agentic-knowledge-base.dev/id/chunk/bb2addb3-a5df-4db6-9623-a80b215b03d7
type: artifact
level: executable
title_ko: 함수 used_foreign_defs (tools/extract.py)
title: function used_foreign_defs in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/3133a231-692d-411f-9a52-fa6f82f6676f, https://agentic-knowledge-base.dev/id/chunk/d767b795-a891-45b2-93cd-f2fb728b749a]
part_of: https://agentic-knowledge-base.dev/id/composite/30b84220-a222-44db-9ae1-0486db2a18ec
---
**함수** — `used_foreign_defs(node, mods, names, targets)` 다. 정의가 **치역 경계 안의 다른 모듈**의 최상위 정의를 이름으로 쓰는 것 — (대상 모듈, 이름) 쌍이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def used_foreign_defs(node, mods: dict, names: dict, targets: set) -> list:
    """정의가 **치역 경계 안의 다른 모듈**의 최상위 정의를 이름으로 쓰는 것 — (대상 모듈, 이름) 쌍이다.

    해소는 둘뿐이다. (a) `ast.Attribute` 의 뿌리가 모듈 별칭이면 그 `attr` 이 대상 모듈의 최상위 이름이다
    (`kb_lib.pct` · `k.pct`). 사슬이 길면(`kb_lib.AGT.usesDefinition`) 안쪽 `ast.Attribute` 가 최상위 이름을
    주므로 뒤쪽 이름은 저절로 빠진다. (b) `from <대상> import X` 로 들어온 이름의 `Load` 참조. 섀도잉 규칙은
    모듈 안과 같다 — `bound_names` 에 묶인 철자는 그 모듈의 정의를 가리키지 않는다. 예외는 정의 안의 **늦은
    import** 다(`try: from tools import kb_lib` 를 함수 안에 두어 무거운 의존을 호출 시점으로 미루는 관례,
    `extract_refs.load_concepts`): 묶는 것이 대상 모듈 자신이므로 섀도잉이 아니고 최상위 import 와 같이 센다.
    이름 → 청크의 사상은 대상 모듈의 등록부가 주고 정의가 아닌 이름(상수·모듈 변수)은 거기 없어 빠진다.
    """
    inner = import_bindings([n for n in ast.walk(node) if isinstance(n, (ast.Import, ast.ImportFrom))], targets)
    mods, names = {**mods, **inner[0]}, {**names, **inner[1]}
    bound = bound_names(node) - set(inner[0]) - set(inner[1])
    out = set()
    for n in ast.walk(node):
        root = n.value if isinstance(n, ast.Attribute) else None
        if isinstance(root, ast.Name) and isinstance(root.ctx, ast.Load) and root.id in mods and root.id not in bound:
            out.add((mods[root.id], n.attr))
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in names and n.id not in bound:
            out.add((names[n.id], n.id))
    return sorted(out)
```
<!-- 인용 끝 -->
