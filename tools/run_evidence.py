#!/usr/bin/env python3
"""실행 증거 → `satisfies` 후보의 증거 기록 (p9-evidence-ledger 결론 "실행 증거가 특별하다", p10-link-types `satisfies`).

검증기의 통과는 `verifies` 뿐 아니라 그것이 검증하는 `satisfies` 후보에도 실행(+)을, 실패는 실행(−)을 적는다 — V&V 결과가
개발 KB 후보의 증거로 흘러드는 유일한 경로이고 링크가 아니라 **증거 기록 항목**이라 방향 규칙(8.5절)을 깨지 않는다.
이 도구가 그 경로의 생성기다. 손으로 쓰는 링크가 아니라 생성물이며 출력은 `//kg:references_kg` 에 이어 붙는다.

후보의 양 끝은 개발 KB 의 코드 **파일 청크**(파일 복합체의 선언 청크, p7-code-links-on-file-composite)와 **결정 결론**이다.
증거의 원천은 둘이다.

  도장  파일 청크의 `verified` 에 `process:bazel-test`(kb_lib.STAMP_ACTOR)가 있으면 — 추출기가 `tested.source_hash` 가 지금
        소스와 같을 때만 내므로 살아 있는 도장이다 — 그 청크가 `refines` 하는 결정 결론마다 실행(+) 한 줄. 참조는 그 파일 청크다
        (도장의 시각 `agt:verifiedAt` 이 거기 있다). 도장은 통과 뒤에만 찍히므로 도장에서 (−)는 나오지 않는다.
  실행  V&V 실행 기록(`kb/vv/run/`, generated.by `process:vv_run`)의 케이스 표 한 행마다 — 그 케이스를 `refines` 하는 검증기가
        `verifies` 하는 개발 KB 파일 청크 A 와 그 케이스가 `verifies` 하는 결정 결론 D 의 쌍에 pass 는 실행(+), fail 은 실행(−)
        한 줄. 참조는 실행 기록과 케이스 둘이다. skip 은 증거가 아니다(SKIP 은 PASS 가 아니다). 건너뛴 명령이 있는데 pass 로 적힌
        옛 행도 (+)로 읽지 않는다 — 절반만 실행한 통과다.

상태는 p9-evidence-ledger 의 전이 규칙 그대로다. 실행(−)만 있으면 `invalid`(배제, 클래스 없음 — space2kg 와 같은 표현), (+)가
하나라도 있으면 `candidate`(agt:CandidateLink) — (+)와 (−)가 공존해도 자동 해소하지 않고 후보로 남긴다(충돌 = open + 유저 큐).
확정 제안은 내지 않는다 — 확정은 사람이 frontmatter `satisfies:` 에 적는 행위다. 그 쌍이 이미 확정이면 상태·클래스를 쓰지 않고
증거 항목만 그 링크에 붙인다(확정 링크도 증거 기록을 유지한다). 직접 트리플 `agt:satisfies` 는 내지 않는다 — 후보는 주장이 아니다.
링크 IRI 는 chunk2kg 와 같은 규칙(양 끝 뿌리 uuid 의 link_hash)이다.

출력·종료: 읽을 수 없는 입력은 `FAIL [run-evidence] <경로>: …` + EXIT_CONFIG. 실행 기록이 가리키는 케이스가 없으면 stderr 에
`info [run-evidence]` 로 세고 건너뛴다 — 실행 기록은 append-only 라 지난 케이스 이름이 남는다.
사용: run_evidence.py --out <생성.ttl> --residency defs/kb.bzl <청크 파일들...>   (.md 만 읽는다)
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.chunk2kg import (ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                                body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)
except ImportError:
    import kb_lib
    from chunk2kg import (ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                          body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)

KIND = "satisfies"                           # p10-link-types — artifact → decision 의 수평 링크
EVIDENCE_KIND = "agt:runResult"              # evidence-ontology — 검증기·판정 도구의 통과(+) 또는 실패(−)
CONCLUSION_SLOT = "결론"                      # 결정 결론의 본문 표지 (STYLEGUIDE §4)
CASE_DIR = kb_lib.KB_VV + "/case"            # 케이스의 자리 — vv_run.CASE_DIR 와 같은 값
POLARITY = {"pass": "+", "fail": "-"}        # 케이스 판정 → 극성. skip 은 증거가 아니다
_SKIPPED = re.compile(r"(\d+)\s*건너뜀")
_SLUG = re.compile(r"^`([^`]+)`$")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 실행 기록(kb/vv/run/)·케이스·검증기와 코드 파일 청크의 도장이다.
# 생성: tools/run_evidence.py (bazel build //kg:references_kg) — satisfies 후보와 실행 증거 (p9-evidence-ledger)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
"""


