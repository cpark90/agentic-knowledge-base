---
id: https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1
type: artifact
level: executable
title_ko: 클래스 Model (tools/weave.py)
title: class Model in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574
---
**클래스** — `class Model` 다. head 그래프의 청크·복합체를 뷰가 쓰는 형태로 — plane·level·status·라벨·위치·시각, 복합체 ↔ 부분.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Model:
    """head 그래프의 청크·복합체를 뷰가 쓰는 형태로 — plane·level·status·라벨·위치·시각, 복합체 ↔ 부분."""

    def __init__(self, g: Graph):
        self.g = g
        self.chunks = {s for s in g.subjects(AGT.lineCount, None)}
        self.plane = {c: self._plane(c) for c in self.chunks}
        self.level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in self.chunks}
        self.status = {c: str(next(g.objects(c, AGT.status), "")) for c in self.chunks}
        self.location = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in self.chunks}
        self.comp_of: dict = {}
        self.parts: dict = defaultdict(list)
        for comp, part in g.subject_objects(AGT.hasDirectPart):
            self.comp_of[part] = comp
            self.parts[comp].append(part)

    def _plane(self, c) -> str:
        for t in self.g.objects(c, RDF.type):
            name = str(t).split("/")[-1]
            if name.endswith("Chunk"):
                return name[: -len("Chunk")].lower()
        return ""

    def ko(self, node) -> str:
        return kb_lib.label_of(self.g, node, "ko")

    def en(self, node) -> str:
        return kb_lib.label_of(self.g, node, "en")

    def at(self, c) -> str:
        return str(next(self.g.objects(c, PROV.generatedAtTime), ""))

    def live(self, c) -> bool:
        return c in self.chunks and self.status[c] != "deprecated"

    def decision_roles(self, comp) -> dict:
        """복합체의 부분을 결론·근거·대안 역할로 — 파일명이 역할이다 (STYLEGUIDE §4). 결정 복합체가 아니면 빈 dict."""
        roles = {}
        for p in self.parts.get(comp, ()):
            if self.plane.get(p) != "decision":
                return {}
            loc = self.location.get(p, "")
            for role, fname in kb_lib.DECISION_PART_FILES.items():
                if loc.endswith("/" + fname):
                    roles[role] = p
        return roles if "conclusion" in roles else {}

    def decision_composites(self) -> list:
        """(복합체, 역할→부분) — 결론 위치 순. 살아 있는 것과 deprecated 를 다 낸다. 호출자가 거른다."""
        out = []
        for comp in self.g.subjects(RDF.type, AGT.Composite):
            roles = self.decision_roles(comp)
            if roles:
                out.append((comp, roles))
        return sorted(out, key=lambda cr: self.location[cr[1]["conclusion"]])

    def decision_unit(self, c):
        """청크가 속한 결정 단위 — 복합체면 복합체, 아니면 청크 자신 (단일 파일 결정)."""
        return self.comp_of.get(c, c)

    def unit_label(self, unit) -> str:
        """결정 단위의 라벨 — 복합체면 결론 라벨, 청크면 자기 라벨."""
        roles = self.decision_roles(unit) if unit not in self.chunks else {}
        return self.ko(roles["conclusion"]) if roles else self.ko(unit)

    def unit_ref(self, unit) -> str:
        """결정 단위의 자리 — 디렉토리(복합체) 또는 파일 stem."""
        roles = self.decision_roles(unit) if unit not in self.chunks else {}
        loc = self.location[roles["conclusion"]] if roles else self.location.get(unit, "")
        return Path(loc).parent.name if roles else Path(loc).stem
```
<!-- 인용 끝 -->
