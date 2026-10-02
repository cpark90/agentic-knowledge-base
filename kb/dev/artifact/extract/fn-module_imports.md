---
id: https://agentic-knowledge-base.dev/id/chunk/1a73eeae-6541-4952-9318-7b2bac9e9ecc
type: artifact
level: executable
title_ko: 함수 module_imports (tools/extract.py)
title: function module_imports in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/30b84220-a222-44db-9ae1-0486db2a18ec
---
**함수** — `module_imports(tree)` 다. 모듈 최상위의 import 노드 — `try`·`if` 안까지 들어가고 정의 안은 보지 않는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def module_imports(tree) -> list:
    """모듈 최상위의 import 노드 — `try`·`if` 안까지 들어가고 정의 안은 보지 않는다.

    이 저장소의 관례가 `try: from tools import kb_lib / except ImportError: import kb_lib` 라서 최상위 `body` 만
    훑으면 경계 안의 모듈을 묶는 import 가 거의 다 빠진다. 정의 안의 늦은 import 는 여기 오지 않는다 — 그 자리는
    정의마다 다르므로 `used_foreign_defs` 가 자기 정의 안에서 다시 읽는다.
    """
    out: list = []

    def walk(body):
        for n in body:
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                out.append(n)
            elif isinstance(n, (ast.Try, ast.If)):
                for part in [n.body, n.orelse, getattr(n, "finalbody", [])] + [h.body for h in getattr(n, "handlers", [])]:
                    walk(part)

    walk(tree.body)
    return out
```
<!-- 인용 끝 -->