# ── 실행 기록의 케이스 표 읽기 ────────────────────

def as_list(v) -> list:
    return v if isinstance(v, list) else []


def run_rows(body: str) -> list[tuple[str, str, int]]:
    """실행 기록 본문의 케이스 표 → [(케이스 슬러그, 판정, 건너뛴 명령 수)]. 헤더의 정의처는 kb_lib.RUN_CASE_TABLE_HEADER."""
    rows, inside = [], False
    for ln in body.splitlines():
        s = ln.strip()
        if not inside:
            inside = s == kb_lib.RUN_CASE_TABLE_HEADER
            continue
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.strip("|").split("|")]
        m = _SLUG.match(cells[0]) if cells else None
        if len(cells) < 3 or not m or cells[2] not in kb_lib.RUN_VERDICTS:
            continue
        skipped = _SKIPPED.search(cells[1])
        rows.append((m.group(1), cells[2], int(skipped.group(1)) if skipped else 0))
    return rows


# ── 후보와 증거 항목의 방출 ────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--residency", required=True, help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — parse_chunk 가 쓴다")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    try:
        apply_plane_level_state(*load_plane_level_state(args.residency))
    except (OSError, ValueError) as e:
        print(f"FAIL [run-evidence] {args.residency}: 값 어휘를 읽을 수 없다 — {e}", file=sys.stderr)
        return kb_lib.EXIT_CONFIG

    meta_of: dict[str, dict] = {}
    path_of: dict[str, str] = {}
    conclusion: set[str] = set()
    spec: dict[str, str] = {}
    for path in sorted(p for p in args.files if p.endswith(".md")):
        try:
            meta, body = parse_chunk(path)
        except (OSError, ValueError) as e:
            print(f"FAIL [run-evidence] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        iri = meta.get("id")
        if not isinstance(iri, str):
            continue
        meta["__body"] = body
        meta_of[iri], path_of[iri] = meta, path
        if isinstance(meta.get(SPECIALIZATION_KEY), str):
            spec[iri] = meta[SPECIALIZATION_KEY]
        if meta.get("type") == "decision" and CONCLUSION_SLOT in body_slots(body.splitlines()):
            conclusion.add(iri)

    def in_kb(iri: str, kb: str) -> bool:
        return f"{kb}/" in path_of.get(iri, "")

    def file_chunk(iri: str) -> bool:
        """개발 KB 의 artifact 청크로 복합체의 부분이 아닌 것 — 파일 청크(선언 청크)와 손으로 쓴 산출물."""
        m = meta_of.get(iri, {})
        return m.get("type") == "artifact" and in_kb(iri, kb_lib.KB_DEV) and not m.get("part_of")

    # (A, D) → [(증거 접미, 참조들, 극성)]
    ledger: dict[tuple[str, str], list[tuple[str, list[str], str]]] = defaultdict(list)

    # 도장 — 살아 있는 process:bazel-test 도장의 파일 청크가 refines 하는 결정 결론
    for a in sorted(meta_of):
        m = meta_of[a]
        if not file_chunk(a) or not any(isinstance(v, dict) and v.get("by") == kb_lib.STAMP_ACTOR for v in as_list(m.get("verified"))):
            continue
        for d in as_list(m.get("refines")):
            if d in conclusion:
                ledger[(a, d)].append(("stamp", [a], "+"))

    # 실행 — 실행 기록의 케이스 행 × (케이스를 refines 하는 검증기가 verifies 하는 파일 청크) × (케이스가 verifies 하는 결정 결론)
    case_of = {Path(path_of[i]).stem: i for i in meta_of if path_of[i].startswith(CASE_DIR + "/") or f"/{CASE_DIR}/" in path_of[i]}
    artifacts_of_case: dict[str, set[str]] = defaultdict(set)
    for v, m in meta_of.items():
        if not in_kb(v, kb_lib.KB_VV) or m.get("type") != "artifact":
            continue
        targets = [a for a in as_list(m.get("verifies")) if file_chunk(a)]
        for c in as_list(m.get("refines")):
            artifacts_of_case[c].update(targets)
    unknown: Counter[str] = Counter()
    halves = 0
    runs = sorted(i for i, m in meta_of.items()
                  if f"{kb_lib.VV_RUN_DIR}/" in path_of[i] and isinstance(m.get("generated"), dict)
                  and m["generated"].get("by") == kb_lib.RUN_GENERATOR)
    for r in runs:
        stem = Path(path_of[r]).stem
        for slug, verdict, skipped in run_rows(meta_of[r]["__body"]):
            c = case_of.get(slug)
            if c is None:
                unknown[slug] += 1
                continue
            if verdict not in POLARITY:
                continue
            if verdict == "pass" and skipped:
                halves += 1
                continue
            for a in sorted(artifacts_of_case.get(c, ())):
                for d in as_list(meta_of[c].get("verifies")):
                    if d in conclusion:
                        ledger[(a, d)].append((f"{stem}-{slug}", [r, c], POLARITY[verdict]))

    lines, states = [PREAMBLE], Counter()
    for (a, d) in sorted(ledger):
        try:
            h = link_hash(work_id(a, spec), KIND, work_id(d, spec))
        except SpecializationError as e:
            print(f"FAIL [run-evidence] {path_of[a]}: {e}", file=sys.stderr)
            return kb_lib.EXIT_CONFIG
        link = f"{ID_BASE}link/{h}"
        entries = ledger[(a, d)]
        evs = [(f"{ID_BASE}evidence/{h}-{suffix}", refs, pol) for suffix, refs, pol in entries]
        ev_list = " , ".join(f"<{e}>" for e, _, _ in evs)
        pols = {p for _, _, p in entries}
        if d in as_list(meta_of[a].get(KIND)):   # 이미 확정 — 증거 항목만 그 링크에 붙인다
            states["confirmed"] += 1
            lines.append(f"\n<{link}>\n    agt:hasEvidence {ev_list} .")
        else:
            cls, state = ("agt:Link , agt:CandidateLink", LINK_STATE_CANDIDATE) if "+" in pols else ("agt:Link", kb_lib.LINK_STATE_INVALID)
            states[state] += 1
            lines.append(f"\n<{link}>\n    a {cls} ;\n    agt:linkFrom <{a}> ;\n    agt:linkTo <{d}> ;\n"
                         f"    agt:linkKind agt:{KIND} ;\n    agt:linkState \"{state}\" ;\n    agt:hasEvidence {ev_list} .")
        for e, refs, pol in evs:
            lines.append(f"\n<{e}>\n    a agt:Evidence ;\n    agt:evidenceKind {EVIDENCE_KIND} ;\n    agt:evidenceRef "
                         + " , ".join(f"<{x}>" for x in refs) + f" ;\n    agt:polarity \"{pol}\" .")

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    both = sum(1 for k in ledger if {p for _, _, p in ledger[k]} == {"+", "-"})
    print(f"[run-evidence] satisfies 쌍 {len(ledger)} (" + " · ".join(f"{k} {v}" for k, v in sorted(states.items())) +
          f") · 증거 항목 {sum(len(v) for v in ledger.values())} · (+)(−) 공존 {both} · 실행 기록 {len(runs)}", file=sys.stderr)
    if halves:
        print(f"info [run-evidence] 건너뛴 명령이 있는 pass 행 {halves} — 증거로 읽지 않았다", file=sys.stderr)
    for slug, n in sorted(unknown.items()):
        print(f"info [run-evidence] 실행 기록의 케이스 `{slug}` 가 {CASE_DIR} 에 없다 — 행 {n}", file=sys.stderr)
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
