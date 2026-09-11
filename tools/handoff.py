#!/usr/bin/env python3
"""읽기 집합 인수인계 — 작업 집합 뷰에서 펼쳐 읽은 청크를 새 청크의 OKF `sources` 로 옮긴다 (노트 10.3절, 부록 E.2).

`sources` 는 "편집 시 읽은 것"의 산출이며 하네스가 채워야 한다. 하네스가 읽기 집합을 기록하기 전까지의 첫 형태:
workset 뷰(bazel-bin/kg/workset-<role>.md)의 `<!-- iri: … -->` 줄이 읽기 집합이고, 이 도구가 대상 청크의 frontmatter
`sources` 에 병합한다 (기존 항목 유지). 사용: handoff.py --workset bazel-bin/kg/workset-developer.md <청크 파일...>
"""
import argparse
import re
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workset", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    read_set = re.findall(r"<!-- iri: (\S+) -->", Path(a.workset).read_text(encoding="utf-8"))
    if not read_set:
        raise SystemExit("handoff: 작업 집합에 펼친 청크가 없다 — 앵커를 주고 다시 만들어라")
    for f in a.files:
        text = Path(f).read_text(encoding="utf-8")
        m = re.search(r"^sources: \[(.*)\]$", text, re.M)
        existing = re.findall(r"resource: (\S+?)[,}]", m.group(1)) if m else []
        merged = existing + [r for r in read_set if r not in existing]
        line = "sources: [" + ", ".join("{resource: " + r + "}" for r in merged) + "]"
        text = text.replace(m.group(0), line) if m else text.replace("\ngenerated:", "\n" + line + "\ngenerated:", 1)
        Path(f).write_text(text, encoding="utf-8")
        print(f"{f}: sources {len(existing)} → {len(merged)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
