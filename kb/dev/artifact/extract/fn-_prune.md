---
id: https://agentic-knowledge-base.dev/id/chunk/6e1136b2-9f7d-4699-b88e-a3ccf6cc8d38
type: artifact
level: executable
title_ko: 함수 _prune (tools/extract.py)
title: function _prune in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9, https://agentic-knowledge-base.dev/id/chunk/829ed4f8-dab5-4026-a1d3-0bd17bb6c708]
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `_prune(regions, lines, parent)` 다. 배선만 남는 구역을 지운다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _prune(regions: list[Region], lines: list[str], parent: Region | None = None) -> list[Region]:
    """배선만 남는 구역을 지운다 — 정의도 하위 구역도 없고 제 몫 줄이 주석·빈 줄뿐이면 절 청크를 세우지 않는다.

    그 주석은 배선을 설명하는 글이라 배선과 함께 빠진다. 지운 구역의 줄 범위는 상위 구역의 배선 범위로 옮긴다 — 옮기지
    않으면 상위 구역(장)의 제 몫 줄로 돌아가 배선 코드가 장 청크에 인용된다. 모듈 머리는 지우지 않는다(파일 복합체의
    첫 부분이다).
    """
    out = []
    for r in regions:
        r.children = _prune(r.children, lines, r)
        own = [lines[i - 1] for a, b in _own_lines(r) for i in range(a, min(b, len(lines)) + 1)]
        if r.is_head or r.defs or r.children or any(l.strip() and not l.lstrip().startswith("#") for l in own):
            out.append(r)
        elif parent is not None:
            parent.skipped.append((r.start, r.end))
    return out
```
<!-- 인용 끝 -->
