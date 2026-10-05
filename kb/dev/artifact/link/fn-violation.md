---
id: https://agentic-knowledge-base.dev/id/chunk/e3fd5c02-635a-402a-ad7b-f2cbc4d10b46
type: artifact
level: executable
title_ko: 함수 violation (tools/link.py)
title: function violation in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed, https://agentic-knowledge-base.dev/id/chunk/f3fcb094-a1c5-414e-ab93-287b0bec0449]
part_of: https://agentic-knowledge-base.dev/id/composite/570df80b-916d-466e-a9fe-8a9ac66eea54
---
**함수** — `violation(u, kind, a, b)` 다. defs/kb.bzl _check_links 의 구조 규칙 — 위반이면 사유, 아니면 None.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def violation(u: Units, kind: str, a, b) -> str | None:
    """defs/kb.bzl _check_links 의 구조 규칙 — 위반이면 사유, 아니면 None."""
    la = LEVELS.index(u.level[a]) if u.level[a] in LEVELS else -1
    lb = LEVELS.index(u.level[b]) if u.level[b] in LEVELS else -1
    if kb_lib.cross_kb_link(kind, (u.kb(a), u.plane[a], u.level[a]), (u.kb(b), u.plane[b], u.level[b])):
        return R_CROSS_LINK  # 판정은 게이트 cross-kb-link 와 같은 함수다 (kb_lib.cross_kb_link — 예외는 목표 → 요구 derivesFrom)
    if kind == "derivesFrom" and u.case(a):
        return R_CASE_DERIVES  # 케이스의 derivesFrom 은 생성기가 자기 시나리오로 쓴다 (tools/case_gen.py)
    if kind in ("refines", "serves"):
        if lb >= la:
            return "refines/serves 대상은 더 높은 수준이어야 한다 (6.2절)"
        if PLANES.index(u.plane[b]) > PLANES.index(u.plane[a]):
            return "plane 단방향 위반 (5.2절)"
        if kind == "serves" and u.plane[b] != "requirement":
            return "serves 의 대상은 requirement 뿐이다 (6.8절)"
    elif kind == "verifies":
        if u.kb(a) != kb_lib.KB_VV:
            return "verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)"
        if u.kb(b) == kb_lib.KB_VV:
            return "verifies 의 대상은 개발 KB 청크다"
        if u.level[a] != u.level[b]:
            return "verifies 는 같은 수준끼리다 (8.3절)"
    return None
```
<!-- 인용 끝 -->
