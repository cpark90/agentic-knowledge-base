#!/usr/bin/env python3
"""코드 → 단위 지식 추출기 — 소스 하나에서 `artifact` 지식 종류의 파일 항목을 생성한다 (p7-code-extraction-direction).

코드가 원본이고 단위 지식은 생성물이다. 단위 지식 파일을 손으로 고치면 드리프트 게이트(`//:extract_drift_test`)가 거부한다.
tangle(단위 지식 → 코드)은 없다. 정체성의 원본은 소스 옆의 **등록부**(`<소스>.chunks.yml`)이고 한정 이름 → uuid 를 담는다
(p10-function-identity-registry).

추출 범위는 파일 항목뿐이다(유저 답 Q191-a, 2026-11-28). 코드 파일 하나에서 **모듈 항목** 하나(`module.md` — 모듈
docstring 과 import 의 인용)를, 질의 파일 하나에서 **질의 항목** 하나를 낸다. 함수와 클래스, 절, 장, 모듈 머리는 항목으로
올리지 않고 그 원문은 소스에만 있다. 모듈 항목은 부분 없는 단위 지식이라 복합체를 선언하지 않는다. 링크(`refines`·`serves`)와
검증기의 `verifies` 도착점이 파일 항목이다 (p7-code-links-on-file-composite). 정의 사이의 `uses`(agt:usesDefinition)는
정의 단위 지식이 없으므로 내지 않는다.

단위 지식의 `generated.at` 은 **그 단위 지식의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 단위 지식에
다시 찍으면 실제 변경 한 건이 diff 여러 건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다. 코드 파일의 한정 이름은 `module` 하나라 (b) 는 질의 파일에만
걸린다. 추출 트리에서 이번 추출이 만들지 않는 `.md` 는 지운다(`--check` 는 그 파일을 어긋남으로 보고한다).

질의 디렉토리(`EXTRACTED_QUERY_DIRS`, 2026-10-03)는 소스가 디렉토리 `tools/<이름>` 이고 그 안의 `*.rq` 질의 파일 하나가
질의 항목 하나다 — 파일 전체가 인용 하나다. 링크(`refines`·`serves`)는 질의 항목마다 붙는다. 등록부는
`tools/<이름>.chunks.yml` 이고 키는 `query:<파일 이름 stem>` 이다. 등록부의 `refines`·`serves` 는 디렉토리의 질의 전부에
붙고, 질의 하나에만 붙는 `refines` 는 선택 키 `query_refines`(`query:<stem>: [<IRI>…]`)에 적는다 — 질의 파일 하나가 파일
항목 하나의 자리이기 때문이다. 갱신 규칙 (a)~(d) 와 도장은 파이썬 소스와 같고 `source_hash` 는 디렉토리 안 질의 파일 전부의
(이름, 바이트) 해시다(`source_digest`).

Starlark 소스(`EXTRACTED_STARLARK`, 유저 답 Q32-a, 2026-10-04)는 파이썬 소스와 같은 모양이다 — `.bzl` 은 파이썬 문법의
부분집합이므로 같은 AST 로 모듈 머리를 읽는다. 다른 것은 셋이다. 모듈 머리의 `load(...)` 가 import 자리이고, 인용 펜스의
언어가 `starlark` 이며, 생성 패키지는 `kb/dev/artifact/<이름>-bzl` 이다. 등록부의 선택 키 `wiring:` 은 **배선**(입력 집합과
인자를 잇기만 하는 최상위 정의·대입, 유저 답 Q10-a "빌드 배선은 항목이 아니다")의 이름 목록이다 — 추출기는 이름이 소스의
최상위에 실재하는지만 보고, 없는 이름이 목록에 있으면 FAIL 이다.

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
CHUNK_IRI = f"{kb_lib.ID_BASE}chunk/"  # 이름공간은 kb_lib.ID_BASE 하나다 (task 0327 손질 9)
DEFAULT_ASSUMES = f"{kb_lib.ID_BASE}asm-chunk-conventions"
MODULE_QNAME = "module"  # 코드 파일의 유일한 한정 이름 — 파일 항목 `module.md` (Q191-a)


class ExtractError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""


# ── 등록부 (사이드카) ─────────────────────────────────────────────────────────────────────
# 손으로 쓰는 것은 `layer`·`refines`·`serves` 와 uuid 이고, `at`·`source_hash` 와 신설 uuid 는 추출기가 더한다.
# `layer` 는 소스 하나의 서비스 층이고 생성 단위 지식 전부의 frontmatter 로 옮겨진다 — 도구는 프로세스 층의 실행
# 표면이므로 값은 `process` 다 (결정 p0-service-is-a-three-layer-wiki).
# `serves` 의 정의역은 `agt:DecisionChunk` 다(fulfilment-ontology) — 산출물 단위 지식이 요구를 직접 `serves` 하면
# 추론이 그것을 결정으로 만들고 shape DecisionSubstanceShape 이 거부한다. 코드가 요구에 닿는 길은 결정을
# `refines` 하는 것이고 그 결정이 요구를 `serves`·`refines` 한다 — 정제 계층을 건너뛰지 않는다 (6.2절).
# YAML 부분집합만 쓴다 — 이 저장소의 frontmatter 파서와 같은 수준이고 외부 의존이 없다.
REGISTRY_HEAD = """\
# 등록부 — 손이 원본이다. 한정 이름 → uuid 가 코드 단위 지식의 정체성이고 이름은 그 위의 라벨이다
# (p10-split-keeps-work-identity · p7-code-extraction-direction). 생성기는 신설 uuid 와 `at`·`source_hash` 만 더한다.
# 개명은 아래 `ids` 의 키를 손으로 고치는 것이고, 삭제는 키를 손으로 지우는 것이다 — 둘 다 사람의 편집이다.
# 생성물은 `{package}/` 이며 손으로 고치면 `//:extract_drift_test` 가 거부한다.
"""


# 배선 목록 — 등록부의 선택 키. 입력 집합과 인자를 잇기만 하는 최상위 정의·대입의 이름이고 추출기는 그것을 단위 지식으로 내지
# 않는다(유저 답 Q10-a "빌드 배선은 항목이 아니다" · Q32-a "규칙을 강제하는 코드는 항목이다"). 손이 원본이다 — 어느 정의가
# 배선인지는 저작자의 판단이고, 추출기는 이름이 소스의 최상위에 실재하는지만 본다.
WIRING_KEY = "wiring"
# 질의별 정제 — 질의 디렉토리 등록부의 선택 키. `query:<stem>: [<IRI>…]` 가 그 질의 단위 지식 하나에만 `refines` 를 더한다
# (디렉토리 전체의 `refines` 다음에, 중복 없이). 질의 파일 하나가 링크의 자리이므로(p7-code-links-on-file-composite) 디렉토리
# 공통 링크와 질의 하나의 링크를 가른다. 파이썬·Starlark 등록부에 적으면 거부한다 — 그쪽의 링크 자리는 파일 단위 지식 하나다.
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


# ── 소스 읽기 — 모듈 머리 ────────────────────────────────────────────────────────────────────
def parse_source(path: Path, wiring: tuple = ()) -> tuple[list[str], int]:
    """소스 → (줄들, 모듈 머리의 끝 줄). 모듈 항목이 인용하는 자리는 모듈 머리뿐이다 (Q191-a).

    배선 목록(등록부 `wiring`)의 이름이 소스의 최상위에 실재하는지는 여기서 본다 — 지운 정의가 목록에 남으면 거부한다.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    tree = ast.parse("\n".join(lines))
    stray = sorted(set(wiring) - {top_name(n) for n in tree.body})
    if stray:
        raise ExtractError(f"{path}: 등록부 `{WIRING_KEY}` 의 이름이 소스의 최상위에 없다 — {' · '.join(stray)}. "
                           f"배선 목록은 소스의 최상위 정의·대입 이름이다 — 지운 정의는 목록에서도 지운다")
    return lines, module_head_end(tree, path.suffix == STARLARK_SUFFIX)


