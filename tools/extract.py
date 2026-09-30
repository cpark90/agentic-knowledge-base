#!/usr/bin/env python3
"""코드 → 청크 추출기 — 소스 파일 하나에서 `artifact` plane 의 청크 트리를 생성한다 (p7-code-extraction-direction).

코드가 원본이고 청크는 생성물이다. 청크 파일을 손으로 고치면 드리프트 게이트(`//:extract_drift_test`)가 거부한다.
tangle(청크 → 코드)은 없다. 정체성의 원본은 소스 옆의 **등록부**(`<소스>.chunks.yml`)이고 한정 이름 → uuid 를 담는다 —
이름이 바뀌어도 uuid 가 유지되므로 개명이 청크의 삭제 + 신설로 보이지 않는다 (p10-split-keeps-work-identity).

구조는 세 층이다 (p7-code-links-on-file-composite). 파일 복합체의 선언 청크가 **파일 청크**(`module.md` — 모듈
docstring 과 import)이고 링크(`refines`·`serves`)와 검증기의 `verifies` 도착점이 거기다. 그 부분은 소스의 절
주석(`# ══ 장` · `# ── 절`)이 여는 **절 복합체**이고, 절 복합체의 부분은 절 청크와 그 절의 정의 청크다.
직접 부분은 9개를 넘을 수 없으므로(4.5절) 넘는 절은 잘라 맞추지 않고 절 주석을 요구한다 — 순서에 뜻이 없는 묶음을
만들지 않는다.

청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 청크에
다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다.

사용: bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check]
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
출력·종료: 생성 시점 거부는 `FAIL [extract] <경로>: …`, `--check` 의 어긋남은 `FAIL [extract-drift] <경로>: …` —
둘 다 EXIT_FAIL. 읽을 수 없는 입력은 EXIT_CONFIG.
"""

from __future__ import annotations

import argparse
import ast
import difflib
import hashlib
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
except ImportError:
    import kb_lib

TAG = kb_lib.EXTRACT_GATE
DRIFT_TAG = kb_lib.EXTRACT_DRIFT_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
CHUNK_IRI = "https://agentic-knowledge-base.dev/id/chunk/"
COMPOSITE_IRI = "https://agentic-knowledge-base.dev/id/composite/"
DEFAULT_ASSUMES = "https://agentic-knowledge-base.dev/id/asm-chunk-conventions"
MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — defs/kb.bzl · gen_build 와 같은 수
_NAME_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


class ExtractError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""


# ── 등록부 (사이드카) ─────────────────────────────────────────────────────────────────────
# 손으로 쓰는 것은 `refines`·`serves` 와 uuid 이고, `at`·`source_hash` 와 신설 uuid 는 추출기가 더한다.
# `serves` 의 정의역은 `agt:DecisionChunk` 다(fulfilment-ontology) — `artifact` 청크가 요구를 직접 `serves` 하면
# 추론이 그것을 결정 청크로 만들고 shape DecisionSubstanceShape 이 거부한다. 코드가 요구에 닿는 길은 결정을
# `refines` 하는 것이고 그 결정이 요구를 `serves`·`refines` 한다 — 사다리를 건너뛰지 않는다 (6.2절).
# YAML 부분집합만 쓴다 — 이 저장소의 frontmatter 파서와 같은 수준이고 외부 의존이 없다.
REGISTRY_HEAD = """\
# 등록부 — 손이 원본이다. 한정 이름 → uuid 가 코드 청크의 정체성이고 이름은 그 위의 라벨이다
# (p10-split-keeps-work-identity · p7-code-extraction-direction). 생성기는 신설 uuid 와 `at`·`source_hash` 만 더한다.
# 개명은 아래 `ids` 의 키를 손으로 고치는 것이고, 삭제는 키를 손으로 지우는 것이다 — 둘 다 사람의 편집이다.
# 생성물은 `{package}/` 이며 손으로 고치면 `//:extract_drift_test` 가 거부한다.
"""


