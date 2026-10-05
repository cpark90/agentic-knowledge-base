#!/usr/bin/env python3
"""생성 문서 머리 `입력` 줄의 union 증분 표기 시험 — 양성 하나와 음성 셋 (유저 답 Q40-a, 2026-10-04).

고정물은 시험이 TEST_TMPDIR 에 쓰는 그래프 파일 셋이다 — `kg/chunks-kg.ttl`(트리플 3, 빈 노드 하나) · `kg/base-kg.ttl`(트리플 2,
그중 1은 chunks 와 같다) · `kg/extra-kg.ttl`(표에 없는 구성원, 트리플 2, 빈 노드 하나). 증분은 선언 순서대로 앞 구성원들의
합집합에 더한 수라 chunks +3 · base +1 · extra-kg +2 이고 합 6은 셋을 한 그래프에 적재한 총수와 같다. 입력 순서를 뒤집어도 표기가
같다(선언 순서이지 입력 순서가 아니다).
  양성  gendoc_union 의 표기가 위와 같고, 그 표기를 가진 머리 블록이 kb_lib.check_gendoc 에서 G4 FAIL 이 없다
  음성  총수가 증분 합과 다른 줄 · 증분이 없는 옛 표기(`union: chunks·base`) · 읽지 못한 구성원(`+?`) — 셋 다 G4 FAIL
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

from rdflib import Graph

from tools import kb_lib

FIXTURE = {
    "kg/chunks-kg.ttl": "<urn:a> <urn:p> <urn:b> .\n<urn:a> <urn:p> <urn:c> .\n_:x <urn:p> <urn:d> .\n",
    "kg/base-kg.ttl": "<urn:a> <urn:p> <urn:b> .\n<urn:e> <urn:p> <urn:f> .\n",
    "kg/extra-kg.ttl": "_:y <urn:p> <urn:d> .\n<urn:g> <urn:p> <urn:h> .\n",
}
WANT = "union: chunks +3 · base +1 · extra-kg +2"


def doc(paths, scale: str) -> str:
    """머리 블록만 가진 생성 문서 — 생성기와 같은 함수로 낸다."""
    head = kb_lib.gendoc_header("fx", "union 증분 시험", "defs/tests/gendoc_union_fixture_test.py", "고정물",
                                "bazel test //defs/tests:gendoc_union_fixture_test", paths, scale,
                                kb_lib.gendoc_view_notice("고정물"), input_kind="그래프 파일")
    return kb_lib.gendoc_assemble(head, ["## 본문", "", "고정물이다.", ""], paths, input_kind="그래프 파일")


def g4(text: str) -> list[str]:
    errors, _ = kb_lib.check_gendoc("fx.md", text)
    return [m for _, m in errors if m.startswith("G4")]


def main() -> int:
    root = Path(tempfile.mkdtemp(dir=os.environ.get("TEST_TMPDIR")))
    paths = []
    for rel, body in FIXTURE.items():
        f = root / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(body, encoding="utf-8")
        paths.append(str(f))
    g = Graph()
    for p in paths:
        g.parse(p, format="turtle")
    fails = []
    got, got_rev = kb_lib.gendoc_union(paths), kb_lib.gendoc_union(list(reversed(paths)))
    if got != WANT or got_rev != WANT:
        fails.append(f"표기 {got!r} · 뒤집은 입력 {got_rev!r} — 기대 {WANT!r}")
    if len(g) != 6:
        fails.append(f"고정물 총수 {len(g)} — 기대 6")
    ok = g4(doc(paths, f"트리플 {len(g)} ({got})"))
    if ok:
        fails.append(f"양성에 G4 FAIL: {ok}")
    for name, scale in (("총수 불일치", f"트리플 {len(g) + 1} ({got})"),
                        ("증분 없는 옛 표기", f"트리플 {len(g)} (union: chunks·base·extra)"),
                        ("읽지 못한 구성원", f"트리플 {len(g)} ({kb_lib.gendoc_union(paths + [str(root / 'kg' / 'missing-kg.ttl')])})")):
        if not g4(doc(paths, scale)):
            fails.append(f"음성 `{name}` 이 G4 FAIL 이 아니다 — {scale}")
    for f in fails:
        print(f"FAIL [gendoc_union_fixture] {f}")
    if not fails:
        print(f"PASS [gendoc_union_fixture] {WANT} = {len(g)} — 양성 1 · 음성 3")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
