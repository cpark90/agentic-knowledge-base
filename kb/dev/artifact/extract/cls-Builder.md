---
id: https://agentic-knowledge-base.dev/id/chunk/33680335-f485-4267-aa96-2bb505425eaa
type: artifact
level: executable
title_ko: 클래스 Builder (tools/extract.py)
title: class Builder in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:59:21Z}
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**클래스** — `class Builder` 다. 소스 하나의 청크 트리를 만든다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Builder:
    """소스 하나의 청크 트리를 만든다 — 한정 이름 → uuid 는 Ids 가 준다."""

    def __init__(self, src_rel: str, lines: list[str], head_end: int, top: list[Region], ids):
        self.src, self.lines, self.head_end, self.top, self.ids = src_rel, lines, head_end, top, ids
        self.chunks: list[Chunk] = []

    def span(self, spans: list[tuple[int, int]]) -> list[str]:
        out: list[str] = []
        for a, b in spans:
            out += self.lines[a - 1:b]
        return trim(out)

    def build(self) -> tuple[str, list[str]]:
        """파일 복합체 IRI 와 그 직접 부분 IRI 들(소스 순서)을 돌려준다."""
        file_iri = self.ids.get("file", COMPOSITE_IRI)
        n_defs = sum(1 for _ in self._all_defs(self.top))
        body = [f"**파일** — `{self.src}` 다. {len(self.lines)}줄 · 최상위 정의 {n_defs}개 · 최상위 절 {len(self.top)}개이고 "
                f"이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.", "",
                "**모듈 머리** — 모듈 docstring 과 import 다.", ""] + quote(self.lines[:self.head_end])
        mod = Chunk("module.md", "module", self.ids.get("module", CHUNK_IRI),
                    f"파일 {self.src}", f"file {self.src}", body)
        self.chunks.append(mod)
        parts = [self.region(r, file_iri) for r in self.top]
        # 파일 복합체도 직접 부분 상한·하한을 받는다 (4.5절) — 절 복합체와 같은 규칙이고 거부의 자리는 추출기다.
        # 이 검사가 없으면 `gen_build._check_bundle` 이 뒤에서 잡아 FAIL 이 소스가 아니라 생성 BUILD 를 가리킨다.
        if len(parts) > MAX_PARTS:
            raise ExtractError(f"{self.src}: 파일 복합체의 직접 부분이 {len(parts)}개다 — 최대 {MAX_PARTS}개(7±2, 4.5절)."
                               f" 장 주석(`# ══ 장`)으로 절을 묶는다 — 순서에 뜻이 없는 묶음을 만들지 않으므로 "
                               f"{MAX_PARTS}개씩 자르지 않는다 (p7-code-links-on-file-composite)")
        if len(parts) < 2:
            raise ExtractError(f"{self.src}: 파일 복합체의 직접 부분이 {len(parts)}개다 — 복합체는 부분 둘 이상의 묶음이고 "
                               f"모듈 머리뿐인 파일은 복합체가 서지 않는다 (4.5절). 절 주석(`# ── 절`) 하나를 "
                               f"모듈 머리 뒤에 넣는다")
        mod.composite = {"id": file_iri, "title_ko": f"파일 복합체 {self.src}", "title": f"file composite {self.src}",
                         "ordered": parts}
        return file_iri, parts

    def _all_defs(self, regions: list[Region]):
        for r in regions:
            for _, n in r.defs:
                yield n
            yield from self._all_defs(r.children)

    def region(self, r: Region, parent: str) -> str:
        """구역 하나 → 절 청크(+ 복합체). 부분이 없으면 절 청크 자체가 상위의 부분이다."""
        qn = region_qname(r)
        comp_iri = self.ids.get("composite:" + qn, COMPOSITE_IRI)
        kind = "모듈 머리" if r.is_head else ("장" if r.depth == 1 else "절")
        sec = Chunk(f"{qn.replace(':', '-')}.md", qn, self.ids.get(qn, CHUNK_IRI),
                    f"{kind} {r.key} ({self.src})", f"{'module head' if r.is_head else ('chapter' if r.depth == 1 else 'section')} "
                    f"{r.key} in {self.src}", [])
        self.chunks.append(sec)
        members = [sec.iri]
        for tag, _, obj in r.items():
            members.append(self.define(obj, comp_iri) if tag == "def" else self.region(obj, comp_iri))
        own = self.span(_own_lines(r))
        head = [f"**{kind}** — `{self.src}` 의 {kind} `{r.key}` 다. {r.title}", ""]
        names = [n.name for _, n in r.defs]
        head += [("**정의** — " + " · ".join(f"`{x}`" for x in names) + " (소스 순서).") if names
                 else "**정의** — 없음. 선언과 상수만 있는 구역이다.", ""]
        if r.children:
            head += ["**하위 구역** — " + " · ".join(f"`{c.key}`" for c in r.children) + " (소스 순서).", ""]
        sec.body = head + (quote(own) if own else ["**선언** — 없음."])
        if len(members) == 1:  # 부분 하나면 복합체가 아니다 (4.5절) — 절 청크가 곧 상위의 부분이다
            sec.part_of = parent
            return sec.iri
        if len(members) > MAX_PARTS:
            raise ExtractError(f"{self.src}:{r.start}: {kind} `{r.key}` 의 직접 부분이 {len(members)}개다 — 최대 {MAX_PARTS}개(7±2, 4.5절)."
                               f" 절 주석(`# ══ 장` · `# ── 절`)으로 나눈다 — 순서에 뜻이 없는 묶음을 만들지 않으므로 "
                               f"{MAX_PARTS}개씩 자르지 않는다 (p7-code-links-on-file-composite)")
        sec.part_of = comp_iri
        sec.composite = {"id": comp_iri, "title_ko": f"{kind} 복합체 {r.key} ({self.src})",
                         "title": f"{'chapter' if r.depth == 1 else 'section'} composite {r.key} in {self.src}",
                         "ordered": members, "part_of": parent}
        return comp_iri

    def define(self, node, parent: str) -> str:
        qn = qualified(def_kind(node), node.name)
        kind = "클래스" if isinstance(node, ast.ClassDef) else "함수"
        src = source_of(self.lines, node)
        summary = first_sentence(node)
        body = [f"**{kind}** — `{signature(node)}` 다." + (f" {summary}" if summary else ""), ""] + quote(src)
        c = Chunk(f"{qn.replace(':', '-')}.md", qn, self.ids.get(qn, CHUNK_IRI),
                  f"{kind} {node.name} ({self.src})",
                  f"{'class' if isinstance(node, ast.ClassDef) else 'function'} {node.name} in {self.src}", body)
        c.part_of = parent
        self.chunks.append(c)
        return c.iri
```
<!-- 인용 끝 -->
