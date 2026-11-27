#!/usr/bin/env python3
"""정규화 직렬화 (노트 2.5절) — diff가 의미 변화만 보여주도록 출력 순서를 고정한다.

  canonicalize.py --check <files>   파일이 정규형과 일치하는지 검사 (비영 종료)
  canonicalize.py --write <files>   파일을 정규형으로 다시 쓴다 (주석은 사라진다)
  canonicalize.py --catalog <dir> --root <ttl> --module <iri> <name> <files...> [--module-import <iri> <iri>]
                                    표준 OWL 도구용 OASIS XML Catalog 와 모듈 합본을 <dir> 에 쓴다 (Q176-a·Q177-c)

정규형: 정렬된 @prefix 블록 + 주어(subject) 정렬 블록, 술어는 rdf:type 우선 후 정렬,
목적어 정렬. 익명 노드는 rdflib 정준화(canonicalization)로 라벨을 고정한다.
출력·종료: --check 위반은 `FAIL [canon] <경로>: …` + EXIT_FAIL. 읽을 수 없거나 파싱되지 않는 입력은 EXIT_CONFIG.
--catalog 는 빌드 액션(`kb_owl_catalog`)의 실행 경로다. 최상위 파일의 owl:imports 가 대응표 밖이면 `FAIL [canon]` + EXIT_FAIL.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import re

from xml.sax.saxutils import quoteattr

from rdflib import BNode, Graph, Literal, OWL, RDF, URIRef
from rdflib.compare import to_canonical_graph

try:  # 종료 코드 규약의 단일 정의 위치는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)

STANDARD_PREFIXES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "sh": "http://www.w3.org/ns/shacl#",
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "co": "http://purl.org/co/",
    "obo": "http://purl.obolibrary.org/obo/",
    "agt": "https://agentic-knowledge-base.dev/agt/",
}


# 접두어 축약이 안전한 로컬 이름만 축약한다. 그 밖은 <IRI> 그대로.
_PN_LOCAL = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")


# ── 정규 직렬화 — 출력 순서를 고정한다 ────────────────────

def _shorten(iri: str, prefixes: dict[str, str]) -> str:
    for p, ns in prefixes.items():
        if iri.startswith(ns):
            local = iri[len(ns):]
            if _PN_LOCAL.match(local) and not local.endswith("."):
                return f"{p}:{local}"
    return f"<{iri}>"


def _term(t, prefixes: dict[str, str]) -> str:
    if isinstance(t, URIRef):
        return _shorten(str(t), prefixes)
    if isinstance(t, BNode):
        return f"_:{t}"
    if isinstance(t, Literal):
        s = t.n3()  # 전체 IRI datatype 포함
        if t.datatype:
            s = s[: s.rindex("^^")] + "^^" + _shorten(str(t.datatype), prefixes)
        return s
    return t.n3()


def canonical_text(path: Path) -> str:
    g = Graph()
    g.parse(str(path), format="turtle")
    return canonical_graph_text(g)


def canonical_graph_text(g: Graph) -> str:
    """그래프 하나의 정규형 — 파일 정규화(`canonical_text`)와 모듈 합본(`write_catalog`)이 같은 직렬화를 쓴다."""
    cg = to_canonical_graph(g)

    # 사용된 네임스페이스만 @prefix 로 선언 — 리터럴 datatype 도 포함해야 한다
    used = []
    for triple in cg:
        for t in triple:
            if isinstance(t, URIRef):
                used.append(str(t))
            elif isinstance(t, Literal) and t.datatype:
                used.append(str(t.datatype))
    used_s = "".join(used)
    prefixes = {p: ns for p, ns in STANDARD_PREFIXES.items() if ns in used_s}

    out = [f"@prefix {p}: <{ns}> ." for p, ns in sorted(prefixes.items())]
    out.append("")

    by_subject: dict[str, list] = {}
    for s, p, o in cg:
        by_subject.setdefault(_term(s, prefixes), []).append((p, o))

    rdf_type = _term(RDF.type, prefixes)
    for skey in sorted(by_subject):
        pairs = by_subject[skey]
        rendered = sorted(
            ((_term(p, prefixes), _term(o, prefixes)) for p, o in pairs),
            key=lambda po: ((po[0] != rdf_type and po[0] != "a"), po[0], po[1]),
        )
        lines = [skey]
        for i, (pk, ok) in enumerate(rendered):
            pk_out = "a" if pk == rdf_type else pk
            sep = " ." if i == len(rendered) - 1 else " ;"
            lines.append(f"    {pk_out} {ok}{sep}")
        out.append("\n".join(lines))
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--catalog", metavar="DIR", help="대응표·모듈 합본·최상위 파일 사본을 쓸 디렉토리")
    ap.add_argument("--root", help="--catalog: 최상위 온톨로지 파일 (owl:imports 를 담는다)")
    ap.add_argument("--module", nargs="+", action="append", default=[], metavar="ARG",
                    help="--catalog: <모듈 IRI> <합본 파일 이름> <원본 TTL...> — 모듈마다 한 번")
    ap.add_argument("--module-import", nargs=2, action="append", default=[], metavar=("IRI", "IMPORT"),
                    help="--catalog: 모듈 합본에 옮길 owl:imports 하나")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    if args.catalog:
        return write_catalog(Path(args.catalog), args.root, args.module, args.module_import)
    if not args.files:
        ap.error("--check·--write 는 파일이 하나 이상 필요하다")

    # `bazel run` 은 runfiles 디렉토리에서 실행되므로, 사용자가 준 상대 경로는
    # 호출 위치(BUILD_WORKING_DIRECTORY) 기준으로 되돌려 원본 파일을 가리키게 한다.
    workdir = os.environ.get("BUILD_WORKING_DIRECTORY")

    dirty = []
    for f in args.files:
        p = Path(f)
        if workdir and not p.is_absolute() and args.write:
            p = Path(workdir) / p
        try:
            canon = canonical_text(p)
            current = p.read_text(encoding="utf-8")
        except Exception as e:  # OSError·rdflib 파서 — 판정 불가 입력
            print(f"FAIL [canon] {f}: 읽거나 파싱할 수 없다 — {e}")
            return EXIT_CONFIG
        if args.write:
            if current != canon:
                p.write_text(canon, encoding="utf-8")
                print(f"wrote {f}")
        else:
            if current != canon:
                dirty.append(f)

    if args.check and dirty:
        for f in dirty:
            print(f"FAIL [canon] {f}: 정규형과 다름 — bazel run //tools:canonicalize -- --write {f}")
        print(f"\nFAIL [canon] — {len(dirty)}건")
        return EXIT_FAIL
    if args.check:
        print(f"PASS [canon] — {len(args.files)}개 정규형")
    return 0


# ── OWL 대응표 — 표준 OWL 도구가 owl:imports 를 로컬 파일로 풀게 하는 OASIS XML Catalog (Q176-a·Q177-c) ────────
# XML Catalog 는 IRI 하나를 파일 하나에 대응시키는데, 모듈은 디렉토리이고 파일이 여럿이며 owl:Ontology 선언이 없다.
# 그래서 모듈마다 원본 파일을 합친 합본에 `<모듈 IRI> a owl:Ontology` 머리를 더하고, 대응표와 최상위 파일 사본을
# 한 디렉토리에 둔다. 출력은 bazel-out 에만 있다(pe-generated-outputs-stay-in-bazel-out). IRI 의 원본은 모듈 BUILD 의
# `iri` 이고 규칙 `kb_owl_catalog`(defs/knowledge.bzl)가 OntologyModuleInfo 에서 읽어 인자로 넘긴다.

CATALOG_FILE = "catalog-v001.xml"  # Protégé·OWL API·ROBOT 가 온톨로지 옆에서 찾는 이름
CATALOG_NS = "urn:oasis:names:tc:entity:xmlns:xml:catalog"


def module_graph(iri: str, files: list[str], imports: list[str]) -> Graph:
    """모듈 하나의 합본 그래프 — 원본 파일의 합집합에 owl:Ontology 머리와 그 모듈의 owl:imports 를 더한다."""
    g = Graph()
    for f in files:
        g.parse(f, format="turtle")
    node = URIRef(iri)
    g.add((node, RDF.type, OWL.Ontology))
    for imp in imports:
        g.add((node, OWL.imports, URIRef(imp)))
    return g


def catalog_xml(entries: dict[str, str]) -> str:
    """IRI → 같은 디렉토리 안 상대 경로의 대응표. 항목은 IRI 순이어서 같은 입력이면 같은 바이트다."""
    lines = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
             f'<catalog prefer="public" xmlns="{CATALOG_NS}">']
    lines += [f"    <uri name={quoteattr(iri)} uri={quoteattr(entries[iri])}/>" for iri in sorted(entries)]
    lines.append("</catalog>")
    return "\n".join(lines) + "\n"


def write_catalog(out: Path, root: str | None, modules: list[list[str]], imports: list[list[str]]) -> int:
    """대응표·모듈 합본·최상위 파일 사본을 `out` 에 쓴다. 최상위 owl:imports 와 모듈 imports 는 대응표 안이어야 한다."""
    if not root or not modules:
        print("FAIL [canon] --catalog: --root 와 --module 이 하나 이상 필요하다")
        return EXIT_CONFIG
    entries: dict[str, str] = {}
    sources: dict[str, list[str]] = {}
    for spec in modules:
        if len(spec) < 3:
            print(f"FAIL [canon] --module {' '.join(spec)}: <IRI> <이름> <원본 TTL...> 꼴이 아니다")
            return EXIT_CONFIG
        iri, name, files = spec[0], spec[1], spec[2:]
        if "/" in name or name == CATALOG_FILE or name == Path(root).name or name in entries.values() or iri in entries:
            print(f"FAIL [canon] --module {iri} {name}: 합본 이름이나 IRI 가 겹치거나 디렉토리 밖을 가리킨다")
            return EXIT_CONFIG
        entries[iri], sources[iri] = name, files
    extra: dict[str, list[str]] = {}
    for iri, imp in imports:
        extra.setdefault(iri, []).append(imp)
    try:
        rg = Graph()
        rg.parse(root, format="turtle")
        graphs = {iri: module_graph(iri, sources[iri], extra.get(iri, [])) for iri in entries}
    except Exception as e:  # OSError·rdflib 파서 — 판정 불가 입력
        print(f"FAIL [canon] --catalog: 읽거나 파싱할 수 없다 — {e}")
        return EXIT_CONFIG
    wanted = {str(o) for o in rg.objects(None, OWL.imports)} | {i for v in extra.values() for i in v}
    missing = sorted(wanted - set(entries))
    for iri in missing:
        print(f"FAIL [canon] {iri}: owl:imports 가 대응표에 없다 — 그 모듈을 --module 로 넘긴다")
    if missing:
        return EXIT_FAIL
    out.mkdir(parents=True, exist_ok=True)
    for iri, g in graphs.items():
        (out / entries[iri]).write_text(canonical_graph_text(g), encoding="utf-8")
    (out / CATALOG_FILE).write_text(catalog_xml(entries), encoding="utf-8")
    (out / Path(root).name).write_bytes(Path(root).read_bytes())
    return 0


if __name__ == "__main__":
    sys.exit(main())
