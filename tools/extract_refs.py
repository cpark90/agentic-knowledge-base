#!/usr/bin/env python3
"""청크 본문의 명시적 인용·개념 사용 → 참조 그래프(-kg) 생성.

링크는 편집의 부산물로 만든다(8.3절). 본문이 다른 항목의 식별자를 적어 가리키는
것은 가장 검사 가능성이 높은 근거이므로, 그 인용을 기계로 뽑아 agt:cites 링크로
방출한다 — 손으로 쓰지 않는 생성물이다 (8.2절, 8.8절).

인용 표기: 본문의 `d-NNNN` (자기 자신은 제외). 대상이 실재하지 않으면 비영 종료 —
"인용한 타깃이 존재하는가"가 여기서 강제된다 (참조 무결성).

개념 사용 표기 (--ontology 를 줄 때만, dependency-graph-design §6 복원 경로):
본문의 `agt:<Term>` 이 온톨로지 union이 정의하는 agt: 클래스·속성·개체이면
agt:usesConcept 링크로 방출한다 (청크당 용어당 1). 온톨로지에 없는 표기는 링크로
만들지 않고 stderr 에 `info [usesConcept]` 로 센다 — 본문의 오타·예시일 수 있으므로
게이트 실패가 아니다. 폐기된 용어 참조의 경고는 validate.py 가 낸다.

사용: extract_refs.py --out <생성.ttl> [--ontology <온톨로지.ttl...> --] <청크 파일들...>
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

CITE = re.compile(r"\bd-(\d{4})\b")
CONCEPT = re.compile(r"\bagt:([A-Za-z][A-Za-z0-9]*)")
IRI = "https://agentic-knowledge-base.dev/id/chunk-d{}"
AGT = "https://agentic-knowledge-base.dev/agt/"
EVIDENCE = "https://agentic-knowledge-base.dev/agt/constructionRecord"

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 본문의 인용·개념 표기다.
# 생성: tools/extract_refs.py (bazel build //kg:references_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id: <https://agentic-knowledge-base.dev/id/> .
"""


def read(path: str) -> tuple[str, str]:
    """(자기 IRI, 본문). frontmatter는 인용 대상이 아니므로 뺀다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: frontmatter가 없다")
    end = lines[1:].index("---") + 1
    iri = ""
    for l in lines[1:end]:
        if l.startswith("id:"):
            iri = l.split(":", 1)[1].strip()
    if not iri:
        raise ValueError(f"{path}: frontmatter에 id 가 없다 (OKF 확장 키, uuid IRI)")
    return iri, "\n".join(lines[end + 1 :])


def load_concepts(paths: list[str]) -> set[str]:
    """온톨로지 union이 정의하는 agt: 용어(클래스·속성·개체)의 로컬 이름 집합.

    rdflib·kb_lib 는 --ontology 를 줄 때만 필요하다 — 없으면 이 함수는 호출되지 않는다.
    """
    try:
        from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
    except ImportError:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    merged, _ = kb_lib.load_merged(paths)
    return {str(t)[len(AGT):] for t in kb_lib.defined_terms(merged)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ontology", nargs="*", default=[],
                    help="온톨로지 모듈 파일들(*-ontology.ttl). 주면 agt:usesConcept 도 방출한다. 뒤에 `--` 를 두고 청크 파일을 잇는다")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    concepts: set[str] | None = set(load_concepts(args.ontology)) if args.ontology else None

    known, bodies, errors = set(), [], []
    # 청크는 .md 뿐이다 — 매크로가 `-- $(SRCS)` 로 넘기면 온톨로지 .ttl 도 섞여 오므로 조용히 건너뛴다
    for path in sorted(p for p in args.files if p.endswith(".md")):
        try:
            iri, body = read(path)
        except ValueError as e:
            errors.append(str(e))
            continue
        known.add(iri)
        bodies.append((path, iri, body))

    blocks, concept_blocks, concept_links = 0, 0, 0
    unknown: Counter[str] = Counter()
    unknown_where: dict[str, list[str]] = defaultdict(list)
    lines = [PREAMBLE]
    for path, iri, body in bodies:
        cited = sorted({IRI.format(n) for n in CITE.findall(body)} - {iri})
        for target in cited:
            if target not in known:
                errors.append(f"{path}: 인용한 항목이 없다: {target}")
        cited = [c for c in cited if c in known]

        used: list[str] = []
        if concepts is not None:
            mentioned = sorted(set(CONCEPT.findall(body)))
            used = [t for t in mentioned if t in concepts]
            for t in mentioned:
                if t not in concepts:
                    unknown[t] += 1
                    unknown_where[t].append(path)

        if not cited and not used:
            continue
        parts = []
        if cited:
            blocks += 1
            parts.append("    agt:cites " + " ,\n        ".join(f"<{c}>" for c in cited))
        if used:
            concept_blocks += 1
            concept_links += len(used)
            parts.append("    agt:usesConcept " + " ,\n        ".join(f"agt:{t}" for t in used))
        lines.append(f"\n<{iri}>\n" + " ;\n".join(parts) + " .")

    if errors:
        for e in errors:
            print(f"FAIL [extract-refs] {e}", file=sys.stderr)
        return 1

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[extract-refs] 인용한 항목 {blocks}개", file=sys.stderr)
    if concepts is not None:
        print(f"[extract-refs] 개념을 사용한 항목 {concept_blocks}개, usesConcept 링크 {concept_links}개", file=sys.stderr)
        for term, n in sorted(unknown.items(), key=lambda kv: (-kv[1], kv[0])):
            where = ", ".join(sorted(set(unknown_where[term]))[:3])
            print(f"info [usesConcept] 온톨로지에 없는 표기 agt:{term} — 청크 {n}개 ({where}{' …' if len(set(unknown_where[term])) > 3 else ''})",
                  file=sys.stderr)
        if unknown:
            print(f"info [usesConcept] 온톨로지에 없는 표기 {len(unknown)}종 / 청크-표기 쌍 {sum(unknown.values())}개 — 링크로 만들지 않음",
                  file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