def load_registry(path: Path) -> dict:
    """등록부 → {source, resource, package, at, source_hash, refines[], serves[], ids{}}. 없으면 빈 등록부다."""
    reg = {"source": "", "resource": "", "package": "", "at": "", "source_hash": "",
           "refines": [], "serves": [], kb_lib.STAMP_KEY: {}, "ids": {}}
    if not path.exists():
        return reg
    section = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip() if raw.lstrip().startswith("#") else raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  "):
            body = line.strip()
            if section in ("refines", "serves"):
                reg[section].append(body.lstrip("- ").strip())
            elif section in ("ids", kb_lib.STAMP_KEY):  # 한정 이름에 `:` 가 있으므로 마지막 `: ` 에서 가른다 — IRI 에는 `: ` 가 없다
                k, sep, v = body.rpartition(": ")
                if sep:
                    reg[section][k.strip()] = v.strip()
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        section = key if key in ("refines", "serves", "ids", kb_lib.STAMP_KEY) else ""
        if key in reg and not section:
            reg[key] = val
    return reg


def dump_registry(reg: dict) -> str:
    out = [REGISTRY_HEAD.format(package=reg["package"])]
    for k in ("source", "resource", "package", "at", "source_hash"):
        out.append(f"{k}: {reg[k]}")
    for k in ("refines", "serves"):
        out.append(f"{k}:" + ("" if reg[k] else " []"))
        out += [f"  - {v}" for v in reg[k]]
    tested = reg.get(kb_lib.STAMP_KEY) or {}
    out.append(f"{kb_lib.STAMP_KEY}:" + ("" if tested else " {}"))
    out += [f"  {k}: {tested[k]}" for k in ("rev", "at", "source_hash") if tested.get(k)]
    out.append("ids:")
    out += [f"  {k}: {reg['ids'][k]}" for k in sorted(reg["ids"])]
    return "\n".join(out) + "\n"


# ── 소스 읽기 — 모듈 머리와 절 구역 ────────────────────────────────────────────────────────
class Region:
    """절 주석 하나가 여는 구역 — 자기 정의와 하위 구역을 소스 순서로 갖는다."""

    def __init__(self, depth: int, title: str, start: int):
        self.depth, self.title, self.start = depth, title, start
        self.end = start
        self.defs: list = []       # (lineno, ast 노드)
        self.children: list = []   # 하위 Region
        self.key = ""
        self.is_head = False       # 모듈 머리 구역 — 절 주석이 없고 어느 절 주석이든 이 구역을 닫는다

    def items(self):
        """소스 순서의 부분 후보 — ("def", 노드) · ("region", Region)."""
        return sorted([("def", n.lineno, n) for _, n in self.defs] + [("region", r.start, r) for r in self.children],
                      key=lambda t: t[1])


def module_head_end(tree: ast.Module) -> int:
    """모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지. 그 뒤가 첫 구역이다."""
    end = 0
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) and end == 0:
            pass
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            pass
        elif isinstance(node, ast.Try) and all(isinstance(n, (ast.Import, ast.ImportFrom)) for n in node.body):
            pass
        else:
            break
        end = node.end_lineno
    return end


def parse_source(path: Path) -> tuple[list[str], int, list[Region]]:
    """소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들). 구역은 절 주석의 깊이로 중첩된다."""
    lines = path.read_text(encoding="utf-8").splitlines()
    tree = ast.parse("\n".join(lines))
    head_end = module_head_end(tree)
    head = Region(max(kb_lib.EXTRACT_MARKERS.values()), "모듈 머리", head_end + 1)
    head.is_head = True  # 가장 깊은 깊이를 줘서 어느 절 주석이든 이 구역을 닫는다 — 모듈 머리는 절을 담지 않는다
    top: list[Region] = [head]
    stack: list[Region] = [head]
    for i, line in enumerate(lines[head_end:], start=head_end + 1):
        m = kb_lib.EXTRACT_MARKER_RE.match(line)
        if not m:
            continue
        depth = kb_lib.EXTRACT_MARKERS[m.group(1)]
        while stack and stack[-1].depth >= depth:
            stack.pop().end = i - 1
        region = Region(depth, m.group(2).strip(), i)
        (stack[-1].children if stack else top).append(region)
        stack.append(region)
    while stack:
        stack.pop().end = len(lines)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            _place(top, node)
    _key_regions(top, lines)
    return lines, head_end, top


