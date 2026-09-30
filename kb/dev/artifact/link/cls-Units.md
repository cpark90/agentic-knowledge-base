---
id: https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed
type: artifact
level: executable
title_ko: 클래스 Units (tools/link.py)
title: class Units in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/570df80b-916d-466e-a9fe-8a9ac66eea54
---
**클래스** — `class Units` 다. 살아 있는 청크를 단위로 — 결정 복합체(결론 부분이 있는 것)는 결론이 대표하고, 나머지 청크는 자기 자신이 단위다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Units:
    """살아 있는 청크를 단위로 — 결정 복합체(결론 부분이 있는 것)는 결론이 대표하고, 나머지 청크는 자기 자신이 단위다."""

    def __init__(self, g):
        self.g = g
        self.plane = kb_lib.chunk_planes(g)
        self.chunks = set(self.plane)
        self.status = {c: str(next(g.objects(c, AGT.status), "")) for c in self.chunks}
        self.level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in self.chunks}
        self.loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in self.chunks}
        self.live = {c for c in self.chunks if self.status[c] != "deprecated"}
        self.comp_of: dict = {}
        parts = defaultdict(list)
        for comp, part in g.subject_objects(AGT.hasDirectPart):
            self.comp_of[part] = comp
            parts[comp].append(part)
        self.unit_of: dict = {}
        concl_name = "/" + kb_lib.DECISION_PART_FILES["conclusion"]
        for comp, ps in parts.items():
            concl = sorted((p for p in ps if self.loc.get(p, "").endswith(concl_name)), key=str)
            if concl and all(self.plane.get(p) == "decision" for p in ps):  # 결정 복합체 — 앵커는 결론 (STYLEGUIDE §4, weave 와 같은 규칙)
                for p in ps:
                    if p in self.chunks:
                        self.unit_of[p] = concl[0]
        for c in self.chunks:
            self.unit_of.setdefault(c, c)
        self.members = defaultdict(set)
        for c, u in self.unit_of.items():
            self.members[u].add(c)

    def alive(self, u) -> bool:
        return u in self.live

    def kb(self, u) -> str:
        return kb_lib.kb_of(self.loc.get(u, ""))

    def ko(self, u) -> str:
        return kb_lib.label_of(self.g, u, "ko")

    def sibling(self, a, b) -> bool:
        ca = self.comp_of.get(a)
        return ca is not None and ca == self.comp_of.get(b)

    def stem(self, c) -> str:
        return Path(self.loc.get(c, str(c))).stem
```
<!-- 인용 끝 -->
