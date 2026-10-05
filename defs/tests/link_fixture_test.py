#!/usr/bin/env python3
"""복원 후보 생성기(`tools/link.py`)의 구조 거름 시험 — 양성 하나와 음성 셋 (orchestrator 판정 2026-10-04, 복원 후보 114건).

고정물은 시험이 TEST_TMPDIR 에 쓰는 그래프 파일 하나다. 청크 여덟이고 증거는 본문 인용(`agt:cites`)뿐이다.
  양성  V&V 검증 목표(kb/vv requirement, functional) → 개발 요구의 인용이 `derivesFrom` 후보로 남는다 — 사다리의 functional
        행이 허용하는 정식 링크다 (p8-scenario-ladder-rungs)
  음성  (가) 개발 파일 청크 → V&V 시나리오 자극의 인용 — `satisfies`·`refines` 칸은 있으나 KB 를 가로지른다 (p6-executable-splits-by-kb)
        (나) 함수 청크(파일 복합체의 부분) → 개발 결정의 인용 — 끝점이 코드 부분이다 (p7-code-links-on-file-composite)
        (다) 케이스 → 자기 것이 아닌 시나리오 자극의 인용 — 케이스의 `derivesFrom` 은 생성기가 쓴다 (tools/case_gen.py)
  셋 다 후보 표에 없고 요약의 탈락 분포에 각자의 사유로 1건씩 센다.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

from tools import kb_lib, link

ID = "https://agentic-knowledge-base.dev/id/"


def chunk(name: str, cls: str, level: str, loc: str, by: str = "human") -> str:
    return (f"<{ID}fx-{name}> a agt:{cls} ; rdfs:label \"{name}\"@ko ; agt:hasLevel agt:{level} ; agt:tokenCount 10 ; "
            f"agt:status \"stable\" ; agt:generatedBy \"{by}\" ; agt:assertionLocation \"{loc}\" .\n")


FIXTURE = (
    "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    + chunk("goal", "RequirementChunk", "functional", "kb/vv/goal/fx-goal.md")
    + chunk("req", "RequirementChunk", "functional", "kb/dev/requirement/fx-req.md")
    + chunk("module", "ArtifactChunk", "executable", "kb/dev/artifact/fx/module.md")
    + chunk("stim", "DecisionChunk", "logical", "kb/vv/scenario/fx-stimulus.md")
    + chunk("fn", "ArtifactChunk", "executable", "kb/dev/artifact/fx/fn-main.md")
    + chunk("dec", "DecisionChunk", "concrete", "kb/dev/decision/fx-dec.md")
    + chunk("case", "SchemaChunk", "concrete", "kb/vv/case/fx-case-1.md", kb_lib.CASE_GEN_ACTOR)
    + chunk("other", "DecisionChunk", "logical", "kb/vv/scenario/fx-other-stimulus.md")
    + f"<{ID}fx-section> agt:hasDirectPart <{ID}fx-fn> .\n"
    + f"<{ID}fx-goal> agt:cites <{ID}fx-req> .\n"
    + f"<{ID}fx-module> agt:cites <{ID}fx-stim> .\n"
    + f"<{ID}fx-fn> agt:cites <{ID}fx-dec> .\n"
    + f"<{ID}fx-case> agt:cites <{ID}fx-other> .\n"
)


def main() -> int:
    tmp = Path(os.environ.get("TEST_TMPDIR") or tempfile.mkdtemp())
    ttl, out = tmp / "fx-kg.ttl", tmp / "link-candidates.md"
    ttl.write_text(FIXTURE, encoding="utf-8")
    sys.argv = ["link.py", "--out", str(out), "--root", str(tmp), str(ttl)]
    code = link.main()
    text = out.read_text(encoding="utf-8") if out.exists() else ""
    rows = [ln for ln in text.splitlines() if ln.startswith("| ") and ln.split("|")[1].strip().isdigit()]
    summary = next((ln for ln in text.splitlines() if ln.startswith("| 탈락 수 |")), "")
    fails = []
    if code != 0:
        fails.append(f"종료 코드 {code} — 0 이어야 한다")
    if len(rows) != 1 or "`kb/vv/goal/fx-goal.md`" not in rows[0] or "`derivesFrom`" not in rows[0]:
        fails.append(f"양성: 후보는 목표 → 요구 derivesFrom 하나여야 한다 — 실제 {rows}")
    for anchor in ("kb/dev/artifact/fx/module.md", "kb/dev/artifact/fx/fn-main.md", "kb/vv/case/fx-case-1.md"):
        if any(f"`{anchor}`" in r for r in rows):
            fails.append(f"음성: {anchor} 앵커 후보가 남았다")
    for reason in (link.R_CROSS_LINK, link.R_CODE_PART, link.R_CASE_DERIVES):
        if f"{reason} 1" not in summary:
            fails.append(f"음성: 탈락 분포에 `{reason} 1` 이 없다 — {summary}")
    for f in fails:
        print(f"FAIL [link-fixture] {f}")
    if not fails:
        print("PASS [link-fixture] — 양성 1 (목표 → 요구 derivesFrom) · 음성 3 (KB 가로지름 · 코드 부분 끝점 · 케이스의 derivesFrom)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
