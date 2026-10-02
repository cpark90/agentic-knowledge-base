---
id: https://agentic-knowledge-base.dev/id/chunk/3133a231-692d-411f-9a52-fa6f82f6676f
type: artifact
level: executable
title_ko: 함수 import_bindings (tools/extract.py)
title: function import_bindings in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/30b84220-a222-44db-9ae1-0486db2a18ec
---
**함수** — `import_bindings(imports, targets)` 다. 치역 경계 안의 모듈을 묶는 최상위 import → (모듈 별칭 → 대상 모듈, 직접 이름 → 대상 모듈).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def import_bindings(imports: list, targets: set) -> tuple:
    """치역 경계 안의 모듈을 묶는 최상위 import → (모듈 별칭 → 대상 모듈, 직접 이름 → 대상 모듈).

    형태는 넷이다. `import kb_lib` · `import kb_lib as k` · `from tools import kb_lib` 는 **모듈 별칭**을 묶고
    그 뒤의 `<별칭>.<이름>` 이 대상 모듈의 최상위 이름이다 — 별칭은 모듈에 붙은 것이므로 이름의 철자를 바꾸지
    않는다. `from kb_lib import X` 는 **직접 이름** X 를 묶는다. `from kb_lib import pct as p` 는 **제외**다:
    `p` 는 정의의 이름이 아니고, 이 잎의 해소 규칙은 모듈 안과 같이 **철자가 정의의 이름과 같은 것**뿐이다.
    """
    mods, names = {}, {}
    for n in imports:
        if isinstance(n, ast.Import):
            for a in n.names:
                leaf = a.name.rsplit(".", 1)[-1]
                if leaf in targets and (a.asname or "." not in a.name):  # import tools.kb_lib 은 `tools` 를 묶는다
                    mods[a.asname or leaf] = leaf
        elif (n.module or "").rsplit(".", 1)[-1] in targets:  # from kb_lib import X — 직접 이름
            names.update({a.name: (n.module or "").rsplit(".", 1)[-1] for a in n.names if not a.asname})
        else:  # from tools import kb_lib — 모듈 별칭
            mods.update({a.asname or a.name: a.name for a in n.names if a.name in targets})
    return mods, names
```
<!-- 인용 끝 -->
