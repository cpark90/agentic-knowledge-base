#!/usr/bin/env python3
"""청크 본문의 명시적 인용 → 참조 그래프(-kg) 생성.

링크는 편집의 부산물로 만든다(8.3절). 본문이 다른 항목의 식별자를 적어 가리키는
것은 가장 검사 가능성이 높은 근거이므로, 그 인용을 기계로 뽑아 agt:cites 링크로
방출한다 — 손으로 쓰지 않는 생성물이다 (8.2절, 8.8절).

인용 표기: 본문의 `d-NNNN` (자기 자신은 제외). 대상이 실재하지 않으면 비영 종료 —
"인용한 타깃이 존재하는가"가 여기서 강제된다 (참조 무결성).

사용: extract_refs.py --out <생성.ttl> <청크 파일들...>
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CITE = re.compile(r"\bd-(\d{4})\b")
IRI = "https://agentic-knowledge-base.dev/id/chunk-d{}"
EVIDENCE = "https://agentic-knowledge-base.dev/agt/constructionRecord"

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 본문의 인용이다.
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    known, bodies, errors = set(), [], []
    for path in sorted(args.files):
        try:
            iri, body = read(path)
        except ValueError as e:
            errors.append(str(e))
            continue
        known.add(iri)
        bodies.append((path, iri, body))

    blocks = 0
    lines = [PREAMBLE]
    for path, iri, body in bodies:
        cited = sorted({IRI.format(n) for n in CITE.findall(body)} - {iri})
        for target in cited:
            if target not in known:
                errors.append(f"{path}: 인용한 항목이 없다: {target}")
        cited = [c for c in cited if c in known]
        if not cited:
            continue
        blocks += 1
        lines.append(f"\n<{iri}>\n    agt:cites " + " ,\n        ".join(f"<{c}>" for c in cited) + " .")

    if errors:
        for e in errors:
            print(f"FAIL [extract-refs] {e}", file=sys.stderr)
        return 1

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[extract-refs] 인용한 항목 {blocks}개", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
