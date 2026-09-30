---
id: https://agentic-knowledge-base.dev/id/chunk/890c6310-9982-474d-831e-9d0a0fc2a114
type: artifact
level: executable
title_ko: 함수 used_defs (tools/extract.py)
title: function used_defs in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `used_defs(node, top_names)` 다. 정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 이름들 — `uses` 의 해소 규칙이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def used_defs(node, top_names: set) -> list:
    """정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 이름들 — `uses` 의 해소 규칙이다 (agt:usesDefinition).

    해소는 AST 의 이름 참조뿐이다. `ast.Name` 의 `id` 와 `ast.Attribute` 의 뿌리 이름(그 사슬의 `ast.Name`)을 보고
    모듈 최상위의 함수·클래스 이름과 철자가 같은 것만 남긴다. 제외는 다섯이다 — 자기 자신, 섀도잉된 이름(지역 변수·
    인자·중첩 정의·import 별칭, `bound_names`), 최상위 정의가 아닌 이름(상수·모듈·import), `ast.Attribute` 의
    뒤쪽 이름(`attr` — 인스턴스·모듈의 속성이라 모듈 최상위 정의가 아니다), 그리고 다른 모듈의 이름
    (`kb_lib.pct` 의 뿌리는 import 이름 `kb_lib` 이므로 거기서 걸린다).
    """
    bound = bound_names(node)
    seen = {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    return sorted((seen & top_names) - bound - {getattr(node, "name", "")})
```
<!-- 인용 끝 -->
