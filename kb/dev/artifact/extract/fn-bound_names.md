---
id: https://agentic-knowledge-base.dev/id/chunk/d767b795-a891-45b2-93cd-f2fb728b749a
type: artifact
level: executable
title_ko: 함수 bound_names (tools/extract.py)
title: function bound_names in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `bound_names(node)` 다. 정의 안에서 이름을 새로 묶는 자리 전부 — 인자·대입 대상·중첩 정의·comprehension 변수·import 별칭·except 이름.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def bound_names(node) -> set:
    """정의 안에서 이름을 새로 묶는 자리 전부 — 인자·대입 대상·중첩 정의·comprehension 변수·import 별칭·except 이름.

    여기 묶인 이름은 철자가 모듈 최상위 정의와 같아도 그 정의를 가리키지 않는다(섀도잉). 이것이 `uses` 의 제외
    목록 가운데 지역 변수·인자·모듈 안 import 를 거르는 자리다.
    """
    out = set()
    for n in ast.walk(node):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = n.args
            out |= {x.arg for x in a.posonlyargs + a.args + a.kwonlyargs}
            out |= {x.arg for x in (a.vararg, a.kwarg) if x}
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n is not node:
            out.add(n.name)
        elif isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            out.add(n.id)
        elif isinstance(n, ast.alias):
            out.add((n.asname or n.name).split(".")[0])
        elif isinstance(n, ast.ExceptHandler) and n.name:
            out.add(n.name)
    return out
```
<!-- 인용 끝 -->
