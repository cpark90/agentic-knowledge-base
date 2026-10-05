---
id: https://agentic-knowledge-base.dev/id/chunk/33680335-f485-4267-aa96-2bb505425eaa
type: artifact
level: executable
title_ko: 클래스 Builder (tools/extract.py)
title: class Builder in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/100129c2-a2cd-484c-b610-46e6ba849016, https://agentic-knowledge-base.dev/id/chunk/21d36097-2599-4a14-8057-733c634ae0b6, https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b, https://agentic-knowledge-base.dev/id/chunk/2d2767c3-e91e-464b-8f72-7fabdd6cca14, https://agentic-knowledge-base.dev/id/chunk/3133a231-692d-411f-9a52-fa6f82f6676f, https://agentic-knowledge-base.dev/id/chunk/4994778f-bd6e-485d-b2f6-ec514f2187d9, https://agentic-knowledge-base.dev/id/chunk/5fef9048-0948-4bfe-ad98-9a6587163b44, https://agentic-knowledge-base.dev/id/chunk/829ed4f8-dab5-4026-a1d3-0bd17bb6c708, https://agentic-knowledge-base.dev/id/chunk/890c6310-9982-474d-831e-9d0a0fc2a114, https://agentic-knowledge-base.dev/id/chunk/8961c276-af1a-4b25-82aa-8ea7a53a20d0, https://agentic-knowledge-base.dev/id/chunk/8b283654-cf54-4445-a8f4-95c8bef0f888, https://agentic-knowledge-base.dev/id/chunk/a489355a-ef09-4411-ac19-0d5203bc0d58, https://agentic-knowledge-base.dev/id/chunk/a8451195-7601-4dd9-aab3-f74defed5506, https://agentic-knowledge-base.dev/id/chunk/aada6cbe-8da7-42be-b193-af12f3127b37, https://agentic-knowledge-base.dev/id/chunk/bb2addb3-a5df-4db6-9623-a80b215b03d7, https://agentic-knowledge-base.dev/id/chunk/cea6fcfc-b3e0-4dab-b8f5-e0727ee9c70d]
part_of: https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0
---
**클래스** — `class Builder` 다. 소스 하나의 청크 트리를 만든다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class Builder:
    """소스 하나의 청크 트리를 만든다 — 한정 이름 → uuid 는 Ids 가 준다."""

    def __init__(self, src_rel: str, lines: list[str], head_end: int, top: list[Region], ids,
                 uses_sources: frozenset = frozenset(), imports: list = (), uses_ids: dict = {}, wiring: tuple = ()):
        self.src, self.lines, self.head_end, self.top, self.ids = src_rel, lines, head_end, top, ids
        self.lang = source_lang(src_rel)  # 인용 펜스의 언어 — 개명 판정(previous_hashes)이 같은 값으로 읽는다
        self.wiring = tuple(wiring)       # 배선으로 뺀 최상위 이름 — 파일 청크 본문이 적는다
        self.uses_sources = uses_sources  # 방출 경계(`tools/<이름>.py` 집합) — 원본은 defs/kb.bzl.EXTRACTED_SOURCES
        self.chunks: list[Chunk] = []
        # 같은 모듈의 최상위 정의 이름 → 한정 이름. 모듈 안 해소의 치역이 이 사상의 값이다
        self.top_defs = {n.name: qualified(def_kind(n), n.name) for n in self._all_defs(top)}
        # 치역 경계(defs/kb.bzl.USES_TARGETS) 안의 모듈 → 그 등록부의 {한정 이름: IRI}. 모듈 밖 해소는 이 사상이
        # 치역이고 등록부가 원본이다 — 여기 없는 이름(상수·모듈 변수)은 가리킬 청크가 없어 빠진다
        self.uses_ids = {m: ids_ for m, ids_ in uses_ids.items() if m != Path(src_rel).stem}
        self.uses_mods, self.uses_names = import_bindings(list(imports), set(self.uses_ids))

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
                f"이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.", ""]
        if self.wiring:  # 배선은 항목이 아니다(유저 답 Q10-a) — 뺀 사실과 이름은 여기 남는다
            body += [f"**배선** — 입력 집합과 인자를 잇기만 하는 최상위 이름 {len(self.wiring)}개를 청크로 내지 않았다 "
                     f"(등록부 `{WIRING_KEY}`): " + " · ".join(f"`{w}`" for w in self.wiring) + ".", ""]
        body += ["**모듈 머리** — 모듈 docstring 과 " + ("`load`" if self.lang == "starlark" else "import") + " 다.", ""] \
            + quote(self.lines[:self.head_end], self.lang)
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
        sec.body = head + (quote(own, self.lang) if own else ["**선언** — 없음."])
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

    def foreign_uses(self, node) -> set:
        """치역 경계 안의 **다른 모듈**의 정의 IRI — 이름 → 청크는 대상 모듈의 등록부가 준다.

        신설하지 않는다: 대상 모듈의 uuid 는 그 모듈의 추출이 정하는 것이고 여기는 읽는 자리다. 등록부에 없는
        이름(상수·모듈 변수·없는 속성)은 가리킬 정의 청크가 없으므로 빠진다.
        """
        out = set()
        for mod, name in used_foreign_defs(node, self.uses_mods, self.uses_names, set(self.uses_ids)):
            ids = self.uses_ids.get(mod, {})
            iri = ids.get(qualified("fn", name)) or ids.get(qualified("cls", name))
            if iri:
                out.add(iri)
        return out

    def define(self, node, parent: str) -> str:
        qn = qualified(def_kind(node), node.name)
        kind = "클래스" if isinstance(node, ast.ClassDef) else "함수"
        src = source_of(self.lines, node)
        summary = first_sentence(node)
        body = [f"**{kind}** — `{signature(node)}` 다." + (f" {summary}" if summary else ""), ""] + quote(src, self.lang)
        c = Chunk(f"{qn.replace(':', '-')}.md", qn, self.ids.get(qn, CHUNK_IRI),
                  f"{kind} {node.name} ({self.src})",
                  f"{'class' if isinstance(node, ast.ClassDef) else 'function'} {node.name} in {self.src}", body)
        c.part_of = parent
        # 호출 관계는 정의 청크가 갖는다 — 정렬은 IRI 순이다. 정체성이 uuid 이므로(p10-function-identity-registry)
        # 개명이 순서를 움직이지 않는다. 이름 순으로 정렬하면 개명 하나가 형제 전부의 frontmatter 를 흔든다.
        # 방출은 경계(`self.uses_sources` — 원본 defs/kb.bzl.EXTRACTED_SOURCES) 안에서만 하고, 치역은 같은 모듈과
        # 경계(`defs/kb.bzl.USES_TARGETS`) 안의 모듈이다 — 키는 하나이고 잎도 하나다(2026-10-01, 유저 답 1)
        if self.src in self.uses_sources:
            own = {self.ids.get(self.top_defs[n], CHUNK_IRI) for n in used_defs(node, set(self.top_defs))}
            c.uses = sorted(own | self.foreign_uses(node))
        self.chunks.append(c)
        return c.iri
```
<!-- 인용 끝 -->
