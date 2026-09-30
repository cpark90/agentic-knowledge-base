---
id: https://agentic-knowledge-base.dev/id/chunk/37924901-a32a-4452-97a3-3e3201ef5117
type: artifact
level: executable
title_ko: 함수 _key_regions (tools/extract.py)
title: function _key_regions in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `_key_regions(regions, lines)` 다. 구역의 키 — 그 구역에서 처음 나오는 최상위 이름.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _key_regions(regions: list[Region], lines: list[str]) -> None:
    """구역의 키 — 그 구역에서 처음 나오는 최상위 이름. 순번이 아니라 이름이므로 절을 끼워 넣어도 움직이지 않는다.

    장은 제 몫 줄이 절 주석뿐이라 이름이 없다 — 그때는 그 장 안에서 처음 나오는 이름을 쓴다. 장과 그 첫 절의 키가
    같아지지만 한정 이름의 접두(`ch:`·`sec:`)가 갈라서 정체성이 겹치지 않는다.
    """
    for r in regions:
        _key_regions(r.children, lines)
        cands = [(n.lineno, n.name) for _, n in r.defs]
        for a, b in _own_lines(r):
            for i in range(a, min(b, len(lines)) + 1):
                m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*(?::[^=]+)?=[^=]", lines[i - 1])
                if m:
                    cands.append((i, m.group(1)))
                    break
        cands += [(c.start, c.key) for c in r.children]
        cands = [c for c in sorted(cands) if c[1]]
        r.key = (cands[0][1] if cands else f"r{r.start}").replace("_", "-").lower()
```
<!-- 인용 끝 -->