def _place(regions: list[Region], node) -> None:
    """정의를 그것을 담는 가장 깊은 구역에 넣는다."""
    for r in regions:
        if r.start <= node.lineno <= r.end:
            if any(c.start <= node.lineno <= c.end for c in r.children):
                _place(r.children, node)
            else:
                r.defs.append((node.lineno, node))
            return


def _own_lines(r: Region) -> list[tuple[int, int]]:
    """구역의 제 몫 줄 범위 — 하위 구역과 정의의 본문을 뺀 나머지 (절 주석과 그 절의 상수)."""
    taken = [(c.start, c.end) for c in r.children] + [(n.lineno if not n.decorator_list else n.decorator_list[0].lineno, n.end_lineno)
                                                      for _, n in r.defs]
    spans, cur = [], r.start
    for a, b in sorted(taken):
        if a > cur:
            spans.append((cur, a - 1))
        cur = max(cur, b + 1)
    if cur <= r.end:
        spans.append((cur, r.end))
    return spans


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


# ── 정의의 이름·해시·시그니처 ────────────────────

def qualified(kind: str, key: str) -> str:
    return f"{kind}:{key}"


def def_kind(node) -> str:
    return "cls" if isinstance(node, ast.ClassDef) else "fn"


def source_of(lines: list[str], node) -> list[str]:
    start = min([d.lineno for d in node.decorator_list] + [node.lineno])
    return lines[start - 1:node.end_lineno]


def normalized_hash(text_lines: list[str], name: str) -> str:
    """이름을 지운 본문의 해시 — 개명 판정의 기준이다. 이름만 바뀐 정의는 같은 해시를 갖는다."""
    body = "\n".join(l.rstrip() for l in text_lines if l.strip())
    body = re.sub(r"\b" + re.escape(name) + r"\b", "@", body)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


def signature(node) -> str:
    if isinstance(node, ast.ClassDef):
        return f"class {node.name}"
    a = node.args
    names = [x.arg for x in a.posonlyargs + a.args] + ([f"*{a.vararg.arg}"] if a.vararg else [])
    names += [x.arg for x in a.kwonlyargs] + ([f"**{a.kwarg.arg}"] if a.kwarg else [])
    return f"{node.name}({', '.join(names)})"


def first_sentence(node) -> str:
    doc = (ast.get_docstring(node) or "").strip()
    if not doc:
        return ""
    head = doc.split("\n\n")[0].replace("\n", " ").strip()
    m = re.search(r"^(.{1,160}?[다\.])(?:\s|$)", head)
    return (m.group(1) if m else head[:160]).strip()


# ── 청크 만들기 — 파일 청크 · 절 청크 · 정의 청크 ─────────────────────────────────────────────
class Chunk:
    """생성할 청크 하나 — 파일 이름·frontmatter·본문."""

    def __init__(self, fname: str, qname: str, iri: str, title_ko: str, title: str, body: list[str]):
        self.fname, self.qname, self.iri = fname, qname, iri
        self.title_ko, self.title, self.body = title_ko, title, body
        self.part_of = ""
        self.composite: dict = {}
        self.links: dict = {}


def region_qname(r: Region) -> str:
    """구역의 한정 이름 — 깊이가 종류를 정한다. 장과 그 첫 절이 같은 이름을 키로 가져도 갈린다."""
    return "head" if r.is_head else (f"ch:{r.key}" if r.depth == 1 else f"sec:{r.key}")


def quote(lines: list[str]) -> list[str]:
    """인용 구역 — 소스를 그대로 옮긴 코드 펜스. 생성기는 원문을 고쳐 쓰지 않는다."""
    return [kb_lib.SOURCE_QUOTE_OPEN, "```python", *[l.rstrip() for l in lines], "```", kb_lib.SOURCE_QUOTE_CLOSE]


