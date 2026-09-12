#!/usr/bin/env python3
"""정규화 직렬화 (노트 2.5절) — diff가 의미 변화만 보여주도록 출력 순서를 고정한다.

  canonicalize.py --check <files>   파일이 정규형과 일치하는지 검사 (비영 종료)
  canonicalize.py --write <files>   파일을 정규형으로 다시 쓴다 (주석은 사라진다)

정규형: 정렬된 @prefix 블록 + 주어(subject) 정렬 블록, 술어는 rdf:type 우선 후 정렬,
목적어 정렬. 익명 노드는 rdflib 정준화(canonicalization)로 라벨을 고정한다.
출력·종료: --check 위반은 `FAIL [canon] <경로>: …` + EXIT_FAIL. 읽을 수 없거나 파싱되지 않는 입력은 EXIT_CONFIG.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import re

from rdflib import BNode, Graph, Literal, RDF, URIRef
from rdflib.compare import to_canonical_graph

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백
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
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

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


if __name__ == "__main__":
    sys.exit(main())