def module_head_end(tree: ast.Module, starlark: bool = False) -> int:
    """모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지다. 모듈 항목은 이 범위를 인용한다.

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


def top_name(node) -> str:
    """최상위 문의 이름 — 정의면 그 이름, 이름 하나에 대입하면 그 이름, 그 밖은 빈 문자열이다 (배선 목록의 키)."""
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return ""


def qualified(kind: str, key: str) -> str:
    return f"{kind}:{key}"


def normalized_hash(text_lines: list[str], name: str) -> str:
    """이름을 지운 본문의 해시 — 개명 판정의 기준이다. 이름만 바뀐 질의는 같은 해시를 갖는다."""
    body = "\n".join(l.rstrip() for l in text_lines if l.strip())
    body = re.sub(r"\b" + re.escape(name) + r"\b", "@", body)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


# ── 단위 지식 만들기 — 모듈 항목 ─────────────────────────────────────────────
class Chunk:
    """생성할 단위 지식 하나 — 파일 이름·frontmatter·본문. 부분이 없으므로 `part_of`·`composite:` 를 갖지 않는다."""

    def __init__(self, fname: str, qname: str, iri: str, title_ko: str, title: str, body: list[str]):
        self.fname, self.qname, self.iri = fname, qname, iri
        self.title_ko, self.title, self.body = title_ko, title, body
        self.links: dict = {}


def source_lang(src_rel: str) -> str:
    """인용 펜스의 언어 — `.bzl` 이면 starlark, 그 밖의 소스 파일은 python 이다."""
    return "starlark" if src_rel.endswith(STARLARK_SUFFIX) else "python"


def quote(lines: list[str], lang: str = "python") -> list[str]:
    """인용 구역 — 소스를 그대로 옮긴 코드 펜스. 생성기는 원문을 고쳐 쓰지 않는다."""
    return [kb_lib.SOURCE_QUOTE_OPEN, f"```{lang}", *[l.rstrip() for l in lines], "```", kb_lib.SOURCE_QUOTE_CLOSE]


def build_module(src_rel: str, lines: list[str], head_end: int, ids, reg: dict) -> Chunk:
    """코드 파일 하나 → 모듈 항목 하나. 본문은 모듈 docstring 과 import 의 인용이고 링크는 등록부에서 옮긴다."""
    lang = source_lang(src_rel)
    body = [f"**파일** — `{src_rel}` 다. {len(lines)}줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 "
            f"올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.", ""]
    body += ["**모듈 머리** — 모듈 docstring 과 " + ("`load`" if lang == "starlark" else "import") + " 다.", ""] \
        + quote(lines[:head_end], lang)
    c = Chunk("module.md", MODULE_QNAME, ids.get(MODULE_QNAME, CHUNK_IRI), f"파일 {src_rel}", f"file {src_rel}", body)
    # 링크는 파일 항목의 것이다 (p7-code-links-on-file-composite) — 함수를 고치거나 쪼개도 링크가 움직이지 않는다
    c.links = {"refines": reg["refines"], "serves": reg["serves"]}
    return c


# ── frontmatter 직렬화 ────────────────────────────────────────────────────────────────────
def stamped(reg: dict) -> str:
    """도장이 지금 소스를 가리키는가 — `tested.source_hash` 가 등록부의 `source_hash` 와 같을 때만 참이다.

    소스가 도장 뒤에 바뀌면 거짓이 되고 `verified` 가 빠진다 (p7-code-extraction-direction "도장"). 사람이 등록부에서
    도장을 지우는 행위도 같은 결과를 낸다 — 도장은 저작물이고 단위 지식은 뷰다.
    """
    t = reg.get(kb_lib.STAMP_KEY) or {}
    return t.get("at", "") if t.get("source_hash") and t["source_hash"] == reg["source_hash"] else ""


def previous_bodies(pkg_dir: Path) -> dict:
    """트리의 생성 단위 지식 → {파일 이름: (본문, generated.at)}. `generated.at` 의 보존 규칙이 이 값을 쓴다.

    단위 지식의 `generated.at` 은 **그 단위 지식의 본문이 바뀐 추출에서만** 갱신된다. 소스 파일의 시각(등록부 `at`)을 모든 단위 지식에
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
    if reg.get(kb_lib.LAYER_KEY):  # 서비스 층 — 등록부가 소스 하나의 층을 선언하고 그 선언이 생성 단위 지식 전부(모듈·질의 항목)로
        fm.append(f"{kb_lib.LAYER_KEY}: {reg[kb_lib.LAYER_KEY]}")  # 옮겨진다. 도구는 프로세스 층의 실행 표면이다 (p0-service-is-a-three-layer-wiki)
    if stamped(reg):  # 테스트 통과 도장 — 소스가 도장 뒤에 바뀌면 빠진다 (수정 뒤 미검증, 재검증 자동)
        fm.append(f"verified: [{{by: {kb_lib.STAMP_ACTOR}, at: {reg[kb_lib.STAMP_KEY]['at']}}}]")
    for key in ("refines", "serves"):
        if c.links.get(key):
            fm.append(f"{key}: [" + ", ".join(c.links[key]) + "]")
    return "---\n" + "\n".join(fm) + "\n---\n" + "\n".join(c.body) + "\n"


