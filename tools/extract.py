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

정의 청크는 선택 키 `uses: [<청크 IRI>…]` 를 갖는다 — 최상위 정의를 이름으로 쓰는 관계이고 `chunk2kg` 가
`agt:usesDefinition`(references 족의 잎)으로 방출한다. 해소는 AST 의 이름 참조뿐이며 제외는 `used_defs` 와
`used_foreign_defs` 에 적혀 있다. 링크 키가 아니므로 Bazel `deps` 도 링크 개체도 되지 않는다 — 링크는 파일 복합체의
것이다. 경계는 둘이고 둘 다 `--residency`(기본 `<루트>/defs/kb.bzl`) 의 리터럴이 단일 정의처다(M1). **방출 경계**
`EXTRACTED_SOURCES` 안의 소스에서만 내고(2026-10-01 — 표본 하나에서 먼저 내고 링크 밀도·게이트 시간을 잰 뒤 37 파일
전부로 넓혔다, 유저 답 1), **치역 경계** `USES_TARGETS` 안의 모듈만 모듈 밖 대상으로 삼는다(2026-10-01, 유저 답 1 —
표본 쌍 `kb_lib` 하나부터). 치역 경계 밖의 모듈을 가리키는 호출은 내지 않는다 — 넓히는 일은 그 리터럴에 이름을
더하는 것이다.

청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 청크에
다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다.

질의 디렉토리(`EXTRACTED_QUERY_DIRS`, 2026-10-03)는 다른 모양이다. 소스가 디렉토리 `tools/<이름>` 이고 그 안의
`*.rq` 질의 파일 하나가 청크 하나다 — 질의는 함수로 나뉘지 않으므로 파일 전체가 인용 하나이고 복합체를 세우지 않는다.
링크(`refines`·`serves`)는 청크마다 붙는다 — 질의 파일이 곧 링크의 자리다. 등록부는 `tools/<이름>.chunks.yml` 이고
키는 `query:<파일 이름 stem>` 이다. 등록부의 `refines`·`serves` 는 디렉토리의 질의 전부에 붙고, 질의 하나에만 붙는 `refines` 는
선택 키 `query_refines`(`query:<stem>: [<IRI>…]`)에 적는다 — 질의 파일 하나가 파일 복합체 하나의 자리이기 때문이다.
갱신 규칙 (a)~(d) 와 도장은 파이썬 소스와 같고 `source_hash` 는 디렉토리 안 질의 파일 전부의 (이름, 바이트) 해시다
(`source_digest`).

Starlark 소스(`EXTRACTED_STARLARK`, 유저 답 Q32-a, 2026-10-04)는 파이썬 소스와 같은 모양이다 — `.bzl` 은 파이썬 문법의
부분집합이므로 같은 AST 로 읽고, 최상위 정의 = 정의 청크 · 절 주석 = 절 복합체 · 최상위 리터럴 = 절 청크의 선언이다.
다른 것은 셋이다. 모듈 머리의 `load(...)` 가 import 자리이고, 인용 펜스의 언어가 `starlark` 이며, 생성 패키지는
`kb/dev/artifact/<이름>-bzl` 이다. 등록부의 선택 키 `wiring:` 은 **배선**(입력 집합과 인자를 잇기만 하는 최상위 정의·대입,
유저 답 Q10-a "빌드 배선은 항목이 아니다")의 이름 목록이고 추출기는 그 정의를 청크로 내지 않는다 — 소스에 없는 이름이
목록에 있으면 FAIL 이고, 배선만 남는 절은 절 청크를 세우지 않는다. 파일 청크 본문이 뺀 이름을 적는다.

사용: bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check] [--residency <defs/kb.bzl>]
      bazel run //tools:extract -- tools/cq-queries   (질의 디렉토리 — EXTRACTED_QUERY_DIRS 안이어야 한다)
      bazel run //tools:extract -- defs/kb.bzl        (Starlark 소스 — EXTRACTED_STARLARK 안이어야 한다)
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      --residency 는 EXTRACTED_SOURCES 리터럴의 원본 — 없으면 <루트>/defs/kb.bzl.
출력·종료: 생성 시점 거부는 `FAIL [extract] <경로>: …`, `--check` 의 어긋남은 `FAIL [extract-drift] <경로>: …` —
둘 다 EXIT_FAIL. 읽을 수 없는 입력(EXTRACTED_SOURCES 포함)은 EXIT_CONFIG.
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
# 손으로 쓰는 것은 `layer`·`refines`·`serves` 와 uuid 이고, `at`·`source_hash` 와 신설 uuid 는 추출기가 더한다.
# `layer` 는 소스 하나의 서비스 층이고 생성 청크 전부의 frontmatter 로 옮겨진다 — 도구는 프로세스 층의 실행
# 표면이므로 값은 `process` 다 (결정 p0-service-is-a-three-layer-wiki).
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


