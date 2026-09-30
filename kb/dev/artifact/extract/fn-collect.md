---
id: https://agentic-knowledge-base.dev/id/chunk/0f9149bc-d39d-4624-bdc2-d97603407e8c
type: artifact
level: executable
title_ko: 함수 collect (tools/extract.py)
title: function collect in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `collect(top, lines)` 다. 소스가 요구하는 한정 이름 전부와 정의의 정규화 해시 — 개명 판정의 입력이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def collect(top: list[Region], lines: list[str]) -> tuple[list[str], dict[str, str]]:
    """소스가 요구하는 한정 이름 전부와 정의의 정규화 해시 — 개명 판정의 입력이다."""
    names, hashes = ["file", "module"], {}
    def walk(regions):
        for r in regions:
            qn = region_qname(r)
            names.append(qn)
            names.append("composite:" + qn)
            own = []
            for a, b in _own_lines(r):
                own += lines[a - 1:b]
            hashes[qn] = normalized_hash(trim(own), r.key)  # 절 키는 그 절의 첫 이름이라 이름이 바뀌면 키가 움직인다
            for _, n in r.defs:
                q = qualified(def_kind(n), n.name)
                names.append(q)
                hashes[q] = normalized_hash(source_of(lines, n), n.name)
            walk(r.children)
    walk(top)
    return names, hashes
```
<!-- 인용 끝 -->
