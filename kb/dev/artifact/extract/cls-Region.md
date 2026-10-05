---
id: https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9
type: artifact
level: executable
title_ko: 클래스 Region (tools/extract.py)
title: class Region in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**클래스** — `class Region` 다. 절 주석 하나가 여는 구역 — 자기 정의와 하위 구역을 소스 순서로 갖는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Region:
    """절 주석 하나가 여는 구역 — 자기 정의와 하위 구역을 소스 순서로 갖는다."""

    def __init__(self, depth: int, title: str, start: int):
        self.depth, self.title, self.start = depth, title, start
        self.end = start
        self.defs: list = []       # (lineno, ast 노드)
        self.children: list = []   # 하위 Region
        self.key = ""
        self.is_head = False       # 모듈 머리 구역 — 절 주석이 없고 어느 절 주석이든 이 구역을 닫는다
        self.skipped: list = []    # 배선(등록부 `wiring`)의 줄 범위 — 청크로 내지 않고 제 몫 줄에서도 뺀다

    def items(self):
        """소스 순서의 부분 후보 — ("def", 노드) · ("region", Region)."""
        return sorted([("def", n.lineno, n) for _, n in self.defs] + [("region", r.start, r) for r in self.children],
                      key=lambda t: t[1])
```
<!-- 인용 끝 -->