# 배선 목록 — 등록부의 선택 키. 입력 집합과 인자를 잇기만 하는 최상위 정의·대입의 이름이고 추출기는 그것을 청크로 내지
# 않는다(유저 답 Q10-a "빌드 배선은 항목이 아니다" · Q32-a "규칙을 강제하는 코드는 항목이다"). 손이 원본이다 — 어느 정의가
# 배선인지는 저작자의 판단이고, 추출기는 이름이 소스의 최상위에 실재하는지만 본다.
WIRING_KEY = "wiring"
# 질의별 정제 — 질의 디렉토리 등록부의 선택 키. `query:<stem>: [<IRI>…]` 가 그 질의 청크 하나에만 `refines` 를 더한다
# (디렉토리 전체의 `refines` 다음에, 중복 없이). 질의 파일 하나가 링크의 자리이므로(p7-code-links-on-file-composite) 디렉토리
# 공통 링크와 질의 하나의 링크를 가른다. 파이썬·Starlark 등록부에 적으면 거부한다 — 그쪽의 링크 자리는 파일 청크 하나다.
QUERY_REFINES_KEY = "query_refines"
STARLARK_SUFFIX = ".bzl"
STARLARK_PKG_SUFFIX = "-bzl"  # 생성 패키지 kb/dev/artifact/<이름>-bzl — 같은 stem 의 tools/<이름>.py 와 갈린다


def load_registry(path: Path) -> dict:
    """등록부 → {source, resource, package, layer, at, source_hash, refines[], serves[], ids{}}. 없으면 빈 등록부다."""
    reg = {"source": "", "resource": "", "package": "", kb_lib.LAYER_KEY: "", "at": "", "source_hash": "",
           "refines": [], "serves": [], WIRING_KEY: [], QUERY_REFINES_KEY: {}, kb_lib.STAMP_KEY: {}, "ids": {}}
    if not path.exists():
        return reg
    section = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip() if raw.lstrip().startswith("#") else raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  "):
            body = line.strip()
            if section in ("refines", "serves", WIRING_KEY):
                reg[section].append(body.lstrip("- ").strip())
            elif section in ("ids", kb_lib.STAMP_KEY):  # 한정 이름에 `:` 가 있으므로 마지막 `: ` 에서 가른다 — IRI 에는 `: ` 가 없다
                k, sep, v = body.rpartition(": ")
                if sep:
                    reg[section][k.strip()] = v.strip()
            elif section == QUERY_REFINES_KEY:  # `query:<stem>: [<IRI>, …]` — 값은 흐름 목록 하나다
                k, sep, v = body.rpartition(": ")
                if sep:
                    reg[section][k.strip()] = [x.strip() for x in v.strip().strip("[]").split(",") if x.strip()]
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        section = key if key in ("refines", "serves", WIRING_KEY, QUERY_REFINES_KEY, "ids", kb_lib.STAMP_KEY) else ""
        if key in reg and not section:
            reg[key] = val
    return reg


def dump_registry(reg: dict) -> str:
    out = [REGISTRY_HEAD.format(package=reg["package"])]
    for k in ("source", "resource", "package", kb_lib.LAYER_KEY, "at", "source_hash"):
        out.append(f"{k}: {reg[k]}")
    for k in ("refines", "serves"):
        out.append(f"{k}:" + ("" if reg[k] else " []"))
        out += [f"  - {v}" for v in reg[k]]
    if reg.get(WIRING_KEY):  # 선택 키 — 비면 쓰지 않는다(배선이 없는 등록부의 바이트를 바꾸지 않는다)
        out.append(f"{WIRING_KEY}:")
        out += [f"  - {v}" for v in reg[WIRING_KEY]]
    if reg.get(QUERY_REFINES_KEY):  # 선택 키 — 비면 쓰지 않는다
        out.append(f"{QUERY_REFINES_KEY}:")
        out += [f"  {k}: [{', '.join(v)}]" for k, v in sorted(reg[QUERY_REFINES_KEY].items())]
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
        self.skipped: list = []    # 배선(등록부 `wiring`)의 줄 범위 — 청크로 내지 않고 제 몫 줄에서도 뺀다

    def items(self):
        """소스 순서의 부분 후보 — ("def", 노드) · ("region", Region)."""
        return sorted([("def", n.lineno, n) for _, n in self.defs] + [("region", r.start, r) for r in self.children],
                      key=lambda t: t[1])