# ── 질의 디렉토리 — 질의 파일 하나 = 단위 지식 하나 (EXTRACTED_QUERY_DIRS, 2026-10-03) ──────────────
# //kg:cq 뷰의 내용 원본(역량 질문 질의)과 //kg:gate_test 의 검증 질의가 코드 단위 지식 밖에 있었다. 파이썬 소스와 같은 방향
# (p7-code-extraction-direction)으로 추출하고 질의 파일 하나가 질의 항목 하나다.
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
    """트리에 있는 질의 단위 지식 → {정규화 해시: 한정 이름}. `previous_hashes` 의 질의판이다 — 펜스 언어만 다르다."""
    out = {}
    for f in sorted(pkg_dir.glob("*.md")) if pkg_dir.is_dir() else []:
        code = re.findall(r"^```" + QUERY_LANG + r"\n(.*?)^```$", f.read_text(encoding="utf-8"), re.M | re.S)
        if code:
            out[normalized_hash(code[0].splitlines(), f.stem)] = qualified("query", f.stem)
    return out


def build_queries(src_rel: str, texts: dict[str, list[str]], ids, reg: dict) -> list[Chunk]:
    """질의 단위 지식들 — 파일 전체가 인용 하나이고 링크는 단위 지식마다 붙는다. 질의 파일이 곧 링크의 자리다."""
    per_query = reg.get(QUERY_REFINES_KEY) or {}
    unknown = sorted(set(per_query) - set(texts))
    if unknown:
        raise ExtractError(f"{src_rel}: 등록부 `{QUERY_REFINES_KEY}` 의 키 {', '.join(unknown)} 가 디렉토리의 질의가 아니다 — "
                           f"키는 `query:<질의 파일 stem>` 이다")
    out = []
    for q, lines in texts.items():
        stem = q.split(":", 1)[1]
        body = [f"**질의** — `{src_rel}/{stem}{kb_lib.EXTRACT_QUERY_SUFFIX}` 다. {len(lines)}줄이고 이 단위 지식은 추출 생성물이다. "
                f"질의 파일 하나가 단위 지식 하나이므로 링크와 가정의 자리가 이 단위 지식이다.", ""] + quote(lines, QUERY_LANG)
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