def trim(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


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


# ── frontmatter 직렬화 ────────────────────────────────────────────────────────────────────
def stamped(reg: dict) -> str:
    """도장이 지금 소스를 가리키는가 — `tested.source_hash` 가 등록부의 `source_hash` 와 같을 때만 참이다.

    소스가 도장 뒤에 바뀌면 거짓이 되고 `verified` 가 빠진다 (p7-code-extraction-direction "도장"). 사람이 등록부에서
    도장을 지우는 행위도 같은 결과를 낸다 — 도장은 저작물이고 청크는 뷰다.
    """
    t = reg.get(kb_lib.STAMP_KEY) or {}
    return t.get("at", "") if t.get("source_hash") and t["source_hash"] == reg["source_hash"] else ""


def previous_bodies(pkg_dir: Path) -> dict:
    """트리의 생성 청크 → {파일 이름: (본문, generated.at)}. `generated.at` 의 보존 규칙이 이 값을 쓴다.

    청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다. 소스 파일의 시각(등록부 `at`)을 모든 청크에
    다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지가 보이지 않는다 — 생성물의 diff 는 변경의 크기를
    말해야 한다. 값의 원본은 트리이므로 `--check` 의 재생성은 그대로 결정론이다.
    """
    out = {}
    if not pkg_dir.is_dir():
        return out
    for f in sorted(pkg_dir.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            continue
        m = re.search(r"^generated: \{by: [^,]+, at: ([^}]+)\}$", parts[1], re.M)
        out[f.name] = (parts[2], m.group(1).strip() if m else "")
    return out


def render(c: Chunk, reg: dict, at: str = "") -> str:
    fm = [f"id: {c.iri}", "type: artifact", "level: executable", f"title_ko: {c.title_ko}", f"title: {c.title}",
          "status: stable", f"sources: [{{resource: {reg['resource']}}}]", f"assumes: [{DEFAULT_ASSUMES}]",
          f"generated: {{by: {kb_lib.EXTRACT_ACTOR}, at: {at or reg['at']}}}"]
    if stamped(reg):  # 테스트 통과 도장 — 소스가 도장 뒤에 바뀌면 빠진다 (수정 뒤 미검증, 재판정 자동)
        fm.append(f"verified: [{{by: {kb_lib.STAMP_ACTOR}, at: {reg[kb_lib.STAMP_KEY]['at']}}}]")
    for key in ("refines", "serves"):
        if c.links.get(key):
            fm.append(f"{key}: [" + ", ".join(c.links[key]) + "]")
    if c.part_of:
        fm.append(f"part_of: {c.part_of}")
    if c.composite:
        inner = [f"id: {c.composite['id']}", f"title_ko: {c.composite['title_ko']}", f"title: {c.composite['title']}",
                 "ordered: [" + ", ".join(c.composite["ordered"]) + "]"]
        if c.composite.get("part_of"):
            inner.append(f"part_of: {c.composite['part_of']}")
        fm.append("composite: {" + ", ".join(inner) + "}")
    return "---\n" + "\n".join(fm) + "\n---\n" + "\n".join(c.body) + "\n"


# ── 등록부 해소 — 개명·신설·삭제 (p10-split-keeps-work-identity 를 코드에 실현한다) ──────────────
class Ids:
    """한정 이름 → uuid. 등록부가 원본이고 신설만 자동이다."""

    def __init__(self, ids: dict):
        self.ids = dict(ids)
        self.added: list[str] = []

    def get(self, qname: str, prefix: str) -> str:
        if qname not in self.ids:
            self.ids[qname] = prefix + str(uuid.uuid4())
            self.added.append(qname)
        return self.ids[qname]


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


def previous_hashes(pkg_dir: Path) -> dict[str, str]:
    """트리에 있는 생성 청크 → {정규화 해시: 한정 이름}. 개명은 이름을 뺀 본문이 같은 것으로 판정한다."""
    out = {}
    for f in sorted(pkg_dir.glob("*.md")):
        stem = f.stem
        if not stem.startswith(("fn-", "cls-", "sec-", "ch-")):
            continue
        qname = stem.replace("-", ":", 1)
        text = f.read_text(encoding="utf-8")
        code = re.findall(r"^```python\n(.*?)^```$", text, re.M | re.S)
        if code:
            out[normalized_hash(trim(code[0].splitlines()), qname.split(":", 1)[1])] = qname
    return out


def registry_path(reg: dict) -> str:
    """등록부 사이드카의 경로 — 소스 옆이다."""
    return Path(reg["source"]).with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX).as_posix()


def resolve(reg: dict, names: list[str], hashes: dict[str, str], pkg_dir: Path, check: bool) -> Ids:
    """등록부 갱신 규칙 (a)~(d). 개명·삭제는 사람의 편집이므로 안내만 하고 등록부를 고치지 않는다."""
    want, have = set(names), set(reg["ids"])
    gone = sorted(have - want)          # 등록부에 있는데 소스에 없는 이름
    fresh = sorted(n for n in names if n not in have)
    prev = previous_hashes(pkg_dir)
    renames = []
    for q in fresh:
        was = prev.get(hashes.get(q, ""))
        if was and was in gone:
            renames.append((was, q))
            if "composite:" + was in gone and "composite:" + q in fresh:  # 절 복합체의 키는 절 청크의 키를 따른다
                renames.append(("composite:" + was, "composite:" + q))
    if renames:
        raise ExtractError(f"{reg['source']}: 개명이다 — 본문이 같고 이름만 바뀐 정의가 {len(renames)}건이다. 등록부 "
                           f"{registry_path(reg)} 의 `ids` 에서 "
                           + " · ".join(f"`{a}` → `{b}`" for a, b in renames)
                           + " 로 키를 고친다 (uuid 는 그대로 — 정체성은 uuid 이고 이름은 그 위의 라벨이다, "
                             "p10-split-keeps-work-identity). 정체성의 변경은 사람의 편집이므로 생성기가 하지 않는다")
    left = [g for g in gone if g not in {a for a, _ in renames}]
    if left:
        raise ExtractError(f"{reg['source']}: 등록부에 있는데 소스에 없는 이름이 {len(left)}건이다 — "
                           + " · ".join(f"`{g}`" for g in left)
                           + f". 삭제는 등록부 {registry_path(reg)} 의 `ids` 에서 그 키를 지우는 "
                             "명시 행위다 — 생성기가 정체성을 버리지 않는다")
    if check and fresh:
        raise ExtractError(f"{reg['source']}: 등록부에 없는 새 이름이 {len(fresh)}건이다 — "
                           + " · ".join(f"`{n}`" for n in fresh[:8]) + (" …" if len(fresh) > 8 else "")
                           + ". `bazel run //tools:extract -- " + reg["source"] + "` 를 돌려 등록한다 (신설은 자동이다)")
    return Ids(reg["ids"])


def source_stamp(root: Path, src_rel: str) -> str:
    """소스 파일의 시각 — git 커밋 시각이 있으면 그것, 없으면 지금 UTC. 소스가 바뀔 때만 갱신된다."""
    import subprocess
    try:
        out = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cI", "--", src_rel],
                             capture_output=True, text=True, timeout=20)
        if out.returncode == 0 and out.stdout.strip():
            return datetime.fromisoformat(out.stdout.strip()).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return kb_lib.now_utc()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="추출할 파이썬 소스 (저장소 상대 경로)")
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    src_rel = Path(a.source).as_posix()
    src = root / src_rel
    reg_path = src.with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX)
    try:
        lines, head_end, top = parse_source(src)
        reg = load_registry(reg_path)
    except (OSError, SyntaxError) as e:
        print(f"FAIL [{TAG}] {src}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not reg["resource"]:
        print(f"FAIL [{TAG}] {reg_path}: 등록부에 `resource`(소스 파일 개체 IRI)가 없다 — 출처는 kg/base-kg.ttl 의 "
              f"`id:src-…` 개체이고 손으로 세운다", file=sys.stderr)
        return EXIT_CONFIG
    reg["source"], reg["package"] = src_rel, reg["package"] or f"{kb_lib.EXTRACT_ROOT}/{src.stem}"
    pkg_dir = root / reg["package"]
    digest = hashlib.sha256(src.read_bytes()).hexdigest()[:16]
    if reg["source_hash"] != digest or not reg["at"]:
        if a.check:
            print(f"FAIL [{DRIFT_TAG}] {reg_path}: 등록부의 `source_hash` 가 소스와 어긋난다 — "
                  f"`bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 (소스가 원본, 청크는 뷰)", file=sys.stderr)
            return EXIT_FAIL
        reg["at"], reg["source_hash"] = source_stamp(root, src_rel), digest
    names, hashes = collect(top, lines)
    try:
        ids = resolve(reg, names, hashes, pkg_dir, a.check)
        b = Builder(src_rel, lines, head_end, top, ids)
        b.build()
    except ExtractError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL
    # 링크는 파일 복합체의 것이다 — 파일 청크와 구역 청크(절·장·모듈 머리)가 그 자리다. 정의 청크는 `part_of` 로만
    # 존재해 함수 churn 이 링크를 움직이지 않는다. 모듈 머리 구역에 정의가 없으면 그 청크는 복합체를 선언하지 않고
    # 파일 복합체의 직접 부분이 되는데, 형제가 절 복합체(청크 아님)뿐이라 링크가 없으면 저작된 지식의 연결 성분에서
    # 홀로 남는다 — 실측 2026-09-30(파일 10개 = 성분 +10). 구역 청크는 정의 청크가 아니므로 링크를 받는다.
    for c in b.chunks:
        if c.qname in ("module", "head") or c.composite:
            c.links = {"refines": reg["refines"], "serves": reg["serves"]}
    reg["ids"] = ids.ids
    prev = previous_bodies(pkg_dir)  # 본문이 그대로면 `generated.at` 을 유지한다 — diff 가 변경의 크기를 말해야 한다
    outputs = {}
    for c in b.chunks:
        body = "\n".join(c.body) + "\n"
        was = prev.get(c.fname)
        outputs[pkg_dir / c.fname] = render(c, reg, was[1] if was and was[0] == body and was[1] else "")
    outputs[reg_path] = dump_registry(reg)
    stale = sorted(f for f in pkg_dir.glob("*.md") if f not in outputs) if pkg_dir.exists() else []
    drift = [f for f, text in outputs.items() if not f.exists() or f.read_text(encoding="utf-8") != text] + stale
    if a.check:
        for f in drift:
            if f in stale:
                print(f"FAIL [{DRIFT_TAG}] {f}: 추출이 만들지 않는 파일이다 — 생성 트리에 손으로 둔 파일은 없다")
                continue
            old = f.read_text(encoding="utf-8").splitlines(True) if f.exists() else []
            sys.stdout.writelines(difflib.unified_diff(old, outputs[f].splitlines(True), f"{f} (커밋본)", f"{f} (생성)", n=1))
            print(f"FAIL [{DRIFT_TAG}] {f}: 소스와 어긋난다 — `bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 "
                  f"(소스가 원본, 청크는 뷰)")
        if drift:
            print(f"\nFAIL [{DRIFT_TAG}] — {len(drift)}건 / 생성 청크 {len(b.chunks)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT_TAG}] — {src_rel} 의 생성 청크 {len(b.chunks)}개와 등록부가 소스와 일치")
        return 0
    pkg_dir.mkdir(parents=True, exist_ok=True)
    for f in stale:
        f.unlink()
    for f, text in outputs.items():
        f.write_text(text, encoding="utf-8")
    comps = sum(1 for c in b.chunks if c.composite)
    print(f"생성 {len(b.chunks)}개 (복합체 {comps}개, 신설 uuid {len(ids.added)}개), 변경 {len(drift)}개: {pkg_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
