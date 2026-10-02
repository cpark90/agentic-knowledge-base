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
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/21d36097-2599-4a14-8057-733c634ae0b6, https://agentic-knowledge-base.dev/id/chunk/2d2767c3-e91e-464b-8f72-7fabdd6cca14, https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9, https://agentic-knowledge-base.dev/id/chunk/5fef9048-0948-4bfe-ad98-9a6587163b44, https://agentic-knowledge-base.dev/id/chunk/829ed4f8-dab5-4026-a1d3-0bd17bb6c708, https://agentic-knowledge-base.dev/id/chunk/8f365d81-2dc9-4f87-8f66-153ed897e871, https://agentic-knowledge-base.dev/id/chunk/a489355a-ef09-4411-ac19-0d5203bc0d58, https://agentic-knowledge-base.dev/id/chunk/a8451195-7601-4dd9-aab3-f74defed5506]
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