def module_head_end(tree: ast.Module, starlark: bool = False) -> int:
    """모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지. 그 뒤가 첫 구역이다.

    Starlark 는 `load(...)` 가 import 자리이고 docstring 이 `load` 뒤에 올 수 있다(`defs/kb.bzl`) — 머리 안의 첫 문자열
    식을 docstring 으로 받는다.
    """
    def is_load(node) -> bool:  # Starlark 의 `load(...)` 문 — 모듈 머리에서 import 의 자리다
        return (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "load")

    end, doc_seen = 0, False
    for node in tree.body:
        is_doc = isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
        if is_doc and (end == 0 or (starlark and not doc_seen)):
            doc_seen = True
        elif starlark and is_load(node):
            pass
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            pass
        elif isinstance(node, ast.Try) and all(isinstance(n, (ast.Import, ast.ImportFrom)) for n in node.body):
            pass
        else:
            break
        end = node.end_lineno
    return end


def parse_source(path: Path, wiring: tuple = ()) -> tuple[list[str], int, list[Region], list]:
    """소스 → (줄들, 모듈 머리의 끝 줄, 최상위 구역들, 최상위 import 노드들). 구역은 절 주석의 깊이로 중첩된다.

    import 를 함께 돌려주는 까닭은 `uses` 의 치역 경계 해소가 "이 이름이 어느 모듈의 정의인가" 를 최상위
    import 에서 풀어서다 — 소스를 두 번 파싱하지 않는다 (`module_imports`).
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    tree = ast.parse("\n".join(lines))
    head_end = module_head_end(tree, path.suffix == STARLARK_SUFFIX)
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
    wired = {top_name(n): n for n in tree.body if top_name(n) in wiring}
    stray = sorted(set(wiring) - set(wired))
    if stray:
        raise ExtractError(f"{path}: 등록부 `{WIRING_KEY}` 의 이름이 소스의 최상위에 없다 — {' · '.join(stray)}. "
                           f"배선 목록은 소스의 최상위 정의·대입 이름이다 — 지운 정의는 목록에서도 지운다")
    for node in tree.body:
        if top_name(node) in wired:
            _place(top, node, skip=True)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            _place(top, node)
    top = _prune(top, lines)
    _key_regions(top, lines)
    return lines, head_end, top, module_imports(tree)


def top_name(node) -> str:
    """최상위 문의 이름 — 정의면 그 이름, 이름 하나에 대입하면 그 이름, 그 밖은 빈 문자열이다 (배선 목록의 키)."""
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return ""


def _place(regions: list[Region], node, skip: bool = False) -> None:
    """정의를 그것을 담는 가장 깊은 구역에 넣는다. `skip` 이면 배선이다 — 줄 범위만 적어 제 몫 줄에서 뺀다."""
    for r in regions:
        if r.start <= node.lineno <= r.end:
            if any(c.start <= node.lineno <= c.end for c in r.children):
                _place(r.children, node, skip)
            elif skip:
                start = min([d.lineno for d in getattr(node, "decorator_list", [])] + [node.lineno])
                r.skipped.append((start, node.end_lineno))
            else:
                r.defs.append((node.lineno, node))
            return


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


def _own_lines(r: Region) -> list[tuple[int, int]]:
    """구역의 제 몫 줄 범위 — 하위 구역과 정의의 본문을 뺀 나머지 (절 주석과 그 절의 상수)."""
    taken = [(c.start, c.end) for c in r.children] + [(n.lineno if not n.decorator_list else n.decorator_list[0].lineno, n.end_lineno)
                                                      for _, n in r.defs] + list(r.skipped)
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


# ── 호출의 해소 — 모듈 안과 치역 경계 안 (`uses`) ────────────────────
def module_imports(tree) -> list:
    """모듈 최상위의 import 노드 — `try`·`if` 안까지 들어가고 정의 안은 보지 않는다.

    이 저장소의 관례가 `try: from tools import kb_lib / except ImportError: import kb_lib` 라서 최상위 `body` 만
    훑으면 경계 안의 모듈을 묶는 import 가 거의 다 빠진다. 정의 안의 늦은 import 는 여기 오지 않는다 — 그 자리는
    정의마다 다르므로 `used_foreign_defs` 가 자기 정의 안에서 다시 읽는다.
    """
    out: list = []

    def walk(body):
        for n in body:
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                out.append(n)
            elif isinstance(n, (ast.Try, ast.If)):
                for part in [n.body, n.orelse, getattr(n, "finalbody", [])] + [h.body for h in getattr(n, "handlers", [])]:
                    walk(part)

    walk(tree.body)
    return out


def import_bindings(imports: list, targets: set) -> tuple:
    """치역 경계 안의 모듈을 묶는 최상위 import → (모듈 별칭 → 대상 모듈, 직접 이름 → 대상 모듈).

    형태는 넷이다. `import kb_lib` · `import kb_lib as k` · `from tools import kb_lib` 는 **모듈 별칭**을 묶고
    그 뒤의 `<별칭>.<이름>` 이 대상 모듈의 최상위 이름이다 — 별칭은 모듈에 붙은 것이므로 이름의 철자를 바꾸지
    않는다. `from kb_lib import X` 는 **직접 이름** X 를 묶는다. `from kb_lib import pct as p` 는 **제외**다:
    `p` 는 정의의 이름이 아니고, 이 잎의 해소 규칙은 모듈 안과 같이 **철자가 정의의 이름과 같은 것**뿐이다.
    """
    mods, names = {}, {}
    for n in imports:
        if isinstance(n, ast.Import):
            for a in n.names:
                leaf = a.name.rsplit(".", 1)[-1]
                if leaf in targets and (a.asname or "." not in a.name):  # import tools.kb_lib 은 `tools` 를 묶는다
                    mods[a.asname or leaf] = leaf
        elif (n.module or "").rsplit(".", 1)[-1] in targets:  # from kb_lib import X — 직접 이름
            names.update({a.name: (n.module or "").rsplit(".", 1)[-1] for a in n.names if not a.asname})
        else:  # from tools import kb_lib — 모듈 별칭
            mods.update({a.asname or a.name: a.name for a in n.names if a.name in targets})
    return mods, names


def bound_names(node) -> set:
    """정의 안에서 이름을 새로 묶는 자리 전부 — 인자·대입 대상·중첩 정의·comprehension 변수·import 별칭·except 이름.

    여기 묶인 이름은 철자가 모듈 최상위 정의와 같아도 그 정의를 가리키지 않는다(섀도잉). 이것이 `uses` 의 제외
    목록 가운데 지역 변수·인자·모듈 안 import 를 거르는 자리다.
    """
    out = set()
    for n in ast.walk(node):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = n.args
            out |= {x.arg for x in a.posonlyargs + a.args + a.kwonlyargs}
            out |= {x.arg for x in (a.vararg, a.kwarg) if x}
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n is not node:
            out.add(n.name)
        elif isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            out.add(n.id)
        elif isinstance(n, ast.alias):
            out.add((n.asname or n.name).split(".")[0])
        elif isinstance(n, ast.ExceptHandler) and n.name:
            out.add(n.name)
    return out


def used_defs(node, top_names: set) -> list:
    """정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 이름들 — `uses` 의 모듈 안 해소 규칙이다 (agt:usesDefinition).

    해소는 AST 의 이름 참조뿐이다. `ast.Name` 의 `id` 와 `ast.Attribute` 의 뿌리 이름(그 사슬의 `ast.Name`)을 보고
    모듈 최상위의 함수·클래스 이름과 철자가 같은 것만 남긴다. 제외는 다섯이다 — 자기 자신, 섀도잉된 이름(지역 변수·
    인자·중첩 정의·import 별칭, `bound_names`), 최상위 정의가 아닌 이름(상수·모듈·import), `ast.Attribute` 의
    뒤쪽 이름(`attr` — 인스턴스·모듈의 속성이라 모듈 최상위 정의가 아니다), 그리고 다른 모듈의 이름
    (`kb_lib.pct` 의 뿌리는 import 이름 `kb_lib` 이므로 거기서 걸린다 — 치역 경계 안의 모듈이면
    `used_foreign_defs` 가 받는다).
    """
    bound = bound_names(node)
    seen = {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    return sorted((seen & top_names) - bound - {getattr(node, "name", "")})


def used_foreign_defs(node, mods: dict, names: dict, targets: set) -> list:
    """정의가 **치역 경계 안의 다른 모듈**의 최상위 정의를 이름으로 쓰는 것 — (대상 모듈, 이름) 쌍이다.

    해소는 둘뿐이다. (a) `ast.Attribute` 의 뿌리가 모듈 별칭이면 그 `attr` 이 대상 모듈의 최상위 이름이다
    (`kb_lib.pct` · `k.pct`). 사슬이 길면(`kb_lib.AGT.usesDefinition`) 안쪽 `ast.Attribute` 가 최상위 이름을
    주므로 뒤쪽 이름은 저절로 빠진다. (b) `from <대상> import X` 로 들어온 이름의 `Load` 참조. 섀도잉 규칙은
    모듈 안과 같다 — `bound_names` 에 묶인 철자는 그 모듈의 정의를 가리키지 않는다. 예외는 정의 안의 **늦은
    import** 다(`try: from tools import kb_lib` 를 함수 안에 두어 무거운 의존을 호출 시점으로 미루는 관례,
    `extract_refs.load_concepts`): 묶는 것이 대상 모듈 자신이므로 섀도잉이 아니고 최상위 import 와 같이 센다.
    이름 → 청크의 사상은 대상 모듈의 등록부가 주고 정의가 아닌 이름(상수·모듈 변수)은 거기 없어 빠진다.
    """
    inner = import_bindings([n for n in ast.walk(node) if isinstance(n, (ast.Import, ast.ImportFrom))], targets)
    mods, names = {**mods, **inner[0]}, {**names, **inner[1]}
    bound = bound_names(node) - set(inner[0]) - set(inner[1])
    out = set()
    for n in ast.walk(node):
        root = n.value if isinstance(n, ast.Attribute) else None
        if isinstance(root, ast.Name) and isinstance(root.ctx, ast.Load) and root.id in mods and root.id not in bound:
            out.add((mods[root.id], n.attr))
        elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in names and n.id not in bound:
            out.add((names[n.id], n.id))
    return sorted(out)


# ── 청크 만들기 — 파일 청크 · 절 청크 · 정의 청크 ─────────────────────────────────────────────
class Chunk:
    """생성할 청크 하나 — 파일 이름·frontmatter·본문."""

    def __init__(self, fname: str, qname: str, iri: str, title_ko: str, title: str, body: list[str]):
        self.fname, self.qname, self.iri = fname, qname, iri
        self.title_ko, self.title, self.body = title_ko, title, body
        self.part_of = ""
        self.composite: dict = {}
        self.links: dict = {}
        self.uses: list = []  # 같은 모듈의 최상위 정의 IRI (agt:usesDefinition) — 정의 청크만 갖는다


def region_qname(r: Region) -> str:
    """구역의 한정 이름 — 깊이가 종류를 정한다. 장과 그 첫 절이 같은 이름을 키로 가져도 갈린다."""
    return "head" if r.is_head else (f"ch:{r.key}" if r.depth == 1 else f"sec:{r.key}")


def source_lang(src_rel: str) -> str:
    """인용 펜스의 언어 — `.bzl` 이면 starlark, 그 밖의 소스 파일은 python 이다."""
    return "starlark" if src_rel.endswith(STARLARK_SUFFIX) else "python"


def quote(lines: list[str], lang: str = "python") -> list[str]:
    """인용 구역 — 소스를 그대로 옮긴 코드 펜스. 생성기는 원문을 고쳐 쓰지 않는다."""
    return [kb_lib.SOURCE_QUOTE_OPEN, f"```{lang}", *[l.rstrip() for l in lines], "```", kb_lib.SOURCE_QUOTE_CLOSE]


def trim(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


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
    if reg.get(kb_lib.LAYER_KEY):  # 서비스 층 — 등록부가 소스 하나의 층을 선언하고 그 선언이 생성 청크 전부(정의·절·파일)로
        fm.append(f"{kb_lib.LAYER_KEY}: {reg[kb_lib.LAYER_KEY]}")  # 옮겨진다. 도구는 프로세스 층의 실행 표면이다 (p0-service-is-a-three-layer-wiki)
    if stamped(reg):  # 테스트 통과 도장 — 소스가 도장 뒤에 바뀌면 빠진다 (수정 뒤 미검증, 재판정 자동)
        fm.append(f"verified: [{{by: {kb_lib.STAMP_ACTOR}, at: {reg[kb_lib.STAMP_KEY]['at']}}}]")
    for key in ("refines", "serves"):
        if c.links.get(key):
            fm.append(f"{key}: [" + ", ".join(c.links[key]) + "]")
    if c.uses:  # agt:usesDefinition — 링크 키가 아니다(references 족): deps 도 링크 개체도 아니고 직접 트리플만 남는다
        fm.append(f"{kb_lib.USES_KEY}: [" + ", ".join(c.uses) + "]")
    if c.part_of:
        fm.append(f"part_of: {c.part_of}")
    if c.composite:
        inner = [f"id: {c.composite['id']}", f"title_ko: {c.composite['title_ko']}", f"title: {c.composite['title']}",
                 "ordered: [" + ", ".join(c.composite["ordered"]) + "]"]
        if c.composite.get("part_of"):
            inner.append(f"part_of: {c.composite['part_of']}")
        fm.append("composite: {" + ", ".join(inner) + "}")
    return "---\n" + "\n".join(fm) + "\n---\n" + "\n".join(c.body) + "\n"


# ── 질의 디렉토리 — 질의 파일 하나 = 청크 하나 (EXTRACTED_QUERY_DIRS, 2026-10-03) ──────────────
# //kg:cq 뷰의 내용 원본(역량 질문 질의)과 //kg:gate_test 의 검증 질의가 코드 청크 밖에 있었다. 파이썬 소스와 같은 방향
# (p7-code-extraction-direction)으로 추출하되 질의는 정의로 나뉘지 않으므로 파일 하나가 청크 하나이고 복합체가 없다.
QUERY_LANG = "sparql"


def source_digest(path: Path) -> str:
    """소스의 내용 해시 — 파일이면 그 바이트, 질의 디렉토리면 질의 파일 전부의 (이름, 바이트)를 이름 순으로 이은 것이다.

    등록부의 `source_hash` 와 도장(`tools/stamp.py`)의 `tested.source_hash` 가 같은 함수를 쓴다 — 둘이 갈리면 도장이
    소스를 가리키는지 판정할 수 없다. 디렉토리의 해시에 이름을 넣는 까닭은 파일 개명만으로도 소스가 바뀐 것이어서다.
    """
    if not path.is_dir():
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    h = hashlib.sha256()
    for f in sorted(path.glob("*" + kb_lib.EXTRACT_QUERY_SUFFIX)):
        h.update(f.name.encode("utf-8") + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()[:16]


def collect_queries(src: Path) -> tuple[list[str], dict[str, str], dict[str, list[str]]]:
    """질의 디렉토리 → (한정 이름들, 정규화 해시, 이름 → 줄들). 한정 이름은 `query:<stem>` 이고 해시는 개명 판정의 입력이다."""
    names, hashes, texts = [], {}, {}
    for f in sorted(src.glob("*" + kb_lib.EXTRACT_QUERY_SUFFIX)):
        q = qualified("query", f.stem)
        texts[q] = f.read_text(encoding="utf-8").splitlines()
        names.append(q)
        hashes[q] = normalized_hash(texts[q], f.stem)
    if not names:
        raise ExtractError(f"{src}: 질의 파일(*{kb_lib.EXTRACT_QUERY_SUFFIX})이 없다 — 빈 질의 디렉토리는 추출 대상이 아니다. "
                           f"EXTRACTED_QUERY_DIRS(defs/kb.bzl)에서 이름을 지운다")
    return names, hashes, texts


def previous_query_hashes(pkg_dir: Path) -> dict[str, str]:
    """트리에 있는 질의 청크 → {정규화 해시: 한정 이름}. `previous_hashes` 의 질의판이다 — 펜스 언어만 다르다."""
    out = {}
    for f in sorted(pkg_dir.glob("*.md")) if pkg_dir.is_dir() else []:
        code = re.findall(r"^```" + QUERY_LANG + r"\n(.*?)^```$", f.read_text(encoding="utf-8"), re.M | re.S)
        if code:
            out[normalized_hash(code[0].splitlines(), f.stem)] = qualified("query", f.stem)
    return out


def build_queries(src_rel: str, texts: dict[str, list[str]], ids, reg: dict) -> list[Chunk]:
    """질의 청크들 — 파일 전체가 인용 하나이고 링크는 청크마다 붙는다. 질의 파일이 곧 링크의 자리다."""
    per_query = reg.get(QUERY_REFINES_KEY) or {}
    unknown = sorted(set(per_query) - set(texts))
    if unknown:
        raise ExtractError(f"{src_rel}: 등록부 `{QUERY_REFINES_KEY}` 의 키 {', '.join(unknown)} 가 디렉토리의 질의가 아니다 — "
                           f"키는 `query:<질의 파일 stem>` 이다")
    out = []
    for q, lines in texts.items():
        stem = q.split(":", 1)[1]
        body = [f"**질의** — `{src_rel}/{stem}{kb_lib.EXTRACT_QUERY_SUFFIX}` 다. {len(lines)}줄이고 이 청크는 추출 생성물이다. "
                f"질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.", ""] + quote(lines, QUERY_LANG)
        c = Chunk(f"{stem}.md", q, ids.get(q, CHUNK_IRI), f"질의 {stem} ({src_rel})", f"query {stem} in {src_rel}", body)
        c.links = {"refines": list(dict.fromkeys(reg["refines"] + per_query.get(q, []))), "serves": reg["serves"]}
        out.append(c)
    return out


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
        code = re.findall(r"^```(?:python|starlark)\n(.*?)^```$", text, re.M | re.S)
        if code:
            out[normalized_hash(trim(code[0].splitlines()), qname.split(":", 1)[1])] = qname
    return out


def registry_path(reg: dict) -> str:
    """등록부 사이드카의 경로 — 소스 옆이다."""
    return Path(reg["source"]).with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX).as_posix()


def resolve(reg: dict, names: list[str], hashes: dict[str, str], pkg_dir: Path, check: bool, prev: dict | None = None) -> Ids:
    """등록부 갱신 규칙 (a)~(d). 개명·삭제는 사람의 편집이므로 안내만 하고 등록부를 고치지 않는다.

    `prev` 는 트리의 {정규화 해시: 한정 이름} 이다 — 없으면 파이썬 청크의 것(`previous_hashes`)을 읽는다.
    """
    want, have = set(names), set(reg["ids"])
    gone = sorted(have - want)          # 등록부에 있는데 소스에 없는 이름
    fresh = sorted(n for n in names if n not in have)
    prev = previous_hashes(pkg_dir) if prev is None else prev
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
    ap.add_argument("source", help="추출할 파이썬·Starlark 소스 또는 질의 디렉토리 (저장소 상대 경로)")
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    ap.add_argument("--residency", default="", help="EXTRACTED_SOURCES 리터럴의 원본 defs/kb.bzl — 안 주면 --root 기준")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 생성 청크가 `artifact` 상한 안인지 보고하는 데 쓴다. "
                                               "--check 는 쓰지 않는다 (드리프트 판정에 크기가 들어가지 않는다)")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    src_rel = Path(a.source).as_posix()
    src = root / src_rel
    reg_path = src.with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX)
    residency = a.residency or root / "defs" / "kb.bzl"
    uses_ids: dict = {}
    try:  # 방출 경계와 치역 경계 — 둘 다 defs/kb.bzl 의 리터럴이 단일 정의처다 (M1)
        uses_sources = frozenset(f"tools/{m}.py" for m in kb_lib.load_extracted_sources(residency))
        query_dirs = frozenset(f"tools/{d}" for d in kb_lib.load_extracted_sources(residency, kb_lib.EXTRACTED_QUERY_DIRS_NAME))
        starlark = frozenset(f"defs/{m}{STARLARK_SUFFIX}" for m in kb_lib.load_extracted_sources(residency, kb_lib.EXTRACTED_STARLARK_NAME))
        if src_rel in uses_sources:  # 치역 경계의 등록부는 `uses` 를 방출하는 소스에서만 입력이다
            uses_ids = {m: load_registry(root / f"tools/{m}{kb_lib.EXTRACT_REGISTRY_SUFFIX}")["ids"]
                        for m in kb_lib.load_extracted_sources(residency, kb_lib.USES_TARGETS_NAME)}
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {residency}: 경계 목록을 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    empty = sorted(m for m, ids_ in uses_ids.items() if not ids_)
    if empty:  # 조용히 비는 사고를 막는다 — 치역 경계 안의 등록부가 없으면 모듈 간 `uses` 가 말없이 0 이 된다
        print(f"FAIL [{TAG}] tools/{empty[0]}{kb_lib.EXTRACT_REGISTRY_SUFFIX}: 치역 경계"
              f"({kb_lib.USES_TARGETS_NAME}, {residency})의 등록부가 비었거나 없다 — {' · '.join(empty)}. "
              f"모듈 간 `{kb_lib.USES_KEY}` 가 조용히 비는 것과 같으므로 통과시키지 않는다", file=sys.stderr)
        return EXIT_CONFIG
    is_query = src_rel in query_dirs
    if src.is_dir() and not is_query:
        print(f"FAIL [{TAG}] {src_rel}: 디렉토리 소스는 질의 디렉토리 목록({kb_lib.EXTRACTED_QUERY_DIRS_NAME}, {residency}) "
              f"안이어야 한다 — 목록에 이름을 더하는 것이 추출 대상을 넓히는 일이다", file=sys.stderr)
        return EXIT_CONFIG
    if src_rel.endswith(STARLARK_SUFFIX) and src_rel not in starlark:
        print(f"FAIL [{TAG}] {src_rel}: Starlark 소스는 목록({kb_lib.EXTRACTED_STARLARK_NAME}, {residency}) 안이어야 한다 — "
              f"규칙을 강제하는 코드가 든 파일만 넣는다(배선만 하는 파일은 항목이 아니다, 유저 답 Q10-a)", file=sys.stderr)
        return EXIT_CONFIG
    try:
        reg = load_registry(reg_path)
        if is_query:
            names, hashes, texts = collect_queries(src)
        else:
            lines, head_end, top, imports = parse_source(src, tuple(reg[WIRING_KEY]))
    except ExtractError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL
    except (OSError, SyntaxError) as e:
        print(f"FAIL [{TAG}] {src}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not reg["resource"]:
        print(f"FAIL [{TAG}] {reg_path}: 등록부에 `resource`(소스 파일 개체 IRI)가 없다 — 출처는 kg/base-kg.ttl 의 "
              f"`id:src-…` 개체이고 손으로 세운다", file=sys.stderr)
        return EXIT_CONFIG
    reg["source"] = src_rel
    reg["package"] = reg["package"] or f"{kb_lib.EXTRACT_ROOT}/{src.stem}" + (STARLARK_PKG_SUFFIX if src_rel.endswith(STARLARK_SUFFIX) else "")
    pkg_dir = root / reg["package"]
    digest = source_digest(src)
    if reg["source_hash"] != digest or not reg["at"]:
        if a.check:
            print(f"FAIL [{DRIFT_TAG}] {reg_path}: 등록부의 `source_hash` 가 소스와 어긋난다 — "
                  f"`bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 (소스가 원본, 청크는 뷰)", file=sys.stderr)
            return EXIT_FAIL
        reg["at"], reg["source_hash"] = source_stamp(root, src_rel), digest
    if not is_query:
        names, hashes = collect(top, lines)
    try:
        if is_query:  # 질의 청크는 링크를 스스로 갖는다 (build_queries) — 아래 파일 복합체의 링크 배정을 타지 않는다
            ids = resolve(reg, names, hashes, pkg_dir, a.check, previous_query_hashes(pkg_dir))
            chunks = build_queries(src_rel, texts, ids, reg)
        else:
            if reg[QUERY_REFINES_KEY]:
                raise ExtractError(f"{reg_path}: `{QUERY_REFINES_KEY}` 는 질의 디렉토리 등록부의 키다 — 이 소스의 링크 자리는 "
                                   f"파일 청크 하나이므로 `refines` 에 적는다 (p7-code-links-on-file-composite)")
            ids = resolve(reg, names, hashes, pkg_dir, a.check)
            b = Builder(src_rel, lines, head_end, top, ids, uses_sources, imports, uses_ids, tuple(reg[WIRING_KEY]))
            b.build()
            chunks = b.chunks
    except ExtractError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL
    # 링크는 파일 복합체의 것이고 그 자리는 선언 청크인 파일 청크 하나다 (p7-code-links-on-file-composite, 유저 결정 Q47-b).
    # 구역 청크(절·장·모듈 머리)와 정의 청크는 `part_of` 로만 존재한다 — 함수 churn 도 구역의 재편도 링크를 움직이지 않는다.
    # 연결은 링크 복사가 아니라 구조로 선다: 선언 청크와 복합체는 한 노드이고(유저 결정 Q49-a, 지표의 회계 — metrics
    # composite_declarers), 부분들은 `part_of`(복합체의 `agt:hasDirectPart`)로 그 노드에 닿는다. 부분이 링크를 가지면
    # 게이트 `code-part-link` 가 거부한다(validate check_code_part_link — 판정은 kb_lib.code_part).
    for c in chunks if not is_query else []:
        if c.qname == "module":
            c.links = {"refines": reg["refines"], "serves": reg["serves"]}
    reg["ids"] = ids.ids
    prev = previous_bodies(pkg_dir)  # 본문이 그대로면 `generated.at` 을 유지한다 — diff 가 변경의 크기를 말해야 한다
    outputs = {}
    for c in chunks:
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
            print(f"\nFAIL [{DRIFT_TAG}] — {len(drift)}건 / 생성 청크 {len(chunks)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT_TAG}] — {src_rel} 의 생성 청크 {len(chunks)}개와 등록부가 소스와 일치")
        return 0
    pkg_dir.mkdir(parents=True, exist_ok=True)
    for f in stale:
        f.unlink()
    for f, text in outputs.items():
        f.write_text(text, encoding="utf-8")
    comps = sum(1 for c in chunks if c.composite)
    print(f"생성 {len(chunks)}개 (복합체 {comps}개, 신설 uuid {len(ids.added)}개), 변경 {len(drift)}개: {pkg_dir}")
    # `artifact` 상한 보고 — 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens). 게이트가 아니라 보고다: 거부는
    # chunk_lint(게이트 id `chunk`)의 몫이고 여기서는 추출이 낸 청크 가운데 상한을 넘은 것을 바로 알려준다.
    limit = kb_lib.body_token_limit("artifact")
    enc = kb_lib.load_tokenizer(a.vocab or None)
    over = sorted(((kb_lib.token_count("\n".join(c.body), enc), c.fname) for c in chunks), reverse=True)
    high = [(n, f) for n, f in over if n > limit]
    print(f"`artifact` 상한 {limit} 토큰: 초과 {len(high)}개 / 생성 {len(chunks)}개 · 최대 {over[0][0] if over else 0} 토큰"
          + ("".join(f"\n  초과 {n} 토큰 — {f}" for n, f in high) if high else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