def registry_path(reg: dict) -> str:
    """등록부 사이드카의 경로 — 소스 옆이다."""
    return Path(reg["source"]).with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX).as_posix()


def resolve(reg: dict, names: list[str], hashes: dict[str, str], pkg_dir: Path, check: bool, prev: dict | None = None) -> Ids:
    """등록부 갱신 규칙 (a)~(d). 개명·삭제는 사람의 편집이므로 안내만 하고 등록부를 고치지 않는다.

    `prev` 는 트리의 {정규화 해시: 한정 이름} 이다 — 질의 디렉토리만 준다. 코드 파일의 한정 이름은 `module` 하나라 개명이 없다.
    """
    want, have = set(names), set(reg["ids"])
    gone = sorted(have - want)          # 등록부에 있는데 소스에 없는 이름
    fresh = sorted(n for n in names if n not in have)
    prev = prev or {}
    renames = []
    for q in fresh:
        was = prev.get(hashes.get(q, ""))
        if was and was in gone:
            renames.append((was, q))
    if renames:
        raise ExtractError(f"{reg['source']}: 개명이다 — 본문이 같고 이름만 바뀐 질의가 {len(renames)}건이다. 등록부 "
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
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 생성 단위 지식이 `artifact` 상한 안인지 보고하는 데 쓴다. "
                                               "--check 는 쓰지 않는다 (드리프트 판정에 크기가 들어가지 않는다)")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    src_rel = Path(a.source).as_posix()
    src = root / src_rel
    reg_path = src.with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX)
    residency = a.residency or root / "defs" / "kb.bzl"
    uses_ids: dict = {}
    try:  # 추출 대상 목록 — defs/kb.bzl 의 리터럴이 단일 정의 위치다 (M1)
        uses_sources = frozenset(f"tools/{m}.py" for m in kb_lib.load_extracted_sources(residency))
        query_dirs = frozenset(f"tools/{d}" for d in kb_lib.load_extracted_sources(residency, kb_lib.EXTRACTED_QUERY_DIRS_NAME))
        starlark = frozenset(f"defs/{m}{STARLARK_SUFFIX}" for m in kb_lib.load_extracted_sources(residency, kb_lib.EXTRACTED_STARLARK_NAME))
        # 치역 경계(USES_TARGETS)의 등록부 — 2026-11-28 부터 정의 사이의 `uses` 를 내지 않아(Q191-a) 아래 빈 등록부 검사만 읽는다
        if src_rel in uses_sources:
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
            lines, head_end = parse_source(src, tuple(reg[WIRING_KEY]))
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
                  f"`bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 (소스가 원본, 단위 지식은 뷰)", file=sys.stderr)
            return EXIT_FAIL
        reg["at"], reg["source_hash"] = source_stamp(root, src_rel), digest
    try:
        if is_query:  # 질의 항목은 링크를 스스로 갖는다 (build_queries)
            ids = resolve(reg, names, hashes, pkg_dir, a.check, previous_query_hashes(pkg_dir))
            chunks = build_queries(src_rel, texts, ids, reg)
        else:
            if reg[QUERY_REFINES_KEY]:
                raise ExtractError(f"{reg_path}: `{QUERY_REFINES_KEY}` 는 질의 디렉토리 등록부의 키다 — 이 소스의 링크 자리는 "
                                   f"모듈 항목 하나이므로 `refines` 에 적는다 (p7-code-links-on-file-composite)")
            ids = resolve(reg, [MODULE_QNAME], {}, pkg_dir, a.check)
            chunks = [build_module(src_rel, lines, head_end, ids, reg)]
    except ExtractError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL
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
                  f"(소스가 원본, 단위 지식은 뷰)")
        if drift:
            print(f"\nFAIL [{DRIFT_TAG}] — {len(drift)}건 / 생성 단위 지식 {len(chunks)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT_TAG}] — {src_rel} 의 생성 단위 지식 {len(chunks)}개와 등록부가 소스와 일치")
        return 0
    pkg_dir.mkdir(parents=True, exist_ok=True)
    for f in stale:
        f.unlink()
    for f, text in outputs.items():
        f.write_text(text, encoding="utf-8")
    print(f"생성 {len(chunks)}개 (신설 uuid {len(ids.added)}개), 변경 {len(drift)}개, 삭제 {len(stale)}개: {pkg_dir}")
    # `artifact` 상한 보고 — 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens). 게이트가 아니라 보고다: 거부는
    # chunk_lint(게이트 id `chunk`)의 몫이고 여기서는 추출이 낸 단위 지식 가운데 상한을 넘은 것을 바로 알려준다.
    limit = kb_lib.body_token_limit("artifact")
    enc = kb_lib.load_tokenizer(a.vocab or None)
    over = sorted(((kb_lib.token_count("\n".join(c.body), enc), c.fname) for c in chunks), reverse=True)
    high = [(n, f) for n, f in over if n > limit]
    print(f"`artifact` 상한 {limit} 토큰: 초과 {len(high)}개 / 생성 {len(chunks)}개 · 최대 {over[0][0] if over else 0} 토큰"
          + ("".join(f"\n  초과 {n} 토큰 — {f}" for n, f in high) if high else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
